import asyncio
import websockets
import time
import json

async def test(websocket, path):
    print('connected')
    await websocket.send('connected')

    while True:
        with open('jason_controller.json') as jason:
            lines = jason.readlines()[4:]
        await websocket.send(open('jason_controller.json'))
        try:
            response = await websocket.recv()
            print(response)
        except:
            print('connection failed')

        time.sleep(2.5)   

start_server = websockets.serve(test, "localhost", 1234)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()