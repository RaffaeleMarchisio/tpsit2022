import requests

from base64 import b64encode

def main():
    username = "pippo"
    password = "lippo"

    encoded = b64encode(f"{username}:{password}".encode()).decode()

    headers = {'Authorization': f'Basic {encoded}'}

    print(requests.get("http://localhost:5000/secret", headers = headers))

if __name__ == "__main__":
    main()
