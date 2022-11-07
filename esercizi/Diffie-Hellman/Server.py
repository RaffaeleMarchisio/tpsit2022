from socket import AF_INET,socket,SOCK_STREAM,SOL_SOCKET,SO_BROADCAST
import random

def potenza(x,n):
    if n<0:
        raise Exception("n")
    res=0
    if n==0:
        res=1
    elif n%2==0:
        res=potenza(x,n//2)
        res=res*res
    elif n%2!=0:
        res=potenza(x,(n-1)//2)
        res=res*res*x
    return res

def chat_server(msgn,HOST,PORT,BUFFER_SIZE):
    b = random.randint(1, 10)
    g=2
    m=11
    with socket(AF_INET,SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen()
        client,clientaddr=s.accept()
        while True:
            numero_elevato1 = potenza(g, b) % m
            client.sendall(numero_elevato1.to_bytes(1,"big"))
            numero_elevato2=client.recv(BUFFER_SIZE)
            numero_elevato2=int.from_bytes(numero_elevato2,'big')
            numero_finale=potenza(numero_elevato2,b)
            print(numero_finale)
if __name__ == '__main__':
    msgn=""
    HOST="0.0.0.0"
    PORT=5000
    BUFFER_SIZE=1024
    chat_server(msgn,HOST, PORT, BUFFER_SIZE)