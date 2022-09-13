from socket import AF_INET,socket,SOCK_DGRAM,SOL_SOCKET,SO_BROADCAST
BUFFER_SIZE=1024

HOST="0.0.0.0"
PORT=5000
def chat_server():
    with socket(AF_INET,SOCK_DGRAM) as s:
        s.bind((HOST,PORT))
        s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
        msg= s.recvfrom(BUFFER_SIZE)
        print(msg[0].decode())
if __name__ == '__main__':
    chat_server()