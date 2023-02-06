import threading
import socket
BUFFER=4096
class LeggiClient(threading.Thread):
    def __init__(self,s):
        threading.Thread.__init__(self)
        self.s=s
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            self.s.bind(("0.0.0.0", 5000))
            self.s.listen()
            client, addr = self.s.accept()
            messaggio = client.recv(BUFFER).decode("utf8")

        return messaggio
