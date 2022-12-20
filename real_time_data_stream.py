import asyncio
import json
import time
import websocket
from binance import AsyncClient, BinanceSocketManager
import datetime
import timeit
import ast
import os
import sys

def on_message(ws, message):
    response = json.loads(message)
    print(response)
    print("-------------------------------------")

def on_error(ws, error):
    print(error)

def on_close(ws, status_code, msg):
    print("WebSocket connection closed")
    # Un-comment line below to restart python script
    # os.execv(sys.executable, [sys.executable] + sys.argv)

if __name__ == "__main__":
    f = open('config.json')
    config = json.load(f)
    ws = websocket.WebSocketApp(f"wss://stream.binance.com/ws/{config['currency']}@kline_5m",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                            )
    ws.run_forever(ping_interval=300)


# f = open('config.json')
# config = json.load(f)
# stream_k_lines(config['currency'], '5m')

# async def main():
#     client = await AsyncClient.create()
#     bm = BinanceSocketManager(client, user_timeout = 60)
#     f = open('config.json')
#     config = json.load(f)
#     ts = bm.kline_socket(config['currency'], AsyncClient.KLINE_INTERVAL_5MINUTE) #Change here
#     async with ts as tscm:
#         while True:
#             start = time.perf_counter()
#             res = await tscm.recv()
#             end = time.perf_counter()
            
#             print("---------------------------------------------")
            
#             print(res)
#             print(" ")
#             print(f"API request took {end - start:.2f} seconds")
            

#     await client.close_connection()

# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())