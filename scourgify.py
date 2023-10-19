import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("To few command-line arguments")
    
    elif len(sys.argv) > 3:
        sys.exit("To many few command-line arguments")


    names = []

with open("before.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        fname, lname = row['name'].split(",")
        house = row['house']
        names.append({"first name" : fname, "last name" : lname, "house" : house})


with open("after.csv", "a") as file:
    fields = ["first name", "last name", "house"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    for n in names:
        writer.writerow(n)

    
    

if __name__ == "__main__":
    main()