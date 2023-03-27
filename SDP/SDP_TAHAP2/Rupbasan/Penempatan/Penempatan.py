from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def staylogin(): 
	options = Options()
	options.add_argument("--user-data-dir=C:\ChromeD")
	options.page_load_strategy = 'normal'
	driver = webdriver.Chrome(options=options)
	driver.get("http://kumbang.torche.id:32400")

