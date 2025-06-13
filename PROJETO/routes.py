from flask import render_template, redirect

from app import app



@app.route('/')
def inicio():
    return redirect('/home')


@app.route('/home')
def home():
    return render_template('homepage.html')

@app.route('/competencia')
def competencia():
    return render_template("competencia.html")

@app.route('/contato')
def contato():
    return render_template("contato.html")

@app.route('/residenciais')
def residenciais():
    return render_template("residenciais.html") 

@app.route('/comerciais')
def comerciais():
    return render_template("comerciais.html") 

@app.route('/interiores')
def interiores():
    return render_template("interiores.html") 

@app.route('/quarto')
def quarto():
    return render_template("quartos.html") 

