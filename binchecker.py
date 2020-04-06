import requests
import json
greencolor = '\033[92;1;1m'
bluecolor = '\033[96;1;1m'
whitecolor = '\033[37;0;1m'
startof = '\033[92;1;1m[\033[91;1;1m+\033[92;1;1m]'
logoyu = """╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━╮╱╱╱╱╱╱╭╮╱
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╮┃╱╱╱╱╱╭╯╰╮
┃┃╱┃┃╭━━╮╭━━╮╭━━╮╱╱╱╱┃╰╯╰╮╭━━╮╰╮╭╯
┃╰━╯┃┃╭╮┃┃╭╮┃┃╭╮┃╭━━╮┃╭━╮┃┃╭╮┃╱┃┃╱
┃╭━╮┃┃┃┃┃┃╰╯┃┃┃┃┃╰━━╯┃╰━╯┃┃╰╯┃╱┃╰╮
╰╯╱╰╯╰╯╰╯╰━━╯╰╯╰╯╱╱╱╱╰━━━╯╰━━╯╱╰━╯\n\n"""
print(logoyu)
while True:
	while True:
		try:
			strinput = input(f'{startof}Enter a Bin \n{startof} {whitecolor}')
			strinput = int(strinput)
			break
		except ValueError:
			print('Please Enter Correct Input')
	aore = requests.get(f'https://lookup.binlist.net/{strinput}')
	if aore.status_code == 404:
		edcolor = '\033[91;0;1m'
		print(edcolor+'Invalid Bin')
		continue
	ao = aore.text
	ao = json.loads(ao)
	auo = bool(ao['number'])
	if auo is not False:
		lenbin= ao['number']['length']
	else:
		lenbin= 'None'
	keysh='brand'
	schmemetype = ao['scheme'].upper()
	if 'type' in ao.keys():
		type_cc = ao['type']
	else:
		type_cc = 'None'
	if keysh in ao.keys():
		brand_cc = ao['brand']
	else:
		brand_cc = 'None'
	
	countr_cc = ao['country']['name']
	emoji_cc = ao['country']['emoji']
	currency_cc = ao['country']['currency']
	if bool(ao['bank']) is not False:
		bank_name = ao['bank']['name']
		if 'phone' in ao['bank'].keys():
			banknum = str(ao['bank']['phone'])
		else:
			banknum = 'None'
		if 'url' in ao['bank'].keys():
			bankinu = ao['bank']['url']
		else:
			bankinu = 'None'
	else:
		bank_name = 'None'
		banknum = 'None'
	print('\nINFO OF CARD\n')
	print(f'{greencolor}Scheme:{bluecolor}{schmemetype}\n')
	print(f'{greencolor}Type:{bluecolor}{type_cc}\n')
	print(f'{greencolor}Brand:{bluecolor}{brand_cc}\n')
	print(f'{greencolor}Country:{bluecolor}{countr_cc}{emoji_cc}\n')
	print(f'{greencolor}Currency:{bluecolor}{currency_cc}\n')
	print(f'{greencolor}Bank:{bluecolor}{bank_name}\n')
	print(f'{greencolor}Bank Number:{bluecolor}{banknum}\n')
	print(f'{greencolor}Bank WebSite:{bluecolor}{bankinu}\033[0m\n\n')