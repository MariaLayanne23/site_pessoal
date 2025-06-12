import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='db_teste.sql',
    user='root',
    password='layanne23')

if conexao.is_connected(): #validando a conexa com o banco de dados
    print('Conectado ao banco de dados com sucesso!')
    cursor = conexao.cursor()#executar comando dentro do banco

cursor.execute('select * from tb_pessoas;')
r = cursor.fetchone()
for r in cursor:
    print(r) 
    
conexao.close()
cursor.close()



    