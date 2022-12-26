from binance.client import Client
import asyncio
import json
import binance
import sys

# Load the configs
f = open('config.json')
config = json.load(f)
api_key = config['api_key_y']
secret_key = config['secure_key_y']
symbol = config['symbol']

# Instance the Client
client = Client(api_key, secret_key)

# Open order / positions array
current_positions_array = [{}]

async def decision_handler(current_price, candlestick_data):
    try:
        print(current_price)
        print(candlestick_data)
        print("------------------")

        if candlestick_data:
            sys.exit("Send order to close")
        elif current_price:
            # Not sure what to do here
            print("Close the trade")

        position = await get_positions()
        current_positions_array.pop()
        current_positions_array.append(position)
        print(current_positions_array)
        return
    except binance.exceptions.BinanceAPIException:
        return

async def get_positions():
    positions = client.futures_account()['positions']
    for position in positions:
        if position['symbol'] == 'BTCBUSD' and position['positionSide'] == 'LONG':
            return position

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(decision_handler())