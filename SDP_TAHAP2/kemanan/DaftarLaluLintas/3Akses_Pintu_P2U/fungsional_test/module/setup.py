import platform, sys, json
from os import environ, path
from selenium import webdriver
from pytest import mark

def initDriver():
    if platform.system() == 'Darwin':
        driver = webdriver.Chrome(environ.get("CHROMEDRIVERMAC"))
    elif platform.system() == 'Windows':
        driver = webdriver.Chrome(environ.get("CHROMEDRIVERWIN"))
    
    driver.get(environ.get("HOST"))
    driver.maximize_window()
    driver.implicitly_wait(5)

    return driver

def loadDataPath():
    sys.path.append( '..' )
    file = open('data.json', 'r')
    data = json.load(file)
    return data

