import os
import re
import string
import subprocess

OUTPUT_DIR = "./bin"


def find_file(prefix: str) -> str:
    for file in os.listdir(os.getcwd()):
        if file.startswith(prefix):
            return file

    print(f"File starting with '{prefix}' could not be found in '{os.getcwd()}'. Exiting . . .")
    exit()


def filename_to_cratename(filename: str) -> str:
    valid_characters = string.ascii_lowercase + string.digits

    cratename = ""
    for char in filename[:-3].lower():
        if char in valid_characters:
            cratename += char
            continue

        cratename += '_'

    return re.sub(r"_{2,}", '_', cratename)


def main():
    solution_prefix = input("Enter problem number: ")
    solution_file = find_file(solution_prefix)
    crate_name = filename_to_cratename(solution_file)

    try:
        subprocess.check_call(
            ("rustc",
             solution_file,
             f"--out-dir={OUTPUT_DIR}",
             f"--crate-name={crate_name}",
             "-C", "opt-level=3"))
    except subprocess.CalledProcessError:
        print(f"'{solution_file}' failed to compile. Exiting . . .")
        exit()

    try:
        program_output = subprocess.check_output(f"{OUTPUT_DIR}/{crate_name}.exe").decode("utf-8")
        print(f"'{crate_name}'.exe finished execution and proudec the following output:\n\n{program_output}")
    except subprocess.CalledProcessError:
        print(f"Runtime error while running '{crate_name}.exe'. Exiting . . . ")


if __name__ == "__main__":
    main()
