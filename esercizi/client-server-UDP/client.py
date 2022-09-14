from socket import AF_INET,socket,SOCK_DGRAM,SOL_SOCKET,SO_BROADCAST
PORT=5000
HOST="127.0.0.1"
def chat_Client():
    with socket(AF_INET,SOCK_DGRAM) as s:
        s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        while True:
            msg=input("messaggio")
            msg= msg.encode('utf8')
            s.sendto(msg,(HOST,PORT))
            print("messaggio inviato")


if __name__ == '__main__':
    chat_Client()

