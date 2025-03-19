# Criar um banco de dados e atualiza-lo

import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, inspect, text
import pandas as pd

engine = create_engine('sqlite:///:memory:')
dados = pd.read_csv('https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv',sep=',')
dados.to_sql('clientes',engine, index=False)

#Atualizações

query = 'UPDATE clientes SET Rendimento_anual=300000 WHERE ID_Cliente=6840104'
with engine.connect() as conn:
    result = conn.execute(text(query))
    conn.commit()  

query = 'DELETE FROM clientes WHERE ID_CLiente=5008809'
with engine.connect() as conn:
    result= conn.execute(text(query))
    conn.commit()

query = 'INSERT INTO clientes VALUES (6850985,33,"Doutorado","Solteiro",1,"Empregado","TI",2,290000,0,"Casa/apartamento próprio")'
with engine.connect() as conn:
    result= conn.execute(text(query))
    conn.commit()
    
print(pd.read_sql_table('clientes',engine))

