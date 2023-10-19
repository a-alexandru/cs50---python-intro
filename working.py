import re
import sys

def main():

    print(convert(input("Hours:")))

def convert(h):
    
    #validate string pattern
    if re.search(r"^([1-9]|1[0-2])(:[0-5][0-9])?\s(AM|PM)\sto\s([1-9]|1[0-2])(:[0-5][0-9])?\s(AM|PM)$", h):

        #split input into time in and time out
        xh = re.split("to", h)

        # r1,r2 string digits group from xh
        r1 = re.search(r"\d+:?\d?\d?", xh[0]).group()    #time in
        r2 = re.search(r"\d+:?\d?\d?", xh[1]).group()    #time out
        
        #call format and take hours for in time and out time
        inH, inM = format(r1, xh[0])   
        outH, outM = format(r2, xh[1])
        
        #return the 24 hour format
        return (f"{inH:02}:{inM:02} to {outH:02}:{outM:02}")

    else:
        print("Invalid time-format")


def format(r, xr):
    if ":" in r:
        x, y = r.split(":")
        h= int(x)
        m = int(y)
    else:
        h = int(r)
        m = 0

    if "AM" in xr and h == 12:
        h = 0
    elif "PM" in xr and h != 12:
        h += 12 
    
    return h,m



if __name__ == "__main__":
    main()