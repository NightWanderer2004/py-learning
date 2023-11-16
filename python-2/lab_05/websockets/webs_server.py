# Server
import websockets
import asyncio

async def main():
    server = await websockets.serve(handler, "localhost", 8080)
    await server.wait_closed()

async def handler(websocket, path):
    await websocket.send("Let's STUDY!!!!")

    data = await websocket.recv()
    print(data)


asyncio.run(main())
