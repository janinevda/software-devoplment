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
                    jason["A1-1"] = 0
                elif (x["A1-1"] == '1'):
                    jason["A1-1"] = 1
                z = json.dumps(jason)

                message = formatHeader(z)

                conn.sendall(message.encode("utf-8"))