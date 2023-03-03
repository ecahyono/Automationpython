from distutils.archive_util import make_archive
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
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
from Settings.login import loginOperatorSumedang, Op_Keamanan_p2u

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Registrasi.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("KeamananUAT"))
sheetrangeIndex = wb['DaftarLaluLintas_Input']

@mark.fixture_test()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')

@mark.fixture_test()
def test_2_login():
    Op_Keamanan_p2u(driver)
    Log.info('Login')


@mark.fixture_test()
def test_Input():
    print('.')
    print('== NEXT == (DLP-001) - Akses halaman Daftar Lalu Lintas ')

    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Akses P2U Internal').click()
    sleep(driver)
    print('.')
    Log.info('(DLP-001 SUKSES) Akses halaman Daftar Lalu Lintas - Mengakses halaman Daftar Lalu Lintas dengan memilih modul Keamanan kemudian pilih menu Lalu Lintas lalu pilih submenu Daftar Lalu Lintas')
    attach(data=driver.get_screenshot_as_png())


    i = 2
        
    while i <= len(sheetrangeIndex['A']):
    
        NamaInput                                 = sheetrangeIndex['B'+str(i)].value
        Nosk                                      = sheetrangeIndex['C'+str(i)].value
        Namacari                                  = sheetrangeIndex['D'+str(i)].value
        jenisKejahatancari                        = sheetrangeIndex['E'+str(i)].value
                
        driver.implicitly_wait(30)


        try:
            print('.')
            print('Click Button Create')
            sleep(driver)
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
            driver.find_element(By.ID, 'createButton').click()

            print('Pilih Dropdown Nama')
            sleep(driver)
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))

            attach(data=driver.get_screenshot_as_png())
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))

            print('== NEXT == Input kata kunci nama')
            sleep(driver)
            driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NamaInput)
            Log.info(' Input Nama  ')
            driver.find_element(By.ID, 'buttonSearch' ).click()
            sleep(driver)

            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
            driver.find_element(By.CSS_SELECTOR, ".h-5 > path").click()
            
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'createButton')))
            driver.find_element(By.ID, 'createButton').click()

            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'buttonSubmit')))
            driver.find_element(By.ID, 'noSK').send_keys(Nosk)

            sleep(driver)
            driver.find_element(By.XPATH, "//div[@id=\'fileSK\']/div/button").click()

            sleep(driver)
            pyautogui.write("///////users/will/test.pdf")
            pyautogui.press('return')
            pyautogui.write("///////users/will/test.pdf")
        
            pyautogui.press('return')
            pyautogui.press('escape')
            pyautogui.press('enter')
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            driver.find_element(By.ID, 'jenisKeluar').click()
            
            driver.find_element(By.XPATH, "//li[@id=\'Izin Alasan Penting\']").click()
    
    

            sleep(driver)


        except TimeoutException:
            print("ERRROR")
            pass
        time.sleep(5)
        i = i + 1
        print(i)

  
        

@mark.fixture_test()
def test_exit():
    quit(driver)




