
from flask import Flask
import os

app = Flask(__name__)
app.secret_key = '12345678'

# Importando suas rotas
from PROJETO.routes import *

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)