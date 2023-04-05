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
from Settings.loginkeamanan import loginOperatorSumedang, Op_Keamanan_p2u, SpvRutanBdg, oplapkamtibwaru,kanwiljabar,pusat
from Settings.Page.keamanan import menulaporan6a

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('LogSuratMutasi.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)





@mark.fixture_test()
def test_1loginOperatir():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')
    oplapkamtibwaru(driver)
    Log.info('Login Op Laporan Kamtib 6A')


@mark.fixture_test()
def test_2_AksesMenu():
    sleep(driver)
    menulaporan6a(driver)
    Log.info('Akses halaman Laporan 6A')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_3_Laporan6aInput():
    sleep(driver)

    i = 2
    laporan6a = wb['Laporan6A']
    while i <= len(laporan6a['A']):
        
        nama                                            = laporan6a['A'+str(i)].value
        nosk                                            = laporan6a['B'+str(i)].value
        tanggalSkAsimilasi                              = laporan6a['C'+str(i)].value
        tanggalAsimilasi                                = laporan6a['D'+str(i)].value
        lokasiAsimilasi                                 = laporan6a['E'+str(i)].value
        namaPetugas                                     = laporan6a['F'+str(i)].value
        namaPenjamin                                    = laporan6a['G'+str(i)].value
        keterlibatanLain                                = laporan6a['H'+str(i)].value
        keterangan                                      = laporan6a['I'+str(i)].value

        try:
            

            sleep(driver)
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
            driver.find_element(By.ID, "createButton").click()
            Log.info('Klik tombol tambah data')

            sleep(driver)
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
            driver.find_element(By.ID, "filterColumn").click()
            driver.find_element(By.ID, "semua").click()
            Log.info('Filter Column Semua')


            sleep(driver)
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
            driver.find_element(By.ID, "kataKunci").click()
            driver.find_element(By.ID, "kataKunci").send_keys(nama)
            Log.info('Search Nama WBP')


            sleep(driver)
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
            driver.find_element(By.ID, "buttonSearch").click()
            Log.info('Klik tombol search')


            sleep(driver)
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
            driver.find_element(By.ID, "daftarkan0").click()
            Log.info('Klik tombol daftarkan')


            sleep(driver)
            driver.find_element(By.ID, "noSkAsimilasi").click()
            driver.find_element(By.ID, "noSkAsimilasi").send_keys(nosk)
            Log.info('Input No SK Asimilasi')


            sleep(driver)
            driver.find_element(By.ID, "tanggalSkAsimilasi").click()
            driver.find_element(By.ID, "tanggalSkAsimilasi").send_keys(tanggalSkAsimilasi)
            Log.info('Input Tanggal SK Asimilasi')


            sleep(driver)
            driver.find_element(By.ID, "tanggalAsimilasi").click()
            driver.find_element(By.ID, "tanggalAsimilasi").send_keys(tanggalAsimilasi)
            Log.info('Input Tanggal Asimilasi')

            sleep(driver)
            driver.find_element(By.ID, "lokasiAsimilasi").click()
            driver.find_element(By.ID, "lokasiAsimilasi").send_keys(lokasiAsimilasi)
            Log.info('Input Lokasi Asimilasi')


            sleep(driver)
            driver.find_element(By.ID, "namaPetugas").click()
            driver.find_element(By.ID, "namaPetugas").send_keys(namaPetugas)
            Log.info('Input Nama Petugas')


            sleep(driver)
            driver.find_element(By.ID, "namaPenjamin").click()
            driver.find_element(By.ID, "namaPenjamin").send_keys(namaPenjamin)
            Log.info('Input Nama Pengjamin')



            sleep(driver)
            driver.find_element(By.ID, "keterlibatanLain").click()
            driver.find_element(By.ID, "keterlibatanLain").send_keys(keterlibatanLain)
            Log.info('Input Keterlibatan Pihak Lain')


            sleep(driver)
            driver.find_element(By.ID, "keterangan").click()
            driver.find_element(By.ID, "keterangan").send_keys(keterangan)
            Log.info('Input Keterangan')



        except TimeoutException:
            print("ERRROR")
            pass
                
        sleep(driver)
        i = i + 1
    print('DONE')

@mark.fixture_test()
def teardown():
    quit(driver)














