import asyncio
import json
from binance import AsyncClient, BinanceSocketManager
    

async def main():
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client, user_timeout = 60)
    f = open('config.json')
    config = json.load(f)

    ts = bm.kline_socket(config['currency'], AsyncClient.KLINE_INTERVAL_5MINUTE)
    async with ts as tscm:
        while True:
            res = await tscm.recv()
            print("---------------------------------------------")
            print(res)

    await client.close_connection()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())