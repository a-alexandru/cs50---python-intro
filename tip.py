def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip =  dollars * percent
    print(f"Leave ${tip:.2f}")


#
def dollars_to_float(d):
    n = d.removeprefix('$')
    new = float(n)
    return new

def percent_to_float(p):
    n = p.removesuffix('%')
    new = float(n) / 100
    return new

main()