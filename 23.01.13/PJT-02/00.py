import requests

def get_bit_krw():
    order_currency = "BTC"
    payment_currency = "KRW"
    url = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"

    response = requests.get(url).json()

    return response["data"]["prev_closing_price"]

if __name__ == "__main__":
    print(get_bit_krw())