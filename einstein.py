# energy output in joules
def main():
    mass = int(input("Mass:"))

    joules = energy(mass)

    print(joules)


# return mass argument multiplied by the speed of light
def energy(m):
    return m * (300000000 ** 2)

main()