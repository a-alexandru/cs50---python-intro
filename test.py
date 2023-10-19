from urllib import response
import requests
import sys
import json

def main():
    if len(sys.argv) != 2:
        sys.exit()

    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit()

    # https://api.coindesk.com/v1/bpi/currentprice.json

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    
    x = response.json()
    
    rate = x["bpi"]["USD"]["rate"]
    
    rate = rate.replace(".", ",")
    m, v, y = rate.split(",")
    price = float(m+v+y)
    total = price * 2.5
    print(f"{total: .4f}")


if __name__ == "__main__":
    main()