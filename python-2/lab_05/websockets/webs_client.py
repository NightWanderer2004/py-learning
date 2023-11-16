# Client 
import websockets
import asyncio

async def main():
    async with websockets.connect("ws://localhost:8080") as websocket:
        await websocket.send("Nice idea!")

        data = await websocket.recv()
        print(data)


asyncio.run(main())
