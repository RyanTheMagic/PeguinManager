import sqlite3
from . import conectarBD

def especificarBanco(id: int):
    conexao = conectarBD.conectarBanco()
    conexao.row_factory = sqlite3.Row

    cursor = conexao.cursor()

    cursor.execute('''
    select
    *
    from bancos_usuario
    where
    bancos_usuario.bancoID = ?
''', (id,))

    resultado = cursor.fetchone()

    return dict(resultado)