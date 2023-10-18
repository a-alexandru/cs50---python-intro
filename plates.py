def main():
    plate = input("Plate: ")
    
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length(s):
        if alpha(s):
            if digits(s):
                return True
    return False


def length(l):
    if len(l) < 2 or len(l) > 6:
        return False
    else:
        for i in range(len(l)):
            if not l[i].isalnum():
                return False
        return True


def alpha(l):
    if l[0].isalpha() and l[1].isalpha():
        return True
    else:
        return False


def digits(l):
    found_digit = False
    for i in range(2, len(l)-1):
        if l[i].isdigit() and l[i] != "0":
            found_digit = True
            for j in range(i+1, len(l)):
                if l[j].isalpha():
                    return True
                else:
                    return False
        elif l[i].isdigit() and l[i] == "0":
            return False
        else:
            return True
    return not found_digit


# Testing the modified code
main()

