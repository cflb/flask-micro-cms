from fastapi import FastAPI

app = FastAPI()

@app.get("/index")
def index():
    return "Pagina do index"

@app.get("/")
def home():
    return "Página inicial"

@app.get("/contato")
def contato():
    return "Página de contato"