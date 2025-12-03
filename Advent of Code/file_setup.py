import os
from pathlib import Path
import shutil
import sys

SNIPPETS_PATH = Path(f"./snippets/")
LANGUAGES = (
    ("python3", ".py"),
    ("scala3", ".scala"),
    ("java", ".java")
)


def prompt_int(
        prompt: str = "Enter an integer: ",
        error_message: str = "Invalid input, please enter an integer.",
        min_value: int = -sys.maxsize - 1,
        max_value: int = sys.maxsize
) -> int:
    while True:
        try:
            value = int(input(prompt))
            if not min_value <= value <= max_value:
                raise ValueError
            return value
        except ValueError:
            print(error_message)


def main() -> None:
    year = prompt_int("Enter year: ")
    day = prompt_int("Enter day (1-25): ", "Invalid input, please enter an integer in the interval [1, 25].", 1, 25)

    directory = Path(f"./{year}/{day}/")

    if directory.exists():
        if input(
                "Directory already exists! Do you want to proceed with total annihilation of directory and then rebirth of the files? [Y/n] (default no): ").lower() != 'y':
            return

        shutil.rmtree(directory)

    directory.mkdir(parents=True, exist_ok=True)
    (directory / "data.in").touch()
    (directory / "example.in").touch()

    for i, (language, extension) in enumerate(LANGUAGES, 1):
        print(f"{f"{i}.": <4}{language}")
    option = prompt_int(
        "Select language: ",
        f"Invalid input, please enter an integer in the interval [1, {len(LANGUAGES)}].",
        1,
        len(LANGUAGES)
    ) - 1
    snippet = Path(SNIPPETS_PATH / f"script{LANGUAGES[option][1]}")
    if not snippet.exists():
        snippet = Path(SNIPPETS_PATH / f"Script{LANGUAGES[option][1]}")
    shutil.copy(snippet, directory / snippet.name)


if __name__ == "__main__":
    main()

