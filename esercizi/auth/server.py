from flask import request, Flask, jsonify

app = Flask(__name__)

# TODO: Aggiungere una tabella
# Utenti (nome, username, password, dataCreazione)


# Aggiungere un URL per registrarsi
@app.route('/signup', methods=["POST"])
def signup():
    content = request.json

    # TODO: Aggiungo alla tabella `utenti`
    # un nuovo utente con dati
    # - content["nome"]
    # - content["username"]
    # - content["password"]

    return jsonify({"success": True})


# TODO: Proteggere i percorsi che permettono di creare nuovi percorsi
# e eseguire un percorso tramite autenticazione Basic
@app.route('/secret')
def secret():
    print(request)
    print(request.headers)
    print(request.authorization)
    if request.authorization:
        # TODO: verificare request.authorization.username
        # e request.authorization.password facendo una query
        # al DB
        return jsonify({"data": f"Autenticato come {request.authorization.username}"})
    else:
        return jsonify({"error": "autenticazione fallita"}), 401

if __name__ == "__main__":
    app.run()

