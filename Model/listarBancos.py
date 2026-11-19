import sqlite3
from . import conectarBD

def listarBancos():
    conexao = conectarBD.conectarBanco()
    conexao.row_factory = sqlite3.Row


    cursor = conexao.cursor()

    cursor.execute('''
    select * from BANCOS_USUARIO
    ''')

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return [dict(resultado) for resultado in resultados]

for banco in listarBancos():
    print(banco['nomeBanco'])
    print(banco['saldoBanco'])
    print('')