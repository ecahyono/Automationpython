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
elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))


from Settings.setup import initDriver, loadDataPath, quit, sleep
from Settings.login import login

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('1SearchData_IndexPortir.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("KEAMANANEXCEL"))
sheetrangeIndex = wb['Portir_SearchDataIndex']

index  = input('')

filterColumnindex                            = sheetrangeIndex['B'+str(index)].value
nama_lengkapindex                            = sheetrangeIndex['C'+str(index)].value
nomor_indukindex                             = sheetrangeIndex['D'+str(index)].value
NomorSuratindex                              = sheetrangeIndex['E'+str(index)].value
Pendaftarindex                               = sheetrangeIndex['F'+str(index)].value
semuaindex                                   = sheetrangeIndex['G'+str(index)].value
statusColumnindex                            = sheetrangeIndex['H'+str(index)].value


@mark.fixture_test()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()


@mark.fixture_test()
def test_2_login():
    login(driver)


@mark.fixture_test()
def test_PTR_001():
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Portir').click()

    Log.info('Mengakses halaman Portir dengan memilih modul Keamanan kemudian pilih menu Lalu Lintas lalu pilih submenu Portir')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_PTR_002():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    sleep(driver)

    if filterColumn == 'semua':
        driver.find_element(By.XPATH, "//li[contains(.,\'Semua\')]").click()
        print('=')
        Log.info(' Memilih Dropdown Semua  ')
        attach(data=driver.get_screenshot_as_png())

        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(semua)

        Log.info(' Input kata kunci semua  ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumn == 'nomor induk':
        driver.find_element(By.ID, 'filterColumn').send_keys('induk')
        driver.find_element(By.XPATH, '//li[contains(.,\'Nomor Induk\')]').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(nomor_induk)

        Log.info(' Input kata kunci No induk  ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumn == 'Nomor Surat Penetapan':
        driver.find_element(By.ID, 'filterColumn').send_keys('Surat')
        driver.find_element(By.XPATH, '//li[contains(.,\'Nomor Surat Penetapan\')]').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NomorSurat)

        Log.info(' Input kata kunci Nomor Surat Penetapan  ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumn == 'Pendaftar':
        driver.find_element(By.ID, 'filterColumn').send_keys('Pendaftar')
        driver.find_element(By.XPATH, '//li[contains(.,\'created_by\')]').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(Pendaftar)
        Log.info(' Input kata kunci Pendaftar  ')
        attach(data=driver.get_screenshot_as_png())

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    time.sleep(1)
    driver.find_element(By.ID, 'searchButton').click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5")))
    print('=')
    Log.info(' Input Semua  ')
    attach(data=driver.get_screenshot_as_png())

    Log.info('Melakukan pengecekan filtering data')


