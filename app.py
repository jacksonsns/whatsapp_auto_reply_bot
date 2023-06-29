from src.bot import Bot
import time

contact_list = ['contato 1', 'contato 2']
contact_filter = True # only send messages to contacts listed in the array above

bot = Bot(contact_list, contact_filter)

while True:
    bot.actions_bot()
    time.sleep(2)