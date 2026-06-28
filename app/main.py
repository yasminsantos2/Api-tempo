from fastapi import FastAPI

app = FastAPI(title="api tempo real")

@app.get("/")
def root():
    return {"message": "api tempo real"}