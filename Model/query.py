import sqlite3
from . import conectarBD

def query():
    conexao = conectarBD.conectarBanco()
    cursor = conexao.cursor()

    cursor.execute('''
    insert into categorias_transferencia (nomeCategoria, tipoTransf, emojiCategoria) values ('Moradia', 0, '🏠');
''')

    conexao.commit()

query()