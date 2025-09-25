from flask import Flask, render_template, redirect, url_for
import json

app = Flask(__name__)

# Dados gerais de SEO e autor
DEV_NAME = "Maria Layanne"
PORTFOLIO_OWNER = "Ana Karolliny"
PORTFOLIO_IMAGE = "imagens/karol.png"

# Rota inicial
@app.route('/')
def inicio():
    return redirect('/homepage')

# Home
@app.route('/homepage')
def homepage():
    seo = {
        "title": f"AK Arquitetura | Sobre {PORTFOLIO_OWNER}",
        "description": f"Conheça o trabalho de {PORTFOLIO_OWNER} em arquitetura, interiores e design.",
        "url": url_for('homepage', _external=True),
        "image": url_for('static', filename=PORTFOLIO_IMAGE, _external=True)
    }
    return render_template("homepage.html", seo=seo)

# Competências
@app.route('/competencia')
def competencia():
    with open("linksRefs.json", encoding="utf-8") as f:
        data = json.load(f)
    linksRefs = data["linksRefs"]

    seo = {
        "title": f"AK Arquitetura | Competências de {PORTFOLIO_OWNER}",
        "description": f"Explore as habilidades técnicas e criativas de {PORTFOLIO_OWNER} em arquitetura, cenografia e figurino.",
        "url": url_for('competencia', _external=True),
        "image": url_for('static', filename=PORTFOLIO_IMAGE, _external=True)
    }
    return render_template("competencia.html", linksRefs=linksRefs, seo=seo)

# Contato
@app.route('/contato')
def contato():
    with open("linkscontatos.json", encoding="utf-8") as f:
        data = json.load(f)
    linksC = data["linksC"]

    seo = {
        "title": f"AK Arquitetura | Contate {PORTFOLIO_OWNER}",
        "description": f"Entre em contato com {PORTFOLIO_OWNER} para projetos de arquitetura e interiores.",
        "url": url_for('contato', _external=True),
        "image": url_for('static', filename=PORTFOLIO_IMAGE, _external=True)
    }
    return render_template("contato.html", linksC=linksC, seo=seo)

# Projetos Residenciais
@app.route('/residenciais')
def residenciais():
    seo = {
        "title": f"AK Arquitetura | Projetos Residenciais de {PORTFOLIO_OWNER}",
        "description": f"Confira os projetos residenciais desenvolvidos por {PORTFOLIO_OWNER}.",
        "url": url_for('residenciais', _external=True),
        "image": url_for('static', filename=PORTFOLIO_IMAGE, _external=True)
    }
    return render_template("residenciais.html", seo=seo)

# Projetos Comerciais
@app.route('/comerciais')
def comerciais():
    seo = {
        "title": f"AK Arquitetura | Projetos Comerciais de {PORTFOLIO_OWNER}",
        "description": f"Explore os projetos comerciais e corporativos de {PORTFOLIO_OWNER}.",
        "url": url_for('comerciais', _external=True),
        "image": url_for('static', filename=PORTFOLIO_IMAGE, _external=True)
    }
    return render_template("comerciais.html", seo=seo)

# Interiores
@app.route('/interiores')
def interiores():
    seo = {
        "title": f"AK Arquitetura | Interiores de {PORTFOLIO_OWNER}",
        "description": f"Veja os projetos de interiores e ambientação criados por {PORTFOLIO_OWNER}.",
        "url": url_for('interiores', _external=True),
        "image": url_for('static', filename=PORTFOLIO_IMAGE, _external=True)
    }
    return render_template("interiores.html", seo=seo)

# Quartos
@app.route('/quarto')
def quarto():
    seo = {
        "title": f"AK Arquitetura | Quartos Projetados por {PORTFOLIO_OWNER}",
        "description": f"Projetos de quartos com design exclusivo assinados por {PORTFOLIO_OWNER}.",
        "url": url_for('quarto', _external=True),
        "image": url_for('static', filename=PORTFOLIO_IMAGE, _external=True)
    }
    return render_template("quartos.html", seo=seo)

if __name__ == '__main__':
    app.run(debug=True)
