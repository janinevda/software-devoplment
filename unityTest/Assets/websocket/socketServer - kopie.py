import socket
import json
import time

import random

#y = True
y = False
while y == True:
    receiveFromClient = input("ontvang van simulator? y/n \n")
    if receiveFromClient != "y":
        if receiveFromClient != "n":
            print("verkeerde input, probeer opnieuw.")
        else:
            y = False
    else:
        y = False

def formatHeader(y):
    x = str(len(str(y))) + ":" + str(y)
    x.replace(" ", "")
    return x

with open('jason_controller.json') as file:
    jason = json.load(file)

host = '127.0.0.1'
port = 54000

def receiveFromSimulator():
    Group01A_array = ["A1-1", "A1-2", "A3-1", "A3-2", "A3-3", "A3-4"]
    Group01B_array = ["A1-1", "A1-2", "A2-1", "A2-2", "A3-3", "A4-4"]
    Group01C_array = ["A1-1", "A1-2", "A1-3", "A2-1", "A2-2"]
    Group02A_array = ["A2-1", "A2-2", "A2-3", "A2-4", "A3-3", "A3-4"]
    Group02B_array = ["A2-1", "A2-2", "A1-1", "A1-2", "A3-3", "A3-4"]

    TrafficLightsThatHasCarsEast = []
    #cars
    jason["A1-1"] = random.randint(0,1)
    jason["A1-2"] = random.randint(0,1)
    jason["A1-3"] = random.randint(0,1)
    jason["A2-1"] = random.randint(0,1)
    jason["A2-2"] = random.randint(0,1)
    jason["A2-3"] = random.randint(0,1)
    jason["A2-4"] = random.randint(0,1)
    jason["A3-1"] = random.randint(0,1)
    jason["A3-2"] = random.randint(0,1)
    jason["A3-3"] = random.randint(0,1)
    jason["A3-4"] = random.randint(0,1)
    jason["A4-1"] = random.randint(0,1)
    jason["A4-2"] = random.randint(0,1)
    jason["A4-3"] = random.randint(0,1)
    jason["A4-4"] = random.randint(0,1)
    jason["A5-1"] = random.randint(0,1)
    jason["A5-2"] = random.randint(0,1)
    jason["A5-3"] = random.randint(0,1)
    jason["A5-4"] = random.randint(0,1)
    jason["A6-1"] = random.randint(0,1)
    jason["A6-2"] = random.randint(0,1)
    jason["A6-3"] = random.randint(0,1)
    jason["A6-4"] = random.randint(0,1)

    for x in jason :
        if(jason[x] == 1):
            TrafficLightsThatHasCarsEast.append(x)
            
    resultsEast = []
    amountOfTrafficlightMatchesEast = []
    
    for i in range(5):
        resultsEast.append([])
        amountOfTrafficlightMatchesEast.append([])

    for i in TrafficLightsThatHasCarsEast:
        resultsEast[0].append(Group01A_array.count(i))
        resultsEast[1].append(Group01B_array.count(i))
        resultsEast[2].append(Group01C_array.count(i))
        resultsEast[3].append(Group02A_array.count(i))
        resultsEast[4].append(Group02B_array.count(i))
    
    amountOfTrafficlightMatchesEast[0].append("groep01A")
    amountOfTrafficlightMatchesEast[1].append("groep01B")
    amountOfTrafficlightMatchesEast[2].append("groep01C")
    amountOfTrafficlightMatchesEast[3].append("groep02A")
    amountOfTrafficlightMatchesEast[4].append("groep02B")
    
    for i in range(5):
        count = 0
        for j in resultsEast[i]:
            if(j == 1):
                count += 1
        amountOfTrafficlightMatchesEast[i].append(count)

    highestAmountOfMatchesGroupNameEast = ""
    highestAmountOfMatchesNumberEast = 0

    for i in range(len(amountOfTrafficlightMatchesEast)):
        if(amountOfTrafficlightMatchesEast[i][1] > highestAmountOfMatchesNumberEast):
            highestAmountOfMatchesNumberEast = amountOfTrafficlightMatchesEast[i][1]
            highestAmountOfMatchesGroupNameEast = amountOfTrafficlightMatchesEast[i][0]

    groepAllRed()
    if(highestAmountOfMatchesGroupNameEast == "groep01A"):
        Group01A()
    elif(highestAmountOfMatchesGroupNameEast == "groep01B"):
        Group01B()
    elif(highestAmountOfMatchesGroupNameEast == "groep01C"):
        Group01C()
    elif(highestAmountOfMatchesGroupNameEast == "groep02A"):
        Group02A()
    elif(highestAmountOfMatchesGroupNameEast == "groep02B"):
        Group02B()
    else:
        print("nothing")


