from flask import Flask
import os

app = Flask(__name__, template_folder="PROJETO/templates", static_folder="PROJETO/static")
app.secret_key = '12345678'

# Importando rotas do pacote
from PROJETO.routes import *

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
