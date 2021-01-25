from googlesearch import search
import requests, sys
import shorter

def searching(mystring):

	query = mystring
	pages = []
	j = 0

	for i in search(query, num_results=10):
		link_cutered = shorter.shorter_links(i)
		print(link_cutered)
		pages.append(i)
	return pages

