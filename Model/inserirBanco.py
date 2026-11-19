import sqlite3
from . import conectarBD
import listarBancos

def inserirBanco(nome: str):
    verifBanco = False
    for banco in listarBancos.listarBancos():
        if banco['nomeBanco'].replace(" ", "").lower() == nome.replace(" ", "").lower():
            verifBanco = True

    if verifBanco:
        return False
    else:
        conexao = conectarBD.conectarBanco()
        cursor = conexao.cursor()

        cursor.execute('''
            insert into BANCOS_USUARIO (nomeBanco) values (?)
    ''', (nome,))
        conexao.commit()

        cursor.close()
        conexao.close()
        
        return True

print(inserirBanco('Pepsi'))
for banco in listarBancos.listarBancos():
    print(banco['nomeBanco'])
    print(banco['saldoBanco'])
    print('')