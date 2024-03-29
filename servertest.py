import socket
from _thread import *
import sys
import pickle
from BaseGame import base as Game
server="192.168.86.38"
port=5555

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)


s.listen(2)
print("Waitin for a connection, Server Started")

connected=set()
games={}
idCount=0

def threadclient(conn,p,gameId):
    global idCount
    conn.send(str.encode(str(p)))
    reply=""
    while True:
        try:
            data=conn.recv(4096).decode()
            if gameId in games:
                game=games[gameId]
                if not data:
                    break
                else:
                    if data=="reset":
                        game.reset()
                    elif data!="get":
                        game.play(p,data)
                    
                    reply=game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break
    
    print("Lost connect")
    print("Closing game", gameId)
    try: 
        del games[gameId]
    except:
        pass
    idCount-=1
    conn.close()

while True:
    conn,addr=s.accept()
    print("Connected to", addr)

    idCount+=1
    p=0
    gameId=(idCount-1)//2
    if idCount%2==1:
        games[gameId]=Game(gameId)
        print("Creating New game") 
    else:
        games[gameId].ready=True
        p=1

    start_new_thread(threadclient,(conn,p,gameId))
   