import os
from dotenv import load_dotenv
import telebot

load_dotenv()

bot = telebot.TeleBot(os.getenv("tokenAPI"))
