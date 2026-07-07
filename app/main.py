from fastapi import FastAPI

from app.services import buscar_clima

app = FastAPI()


@app.get("/")
def raiz():
    return {"mensagem": "Servidor de clima no ar!"}


@app.get("/clima")
def clima(cidade: str):
    return buscar_clima(cidade)