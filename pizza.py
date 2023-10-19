import sys
import csv
from tabulate import tabulate


def main():

    with open("sicilian.csv", "r") as f:
        file = csv.reader(f)
        print(tabulate(file))



if __name__ == "__main__":
    main()