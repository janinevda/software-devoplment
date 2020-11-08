import socket
import json

def formatHeader(y):
    x = str(len(str(y))) + ":" + str(y)
    x.replace(" ", "")
    return x

with open('jason_controller.json') as file:
    jason = json.load(file)

host = '127.0.0.1'
port = 54000

def changeToSame(x):
    jason["A1-1"] = x
    jason["A1-2"] = x
    jason["A1-3"] = x
    jason["A2-1"] = x
    jason["A2-2"] = x
    jason["A2-3"] = x
    jason["A2-4"] = x
    jason["A3-1"] = x
    jason["A3-2"] = x
    jason["A3-3"] = x
    jason["A3-4"] = x
    jason["A4-1"] = x
    jason["A4-2"] = x
    jason["A4-3"] = x
    jason["A4-4"] = x
    jason["A5-1"] = x
    jason["A5-2"] = x
    jason["A5-3"] = x
    jason["A5-4"] = x
    jason["A6-1"] = x
    jason["A6-2"] = x
    jason["A6-3"] = x
    jason["A6-4"] = x

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((host, port))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        print('Connected by: ', addr)
        while True:
            data = conn.recv(1024)
            data = data.decode("utf-8")
            splittedData = data.split(":", 1)
            if (len(splittedData[1]) == int(splittedData[0])):
                x = json.loads(splittedData[1])
                print(x["A1-1"])
                if (x["A1-1"] == '0'):
                    changeToSame(0)
                elif (x["A1-1"] == '1'):
                    changeToSame(1)
                z = json.dumps(jason)

                message = formatHeader(z)

                conn.sendall(message.encode("utf-8"))