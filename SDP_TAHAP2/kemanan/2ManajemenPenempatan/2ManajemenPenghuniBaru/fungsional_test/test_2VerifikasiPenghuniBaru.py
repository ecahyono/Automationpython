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
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
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
from Settings.login import loginOperatorSumedang, Op_Keamanan_p2u, SpvRutanBdg, op_keamanan_mp

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Log1TambahManajemenPenghuniBaru.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("KeamananUAT"))
sheetrange = wb['TambahManajemenPenghuniBaru']

@mark.fixture_test()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')

@mark.fixture_test()
def test_2_login():
    SpvRutanBdg(driver)
    Log.info('Login Operator Manajemen Penempatan')


@mark.fixture_test()
def test_3_Input():

    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['ManajemenPenempatan']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Manajemen Penghuni Baru').click()
    sleep(driver)
    print('.')
    Log.info('Akses halaman Manajemen Penghuni Baru')
    attach(data=driver.get_screenshot_as_png())

    i = 2
        
    while i <= len(sheetrange['A']):
    
        Nama                                    = sheetrange['A'+str(i)].value
        Keterangan                              = sheetrange['G'+str(i)].value
    
    

        try:
            sleep(driver)
            driver.implicitly_wait(10)
            #sleep(driver)
           

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

            driver.find_element(By.ID, 'filterColumn').click()
            driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()

            driver.find_element(By.ID, 'statusVerifikasi').click()
            driver.find_element(By.ID, 'DalamProses').click()

            driver.find_element(By.ID, 'kataKunci').click()
            driver.find_element(By.ID, 'kataKunci').send_keys(Nama)
            driver.find_element(By.ID, 'searchButton').click()
            driver.execute_script("window.scrollTo(0,1.5)")
            Log.info('memilih pencarian berdasarkan Nama Lengkap')
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
            attach(data=driver.get_screenshot_as_png())
            time.sleep(3)
            driver.find_element(By.CSS_SELECTOR, ".text-yellow-500").click()
            Log.info("Click Button  Verifikasi")

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#status_verifikasi')))
            driver.find_element(By.CSS_SELECTOR, '#status_verifikasi').click()
            driver.find_element(By.XPATH, "//li[@id='diizinkan']").click()

            driver.find_element(By.ID, "keterangan").send_keys(Keterangan)

        except TimeoutException:
            print("ERRROR")
            pass
                
        sleep(driver)
        i = i + 1
    print('DONE')

def teardown():
    quit(driver)