from fastapi import FastAPI

from clima import buscar_clima   # importa o miolo!

app = FastAPI()


@app.get("/")
def raiz():
    return {"mensagem": "Servidor de clima no ar!"}


@app.get("/clima")
def clima(cidade: str):
    return buscar_clima(cidade)   # só chama a função do miolo