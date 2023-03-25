from distutils.archive_util import make_archive
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import platform
from pytest import mark
import time
from pytest_html_reporter import attach
import pyautogui

import sys
from os import environ, path
from dotenv import load_dotenv
load_dotenv()
from openpyxl import load_workbook

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR"))

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))


from Settings.setup import initDriver, loadDataPath, quit, sleep
from Settings.login import LapasPerempuan, testsukamiskin

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Registrasi.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("RegSelenium"))
sheetrange = wb['RegSelenium']

@mark.fixture_test()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')

@mark.fixture_test()
def test_2_login():
    testsukamiskin(driver)
    Log.info('Login')


@mark.fixture_test()
def test_Input_Registrasi():
    driver.implicitly_wait(60)
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Registrasi']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Registrasi']['child']['ManajemenRegistrasi']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Registrasi Tahanan/ Narapidana').click()
    Log.info('Akses Menu Registrasi')
    attach(data=driver.get_screenshot_as_png())

    i = 2
        # nge baca mulai dari tabel A
    
    while i <= len(sheetrange['A']):
        # deklarasi bahwa NIP itu ada di A 
        NamaWBP                             = sheetrange['A'+str(i)].value
        NoRegistrasi                        = sheetrange['B'+str(i)].value
        NomorSuratPenahanan                 = sheetrange['C'+str(i)].value
        Tgl                                 = sheetrange['D'+str(i)].value

      
        driver.implicitly_wait(30)

        
        try:
            
            driver.implicitly_wait(60)
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(.,\'Registrasi Baru\')]')))
            driver.find_element(By.XPATH, "//span[contains(.,\'Registrasi Baru\')]").click()
            Log.info('Click Button Registrasi')
    
         
            #jadiin def
            driver.find_element(By.ID, "submitButton").click()
            Log.info('Klik Button Submit')
        
            
        except TimeoutException:
            print("MASIH ADA ERROR, CEK LAGI PAK WIL")
            
            pass
        time.sleep(5)
        i = i + 1

  
        

@mark.fixture_test()
def test_exit():
    quit(driver)




