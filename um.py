import re

def main():

    text = input("Test:")

    x = re.findall(r"\bum\b", text)

    print(x)
    print(len(x))

if __name__ == "__main__":
    main()