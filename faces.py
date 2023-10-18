# convert into emoji
def main():
    text = input("User text: ")

    convert(text)

#define a function that converts emoji
def convert(t):
    t = t.replace(":(", "🙁")
    t = t.replace(":)", "🙂")
    print(t)

main()