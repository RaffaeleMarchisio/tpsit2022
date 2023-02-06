from threading import Thread
class Incrementa():
    def __init__(self,x):
        self.x=x
    def inc(self):
        for _ in range(100000):
            self.x = self.x + 1
class ThreadIncrementa(Thread):
    def __init__(self,Incrementa):
        Thread.__init__(self)
        self.Incrementa=Incrementa
    def run(self):
        Incrementa.inc(self)
def main():
    thrs = []
    x=Incrementa(0)
    for t in range(100):
        thrs.append(ThreadIncrementa(x))
    for t in thrs:
        t.start()
    for t in thrs:
        t.join()


    print(x.x)


if __name__ == '__main__':
    main()