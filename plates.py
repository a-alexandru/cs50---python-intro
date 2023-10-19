def main():
    plates = input("Plates:")
    x = is_valid(plates)
    print(x)

    

def is_valid(text):
    ln = len(text)

    if ln < 2 or ln > 6:
        return False

    if not text[0:2].isalpha():
        return False

    for i in range(ln):
        if text[i].isdigit():
            x = text[i:ln]
            if x[0] == "0":
                return False

            if not x.isdigit():
                return False         
    
        
        
    return True
        

       
            
 
    return True
if __name__ == "__main__":
    main()