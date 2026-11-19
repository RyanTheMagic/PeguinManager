import os
from dotenv import load_dotenv
import telebot
from telebot import types
from Model.deposito import deposito

load_dotenv()

bot = telebot.TeleBot(os.getenv("tokenAPI"))

@bot.message_handler(["menu"])
def mostrar_menu(msg:types.Message):
    tecladoMenu = types.InlineKeyboardMarkup(row_width=2)

    botao_nome = types.InlineKeyboardButton(
        "Gastos",
        callback_data="gasto"
    )
    botao_sobre = types.InlineKeyboardButton(
        "Editar descrição",
        callback_data="editar_descricao"
    )

    tecladoMenu.add(botao_nome, botao_sobre)

    bot.send_message(msg.chat.id, f"Fala meu nobre, seja Bem-vindo, \nsou o PenguinBot.🐧 Do que precisas hoje?", reply_markup=tecladoMenu)

    @bot.callback_query_handler(func=lambda chamada: chamada.data  == 'gasto')   
    def pedir_valor(chamada: types.CallbackQuery):
        bot.answer_callback_query(chamada.id)
        mensagem = bot.send_message(chamada.message.chat.id,"Qual o valor do gasto? (Ex: 10.50)")
        bot.register_next_step_handler(mensagem,receber_valor)
    def receber_valor(msg:types.Message):
        valor = msg.text
        valor = float(valor)
        deposito(valor)
        bot.send_message(msg.chat.id, f"Valor Acrescentado: {valor}")
            

    #bot.answer_callback_query(chamada.id)
    #bot.send_message(chamada.message.chat.id, resposta)

bot.infinity_polling()