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
def test_1_loginKanwil():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')
    kanwiljabar(driver)
    Log.info('Login Spv Laporan Kamtib 6A')

@mark.fixture_test()
def test_2_AksesMenuSpv():
    sleep(driver)
    menulaporan6a(driver)
    Log.info('Akses halaman Laporan 6A')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_3_VerifikasiLaporan():
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
            time.sleep(2)
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'formfilterUpt2')))
            driver.find_element(By.ID, "formfilterUpt2").click()
            driver.find_element(By.ID, "formfilterUpt2").send_keys("Rutan Kelas I Bandung")
            driver.find_element(By.XPATH, "//span[contains(.,\'Rutan Kelas I Bandung\')]").click()
            Log.info('Input UPT')

            sleep(driver)
            driver.find_element(By.ID, "searchButton").click()
            Log.info('Click Button Search')

            sleep(driver)
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'buttonVerifikasi')))
            driver.find_element(By.ID, "buttonVerifikasi").click()
            Log.info('Click Button Verifikasi')



            sleep(driver)
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'simpanVerifikasi')))
            time.sleep(3)
            driver.find_element(By.ID, "statusVerifikasiModal").click()
            Log.info('Click Verifikasi Modal')


            sleep(driver)
            driver.find_element(By.ID, "diizinkan").click()
            Log.info('Ubah Status Verifikasi')


            sleep(driver)
            driver.find_element(By.ID, "keterangan").send_keys("keterangan")
            Log.info('Input Keterangan')


            sleep(driver)
            driver.find_element(By.ID, "simpanVerifikasi").click()
            Log.info('Click Button Simpan Verifikasi')

        except TimeoutException:
            print("ERRROR")
            pass
                
        sleep(driver)
        i = i + 1
    print('DONE')

@mark.fixture_test()
def teardown():
    quit(driver)














