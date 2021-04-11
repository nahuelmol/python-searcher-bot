from searcher import searcher_algory
from translator import translating

from telegram import Update
from telegram.ext import CallbackContext
from googletrans import Translator 


def menu(update:Update,context:CallbackContext):
	update.message.reply_text(f'Main menu:\n\
		/trans -> translate texts\n\
		/search-> search in google\n\
		/trnasearch-> trans and search in google\n\
		\n')

def text_to_translate(update:Update,context:CallbackContext):
	mylist = []
	mylist = context.args
	mystring = ""

	for i in mylist:
		mystring = mystring + " "+ i

	translated_text = translating.trans(mystring)

	update.message.reply_text(f'Translated text: {translated_text}')

def show_results(update:Update,context:CallbackContext):
	mylist = []
	mylist = context.args
	mystring = ""

	for i in mylist:
		mystring = mystring + " "+ i
	pages = searcher_algory.searching(mystring)

	update.message.reply_text(f'Results for:"{mystring}"\n')
	for j in pages:	
		update.message.reply_text(f'{j}')

def search_foreignly(update:Update,context:CallbackContext):
	mylist = []
	mylist = context.args
	mystring = ""

	for u in mylist:
		mystring = mystring + "" + i
	translated_text = translating.trans(mystring)	
	update.message.reply_text(f'Translated text: {translated_text}')

	pages = searcher_algory.searching(translated_text)
	update.message.reply_text(f'Results for:"{translated_text}"\n')
	for j in pages:	
		update.message.reply_text(f'{j}')


def halloToUser(update:Update, context:CallbackContext):
	update.message.reply_text(f'Hello {update.effective_user.first_name}!\n\
		You can request at the bot by the following commands:\n\
		personal -> personal data\n\
		search "key words" -> method for searching in google\n\
		')

def personal_data(update:Update,context:CallbackContext):
	update.message.reply_text(f'\
		{update.effective_user.first_name}\
		{update.effective_user.last_name}\n\
		id: {update.effective_user.id}\n\
		user: {update.effective_user.username}\n\
		lang: {update.effective_user.language_code}\n\
		jg: {update.effective_user.can_join_groups}\n\
		rg: {update.effective_user.can_read_all_group_messages}\n\
		')