def Group01A():
    jason["A1-1"] = 1
    jason["A1-2"] = 1
    jason["A3-1"] = 1
    jason["A3-2"] = 1
    jason["A3-3"] = 1
    jason["A3-4"] = 1

def Group01B():
    jason["A1-1"] = 1
    jason["A1-2"] = 1
    jason["A2-1"] = 1
    jason["A2-2"] = 1
    jason["A3-3"] = 1
    jason["A4-4"] = 1

def Group01C():
    jason["A1-1"] = 1
    jason["A1-2"] = 1
    jason["A1-3"] = 1
    jason["A2-1"] = 1
    jason["A2-2"] = 1

def Group02A():
    jason["A2-1"] = 1
    jason["A2-2"] = 1
    jason["A2-3"] = 1
    jason["A2-4"] = 1
    jason["A3-3"] = 1
    jason["A3-4"] = 1

def Group02B():
    jason["A2-1"] = 1
    jason["A2-2"] = 1
    jason["A1-1"] = 1
    jason["A1-2"] = 1
    jason["A3-3"] = 1
    jason["A3-4"] = 1
    

    
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

def groepAllRed():
    jason["A1-1"] = "0"
    jason["A1-2"] = "0"
    jason["A1-3"] = "0"
    jason["A2-1"] = "0"
    jason["A2-2"] = "0"
    jason["A2-3"] = "0"
    jason["A2-4"] = "0"
    jason["A3-1"] = "0"
    jason["A3-2"] = "0"
    jason["A3-3"] = "0"
    jason["A3-4"] = "0"
    jason["A4-1"] = "0"
    jason["A4-2"] = "0"
    jason["A4-3"] = "0"
    jason["A4-4"] = "0"
    jason["A5-1"] = "0"
    jason["A5-2"] = "0"
    jason["A5-3"] = "0"
    jason["A5-4"] = "0"
    jason["A6-1"] = "0"
    jason["A6-2"] = "0"
    jason["A6-3"] = "0"
    jason["A6-4"] = "0"

def groepO1A():
    jason["A1-1"] = "1"
    jason["A1-2"] = "1"
    jason["A1-3"] = "0"
    jason["A2-1"] = "0"
    jason["A2-2"] = "0"
    jason["A2-3"] = "0"
    jason["A2-4"] = "0"
    jason["A3-1"] = "1"
    jason["A3-2"] = "1"
    jason["A3-3"] = "1"
    jason["A3-4"] = "1"
    jason["A4-1"] = "0"
    jason["A4-2"] = "0"
    jason["A4-3"] = "0"
    jason["A4-4"] = "0"
    jason["A5-1"] = "0"
    jason["A5-2"] = "0"
    jason["A5-3"] = "0"
    jason["A5-4"] = "0"
    jason["A6-1"] = "0"
    jason["A6-2"] = "0"
    jason["A6-3"] = "0"
    jason["A6-4"] = "0"

def groepO1B():
    jason["A1-1"] = "1"
    jason["A1-2"] = "1"
    jason["A1-3"] = "0"
    jason["A2-1"] = "1"
    jason["A2-2"] = "1"
    jason["A2-3"] = "0"
    jason["A2-4"] = "0"
    jason["A3-1"] = "0"
    jason["A3-2"] = "0"
    jason["A3-3"] = "1"
    jason["A3-4"] = "1"
    jason["A4-1"] = "0"
    jason["A4-2"] = "0"
    jason["A4-3"] = "0"
    jason["A4-4"] = "0"
    jason["A5-1"] = "0"
    jason["A5-2"] = "0"
    jason["A5-3"] = "0"
    jason["A5-4"] = "0"
    jason["A6-1"] = "0"
    jason["A6-2"] = "0"
    jason["A6-3"] = "0"
    jason["A6-4"] = "0"

