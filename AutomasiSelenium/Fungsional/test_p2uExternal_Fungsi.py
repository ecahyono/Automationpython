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

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))

from Settings.setup import initDriver, loadDataPath, quit, sleep
from Settings.login import Op_Keamanan_p2u

import logging

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Log_p2uExternal.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("KeamananUAT"))
sheetrangeIndex = wb['P2U_External']

i = 2

inputKategori = sheetrangeIndex['A' + str(i)].value
NamaAtauNip = sheetrangeIndex['B' + str(i)].value
inputKeperluan = sheetrangeIndex['C' + str(i)].value
inputNip = sheetrangeIndex['D' + str(i)].value
inputJabatan = sheetrangeIndex['E' + str(i)].value
InputInstansi = sheetrangeIndex['F' + str(i)].value

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
def test_3_Input():
    driver.implicitly_wait(10)
    sleep(driver)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Akses P2U Eksternal').click()
    sleep(driver)
    print('.')
    Log.info('Akses halaman Daftar Lalu Lintas P2U External')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_3_ClickCreateButton():

    sleep(driver)
    print('masuk ke halaman daftar lalu lintas external')
    sleep(driver)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    Log.info('masuk ke halaman daftar lalu lintas external')

    sleep(driver)
    driver.find_element(By.ID, 'createButton').click()
    Log.info('masuk ke halaman tambah')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_4_inputKategori():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'inputKategori').click()

    if inputKategori == 'Pegawai':
        driver.find_element(By.ID, "pegawai").click()
        driver.find_element(By.ID, 'inputSearch').send_keys(NamaAtauNip)

        if driver.find_elements(By.XPATH, "//li[@id='searchOption0']/div/div/table/tbody/tr/td"):
            driver.find_element(By.XPATH, "//li[@id='searchOption0']/div/div/table/tbody/tr/td").click()
            driver.find_element(By.ID, 'inputKeperluan').send_keys(inputKeperluan)
            attach(data=driver.get_screenshot_as_png())
        else:
            driver.find_element(By.ID, 'inputNip').click()
            driver.find_element(By.ID, 'inputNip').send_keys(inputNip)
            Log.info(' Input NIP ')
            sleep(driver)
            attach(data=driver.get_screenshot_as_png())
            driver.find_element(By.ID, 'inputNama').send_keys(NamaAtauNip)
            Log.info(' Input Nama ')
            sleep(driver)
            attach(data=driver.get_screenshot_as_png())
            driver.find_element(By.ID, 'inputJabatan').send_keys(inputJabatan)
            Log.info(' Input Jabatan ')
            sleep(driver)
            attach(data=driver.get_screenshot_as_png())
            driver.find_element(By.ID, 'inputKeperluan').send_keys(inputKeperluan)
            Log.info(' Input Keperluan ')
            sleep(driver)
            attach(data=driver.get_screenshot_as_png())
            

    elif inputKategori == 'Tamu Dinas':
        driver.find_element(By.ID, "tamuDinas").click()
        Log.info(' Memilih Kategori Tamu Dinas ')
        driver.find_element(By.ID, 'inputSearch').send_keys(NamaAtauNip)
        Log.info(' Cari Nama atau Nip Kategori Tamu Dinas ')
        attach(data=driver.get_screenshot_as_png())

        if driver.find_elements(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label'):
            driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label').click()
            driver.find_element(By.ID, 'inputKeperluan').send_keys(inputKeperluan)
            attach(data=driver.get_screenshot_as_png())

        else:
            driver.find_element(By.ID, 'inputNip').send_keys(inputNip)
            sleep(driver)
            driver.find_element(By.ID, 'inputNama').send_keys(NamaAtauNip)
            sleep(driver)
            driver.find_element(By.ID, 'inputInstansiId').send_keys(InputInstansi)

            driver.find_element(By.XPATH, "//li[contains(.,'" + InputInstansi + "')]").click()
            sleep(driver)
            driver.find_element(By.ID, 'inputJabatan').send_keys(inputJabatan)
            sleep(driver)
            driver.find_element(By.ID, 'inputKeperluan').send_keys(inputKeperluan)
            print('.')
            Log.info(' Input NIP ')
            attach(data=driver.get_screenshot_as_png())
    elif inputKategori == 'Kunjungan Tatap Muka':
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
        driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
        driver.find_element(By.ID, "kunjungan").click()

        driver.find_element(By.ID, "kataKunci").send_keys(NamaAtauNip)
        driver.find_element(By.ID, 'searchButton').click()
        sleep(driver)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
        driver.find_element(By.ID, 'pickKunjungan0').click()
        attach(data=driver.get_screenshot_as_png())

    elif inputKategori == 'Kunjungan Online':
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
        driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
        driver.find_element(By.ID, "kunjungan").click()
        attach(data=driver.get_screenshot_as_png())

        driver.find_element(By.ID, "kataKunci").send_keys(NamaAtauNip)
        driver.find_element(By.ID, 'searchButton').click()
        attach(data=driver.get_screenshot_as_png())
        sleep(driver)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
        driver.find_element(By.ID, 'pickKunjungan0').click()
        attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_ClickSubmitButton():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#submitButton')))
    driver.find_element(By.CSS_SELECTOR, '#submitButton').click()
    Log.info('click button submit')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_6_FilterDataSemua():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys('semua')
    sleep(driver)
    # KETIK NAMA
    driver.find_element(By.XPATH, "//li[contains(.,\'Semua\')]").click()
    Log.info('Katakunci Semua')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_7_InputKatakunci():
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NamaAtauNip)
    sleep(driver)
    Log.info('Search Bedasarkan Nama Lengkap')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test
def test_8_KlikFilterKonfirmBelumKeluar():
    driver.find_element(By.ID, "konfirmasiKeluar").click()
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    Log.info('Clik Filter Belum Konfirmasi Keluar')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_9_KlikDetailWbp():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.CSS_SELECTOR, "#detailButton0 .h-5").click()
    Log.info('Click Button Detail')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_10_KlikKonfirmasiKeluar():
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'backButton')))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    time.sleep(3)
    driver.find_element(By.ID, "submitButton").click()
    Log.info("click Button Submit")
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_11_BerhasilDiperbaharui():
    WebDriverWait(driver, 30).until( EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Diperbaharui\')]')))
    Log.info('Berhasil diperbaharui')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_12_exit():
    quit(driver)










