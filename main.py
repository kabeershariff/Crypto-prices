import requests
import apikey
import time
import os
from prettytable import PrettyTable
from humanize import intword
from colored import Fore, Back, Style

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {'Accepts': 'application/json',
		  'X-CMC_PRO_API_KEY' : apikey.key,
		  }

limit = 30

params = {'start': 1,
		 'limit': limit,
		 'convert': 'INR',
		 }

def percent_color(value):
	if float(value) > 0:
		return f"{Fore.black}{Back.green} {format(value, '.2f')}{Style.reset}"
	else:
		return f"{Fore.white}{Back.red} {format(value, '.2f')}{Style.reset}"

while True:	
	response = requests.get(url, params=params, headers=headers).json()

	table = PrettyTable()
	table.field_names = ['ID','Rank', 'Name', 'Symbol', 'Price[INR]', '1h%', '24h%', '7d%', 'Market Cap']

	coins = response['data']
	for i in coins:	
		table.add_row([
				i['id'],
				i['cmc_rank'],
				i['name'],
				i['symbol'],
				i['quote']['INR']['price'],
				percent_color(i['quote']['INR']['percent_change_1h']),
				percent_color(i['quote']['INR']['percent_change_24h']),
				percent_color(i['quote']['INR']['percent_change_7d']),
				intword(i['quote']['INR']['market_cap'])])
	#Clear the terminal screen
	os.system('cls' if os.name == 'nt' else 'clear')
	print(f"{Style.BOLD}{Fore.black}{Back.cyan}CRYPTOCURRENCY STATS{Style.reset}")
	print(f"{Fore.black}{Back.green}Values are updated every 10 secs{Style.reset}")
	print(table)
	print(f"{Fore.white}{Back.red}Ctrl+Z to quit{Style.reset}")
	#Time to refresh
	time.sleep(10)
