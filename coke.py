def main():

    coke()

def coke():
    amount = 50
    while True:
        print("Amount Due:", amount)
        insert = int(input("Insert Coin: "))
        amount = amount - insert
        print("Owned:", amount)

        if amount == 0:
            break

        else:
            continue

main()