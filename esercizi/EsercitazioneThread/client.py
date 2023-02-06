import socket
BUFFER=4096
from SalvaClient import SalvaClient
from LeggiClient import LeggiClient
def client():
    comandi=""
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 6000))
        while True:
            comandi=input("immmetti salva o immetti leggi a seconda delle operazione che vuoi fare:")
            s.send(comandi.encode("utf8"))
            if comandi=="salva":
                t1=SalvaClient(s)
                t1.run()
                t1.join()
            if comandi=="leggi":
                t=LeggiClient(s)
                messaggio=LeggiClient.run()
                t.join()
            comandi=""
if __name__ == '__main__':
    client()