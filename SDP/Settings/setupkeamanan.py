import platform, sys, json
from os import environ, path
from selenium import webdriver
from pytest import mark
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options
import pyautogui
import requests

from dotenv import load_dotenv
load_dotenv()

def initDriver():
    
    if platform.system() == 'Darwin':
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'normal'
        driver = webdriver.Chrome(environ.get("CHROMEDRIVERMAC"))

        
    elif platform.system() == 'Windows':
        swin = Service(environ.get("CHROMEDRIVERWIN"))
        driver = webdriver.Chrome(service=swin)

    driver.get(environ.get("HOSTDO"))
    #driver.get(environ.get("HOST"))
    driver.maximize_window()
    driver.implicitly_wait(60)
    return driver

def loadDataPath():
    if platform.system() == 'Darwin':
        file = open(environ.get("MACJSONDATA"), 'r')
    elif platform.system() == 'Windows':
        file = open(environ.get("WINJSONDATA"), 'r')

    data = json.load(file)
    return data

def buttonTambah(driver):
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButton"]')))
    print('.')

def buttonSubmit(driver):
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    print('.')

def selectKategoriPegawai(driver):
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "pegawai").click()
    print('.')

def selectKategoriTamuDinas(driver):
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "tamuDinas").click()
    print('.')

def sleep(driver):
    driver.implicitly_wait(60)
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'

    print('=')
    print(driver.current_url)
    status_code = requests.get(driver.current_url).status_code
    status = True
    while status:
        if status_code != 200:
            print("Status code is not 200")
            quit(driver)
        else:
            print("status code is 200")
            status = False

            #time.sleep(5)
            print("-")
            time.sleep(0.1)
            #input("")
            print('wait . . . . . . . . . . . . . . . . . . . . . ')

def waituntill(driver):
    driver.implicitly_wait(60)
    
def quit(driver):
    time.sleep(3)
    print('.')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▓▒▒▒▒▒▒▒▒▓▒')
    print('▒▒▓▓▓▓▓▓▓▓▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')

    driver.close()
    driver.quit()


def upload(driver):
    sleep(driver)
    pyautogui.press('return')
    time.sleep(1)
    pyautogui.write("///////users/will/test.pdf")
    pyautogui.press('return')
    time.sleep(1)
    pyautogui.press('return')
    time.sleep(1)
    pyautogui.write("///////users/will/test.pdf")
    time.sleep(1)
    pyautogui.press('return')
    time.sleep(1)
    pyautogui.press('return')
    
def hold(driver):
    WARNING = '\033[93m'
    print(WARNING +"================================================================= Press Enter to continue")
    input("")

