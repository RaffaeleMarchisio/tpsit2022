import sqlite3 as sq
import socket as s

def inserisciUtente():
    username=input("inserire nome utente:")
    password=input("inserire password:")
    data=sq.connect("UTENTI.db")
    curs=data.cursor()
    curs.execute("INSERT INTO UTENTI (username,password) VALUES (?,?)",(username,password))
    data.commit()
    data.close()
def signup():
    pass
def login(usrn,password):
    pass
def main():
    with s.socket(s.AF_INET,s.SOCK_STREAM) as s:
        s.bind(("0.0.0.0",5000))
        s.listen()
        while True:
            conn,addr=s.accept()

if __name__ == '__main__':
