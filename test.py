import csv
import sys

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



            