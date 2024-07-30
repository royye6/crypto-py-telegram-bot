import os
import requests
import json


def get_coin_data() -> str:
    API_KEY = os.environ.get("COINRANKING_API_KEY")

    headers = {
        'x-access-token': API_KEY
    }

    url = "https://api.coinranking.com/v2/coins?limit=10"

    try:
        response = requests.get(url, headers=headers)
        coins = response.json()
    except Exception as e:
        print("Failed connection to", url, ":", e)


    if response.status_code == 200:
        if coins.get('data'):

            for coin in coins['data']['coins']:
                name = coin.get('name')
                symbol = coin.get('symbol')
                price = float(coin.get('price'))
                change = float(coin.get('change'))
                """ 
                Exchange rate is constantly fluctuating and should be fetched from an API
                But implementation is currently too elaborate with API request limits, use fixed rate.
                """
                zar = float(price*18.34)         
                print(f"\nName: {name}\n\nSymbol: {symbol}\n\nPrice (USD): $ {price:.2f}\n\nPrice (ZAR): R {zar:.2f} (approx)\n\nChange: {change:.2f}%\n")
                
        else:
            print("No data found in response")
    else:
        print("API request failed with status code:", response.status_code)

    return 

get_coin_data()





