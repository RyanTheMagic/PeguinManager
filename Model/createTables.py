import sqlite3

conexao = sqlite3.connect('bot.db')
cursor = conexao.cursor()

cursor.executescript('''
    CREATE TABLE IF NOT EXISTS BANCOS_USUARIO (
        bancoID INTEGER PRIMARY KEY AUTOINCREMENT,
        nomeBanco varchar(255) not null,
        saldoBanco REAL not null default 0,
        cofrinhoBanco REAL not null default 0
    );

    CREATE TABLE IF NOT EXISTS CATEGORIAS_TRANSFERENCIA (
        categID INTEGER PRIMARY KEY AUTOINCREMENT,
        nomeCategoria varchar(255) not null,
        tipoTransf int not null
    );
''')

conexao.commit()

cursor.close()
conexao.close()

#CREATE TABLE IF NOT EXISTS BANCOS_USUARIO (
#        bancoID INTEGER PRIMARY KEY AUTOINCREMENT,
#        nomeBanco varchar(255) not null,
#        saldoBanco REAL);