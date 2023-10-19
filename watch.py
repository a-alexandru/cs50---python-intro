#extract youtube URL's
#return the short form , eg. "youtu.be"

import re
import sys

def main():

    print(parse(input("HTML: ")))    

def parse(text):

    #check iframe and src attr

    if re.search(r"^<iframe.*src=.*/iframe>$", text):
        #check for the youtube link
        tt = re.search(r"https?://(?:www\.)?youtube\.com/embed/[a-zA-Z0-9]*", text)
        
        #get the string form of the link
        x = tt.group()

        #convert the link
        xc = re.sub(r"youtube\.com/embed", "youtu.be", x)
        return xc
            
    else:
        return "None"



if __name__ == "__main__":
    main()