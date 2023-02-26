"""Effettua la richiesta di creazione di un utente
"""
import requests

from base64 import b64encode

def main():
    username = "pippo"
    password = "lippo"

    print(requests.post("http://localhost:5000/signup",
                        json={
                            "nome": "Pippo Lippo",
                            "username": "pippo",
                            "password": "password"
                            }
                        ))

if __name__ == "__main__":
    main()
