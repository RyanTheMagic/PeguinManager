import sqlite3
from . import conectarBD

def query():
    conexao = conectarBD.conectarBanco()
    cursor = conexao.cursor()

    cursor.execute('''
    update bancos_usuario set emojiBanco = '🧡' where bancoID = 4
''')

    conexao.commit()

query()