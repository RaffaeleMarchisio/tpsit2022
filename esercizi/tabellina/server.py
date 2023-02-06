import socket
import threading
import time

def serverFun(conn,addr):
    print(f"connesso con {addr}")
    mess = conn.recv(4096)
    mess = mess.decode()
    risultato = int(mess)
    #tab=[i*risultato for i in range(1,11)]
    for i in range(1,11):
        tab=str(risultato*i)
        inv=str(risultato)+"*"+str(i)+"="+tab+"\n"
        print(inv)
        conn.send(inv.encode("utf8"))
    conn.send("exit".encode("utf8"))
    print("exit")

def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(("0.0.0.0",5000))
    server.listen()
    while True:
        conn,addr=server.accept()
        t=threading.Thread(target=serverFun,args=(conn,addr,))
        t.start()

if __name__ == '__main__':
    main()