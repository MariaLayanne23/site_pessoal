from flask import Flask
import os

app = Flask(__name__)
app.secret_key = '12345678'

# Aqui você pode importar suas rotas direto
from routes import *

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    server.run(host='0.0.0.0', port=port, debug=True)
