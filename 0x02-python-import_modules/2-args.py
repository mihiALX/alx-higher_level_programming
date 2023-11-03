#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 2:
        print(f"{len(argv) - 1} argument:")
        print(f"{1}: {argv.__getitem__(1)}")
    elif len(argv) > 2:
        print(f"{len(argv) - 1} arguments:")
        for i in range(1, len(argv)):
            print(f"{i}: {argv.__getitem__(i)}")
    else:
        print(f"{len(argv) - 1} arguments.")
