import platform, sys, json
from os import environ, path
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager #Use with Chrome
from webdriver_manager.firefox import GeckoDriverManager #Use with Firefox
from webdriver_manager.microsoft import EdgeChromiumDriverManager #Use with Edge
from webdriver_manager.microsoft import IEDriverManager #Use with Internet Explorer
#opera
from selenium.webdriver.chrome import service 
from webdriver_manager.opera import OperaDriverManager

from dotenv import load_dotenv
load_dotenv()

def webchrome(): #webdriver form chrome
  if platform.system() == 'Windows':
    options = webdriver.ChromeOptions()
    options.add_argument('--remote-debugging-port=9222') # port number bisa diubah sesuai keinginan
    #chromedriver
    usechromedriver = webdriver.Chrome(ChromeDriverManager().install())
    # jalankan Chrome dengan opsi dan path yang ditentukan
    driver = webdriver.Chrome(executable_path=usechromedriver, chrome_options=options)
  elif platform.system() == 'Darwin':
    pass
  driver.get(environ.get("HOSTKUMBANG"))
  #driver.get(environ.get("HOST"))
  driver.maximize_window()
  return driver

def webfirefox(): #webdriver form firefox
  if platform.system() == 'Windows':
    options = FirefoxOptions()
    # options.add_argument("--headless")
    driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
  elif platform.system() == 'Darwin':
    pass
  driver.get(environ.get("HOSTKUMBANG"))
  #driver.get(environ.get("HOST"))
  driver.maximize_window()
  return driver

