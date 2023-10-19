def main():

    groceries = {}
    n = items(groceries)

def items(g):
    while True:
        try:
            x = input("").upper()

            if x not in g:
                g[x] = 1
            else:
                g[x] += 1
        
        except EOFError:
            n = sorted(g.items())
            
            for i in range(len(n)):
                print(n[i][1], n[i][0])

            return n
                 
    
    
    
main()
