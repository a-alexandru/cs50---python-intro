import random
import sys

def main():
    l = level()
    scores = 0

    for i in range(10):
        trials = 0
        n = generate_integer(l)
        x = n[0]
        y = n[1]
        result = x + y
        
        try:
            answer = int(input(f"{x} + {y} ="))
        except ValueError:
            pass
        else:
            if answer == result:
                scores += 1
                break
            else:
                print("EEE")
                trials += 1
                while True:
                    try:
                        answer = int(input(f"{x} + {y} ="))
                    except ValueError:
                            pass
                    else:
                        if answer != result:
                            trials += 1
                            if trials == result:
                                print(scores)
                                sys.exit()
                            elif answer == result:
                                scores += 1
                                break


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