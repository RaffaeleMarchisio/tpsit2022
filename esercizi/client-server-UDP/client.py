from socket import AF_INET,socket,SOCK_DGRAM,SOL_SOCKET,SO_BROADCAST
PORT=5000
HOST="192.168.88.255"
def chat_Client():
    with socket(AF_INET,SOCK_DGRAM) as s:
        s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        msg="hello world"
        msg= msg.encode('utf8')
        s.sendto(msg,(HOST,PORT))


if __name__ == '__main__':
    chat_Client()

