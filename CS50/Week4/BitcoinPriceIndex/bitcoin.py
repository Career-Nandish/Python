import requests
import sys

def get_input():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            return float(sys.argv[1])
        except ValueError:
            sys.exit(f"{sys.argv[1]} is not a number")

def get_bitcoin_price_usd(n):
    res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    return f"${n * res['bpi']['USD']['rate_float']:,.4f}"

def main():
    n = get_input()
    print(get_bitcoin_price_usd(n))

if __name__ == "__main__":
    main()