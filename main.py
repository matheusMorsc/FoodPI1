import json
from unicodedata import name
import requests
import pandas as pd
import psycopg2
from fastapi import FastAPI


app = FastAPI()

def conecta_db():
    con1 = psycopg2.connect(host='localhost',
                          database='foodpi',
                          user='postgres',
                          password='00019008')
    return con1

# Função Consulta Tabela Banco
def consulta_db(sql):
    con = conecta_db()
    cur = con.cursor()
    cur.execute(sql)
    recset = cur.fetchall()
    registros = []
    for rec in recset:
        registros.append(rec)
    con.close()
    return registros


@app.get("/")
def home():
    return "É assim que era pra funcionar?"

@app.get("/usuarios")
def usr():
    reg = consulta_db('select * from usuarios')
    df_bd = pd.DataFrame(reg, columns=['uId','uNome', 'uTelefone','uEndereco', 'uEmail', 'uUsername', 'uSenha'])
    print(df_bd)

    return reg

@app.get("/user1/{uId_usr}")
def usr(uId_usr:str):
    sql = "select * from usuarios where id = "+uId_usr
    reg = consulta_db(sql)
    df_bd = pd.DataFrame(reg, columns=['uId','uNome', 'uTelefone','uEndereco', 'uEmail', 'uUsername', 'uSenha'])
    print(df_bd)

    return reg


#@app.get("/user2/{codigo_usr},{nome}")
#def usr(codigo_usr:str,nome : str):
 #   sql = "select * from cliente where codigo = "+codigo_usr+" AND nome = '"+nome+"'"
  #  reg = consulta_db(sql)
   # df_bd = pd.DataFrame(reg, columns=['codigo','nome','endereco', 'telefone'])
    #print(df_bd)

    #return reg

reg = consulta_db('select * from usuarios')
print(reg)