import random
import sys


def main():

    l = level()
    scores = 0
    i = 0    

    for _ in range(10):
        #generate the problem, store the result
        n = generate_integer(l)
        x = n[0]
        y = n[1]
        trials = 0
        r = x + y
        
        #print the problem and ask the user for a result
        while True:
            try:
                ask = int(input(f"{x} + {y} ="))
                
            except ValueError:      #if the user input's is not a num value
                print("EEE")
                trials += 1
                if trials == 3:
                    print(f"Result:{r}")
                    break
            else:                   #update scores or trials based on the user answer
                if ask == r:
                    scores += 1
                    break
                else:
                    if ask != r:
                        print("EEE")
                        trials += 1
                        if trials == 3:
                            print(f"Result:{r}")
                            break


                            
                            
    print(f"Score:{scores}")
                        


def level():
    while True:
        try:
            x = int(input("Level:"))
            if x < 1 or x > 3:
                continue
            else:
                return x
        except ValueError:
            pass

def generate_integer(level):
    try:
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            return (x,y)
    
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
            return (x, y)
            
        elif level == 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
            return (x, y)

    except:
        raise ValueError





if __name__ == "__main__":
    main()