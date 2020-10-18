import asyncio
import websockets
import time
import json

async def test(websocket, path):
    print('connected')
    await websocket.send('connected')

    with open('jason_controller.json') as file:
            jason = json.load(file)

    z = json.dumps(jason)

    status = 0

    while True:
        await websocket.send(z)
        time.sleep(1)
        try:
            response = await websocket.recv()
            x = json.loads(response)
            print(x["A1-1"])
            if (x["A1-1"] == '0'):
                jason["A1-1"] = 0
            elif (x["A1-1"] == '1'):
                jason["A1-1"] = 1
            print(jason["A1-1"])
            z = json.dumps(jason)
            print(z)
            
        except:
            print('connection failed')

        

start_server = websockets.serve(test, "localhost", 54000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()