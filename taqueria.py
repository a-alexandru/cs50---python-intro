from webbrowser import get


def main():
    
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    
    total = 0
    x = order(menu, total)
    print("$%.2f" % x)

def order(m, t):
    while True:
        try:
            x = input("Order:")
            xt = x.title()
             
            if xt in m:
                t = t + m[xt]
        except KeyError:
            pass

        except EOFError:
            break
        else:
            print(f"Total: ${t}")
        
        
            
main()








 