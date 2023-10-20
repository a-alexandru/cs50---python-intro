import datetime
import sys
import inflect


def main():
    

    p = inflect.engine()

    #get user input
    try:
        
        user = input("Date of Birth:")

        if datetime.date.fromisoformat(user):         #check user input format
            db = datetime.date.fromisoformat(user)    #db is now a date format
    
    except ValueError:
        sys.exit()      


    #get curent date
    cd = datetime.date.today()

    dif = cd - db    #the difference in days between the two dates

    min = round(dif.days * 24 * 60)    #calculate total minutes

    #convert min into literals
    words = p.number_to_words(min, andword="")
    
    print(words.capitalize() + " " + "minutes")
    

if __name__ == "__main__":
    main()