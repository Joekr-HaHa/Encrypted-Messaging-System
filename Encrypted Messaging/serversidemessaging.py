import time, socket, sys
from threading import Thread
from encryptionprogram import encrypt, decrypt
print("Setup server..")
time.sleep(1)
#get hostnname, ip address from socket and set port
sock=socket.socket()
host=socket.gethostname()
ip=socket.gethostbyname(host)
port=1234
sock.bind((host,port))
print(host,'({})'.format(ip))
def accept_requests(sock):
    conn,addr=sock.accept()
    print('recieved connection from',addr[0],'(',addr[1], ')\n')
    print('connection established. connected from: {}, ({})'.format(addr[0],addr[0]))
    Thread(target=message_thread, args=(conn,sock,)).start()
def message_thread(conn,sock):
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

if __name__ == "__main__":
    sock.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_requests, args=(sock,))
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    sock.close()

