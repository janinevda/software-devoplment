import asyncio
import websockets
import time
import json

with open('jason_controller.json') as file:
    test = json.load(file)

def formatHeader(y):
    x = str(len(str(y))) + ":" + str(y)
    x.replace(" ", "")
    return x

async def fun(websocket, path):
    print('connected')

    with open('jason_controller.json') as file:
            jason = json.load(file)

    z = json.dumps(jason)

    status = 0

    while True:
        try:
            response = await websocket.recv()
            splittedResponse = response.split(":", 1)
            if (len(splittedResponse[1]) == int(splittedResponse[0])):
                x = json.loads(splittedResponse[1])
                print(x["A1-1"])
                if (x["A1-1"] == '0'):
                    jason["A1-1"] = 0
                elif (x["A1-1"] == '1'):
                    jason["A1-1"] = 1
                print(jason["A1-1"])
                z = json.dumps(jason)

                await websocket.send(formatHeader(z))
            else:
                print("failed")
                print(type(len(splittedResponse[1])))
                print(type(int(splittedResponse[0])))
        except:
            print('connection failed')

        

start_server = websockets.serve(fun, "localhost", 54000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()