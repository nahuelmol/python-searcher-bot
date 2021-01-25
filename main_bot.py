from telegram.ext import Updater, CommandHandler

import searcher_algory, commands

updater = Updater("1504588360:AAE4OwLk_9HB7V9oj1oP8ZfgaCg1GUjFDns")
dispatcher = updater.dispatcher

start_value = CommandHandler('search', commands.show_results, pass_args=True,pass_chat_data=True)
hallo_command=CommandHandler('hallo', commands.halloToUser)


dispatcher.add_handler(start_value)
dispatcher.add_handler(hallo_command)

updater.start_polling()
updater.idle()