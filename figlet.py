from pyfiglet import Figlet
import random
import sys

#zero or two cli arguments
#two for user specified font and zero for random
#-f or --font as argument 1 and font's name as argument 2
#prompt user for a str
#output the str

try:
    if len(sys.argv) == 1:
        figlet = Figlet()
        fonts = figlet.getFonts()
        
        f = random.choice(fonts)
        figlet.setFont(font=f)
        
        st = input("Input:")
        print(figlet.renderText(st))
    
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-f' or sys.argv[1] == "--font":
            
            figlet = Figlet()
            fonts = figlet.getFonts()
            
            if sys.argv[2] in fonts:
                f = sys.argv[2]
                figlet.setFont(font=f)
                st = input("Input:")
                print(figlet.renderText(st))
    
except:
    pass
        

