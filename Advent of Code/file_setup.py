import os
import shutil

year = input("Enter year: ").strip()
day = input("Enter day (1-25): ").strip()

directory = fr"{year}/{day}/"

if os.path.exists(directory):
    if input("Directory already exists! Do you want to proceed with total annihilation of directory and then rebirth of the files? [Y/n]: ").lower() != 'y':
        exit()

    shutil.rmtree(directory)

os.makedirs(directory)

with open(directory + "data.in", 'w') as _:
    pass

with open(directory + "example.in", 'w') as _:
    pass

with open(directory + "script.py", 'w') as f:
    f.write('def part1():\n    with open("data.in", \'r\') as f:\n        pass\n\n\ndef part2():\n    with open("data.in", \'r\') as f:\n        pass\n\n\nif __name__ == "__main__":\n    print(part1())\n    print(part2())\n')
