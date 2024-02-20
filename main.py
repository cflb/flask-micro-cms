from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Página inicial"

@app.get("/contato")
def contato():
    return "Página de contato"