def main():
    str = input("Input:")
    twttr(str)


def twttr(ex):
    temp = "#"
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    
    for e in ex:
        if e not in vowels:
            temp += e


    print(temp.removeprefix('#'))


main()