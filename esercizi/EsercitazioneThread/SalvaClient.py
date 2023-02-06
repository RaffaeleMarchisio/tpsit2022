import threading
import socket
class SalvaClient(threading.Thread):
    def __init__(self,s):
        threading.Thread.__init__(self)
        self.s=s
    def run(self):
        mess = input("inserire messaggio che si vuole inviare:")
        nome_utente = input("inserire nome_utente")
        messaggio_tot = nome_utente + ";" + mess
        messaggio_tot = messaggio_tot.encode("utf8")
        self.s.send(messaggio_tot)