
def main():
    x = get_int()
    
    if x <= 1:
        print("E")
    elif x >= 99:
        print("F")
    else:
        print(f"{x}%")

def get_int():
    
    while True:
        try:
            x = input("Fraction:")
            numbers = x.split("/")
            
            nA = int(numbers[0])
            nB = int(numbers[1])

            r = round(nA / nB * 100)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return r 
            
main()
        
