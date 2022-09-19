from socket import AF_INET,socket,SOCK_DGRAM,SOL_SOCKET,SO_BROADCAST

def chat_Client(HOST,PORT):
    with socket(AF_INET,SOCK_DGRAM) as s:
        s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        while True:
            msg=input("messaggio")
            msg= msg.encode('utf8')
            s.sendto(msg,(HOST,PORT))
            print("messaggio inviato")


if __name__ == '__main__':
    HOST=input("inserire l'indirizzo ip dell'host:")
    PORT=int(input("inserire porta:"))
    chat_Client(HOST, PORT)

