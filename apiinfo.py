import asyncio
import json
import websockets
from datetime import datetime, timezone

# Replace YOUR_API_KEY and YOUR_API_SECRET with your Binance API key and secret
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"

# Set the base URL for the Binance API
base_url = "wss://fstream.binance.com/ws"

# Set the symbol for the commodity
symbol = "ETHBUSD"

# Set the ping interval in seconds
ping_interval = 300

async def ping(websocket):
  while True:
    # Send a pong frame every 5 minutes to keep the connection alive
    await asyncio.sleep(ping_interval)
    await websocket.ping()
   

async def get_current_price():
  # Connect to the websocket endpoint
  endpoint = f"{base_url}/{symbol.lower()}@kline_5m"
  while True:
    try:
      async with websockets.connect(endpoint) as websocket:
        # Send the API key and secret to authenticate the connection
        payload = {
          "apiKey": api_key,
          "secret": api_secret
        }
        await websocket.send(json.dumps(payload))

        # Create an asyncio task to send a pong frame every 5 minutes
        asyncio.create_task(ping(websocket))

        # Continuously receive data from the websocket
        async for message in websocket:
          try:
            data = json.loads(message)
            current_price = data['k']['c']
            print(f"Current price of {symbol}: {current_price} ({datetime.now(timezone.utc)} - {datetime.now(timezone.utc).timestamp()*1000 - data['E']})")
            if data['k']['x']:
              candlestick_data = data['k']
              print(f"5 minute candlestick data: {candlestick_data}")
          except KeyError:
            print("Faulty data received from API")
            continue

        # Connection was closed by the server
        print("Websocket connection lost, attempting to reconnect...")
    except websockets.exceptions.ConnectionClosed:
      # Connection was closed, try to reconnect
      continue

async def main():
  # Get the current price
  await get_current_price()

# Run the main function
asyncio.run(main())

