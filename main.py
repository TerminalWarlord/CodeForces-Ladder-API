# Copyright © 2022 TerminalWarlord
# Encoding = 'utf-8'
# Licensed under MIT License
# https://github.com/TerminalWarlord/
# Date: 26.03.2022 - 16:31(BST)



import requests
from bs4 import BeautifulSoup as bs
import cloudscraper
from is_solved import get_solved


scraper =cloudscraper.create_scraper(
  browser={
    'browser': 'firefox',
    'platform': 'windows',
    'desktop': True
  }
)
def main(rating, handle):
	solved = get_solved(handle)
	url = f'https://codeforces.com/problemset?tags={rating}-{rating}'
	r = scraper.get(url)
	problems = {}
	soup = bs(r.text, 'html.parser')
	pb = soup.find_all('tr')
	i = 1
	for p in pb:
		try:
			link = "https://codeforces.com/" + p.find_all('td')[0].find("a")['href']
			pb_id = p.find_all('td')[0].find("a").text.strip()
			pb_name = p.find_all('td')[1].find("a").text.strip()
			if pb_id in solved:
				done = 1
			else:
				done = 0
			problems[i] = {
				'link' : link,
				'problem_id': pb_id,
				'problem_name': pb_name,
				'solved': done
			}
			i+=1
			if i>50:
				break
		except:
			pass
	return problems
