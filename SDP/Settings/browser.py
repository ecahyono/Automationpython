from selenium import webdriver
from os import environ, path
import platform, sys, json
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
import time
from selenium.webdriver.chrome.options import Options



import undetected_chromedriver as lolo
from dotenv import load_dotenv
load_dotenv()
optionweb = lolo.ChromeOptions()

def initoption():
	if platform.system() == 'Darwin':
		driver = webdriver.Chrome(environ.get("CHROMEDRIVERMAC"))
	elif platform.system() == 'Windows':
		profil = r'C:\Users\user\AppData\Local\Google\Chrome\User Data\Default'
		optionweb.add_argument(f'-user-data-dir={profil}')
		# url ='http://sdp.torche.id:32400/'
		# optionweb.add_argument(f'{url}')
		optionweb.add_experimental_option('debuggerAddress', 'localhost:9229')
		driver = lolo.Chrome(executable_path="C:\\Users\\user\\Documents\\110.0.5481.exe", options=optionweb)

