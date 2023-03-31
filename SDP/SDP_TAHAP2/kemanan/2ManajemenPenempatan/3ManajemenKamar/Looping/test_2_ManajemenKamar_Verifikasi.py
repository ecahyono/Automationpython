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
    wb = load_workbook(environ.get("KeamananUAT"))

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))


from Settings.setup import initDriver, loadDataPath, quit, sleep
from Settings.loginkeamanan import loginOperatorSumedang, Op_Keamanan_p2u, SpvRutanBdg, op_keamanan_mp
from Settings.Page.keamanan import manajemenpenghunibaru
from Settings.Page.keamanan import manajemenkamar

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('LogManajemenKamarVerifikasi.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)



@mark.fixture_test()
def test_1loginSPV():

    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')
    SpvRutanBdg(driver)
    Log.info('Login Spv Manajemen Penempatan')


@mark.fixture_test()
def test_2_AksesMenu():
    sleep(driver)
    manajemenkamar(driver)
    print('.')
    Log.info('Akses halaman Manajemen Penghuni Baru')
    attach(data=driver.get_screenshot_as_png())
    Log.info('Akses Menu Manajemen Kamar')


@mark.fixture_test()
def test_3_Verifikasi():
    sleep(driver)

    i = 2
    Verifikasi = wb['ManajemenKamar']
    while i <= len(Verifikasi['A']):
        



    
        Nama                                    = Verifikasi['A'+str(i)].value
        blokform                                = Verifikasi['B'+str(i)].value
        Lantai                                  = Verifikasi['C'+str(i)].value
        Kamar                                   = Verifikasi['D'+str(i)].value
        TanggalPenempatan                       = Verifikasi['E'+str(i)].value
        Keterangan                              = Verifikasi['F'+str(i)].value
        status                                  = Verifikasi['G'+str(i)].value

        try:

            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
            driver.find_element(By.ID, "filterColumn").click()
            driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
            Log.info('Filter Data Berdasarkan Nama')


            sleep(driver)
            driver.find_element(By.ID, "kataKunci").click()
            driver.find_element(By.ID, "kataKunci").send_keys(Nama)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
            driver.find_element(By.ID, "statusVerifikasi").click()
            driver.find_element(By.XPATH, "//li[contains(.,\'Dalam Proses\')]").click()
            Log.info('Search nama wbp')


            sleep(driver)
            driver.find_element(By.ID, 'searchButton').click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'searchButton')))searchButton
            Log.info('Click Button Search')

            time.sleep(2)
            driver.find_element(By.ID, "verifikasi-0").click()
            Log.info("Click Button Verifikasi")


            sleep(driver)
            driver.find_element(By.ID, "status_verifikasi").click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'diizinkan')))
        
            driver.find_element(By.XPATH, "//li[@id=\'"+status+"\']").click()


            sleep(driver)
            driver.find_element(By.CSS_SELECTOR, ".el-textarea > #keterangan").click()
            driver.find_element(By.CSS_SELECTOR, ".el-textarea > #keterangan").send_keys(Keterangan)

            sleep(driver)
            driver.find_element(By.ID, "submitButton").click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'searchButton')))



        except TimeoutException:
            print("ERRROR")
            pass
                
        sleep(driver)
        i = i + 1
    print('DONE')

@mark.fixture_test()
def teardown():
    quit(driver)

