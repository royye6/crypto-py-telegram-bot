import os
import requests
import json


def fetch_data(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetcing data from {url}: {e}")
        return None
    

def format_data():
    CR_API_KEY = os.environ.get("COINRANKING_API_KEY")
    OX_API_KEY = os.environ.get("OPENEXCHANGERATES_API_KEY")

    header1 = {
        'x-access-token': CR_API_KEY
    }

    header2 = {
        'accept': 'application/json'
    }

    url1 = "https://api.coinranking.com/v2/coins?limit=10"
    url2 = f"https://openexchangerates.org/api/latest.json?app_id={OX_API_KEY}&base=USD&symbols=ZAR"

    coins_data = fetch_data(url1, header1)
    exchange_rate_data = fetch_data(url2, header2)

    if coins_data and exchange_rate_data:
        try:
            rate = float(exchange_rate_data['rates'].get('ZAR', 0.0))
        except Exception as e:
            print("Could not deserialize json data", e)

        if coins_data.get('data'):

            for coin in coins_data['data']['coins']:
                name = coin.get('name', "")
                symbol = coin.get('symbol', "")
                price = float(coin.get('price', 0.0),)
                change = float(coin.get('change', 0.0))
                zar = float(price*rate)         
                print(f"\nName: {name}\n\nSymbol: {symbol}\n\nPrice (USD): $ {price:.2f}\n\nPrice (ZAR): R {zar:.2f} \n\nChange: {change:.2f}%\n")
                
        else:
            print("No data found in response")
        
    else:
        print("Error fetching data for coins and exchange rate")


if __name__ == "__main__":
    format_data()