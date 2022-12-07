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

import sys
from os import environ, path
from dotenv import load_dotenv
load_dotenv()
from openpyxl import load_workbook

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR"))
    wb = load_workbook(filename=r"/Users/will/Documents/work/Automationpython/Filexel/Keamanan.xlsx")
    sys.path.append(environ.get("MACEXCELDIR"))

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))
    sys.path.append(environ.get("WINEXCELDIR"))


from Settings.setup import initDriver, loadDataPath, quit, buttonTambah, buttonSubmit, selectKategoriPegawai, selectKategoriTamuDinas, sleep
from Settings.login import login, loginOperator

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('1Fungsi_Laporan6A_Tambah.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrange = wb['Laporan6A_Tambah']
xr = input('')
i  = xr

filterColumn                          = sheetrange['B'+str(i)].value
nama                                  = sheetrange['C'+str(i)].value


@mark.fixture_test()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')

@mark.fixture_test()
def test_2_login():
    loginOperator(driver)
    Log.info('Login')


@mark.fixture_test()
def test_3_akses_menu_index():
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaporanBulanan']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Formulir Kamtib 6A').click()
    Log.info('Akses Menu Laporan Bulanan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_4_ClickButtonTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#createButton > span')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#createButton > span')))
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, '#createButton > span').click()
    Log.info('Akses Menu Laporan Bulanan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_search_Nama():
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filterColumn"]')))
    if filterColumn == "nama":
        driver.find_element(By.XPATH, '//*[@id="filterColumn"]').send_keys('nama')
        driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
    elif filterColumn == "noregis":
        driver.find_element(By.XPATH, '//*[@id="filterColumn"]').send_keys('no')
        driver.find_element(By.XPATH, "//li[contains(.,\'No Registrasi\')]").click()

@mark.fixture_test()
def test_exit():
    quit(driver)