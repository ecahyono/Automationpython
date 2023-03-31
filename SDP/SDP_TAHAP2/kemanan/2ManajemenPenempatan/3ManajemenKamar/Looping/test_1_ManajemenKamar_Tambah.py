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
fh = logging.FileHandler('LogManajemenKamarTambah.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)



@mark.fixture_test()
def test_1loginOperator():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')
    op_keamanan_mp(driver)
    Log.info('Login Operator Manajemen Penempatan')


@mark.fixture_test()
def test_2_AksesMenu():
    sleep(driver)
    manajemenkamar(driver)
    print('.')
    Log.info('Akses halaman Manajemen Penghuni Baru')
    attach(data=driver.get_screenshot_as_png())
    Log.info('Akses Menu Manajemen Kamar')


@mark.fixture_test()
def test_3_Tambah():
    i = 2
    Tambah = wb['ManajemenKamar']
    while i <= len(Tambah['A']):
        



    
        Nama                                    = Tambah['A'+str(i)].value
        blokform                                = Tambah['B'+str(i)].value
        Lantai                                  = Tambah['C'+str(i)].value
        Kamar                                   = Tambah['D'+str(i)].value
        TanggalPenempatan                       = Tambah['E'+str(i)].value
        Keterangan                              = Tambah['F'+str(i)].value
        status                                  = Tambah['G'+str(i)].value

        try:


            sleep(driver)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
            driver.find_element(By.ID, 'createButton').click()


            sleep(driver)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
            driver.find_element(By.ID, "filterColumn").click()
            driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
            driver.find_element(By.ID, "kataKunci").click()
            driver.find_element(By.ID, "kataKunci").send_keys(Nama)
            Log.info("Search Nama lengkap")


            sleep(driver)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
            driver.find_element(By.CSS_SELECTOR, "#searchButton svg").click()
            Log.info('Click Button Search')

            sleep(driver)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
            driver.find_element(By.ID, "mutasi-0").click()
            Log.info('Click Button mutasi')


            sleep(driver)
            driver.find_element(By.ID, "blokForm").send_keys(blokform)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'blokOption-0')))
            driver.find_element(By.ID, "blokOption-0").click()
            Log.info('Pilih Blok')


            sleep(driver)
            driver.find_element(By.ID, "lantaiForm").send_keys(Lantai)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'lantaiOption-0')))
            driver.find_element(By.ID, "lantaiOption-0").click()
            Log.info('Pilih Lantai')


            sleep(driver)
            driver.find_element(By.ID, "kamarForm").send_keys(Kamar)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'kamarOption-0')))
            driver.find_element(By.CSS_SELECTOR, "#kamarOption-0 > span").click()
            Log.info("Pilih Kamar")


            sleep(driver)
            driver.find_element(By.ID, "tanggalMutasiForm").click()
            driver.find_element(By.ID, "tanggalMutasiForm").send_keys(TanggalPenempatan)
            Log.info('input tanggal penempatan')


            sleep(driver)
            driver.find_element(By.ID, "keteranganForm").click()
            driver.find_element(By.ID, "keteranganForm").send_keys(Keterangan)
            Log.info('Input Keterangan')

            sleep(driver)
            driver.find_element(By.ID, "submitButton").click()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
            Log.info('Click Button Submit')


        except TimeoutException:
            print("ERRROR")
            pass
                
        sleep(driver)
        i = i + 1
    print('DONE')

@mark.fixture_test()
def teardown():
    quit(driver)

