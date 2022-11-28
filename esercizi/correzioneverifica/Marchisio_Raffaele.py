import socket
import sys
BUF_SIZE=4096
class Options:
    def __init__(self,portaserver,host,porta):
        self.portaserver=int(portaserver)
        self.host=host
        self.porta=int(porta)
    def get_socket(self):
        return self.host,self.porta



def richiedi_dati(tupla,percorso):
    data=b''
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect(tupla)
        s.sendall(f"GET {percorso} HTTP/1.0\n\n".encode("utf8"))
        data1=s.recv(BUF_SIZE)
        return data1
def main(args):
    data=None
    opt=Options(args[1],args[2],args[3])
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0',opt.portaserver))
        s.listen()
        while True:
            client,client_address= s.accept()
            data=client.recv(BUF_SIZE)
            data=data.decode('utf8')
            campi=data.split(" ")
            data1=richiedi_dati(opt.get_socket(),campi[1])
            print(data)
if __name__ == '__main__':
    main(sys.argv)
#def ServerTCP(host,port,buffer):
 #   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  #      s.connect((host,8000))
   #     msg=input("inserire richiesta HTTP:")
    #    print(msg)
     #   s.sendall(msg.encode())
      #  msg = s.recv(buffer)
#        print(msg)
 #   with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
  #      s.bind((host,8000))
   #     print('connesso')
    #    s.listen()
     #   client,adress=s.accept()
      #  msg=client.recv(buffer)
       # print(msg)
