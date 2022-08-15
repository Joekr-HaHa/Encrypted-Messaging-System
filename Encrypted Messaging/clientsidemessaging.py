import time, socket, sys, random
from threading import Thread
from encryptionprogram import encrypt,decrypt
print('Client Server..')
time.sleep(1)
#get the hostname, IP address from socket and set port
sock=socket.socket()
shost=socket.gethostname()
ip=socket.gethostbyname(shost)
#get information to connect with server
print(shost,'({})'.format(ip))
servhost="192.168.0.29"
#input("Enter server IP: ")
def message_thread(sock):
    name=input("Enter client name: ")
    port=1234 
    print('attempting to establish connection with server: \
    {}, ({})'.format(servhost,port))
    time.sleep(1)
    sock.connect((servhost,port))
    print("Connected..\n")
    sock.send(name.encode())
    servname=sock.recv(1024)
    servname=servname.decode()
    print('{} has joined...'.format(servname))
    print('Enter [leave] to exit')
    while True:
        message=sock.recv(1024)
        message=message.decode()
        keyslist=sock.recv(1024)
        keyslist=keyslist.decode()
        message=decrypt(message,keyslist)
        print(servname,">",message)
        message=input(str("Me > "))
        message,keyslist=encrypt(message)
        if message=="[leave]":
            message="Leaving chatroom"
            sock.send(message.encode())
            print("\n")
            break
        sock.send(message.encode())
        sock.send(keyslist.encode())
Thread(target=message_thread, args=(sock,)).start()

