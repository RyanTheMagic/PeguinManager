import sqlite3
from . import conectarBD

def listarCategoriasTransf():
    conexao = conectarBD.conectarBanco()
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()

    cursor.execute('''
    SELECT * FROM CATEGORIAS_TRANSFERENCIA
''')

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return [dict(resultado) for resultado in resultados]