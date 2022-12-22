# import asyncio
# import json
# import time
# import websocket
# from binance import AsyncClient, BinanceSocketManager
# from datetime import datetime, timezone
# import timeit
# import ast
# import os
# import sys

# # def on_message(ws, message):
# #     response = json.loads(message)
# #     time_received = datetime.fromtimestamp(response['E']/1e3) 
# #     print(" ")
# #     print(f"Current price of {config['currency']}: {response['k']['c']} ({datetime.now()} - {datetime.now(timezone.utc).timestamp()*1000 - response['E']})")
# #     print("-------------------------------------")
# #     # print(f"Current price of {config['currency']}: {res['k']['c']} ({datetime.now()} - {datetime.now(timezone.utc).timestamp()*1000 - res['E']})")

# # def on_error(ws, error):
# #     print(error)

# # def on_close(ws, status_code, msg):
# #     print("WebSocket connection closed")
# #     # Un-comment line below to restart python script
# #     # os.execv(sys.executable, [sys.executable] + sys.argv)

# # async def main():
       
# #         ws = websocket.WebSocketApp(f"wss://stream.binance.com/ws/{config['currency']}@kline_5m",
# #             on_message=on_message,
# #             on_error=on_error,
# #             on_close=on_close,
# #         )
# #         await ws.run_forever()

# # if __name__ == "__main__":
# #     f = open('config.json')
# #     config = json.load(f)
# #     loop = asyncio.get_event_loop()
# #     loop.run_until_complete(main())

# # if __name__ == "__main__":
# #     f = open('config.json')
# #     config = json.load(f)
# #     ws = websocket.WebSocketApp(f"wss://stream.binance.com/ws/{config['currency']}@kline_5m",
# #                                 on_message=on_message,
# #                                 on_error=on_error,
# #                                 on_close=on_close,
# #                             )
# #     ws.run_forever(ping_interval=300)


# # f = open('config.json')
# # config = json.load(f)

# async def main():
#     client = await AsyncClient.create()
#     bm = BinanceSocketManager(client, user_timeout = 60)
#     f = open('config.json')
#     config = json.load(f)
#     ts = bm.kline_futures_socket(config['currency'], AsyncClient.KLINE_INTERVAL_5MINUTE) #Change here
#     async with ts as tscm:
#         while True:
#             res = await tscm.recv()
#             print("---------------------------------------------")
#             print(res)
#             print(f"Current price of {config['currency']}: {res['k']['c']} ({datetime.now()} - {datetime.now(timezone.utc).timestamp()*1000 - res['E']})")
            

#     await client.close_connection()

# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())