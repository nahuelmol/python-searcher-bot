from googletrans import Translator

def trans(mystring):

	translater = Translator()

	obj_result = translater.translate(mystring)
	text = obj_result.text

	return text