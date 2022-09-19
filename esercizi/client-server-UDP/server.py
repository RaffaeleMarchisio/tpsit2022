from socket import AF_INET,socket,SOCK_DGRAM,SOL_SOCKET,SO_BROADCAST

def chat_server(HOST,PORT,BUFFER_SIZE):
    with socket(AF_INET,SOCK_DGRAM) as s:
        s.bind((HOST,PORT))
        s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
        while True:
            msg= s.recvfrom(BUFFER_SIZE)
            print(msg[0].decode())
if __name__ == '__main__':
    HOST="0.0.0.0"
    PORT=5000
    BUFFER_SIZE=1024
    chat_server(HOST, PORT, BUFFER_SIZE)