import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, inspect, text
import pandas as pd
import time

engine = create_engine('sqlite:///:memory:')
inspector = inspect(engine)
dados = pd.read_csv('C:\Marcos\Programação\Python\Alura\Python para Data Science\Pandas IO\dados\clientes_banco.csv')

# Tranasformando os dados em um banco de dados cujo nome é clientes
dados.to_sql('Clientes', engine, index=False)
#Lendo o nome da tabela
print(inspector.get_table_names())

#Selecionando todas as colunas cuja a categoria de renda é empregado e transformando em sql
query = 'SELECT * FROM Clientes WHERE Categoria_de_renda="Empregado"'
empregados = pd.read_sql(query,engine) 
empregados.to_sql('Empregados', con=engine, index=False)

#Exibindo toda a tabela e colunas especificas
print(pd.read_sql_table('Empregados', engine))
print(pd.read_sql_table('Empregados', engine,columns=['Grau_escolaridade', 'Estado_civil', 'Tamanho_familia']))

# Atualizando os dados

query = 'DELETE FROM Clientes WHERE ID_Cliente=5008804'
with engine.connect() as conn:
    result = conn.execute(text(query))
    conn.commit()  

query = 'UPDATE Clientes SET Grau_escolaridade="Ensino superior" WHERE ID_Cliente=5008808'
with engine.connect() as conn:
    result = conn.execute(text(query))
    conn.commit()  

print(pd.read_sql_table('Clientes', engine))