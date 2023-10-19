
def main():
    x = input("Fraction")
    
    p = convert(x)
    
    fuel = gauge(p)

    print(fuel)


def convert(fraction):
    while True:
        try:
            numbers = fraction.split("/")
            
            nA = int(numbers[0])
            nB = int(numbers[1])

            r = round(nA / nB * 100)

            return r
            
        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError
            


def gauge(percentaje):

    if percentaje <= 1:
        return "E"
    elif percentaje >= 99:
        return "F"
    elif percentaje >= 75:
        return "75%"
    elif percentaje >= 50:
        return "50%"
    elif percentaje >= 25:
        return "25%"



if __name__ == "__main__":
    main()
        
