# Copyright © 2021 TerminalWarlord
# Encoding = 'utf-8'
# Licensed under MIT License
# https://github.com/TerminalWarlord/
# Data: 26.03.2022 - 16:31(BST)

import requests
import json


def get_solved(handle):
	url = f'https://codeforces.com/api/user.status?handle={handle}'
	solved = {}
	r = requests.get(url).json()['result']
	for i in r:
		if i['verdict'] == 'OK':
			pb = str(i['contestId']) + i['problem']['index']
			solved[pb] = 1 
	# print(len(solved))
	return solved
# get_solved('terminalwarlord')