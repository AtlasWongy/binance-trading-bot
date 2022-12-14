from binance.client import Client
import json
import requests
import pandas as pd

f = open('config.json')
config = json.load(f)

client = Client(config["api_key"], config["secure_key"])
print("Connected to Binance successfully....")

klines = client.get_historical_klines(config["currency"], Client.KLINE_INTERVAL_5MINUTE, "1 day ago UTC")

klines_dataframe = pd.DataFrame(
    klines, 
    columns=[
        'Open Time', 
        'Open', 
        'High', 
        'Low', 
        'Close', 
        'Volume',
        'Close Time',
        'Quote Asset',
        'Volume',
        'Number of Trades',
        'Taker buy base asset volume',
        'Taker buy quote asset volume'
    ])

print(klines_dataframe)




