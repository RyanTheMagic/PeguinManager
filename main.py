import os
from dotenv import load_dotenv
import telebot
from telebot import types
from Model.transferenciaBanco import transferenciaBanco
from Model.listarBancos import listarBancos

load_dotenv()

bot = telebot.TeleBot(os.getenv("tokenAPI"))

@bot.message_handler(["menu"])
def mostrar_menu(msg:types.Message):
    tecladoMenu = types.InlineKeyboardMarkup(row_width=2)

    botao_nome = types.InlineKeyboardButton(
        "Gerenciar Bancos",
        callback_data="manager_banco"
    )
    botao_sobre = types.InlineKeyboardButton(
        "Editar descrição",
        callback_data="editar_descricao"
    )

    tecladoMenu.add(botao_nome, botao_sobre)

    bot.send_message(msg.chat.id, f"<b>PENGUIN BOT - MENU PRINCIPAL</b>\nFala meu nobre, seja Bem-vindo, \nsou o PenguinBot.🐧 Do que precisas hoje?", reply_markup=tecladoMenu, parse_mode="HTML")

    @bot.callback_query_handler(func=lambda chamada: chamada.data  == 'manager_banco')   
    def pedir_valor(chamada: types.CallbackQuery):
        bot.answer_callback_query(chamada.id)
        resposta = [f"ID: {banco['bancoID']} - {banco['nomeBanco']}" for banco in listarBancos()]

        banco_texto = "\n".join(resposta)

        mensagem = bot.send_message(chamada.message.chat.id,f"<b>PENGUIN BOT - BANCOS</b>\nBancos Disponiveis:\n\n{banco_texto}", parse_mode="HTML")
        bot.register_next_step_handler(mensagem,receber_valor)
    def receber_valor(msg:types.Message):
        valor = msg.text
        valor = float(valor)
        transferenciaBanco(valor)
        bot.send_message(msg.chat.id, f"Valor Acrescentado: {valor}")
            

    #bot.answer_callback_query(chamada.id)
    #bot.send_message(chamada.message.chat.id, resposta)

bot.infinity_polling()