def main():
    plate = input("Plate: ")
    
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length(s) and starts_with_letters(s) and no_invalid_chars(s):
        if has_valid_numbers(s):
            return True
    return False


def length(l):
    return 2 <= len(l) <= 6


def starts_with_letters(l):
    return l[:2].isalpha()


def no_invalid_chars(l):
    return all(c.isalnum() for c in l)


def has_valid_numbers(l):
    if l[-1] == "0":
        return False
    return l[2:].isdigit()


# Testing the modified code
main()

