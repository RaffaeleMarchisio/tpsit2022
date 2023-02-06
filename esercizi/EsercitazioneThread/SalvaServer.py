import threading
import socket
class SalvaServer(threading.Thread):
    def __init__(self,conn,info):
        threading.Thread.__init__(self)
        self.conn=conn
        self.info=info
    def run(self):
        self.info.append(self.conn.recv(4096).decode("utf8").split(";"))
        print(self.info)