def main():
    x = get_date()



def get_date():
    while True:
        dd = input("Date:")
        new = []
        months = ["January","February","March","April","May","June","July","August","September","October","November","December"]


        try:
            if "/" in dd:
                x = dd.split("/")
                mm = int(x[0])
                md = int(x[1])
                my = int(x[2])
                

                if my >= 1636 and my <=2022:
                    new.append(my)
                    
                    if mm <= 12 and mm >= 1:
                        new.append(mm)
                        
                        if md <= 31 and md >= 1:
                            new.append(md) 
                            
                            print(f"{new[0]}-{new[1]:02}-{new[2]:02}")      
                            break
            elif "," in dd:
                m, d, y = dd.split()
                
                if m in months:
                    mm = months.index(m) + 1
                    new.append(mm)
                    
                    if d[-1] == ",":
                        md = int(d[0:-1])
                        if md <= 31 and md >=1:
                            new.append(md)
                            
                            if len(y) == 4:
                                my = int(y)
                                new.append(my)
                                print(f"{new[2]}-{new[0]:02}-{new[1]:02}")
                                break


        except ValueError:
            pass

       
        
        
        
            
    
main()

