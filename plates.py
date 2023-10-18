
def main():
    plate = input("Plate: ")
    
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):

    #if length is true, check first two characters, else return False
    if length(s):
        
        #if alpha is true, check for digits, else return False
        if alpha(s):

            #check digits
            if digits(s):
                return True
            else:
                return False
            
        else:
            return False
    else:
        return False



#function definitions

#text's length
def length(l):
    if len(l) < 2 or len(l) > 6:
        return False
    else:
        for i in range(len(l)):
            if not l[i].isalnum():
                return False
            else:
                return True


#first two characters function
def alpha(l):
    if l[0].isalpha() and l[1].isalpha():
        return True
    else:
        return False

#check for digits function
def digits(l):
    for i in range(2, len(l)):
        if l[i].isdigit() and l[i] != "0":
            for j in range(i, len(l)):
                if l[j].isalpha():
                    return False
                else:
                    return True
        elif l[i].isdigit() and l[i] == "0":
            return False
        else:
            return True
                


main()