from src.bot import Bot
import time

contact_list = ['contato 1', 'contato 2']
contact_filter = True # fala apenas com contatos listados no array acima

bot = Bot(contact_list, contact_filter)

while True:
    bot.actions_bot()