import random
import socket
import struct
import math
HOST="127.0.0.1"
PORT=5000
BUFFER=1024
def potenza(x,n,m):
    if n<0:
        raise Exception("n")
    res=0
    if n==0:
        res=1
    elif n%2==0:
        res=potenza(x,n//2,m)
        res=(res*res)%m
    elif n%2!=0:
        res=potenza(x,(n-1)//2,m)
        res=(res*res*x)%m
    return res

def main():
    generatore = 2
    modulo=11
    a = random.randint(1, 10)
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        while True:
            t=b''
            numero_elevato1=potenza(generatore,a,modulo)
            s.sendall(numero_elevato1.to_bytes(1000,"big"))
            numero_elevato2=s.recv(BUFFER)
            numero_elevato2=int.from_bytes(numero_elevato2,"big")
            numero_finale=math.pow(numero_elevato2,a)
            print(numero_finale)

if __name__ == '__main__':
    main()
