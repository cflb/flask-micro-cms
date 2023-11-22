from flask import Flask

app = Flask(__name__)

@app.route("/")
def  inicio():
    return "<h1>Pagina Incial</h1>"

@app.route("/falecom")
def  fale_conosco():
    return "<h1>fale conosco</h1>"

@app.route("/sobre")
def  sobre():
    return "<h1>Sobre nossa ideia</h1>"

if "__main__" == __name__:
    app.run()