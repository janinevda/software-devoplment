import asyncio
import websockets
import time

async def test(websocket, path):
    print('connected')
    await websocket.send('connected')

    while True:
        await websocket.send('1')
        try:
            response = await websocket.recv()
            print(response)
        except:
            print('connection failed')

        time.sleep(2.5)

        await websocket.send('0')
        try:
            response = await websocket.recv()
            print(response)
        except:
            print('connection failed')

        time.sleep(2.5)    

start_server = websockets.serve(test, "localhost", 1234)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()