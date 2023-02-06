import threading
import socket
class LeggiServer(threading.Thread):
    def __init__(self,conn,info):
        threading.Thread.__init__(self)
        self.conn=conn
        self.info=info
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("127.0.0.1", 5000))
            s.send(':'.join(self.info[0]).encode("utf8"))
            self.info.pop(0)