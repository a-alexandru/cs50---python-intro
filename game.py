import random
import sys

def main():
    game()


def game():
    while True:
        try:
            x = int(input("Level:"))
            
            if x < 1:
                continue
            else:
                n = random.randint(1, x + 1)
        except ValueError:
            pass
        else:
            break


    while True:
        try:
            guess = int(input("Guess:"))

            if guess < n:
                print("To small")
            if guess > n:
                print("To big")
            elif guess == n:
                print("Right number")
                break
        except ValueError:
            pass
        
main()