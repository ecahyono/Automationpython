from selenium import webdriver
from os import environ, path
import platform, sys, json
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



from dotenv import load_dotenv
load_dotenv()


def initoption():
	if platform.system() == 'Darwin':
		driver = webdriver.Chrome(environ.get("CHROMEDRIVERMAC"))
	elif platform.system() == 'Windows':
		optionweb = Options()
		
		optionweb.add_experimental_option("debuggerAddress", "localhost:9222")

		# profil = r'C:\Users\user\AppData\Local\Google\Chrome\User Data\Default'
		# url ='http://sdp.torche.id:32400/'
		# optionweb.add_argument(f'{url}')
		# optionweb.add_argument(f'-user-data-dir={profil}')

		driver = webdriver.Chrome(executable_path="C:\\Users\\user\\Documents\\chromedriver.exe",chrome_options=optionweb)
		driver.get('http://sdp.torche.id:32400/')
		# WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'login')))
		# driver.find_element(By.ID, "login").click()
		# # ini masuk ke form input username
		# driver.find_element(By.ID, "username").click()
		# driver.find_element(By.ID, "username").send_keys("oprupbasanbdg")
		# time.sleep(2)
		# driver.find_element(By.ID, "password").send_keys("password")
		# # click button login
		# driver.find_element(By.ID, "kc-login").click()
