import sys

def main():

    if len(sys.argv) < 2:
        sys.exit("To few command-line arguments")
    
    elif len(sys.argv) > 2:
        sys.exit("To many command-line arguments")
    else:
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a python file")


    file_name = sys.argv[1]
    try:
        with open(file_name, "r") as f:
            file = f.read()

    except FileNotFoundError:
        raise FileNotFoundError

    ff = file.split("\n")
    comm = 0
    spaces = 0
    total = 0

    for f in ff:
        if f.lstrip().startswith("#"):
            comm += 1
        elif f.lstrip() == "":
            spaces += 1
        else:
            total += 1
    


    
    print(comm)
    print(spaces)
    print(total)
    


if __name__ == "__main__":
    main()