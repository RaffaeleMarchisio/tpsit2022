import socket


def main():
    espressione=input("di quale numero vuoi la tabellina:")
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("localhost",5000))
    client.send(espressione.encode())

    while True:
        risp=client.recv(4096)
        risp=risp.decode()
        print(risp)
if __name__ == '__main__':
    main()