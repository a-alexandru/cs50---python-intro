def main():


    date = input("Date:")
    new = []

    if "/" in date:
        x = date.split("/")
        mm = int(x[0])
        md = int(x[1])
        my = int(x[2])
        
        if my >= 1636 and my <= 2022:
            new.append(my)
            
main()


"""
def main():

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "Octomber", "November", "December"]


#format user date
def dd():
    while True:
        try:
            date = input("Date:")
            new = []
            if "/" in date:
                x = date.split("/")
                mm = int(x[0])
                md = int(x[1])
                my = int(x[2])
                
                if my >= 1636 and my <= 2022:
                    new.append(my)
                    
                    if mm <= 12 and mm >= 1:
                        new.append(mm)
        except:
            continue
    if md <= 31 and md >= 1:
        new.append(md)

ys = new[0]
sm = new[1]
sd = new[2]


print(f"{ys}-{sm:02}-{sd:02}")

main()




"""