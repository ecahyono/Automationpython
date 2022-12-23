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

from Settings.setup import initDriver, loadDataPath, quit, buttonTambah, buttonSubmit, selectKategoriPegawai, selectKategoriTamuDinas, sleep, waituntill
from Settings.login import login

import logging

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Fungsi_P2U_KonfirmasiKeluar.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrange = wb['Fungsi_P2U_Index']
xr = input("")
i = xr

inputKategori                        = sheetrange['B' + str(i)].value
NamaWBP                              = sheetrange['C' + str(i)].value

@mark.fixture_test()
def test_1_SetupOS_Search_Tambah():
    
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()


@mark.fixture_test()
def test_2_Login_SearchTambah():
    login(driver)


@mark.fixture_test()
def test_3_Akses_menu_index():
    sleep(driver)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Akses Pintu P2U').click()
    print('.')
    Log.info(' akses menu daftar lalu lintas =')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_4_Search_Nama():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys('nama')
    sleep(driver)
    # KETIK NAMA
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama Lengkap\')]").click()
    sleep(driver)
    # PILIH DROPDOWN NAMA LENGKAP
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NamaWBP)
    sleep(driver)
    # KETIK GALIH DI FORM MASUKAN KATA KUNCI
    Log.info('Search Bedasarkan Nama Lengkap')
    attach(data=driver.get_screenshot_as_png())
    driver.find_element(By.ID, "konfirmasiKeluar").click()
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()

@mark.fixture_test()
def test_5_ClickDetail_KonfirmKeluar():
    sleep(driver)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    time.sleep(5)
    driver.find_element(By.ID, "detailButton0").click()

@mark.fixture_test()
def test_6_KonfirmKeluar():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    time.sleep(5)
    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Diperbaharui\')]')))

def teardown():
    quit(driver)