def groepO1C():
    jason["A1-1"] = "1"
    jason["A1-2"] = "1"
    jason["A1-3"] = "1"
    jason["A2-1"] = "1"
    jason["A2-2"] = "1"
    jason["A2-3"] = "0"
    jason["A2-4"] = "0"
    jason["A3-1"] = "0"
    jason["A3-2"] = "0"
    jason["A3-3"] = "0"
    jason["A3-4"] = "0"
    jason["A4-1"] = "0"
    jason["A4-2"] = "0"
    jason["A4-3"] = "0"
    jason["A4-4"] = "0"
    jason["A5-1"] = "0"
    jason["A5-2"] = "0"
    jason["A5-3"] = "0"
    jason["A5-4"] = "0"
    jason["A6-1"] = "0"
    jason["A6-2"] = "0"
    jason["A6-3"] = "0"
    jason["A6-4"] = "0"

def groepO3A():
    jason["A1-1"] = "0"
    jason["A1-2"] = "0"
    jason["A1-3"] = "0"
    jason["A2-1"] = "1"
    jason["A2-2"] = "1"
    jason["A2-3"] = "1"
    jason["A2-4"] = "1"
    jason["A3-1"] = "0"
    jason["A3-2"] = "0"
    jason["A3-3"] = "1"
    jason["A3-4"] = "1"
    jason["A4-1"] = "0"
    jason["A4-2"] = "0"
    jason["A4-3"] = "0"
    jason["A4-4"] = "0"
    jason["A5-1"] = "0"
    jason["A5-2"] = "0"
    jason["A5-3"] = "0"
    jason["A5-4"] = "0"
    jason["A6-1"] = "0"
    jason["A6-2"] = "0"
    jason["A6-3"] = "0"
    jason["A6-4"] = "0"

def groepO3C():
    jason["A1-1"] = "1"
    jason["A1-2"] = "1"
    jason["A1-3"] = "0"
    jason["A2-1"] = "1"
    jason["A2-2"] = "1"
    jason["A2-3"] = "0"
    jason["A2-4"] = "0"
    jason["A3-1"] = "0"
    jason["A3-2"] = "0"
    jason["A3-3"] = "1"
    jason["A3-4"] = "1"
    jason["A4-1"] = "0"
    jason["A4-2"] = "0"
    jason["A4-3"] = "0"
    jason["A4-4"] = "0"
    jason["A5-1"] = "0"
    jason["A5-2"] = "0"
    jason["A5-3"] = "0"
    jason["A5-4"] = "0"
    jason["A6-1"] = "0"
    jason["A6-2"] = "0"
    jason["A6-3"] = "0"
    jason["A6-4"] = "0"

def groepW1A():
    jason["A1-1"] = "0"
    jason["A1-2"] = "0"
    jason["A1-3"] = "0"
    jason["A2-1"] = "0"
    jason["A2-2"] = "0"
    jason["A2-3"] = "0"
    jason["A2-4"] = "0"
    jason["A3-1"] = "0"
    jason["A3-2"] = "0"
    jason["A3-3"] = "0"
    jason["A3-4"] = "0"
    jason["A4-1"] = "1"
    jason["A4-2"] = "1"
    jason["A4-3"] = "1"
    jason["A4-4"] = "1"
    jason["A5-1"] = "0"
    jason["A5-2"] = "0"
    jason["A5-3"] = "1"
    jason["A5-4"] = "1"
    jason["A6-1"] = "0"
    jason["A6-2"] = "0"
    jason["A6-3"] = "0"
    jason["A6-4"] = "0"

def groepW2A():
    jason["A1-1"] = "0"
    jason["A1-2"] = "0"
    jason["A1-3"] = "0"
    jason["A2-1"] = "0"
    jason["A2-2"] = "0"
    jason["A2-3"] = "0"
    jason["A2-4"] = "0"
    jason["A3-1"] = "0"
    jason["A3-2"] = "0"
    jason["A3-3"] = "0"
    jason["A3-4"] = "0"
    jason["A4-1"] = "0"
    jason["A4-2"] = "0"
    jason["A4-3"] = "1"
    jason["A4-4"] = "1"
    jason["A5-1"] = "0"
    jason["A5-2"] = "0"
    jason["A5-3"] = "1"
    jason["A5-4"] = "1"
    jason["A6-1"] = "1"
    jason["A6-2"] = "1"
    jason["A6-3"] = "0"
    jason["A6-4"] = "0"

