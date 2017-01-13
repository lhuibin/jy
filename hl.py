#!/usr/bin/env python3
#coding:utf-8
import requests
import time
#from colorama import init, Fore

while True:
	time.sleep(2)
	url_cn = 'https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny'
	url_int = 'https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd'
	r = requests.get(url_cn)
	l = requests.get(url_int)
	last_price_cn = r.json()['ticker']['last']
	last_price_int = l.json()['ticker']['last']
	hl = float(last_price_cn)/float(last_price_int)
	print('币价: |', str(last_price_cn),'¥',(last_price_int),'$')
	print('汇率: |', str(hl), '\n--------------------------')
