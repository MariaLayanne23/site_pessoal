import os
from PROJETO import server

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    env = os.environ.get('RAILWAY_ENV', 'local')  # variável que você pode definir no Railway

    if env == 'production':
        # Em produção, roda com Gunicorn (na verdade o Railway vai usar o Procfile)
        # Então aqui só deixamos pronto para rodar com Flask localmente
        print("Rodando em produção (aguardando gunicorn no Railway)")
    else:
        # Local: roda Flask direto com debug
        server.run(host='0.0.0.0', port=port, debug=True)
