
def iniziofine(func):
    def wrapper():
        print("inizio")
        func()
        print("fine")
    return wrapper()
@iniziofine
def scriviCiao():
    print("ciao")
@iniziofine
def scriviHello():
    print("hello")

