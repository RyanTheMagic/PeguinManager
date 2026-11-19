import sqlite3

bd = 'bot.db'

def conectarBanco():
    conexao = sqlite3.connect(bd)
    return conexao