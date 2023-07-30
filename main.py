import requests
import apikey
from prettytable import PrettyTable
from humanize import intword
from colored import Fore, Back, Style

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {'Accepts': 'application/json',
		  'X-CMC_PRO_API_KEY' : apikey.key,
		  }

params = {'start': 1,
		 'limit': 20,
		 'convert': 'INR',
		 }

response = requests.get(url, params=params, headers=headers).json()
table = PrettyTable()
table.field_names = ['ID','Rank', 'Name', 'Symbol', 'Price[INR]', '1h%', '24h%', '7d%', 'Market Cap']

coins = response['data']


for i in coins:
	up_1h = f"{Fore.black}{Back.green} {format(i['quote']['INR']['percent_change_1h'], '.2f')}{Style.reset}"
	down_1h = f"{Fore.white}{Back.red}{format(i['quote']['INR']['percent_change_1h'], '.2f')}{Style.reset}"
	
	up_24h = f"{Fore.black}{Back.green} {format(i['quote']['INR']['percent_change_24h'], '.2f')}{Style.reset}"
	down_24h = f"{Fore.white}{Back.red}{format(i['quote']['INR']['percent_change_24h'], '.2f')}{Style.reset}"
	
	up_7d = f"{Fore.black}{Back.green} {format(i['quote']['INR']['percent_change_7d'], '.2f')}{Style.reset}"
	down_7d = f"{Fore.white}{Back.red}{format(i['quote']['INR']['percent_change_7d'], '.2f')}{Style.reset}"
	
	table.add_row([i['id'],
				   i['cmc_rank'],
				   i['name'],
				   i['symbol'],
				   i['quote']['INR']['price'],
				   up_1h if float(i['quote']['INR']['percent_change_1h']) > 0 else down_1h,
				   up_24h if float(i['quote']['INR']['percent_change_24h']) > 0 else down_24h,
				   up_7d if float(i['quote']['INR']['percent_change_7d']) > 0 else down_7d,
				   intword(i['quote']['INR']['market_cap'])])
print(table)
