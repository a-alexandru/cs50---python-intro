def main():
    expression = input("Expression :")

    calculator(expression)


def calculator(e):
    x, y, z = e.split(" ")
    a = int(x)
    b = int(z)
    if y == "+":
        print(float(a + b))

    elif y == "-":
        print(float(a-b))

    elif y == "*":
        print(float(a*b))

    elif y == "/":
        print(float(a/b))

    else:
        print("Invalid symbol")
    
main()