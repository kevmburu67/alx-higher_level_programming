#!/usr/bin/python3
from sys import argv

def print_arguments():
    num_args = len(argv) - 1  # Subtract 1 to exclude the script name from the count
    print(f"Number of argument{'s' if num_args != 1 else ''}: {num_args}{'.' if num_args == 0 else ':'}")

    if num_args > 0:
        for i in range(1, num_args + 1):
            print(f"{i}: {argv[i]}")

if __name__ == "__main__":
    print_arguments()
