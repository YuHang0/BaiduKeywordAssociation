#!/usr/bin/python3
# -*- coding:utf-8 -*-

from urllib.parse import quote
import requests
import platform
import os

SYSTEM = platform.system() # 得到系统信息

def get_baidu_word(wd):
	'''
	爬取百度关键词联想
	'''
	url = 'https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd='+quote(wd)
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
	}
	response = requests.get(url, headers=headers)
	text = response.text
	i = text.index('s:[')
	data = eval(text[i+2:-3])
	return data # 关键词联想, list类型

def show_baidu_word(wd):
	'''
	打印联想词反馈结果
	'''
	data = get_baidu_word(wd)
	print('--------联想词反馈:--------')
	for item in data:
		print('\t', item)
	print('------------End-------------')

def cls():
	'''
	清屏函数
	'''
	if SYSTEM == 'Linux':
		os.system('clear')
	elif SYSTEM == 'Windows':
		os.system('cls')
	elif SYSTEM == '':
		pass	

def main():
	while True:
		print('请输入关键词:', end='')
		input1 = input()
		cls()
		if input1 == 'quit':
			print('bye!') # 输入quit,退出程序
			break
		elif input1 == '':
			cls()
			continue
		else:
			print('关键词:', input1)
			show_baidu_word(input1)
			
if __name__ == '__main__':
	main()
