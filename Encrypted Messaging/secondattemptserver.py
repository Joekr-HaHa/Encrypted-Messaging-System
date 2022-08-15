import time, socket, sys
from threading import Thread
from socket import AF_INET, socket, SOCK_STREAM
from encryptionprogram import encrypt, decrypt
print("Setup server..")
time.sleep(1)
#get hostnname, ip address from socket and set port
def message_thread():
    name=input('Enter name')
    sock.listen(1)#try to locate using socket
    print('Waiting for incoming connections..')
    #get a connection from the client side
    client=conn.recv(1024)
    client=client.decode()
    print(client,'has connected')
    print('press [leave] to leave the chat room')
    conn.send(name.encode())
    while True:
        message=input('Me > ')
        if message=='[leave]':
            message='Good night..'
            conn.send(message.encode())
            print('\n')
            break
        message,keyslist=encrypt(message)
        conn.send(message.encode())
        conn.send(keyslist.encode())
        message=conn.recv(1024)
        message=message.decode()
        time.sleep(1)
        keyslist=conn.recv(1024)
        keyslist=keyslist.decode()
        message=decrypt(message,keyslist)
        print(client,'>',message)
HOST = "198.162.0.29"
PORT = 33000
PORT = int(PORT)
BUFSIZ = 1024
ADDR = (HOST, PORT)
conn = socket(AF_INET, SOCK_STREAM)
conn.connect(ADDR)

message_thr=Thread(target=message_thread)
message_thr.start()
