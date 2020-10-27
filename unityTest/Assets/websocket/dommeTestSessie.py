import socket
import json
import time

def formatHeader(y):
    x = str(len(str(y))) + ":" + str(y)
    x.replace(" ", "")
    return x

with open('jason_controller.json') as file:
    jason = json.load(file)

host = '127.0.0.1'
port = 54000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((host, port))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        print('Connected by: ', addr)
        while True:
            jason["A1-1"] = 0
            print(jason["A1-1"])
            time.sleep(1)
            z = json.dumps(jason)

            message = formatHeader(z)

            conn.sendall(message.encode("utf-8"))



            jason["A1-1"] = 1
            print(jason["A1-1"])
            time.sleep(1)
            z = json.dumps(jason)

            message = formatHeader(z)

            conn.sendall(message.encode("utf-8"))