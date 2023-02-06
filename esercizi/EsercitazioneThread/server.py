import socket
BUFFER=4096
"""confserver.PORT"""
from LeggiServer import LeggiServer
from SalvaServer import SalvaServer
def server(info):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind(("0.0.0.0", 6000))
        s.listen()
        client, addr = s.accept()
        while True:
            mes=client.recv(BUFFER).decode("utf8")
            if mes=="salva":
                t1=SalvaServer(client,info)
                SalvaServer.run()
                t1.join()
            if mes=="leggi":
                t=LeggiServer(client,info)
                LeggiServer.run()
                t.join()

if __name__ == '__main__':
    info=[]
    server(info)