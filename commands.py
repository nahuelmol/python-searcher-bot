import searcher_algory
from telegram import Update
from telegram.ext import CallbackContext

def show_results(update:Update,context:CallbackContext):
	mylist = []
	mylist = context.args
	mystring = ""

	for i in context.args:
		mystring = mystring + " "+ i
	pages = searcher_algory.searching(mystring)

	update.message.reply_text(f'Results for "{mystring}"\n')
	for j in pages:	
		update.message.reply_text(f'{j}')


def halloToUser(update:Update, context:CallbackContext):
	update.message.reply_text(f'Hello {update.effective_user.first_name}')