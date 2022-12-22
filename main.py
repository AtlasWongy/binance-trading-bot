import json
import websockets
import asyncio
import requests

f = open('config.json')
config = json.load(f)

# Load configs
api_key = config["api_key_y"]
secret_key = config["secure_key_y"]
symbol = config["symbol"]

# Set the base URL for the Binance API
BINANCE_FUTURES_END_POINT = "https://fapi.binance.com/fapi/v1/listenKey"
FUTURES_STREAM_END_POINT_1 = "wss://fstream.binance.com"

# Ping the Connection Alive
async def ping():
    while True:
        await asyncio.sleep(1800)
        await requests.put("https://fapi.binance.com/fapi/v1/listenKey")

def get_listen_key_by_REST(api_key):
    response = requests.post(url=BINANCE_FUTURES_END_POINT, headers={'X-MBX-APIKEY': api_key})
    return response.json()['listenKey']

async def main():
    listen_key = get_listen_key_by_REST(api_key)
    futures_connection_url = f"{FUTURES_STREAM_END_POINT_1}/ws/{listen_key}"

    while True:
        try:
            async with websockets.connect(futures_connection_url) as ws:
                payload = {
                    "apiKey": api_key,
                    "secret": secret_key
                }
                await ws.send(json.dumps(payload))

                # Keep the connection alive
                asyncio.create_task(ping())
                while ws.closed == False:
                    response = await ws.recv()
                    message = json.loads(response)
                    print(message)
                

        except websockets.exceptions.ConnectionClosed:
            continue

asyncio.run(main())
















# # Get the time current time stamp
# current_timestamp = int(time.time() * 1000)

# # Open a trade
# def open_order():
#     buy_order = client.futures_create_order(
#         symbol = symbol,
#         side = 'SELL',
#         positionSide = 'LONG',
#         type = 'stop_loss',
#         timestamp = {
#             'timestamp': current_timestamp
#         },
#         quantity = 10,
#         price = 1215.00

#     )





