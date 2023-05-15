from selenium import webdriver
from os import environ, path
import platform, sys, json
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
import time
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv
load_dotenv()

def initoption():
	if platform.system() == 'Darwin':
		driver = webdriver.Chrome(environ.get("CHROMEDRIVERMAC"))
	elif platform.system() == 'Windows':
		options = webdriver.ChromeOptions() 
		options.add_argument(f'--user-data-dir=C:/Users/user/AppData/Local/Google/Chrome/User Data')
		options.add_argument('--profile-directory=Default')
		driver = webdriver.Chrome(options=options)
		# exec_path_chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe" #Do not use this path that is extracted from "chrome://version/"
		# exec_path_driver = "C:/Users/user/Documents/TRCH/chromedriver.exe"
		# ch_options = Options() #Chrome Options
		# ch_options.add_argument("user-data-dir =C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data") #Extract this path from "chrome://version/"
		# driver = webdriver.Chrome(executable_path = exec_path_driver, options = ch_options) #Chrome_Options is deprecated. So we use options instead.
		
	driver.get('http://sdp.torche.id:32400/')
	return driver

