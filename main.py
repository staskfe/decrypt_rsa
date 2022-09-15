import json
from domain.RSA import RSA
from base64 import b64decode
from fastapi import FastAPI

app = FastAPI()


@app.get("/rsa/get_public_key")
def get_public_key():
    private_key = RSA.instance()
    public_key = private_key.get_public_key()

    return {"public_key": public_key.decode("utf-8").replace('\n', '')}


@app.post("/rsa/send_data")
def send_data(data: str):
    private_key = RSA.instance()
    data = b64decode(data)

    message = private_key.decrypt(message=data)

    return json.loads(message.decode("utf-8"))
