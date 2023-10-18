def main():
    camelCase = input("camelCase:")

    snake_case(camelCase)


def snake_case(t):
    snake = t[0].lower()
    t_len = len(t)

    for i in range(1, t_len):
        temp = t[i]
        if temp.isupper():
            snake += "_" + temp.lower()
        
        else:
            snake += temp

    print("snake_case:", snake)

main()
    

