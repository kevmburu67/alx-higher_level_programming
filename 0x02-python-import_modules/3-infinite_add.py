#!/usr/bin/python3
from sys import argv

def sum_arguments():
    total_sum = 0
    # Start from index 1 to exclude the script name from the sum
    for arg in argv[1:]:
        total_sum += int(arg)
    print(total_sum)

if __name__ == "__main__":
    sum_arguments()
