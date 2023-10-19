def main():

    text = input("Twitter:")
    p = shorten(text)
    print(p)

def shorten(word):
    temp = "#"
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for e in word:
        if e not in vowels and e.isalpha():
            temp += e
            
            
    return (temp.removeprefix('#'))

if __name__ == "__main__":
    main()
