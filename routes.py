from flask import render_template, redirect
from PROJETO import server
import feedparser



@server.route('/')
def inicio():
    return redirect('/home')


@server.route('/home')
def home():
    return render_template('homepage.html')

@server.route('/competencia')
def competencia():
    return render_template("competencia.html")

@server.route('/contato')
def contato():
    return render_template("contato.html")

@server.route('/residenciais')
def residenciais():
    return render_template("residenciais.html") 

@server.route('/comerciais')
def comerciais():
    return render_template("comerciais.html") 

@server.route('/interiores')
def interiores():
    return render_template("interiores.html") 

@server.route('/quarto')
def quarto():
    return render_template("quartos.html") 

