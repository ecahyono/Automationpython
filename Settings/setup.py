import platform, sys, json
from os import environ, path
from selenium import webdriver
from pytest import mark
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
    sys.path.append( '/Users/will/Documents/work/Automationpython' )
    #sys.path.append( '..' )
    file = open('data.json', 'r')
    data = json.load(file)
    return data

def buttonTambah(driver):
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButton"]')))

