from binance.client import Client
import json

f = open('config.json')
api_data = json.load(f)

client = Client(api_data["api_key"], api_data["secure_key"])
print("Connected to Binance successfully....")

info = client.get_symbol_info('BNBBTC')

for i in info:
    print(i)