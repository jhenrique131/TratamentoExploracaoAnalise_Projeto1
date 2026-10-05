#Importa a biblioteca
import psycopg2

#Estabelece Conexão
conn = psycopg2.connect(
    host = 'localhost',
    database = 'aulas',
    user = 'postgres',
    password = '123456',
    port = 5432
)

#Cria cursor
cur = conn.cursor()

#Executa Query
cur.execute("SELECT id_cliente, nome_cliente, sobrenome_cliente, telefone FROM public.clientes;")
dados = cur.fetchall()
print(dados)

#Fecha conexão
cur.close()
conn.close()