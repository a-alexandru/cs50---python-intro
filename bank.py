def main():

    greeting = value(input("Greeting: "))
    print(f"${greeting}")


def value(greeting):
    greeting = greeting.lower()

    if greeting.startswith("hello"):
        return 0
    
    elif greeting.startswith("h") and greeting.startswith("hello") == False:
        return 20

    else:
        return 100
        
if __name__ == "__main__":
    main()



