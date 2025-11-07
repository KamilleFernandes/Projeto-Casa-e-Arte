from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def home():
    return 'render_template("./template/index.html")'

@app.route("/sobre.html")
def home():
    return 'render_template("sobre.html")'

@app.route("/contato.html")
def home():
    return 'render_template("contato.html")'
