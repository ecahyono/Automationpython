import platform, sys, json
from os import environ, path
from selenium import webdriver
from pytest import mark
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def initDriver():
    if platform.system() == 'Darwin':
        smac = Servic(environ.get("CHROMEDRIVERMAC"))
        driver = webdriver.Chrome(service=smac)
    elif platform.system() == 'Windows':
        swin = Service(environ.get("CHROMEDRIVERWIN"))
        driver = webdriver.Chrome(service=swin)
    driver.get(environ.get("HOST"))
    driver.maximize_window()
    driver.implicitly_wait(5)

    return driver

def loadDataPath():
    sys.path.append('.....')
    file = open('data.json', 'r')
    data = json.load(file)
    return data

def buttonTambah(driver):
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
