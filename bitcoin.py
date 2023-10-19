import requests
import sys

def main():

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            btc = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    
    x = response.json()

    rate = x["bpi"]["USD"]["rate_float"]

    total = rate * btc

    print(f"{total:,.4f}")
    
    

if __name__ == "__main__":
    main()