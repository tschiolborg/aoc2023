import os
import sys

import requests
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("TOKEN")
if TOKEN is None:
    raise ValueError("No token found in .env file")

YEAR = 2023


def make_path(name: str = "lol") -> str:
    """The path to output file."""

    filename = f"{name}.in"
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)

    # Construct the full file path
    file_path = os.path.join(script_dir, "data", filename)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    return file_path


def get_data(day: int) -> str:
    """Get data from from the api and save it."""

    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    response = requests.get(url=url, cookies={"session": TOKEN})
    response_data = response.text

    with open(make_path(str(day)), "w") as f:
        f.write(response_data)

    return response_data


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("You need to provide a day number")

    try:
        day = int(sys.argv[1])
    except ValueError:
        raise ValueError("Day number must be an integer :D")
    assert 1 <= day <= 25, "Day number must be between 1 and 25"

    get_data(day)
