import sqlite3

def transferenciaBanco(valor: float, idBanco: int):
    conexao = sqlite3.connect('bot.db')
    cursor = conexao.cursor()

    cursor.execute('''
    UPDATE BANCOS_USUARIO set saldoBanco = saldoBanco + ? where bancoID = ?
''', (valor, idBanco))

    conexao.commit()
    cursor.close()
    conexao.close()