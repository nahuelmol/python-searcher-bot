from googlesearch import search
import requests, sys
from . import shorter

def searching(mystring):
	pages_scoped = 10
	query = mystring
	pages = []
	resulted = []
	j = 0

	resulted = search(query, num_results=pages_scoped)

	for i in resulted:
		link_cutered = shorter.shorter_links(i)
		print(link_cutered)
		pages.append(i)
	return pages


