import requests
import os
from bs4 import BeautifulSoup


# Exploring BeautifulSoup possibilities - content followed
def scrap_explore():
	""" Scrap / explorations https://www.crummy.com/software/BeautifulSoup/bs4/doc/"""

	# 0 - Make a requests against hacker news
	res = requests.get('https://news.ycombinator.com/')
	# res --> <Response [200]>
	# res.text --> text within the file

	# 1 - Parse the text
	html = BeautifulSoup(res.text, 'html.parser')

	# 2 - Explore the DOM
	# 2.01 - Can access DOM with dot notation --> HTML head tag content
	html_heads = html.head
	html_body = html.body
	print(html_body)

	# 2.02 - Find all elements ( class, ids, tag elements )
	print(html.find_all('meta'))
	# Can find_all matched elements --> collection of meta tags

	# 2.03 - Select: select an element by its css selector
	print( html.select('.score'))

############################################################
# 	    Objective: get list of news by highest rank
#       - extra: store them to a file
#       Note: own implementation beneath has been created
#       ahead of each video ( once the concept was grasped
#           - thought as extras ( appropriating the use of scrapping )
#               not following course:
#               - store news in a file
#               - functions flexibility with vote_rank, amount of result desired
#               - EXTRA: write an email


# Filtering function by vote
def filter_by_votes(_duo, _vote_rank):
	f"""Filters news by vote rank {_vote_rank}"""
	return int(_duo[1].getText().split(' ')[0]) >= _vote_rank


# Sorting function by vote
def sort_by_votes(news):
	return sorted(news, key=lambda item: int(item["votes"]), reverse=True)


# Proceed to scrap hackernews
def scrap_hacker_news(_vote_rank, number_of_pages=1):
	""" Scrap hacker news https://www.crummy.com/software/BeautifulSoup/bs4/doc/"""
	print('\n1/2 - Start scrapping...')

	news_dictionaries = []
	for page_number in range(1, number_of_pages+1):
		url = 'https://news.ycombinator.com/' if not number_of_pages else f'https://news.ycombinator.com/?p={page_number}'
		response = requests.get(url)

		# Gets access to the DOM
		html = BeautifulSoup(response.text, 'html.parser')
		body = html.body

		# DOM Elements of interest
		links_nodes = body.select('tr.athing .titleline')
		votes_nodes = body.select('tr.athing + tr .score')

		# Organizes as tuples of links_nodes and votes_nodes
		pair = zip(links_nodes, votes_nodes)

		filtered_news = list(
			filter(
				lambda _pair: filter_by_votes(_pair, _vote_rank),
				pair
			)
		)

		# Gets a list of news dictionaries with news' title, link, number of votes
		for item in filtered_news:
			title = item[0].find('a').getText()
			link = item[0].find('a').get('href')
			votes = item[1].getText().split(' ')[0]
			details = {"title": title, "link": link, "votes": votes }
			news_dictionaries.append(details)

	return sort_by_votes(news_dictionaries)


# Proceed to save news into a file
def write_news_document(news):
	print('2/2 - Saving news into file...')
	with open('./scrapped_news.txt', 'w') as file:
		for idx, item in enumerate(news):
			file.write(f'''
			#{idx + 1} - {item["title"]}
				{item["link"]}
				{item["votes"]}
				
			''')


# entry function to scrap news and save them into a file
def get_news(vote_rank=100, number_of_pages=1, maximum=None):
	"""
	Get news from Hacker News and store them in a file
	        Parameters
        ----------
        vote_rank : int, optional
            Indicator of news pertinence based on the number of votes:
            100 would be minimum 100 votes to be considered as news of interest

        number_of_page : int, optional
            The number of pages to scrap

        maximum : None | int, optional
            Maximum news to store in a file ( based on filtered and sorted news )
	"""
	news_details_sorted = scrap_hacker_news(vote_rank, number_of_pages)
	write_news_document(news_details_sorted[:maximum])
	print(f"""
	Summary: 
		- {len(news_details_sorted)} scrapped news
		- with a minimum of {vote_rank} votes
		- through {number_of_pages} pages
		{ f'- saved {maximum} in file' if maximum 
		else f"- saved in file {len(news_details_sorted)} scrapped news"}
		""")


if __name__ == '__main__':
	get_news(vote_rank=100, number_of_pages=2, maximum=5)