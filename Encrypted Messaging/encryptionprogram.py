import random
alphabet="abcdefghijklmnopqrstuvwxyz"
'''message=input("Please enter a message: ")'''
def encrypt(message):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    newMessage=""
    keys=""
    keyslist=[]
    for i in message:
        if i.lower() in alphabet:
            pos=alphabet.find(i.lower())
            key=random.randint(0,30)
            keyslist.append(key)
            newPosition=(pos+key)
            while newPosition <0 or newPosition >25:
                if newPosition>25:
                    newPosition-=25
                if newPosition<0:
                    newPosition+=25
            newCharacter=alphabet[newPosition]
            newMessage+=newCharacter

        else:
            newMessage+=i
            keyslist.append(100)
    for i in range(len(keyslist)):
        if i != (len(keyslist)-1):
            keys+=(str(keyslist[i])+",")
        else:
            keys+=str(keyslist[i])
    #print("New Message: ",newMessage,"Keys: ",keys)
    return newMessage,keys
decryptMessage=""
def decrypt(newMessage,keyslist):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    acpos=0
    decryptMessage=""
    keys=keyslist.split(",")
    keys = list(map(int, keys))
    #delete empty
    '''for x in range(len(keys)-2):
        if keys[x]=="" or " ":
            keys.pop(x)'''
    for i in newMessage:
        pos=alphabet.find((i.lower()))
        key=keys[acpos]
        pos=int(pos)
        key=int(key)
        if keys[acpos]!=100:
            newPosition=(pos-key)
            while newPosition <0 or newPosition >25:
                    if newPosition>25:
                        newPosition-=25
                    if newPosition<0:
                        newPosition+=25
            newCharacter=alphabet[newPosition]
            decryptMessage+=newCharacter
        else:
            decryptMessage+=" "
        if i !=newMessage[len(newMessage)-1]:
            acpos+=1
    return str(decryptMessage)