def groepW2B():
    jason["A1-1"] = "0"
    jason["A1-2"] = "0"
    jason["A1-3"] = "0"
    jason["A2-1"] = "0"
    jason["A2-2"] = "0"
    jason["A2-3"] = "0"
    jason["A2-4"] = "0"
    jason["A3-1"] = "0"
    jason["A3-2"] = "0"
    jason["A3-3"] = "0"
    jason["A3-4"] = "0"
    jason["A4-1"] = "0"
    jason["A4-2"] = "0"
    jason["A4-3"] = "1"
    jason["A4-4"] = "1"
    jason["A5-1"] = "0"
    jason["A5-2"] = "0"
    jason["A5-3"] = "0"
    jason["A5-4"] = "0"
    jason["A6-1"] = "1"
    jason["A6-2"] = "1"
    jason["A6-3"] = "1"
    jason["A6-4"] = "1"

def groepW3A():
    jason["A1-1"] = "0"
    jason["A1-2"] = "0"
    jason["A1-3"] = "0"
    jason["A2-1"] = "0"
    jason["A2-2"] = "0"
    jason["A2-3"] = "0"
    jason["A2-4"] = "0"
    jason["A3-1"] = "0"
    jason["A3-2"] = "0"
    jason["A3-3"] = "0"
    jason["A3-4"] = "0"
    jason["A4-1"] = "0"
    jason["A4-2"] = "0"
    jason["A4-3"] = "0"
    jason["A4-4"] = "0"
    jason["A5-1"] = "1"
    jason["A5-2"] = "1"
    jason["A5-3"] = "1"
    jason["A5-4"] = "1"
    jason["A6-1"] = "1"
    jason["A6-2"] = "1"
    jason["A6-3"] = "0"
    jason["A6-4"] = "0"
    
receiveFromSimulator()
print(jason)
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    #sock.bind((host, port))
    #sock.listen()
    #conn, addr = sock.accept()
    #with conn:
    #    print('Connected by: ', addr)
    #    while True:
    #        if receiveFromClient == "y":
                #data = conn.recv(1024)
                #data = data.decode("utf-8")
                #splittedData = data.split(":", 1)
                #if (len(splittedData[1]) == int(splittedData[0])):
                #    x = json.loads(splittedData[1])
                #    print(splittedData[1])
                #    print(x["A1-1"])
                #    if (x["A1-1"] == '0'):
                #        changeToSame(0)
                #    elif (x["A1-1"] == '1'):
                #        changeToSame(1)
                #    z = json.dumps(jason)

                #    message = formatHeader(z)

                #    conn.sendall(message.encode("utf-8"))
     #       else:
     #           sleepTime = 20

     #           groepAllRed()
     #           z = json.dumps(jason)
     #           message = formatHeader(z)
     #           conn.sendall(message.encode("utf-8"))
     #           time.sleep(sleepTime)
     #           print("0")

                #groepO1A()
                #z = json.dumps(jason)
                #message = formatHeader(z)
                #conn.sendall(message.encode("utf-8"))
                #time.sleep(sleepTime)
                #print("1")

                #groepO1B()
                #z = json.dumps(jason)
                #message = formatHeader(z)
                #conn.sendall(message.encode("utf-8"))
                #time.sleep(sleepTime)
                #print("2")

                #groepO1C()
                #z = json.dumps(jason)
                #message = formatHeader(z)
                #conn.sendall(message.encode("utf-8"))
                #time.sleep(sleepTime)
                #print("3")

                #groepO3A()
                #z = json.dumps(jason)
                #message = formatHeader(z)
                #conn.sendall(message.encode("utf-8"))
                #time.sleep(sleepTime)
                #print("4")

                #groepO3C()
                #z = json.dumps(jason)
                #message = formatHeader(z)
                #conn.sendall(message.encode("utf-8"))
                #time.sleep(sleepTime)
                #print("5")

                #groepW1A()
                #z = json.dumps(jason)
                #message = formatHeader(z)
                #conn.sendall(message.encode("utf-8"))
                #time.sleep(sleepTime)
                #print("6")

                #groepW2A()
                #z = json.dumps(jason)
                #message = formatHeader(z)
                #conn.sendall(message.encode("utf-8"))
                #time.sleep(sleepTime)
                #print("7")

                #groepW2B()
                #z = json.dumps(jason)
                #message = formatHeader(z)
                #conn.sendall(message.encode("utf-8"))
                #time.sleep(sleepTime)
                #print("8")

                #groepW3A()
                #z = json.dumps(jason)
                #message = formatHeader(z)
                #conn.sendall(message.encode("utf-8"))
                #time.sleep(sleepTime)
                #print("9")
