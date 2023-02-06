
import requests
HOST = "http://127.0.0.1:5000"

def getPercorsi():
    percorsi = requests.get(HOST+ "/api/v1/percorsi")
    return percorsi

def creaPercorso():
    data={"nome":"triangolo"}
    requests.post(HOST+"/api/v1/percorsi",json=data)

def main(): 
    percorsi=getPercorsi()
    creaPercorso()
    print(percorsi.content)

if __name__ == "__main__":
    main()