import os
import searcher, commands

from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv

if __name__ == '__main__':
	token 		= os.environ.get("api-token")

	updater 	= Updater(token)
	dispatcher 	= updater.dispatcher

	init 		= CommandHandler('menu', commands.menu)

	start_value 	= CommandHandler('search', commands.show_results, pass_args=True,pass_chat_data=True)
	hallo_command	= CommandHandler('hallo', commands.halloToUser)
	personal_data	= CommandHandler('personal', commands.personal_data) 
	translate 		= CommandHandler('trans', commands.text_to_translate, pass_args= True, pass_chat_data=True)
	trans_n_search 	= CommandHandler('transearch',commands.search_foreignly,pass_args= True, pass_chat_data=True)
	
	dispatcher.add_handler(start_value)
	dispatcher.add_handler(hallo_command)
	dispatcher.add_handler(personal_data)
	dispatcher.add_handler(translate)
	dispatcher.add_handler(init)
	dispatcher.add_handler(trans_n_search)

	updater.start_polling()
	updater.idle()