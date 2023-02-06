import flask
#API interfaccia che permette di fare richieste da parte di un programma
#Scraper:programmi che navigano all'interno di una pagina internet alla ricerca di contenuti
#se trova un link può decidere se seguirlo
fl=flask.Flask(__name__)
@fl.route("/somma",methods=["POST"])
def somma():
    try:
        a=int(flask.request.form.get("txta"))
        b = int(flask.request.form.get("txtb"))
        c=a+b
        return str(c)
    except:
        return "errore dati non inseriti"
@fl.route("/",methods=["GET"])
def homepage():
    return """<html>
                <body>
                    <form action="/somma" method="POST">
                        <label>primo numero<label>
                        <input type="text" id="primoNum" name="txta"><br>
                        <label>secondo numero<label>
                        <input type="text" id="seconNum" name="txtb"><br>
                        <button type="submit">Somma</button>
                    </form>
                </body>
            </html>"""

def main():
    fl.run()
if __name__ == '__main__':
    main()