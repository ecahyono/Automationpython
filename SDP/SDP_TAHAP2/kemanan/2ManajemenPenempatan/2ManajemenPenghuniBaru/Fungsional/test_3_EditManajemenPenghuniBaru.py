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
log_format = '[%(asctime)s %(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('1TambahManajemenPenghuniBaru.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrange = wb['EditManajemenPenghuniBaru']
print('.')
print('Mau Baris Ke Berapa ?')
xr = input('')
i  = xr

filterColumn                                = sheetrange['B'+str(i)].value
NamaEdit                                    = sheetrange['C'+str(i)].value
NoRegisEdit                                 = sheetrange['D'+str(i)].value
SemuaEdit                                   = sheetrange['E'+str(i)].value
Status                                      = sheetrange['F'+str(i)].value
blokformEdit                                = sheetrange['G'+str(i)].value
LantaiEdit                                  = sheetrange['H'+str(i)].value
KamarEdit                                   = sheetrange['I'+str(i)].value
TanggalPenempatanEdit                       = sheetrange['J'+str(i)].value
KeteranganEdit                              = sheetrange['K'+str(i)].value


@mark.fixture_test()
def test_1_SetupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Login')


@mark.fixture_test()
def test_2_Login():
    login(driver)
    Log.info('Login')

@mark.fixture_test()
def test_3_AksesMenu_ManajemenBlokDanKamar():
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['ManajemenPenempatan']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Manajemen Penghuni Baru').click()
    Log.info('akses menu Manajemen Blok Dan Kamar')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_4_Pilih_filterColumn():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.ID, 'statusVerifikasi').click()
    if Status == 'Dalam Proses':
        driver.find_element(By.XPATH, "//li[contains(.,\'Dalam Proses\')]").click()

    elif Status == 'Perbaikan':
        driver.find_element(By.XPATH, "//li[contains(.,\'Perbaikan\')]").click()

@mark.fixture_test()
def test_5_clickButtonSearch():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.ID, 'searchButton').click()
    Log.info('Menekan button search')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_6_klikButtonEdit():
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    sleep(driver)
    driver.find_element(By.ID, 'updateButton0').click()
@mark.fixture_test()
def test_8_KlikPenempatan():
    sleep(driver)
    driver.find_element(By.ID, 'penempatan-0').click()
    Log.info('Klik button Penempatan')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_9_PilihBlok():
    sleep(driver)
    driver.execute_script("window.scrollTo(0,310.9090881347656)")
    driver.find_element(By.ID, "blokForm").click()
    if blokform == 'Blok mapenaling E':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Blok mapenaling E\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Blok mapenaling E\')]").click()
    elif blokform == 'Blok mapenaling gal':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'blok mapenaling gal\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'blok mapenaling gal\')]").click()
    elif blokform == 'Naga':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Naga\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Naga\')]").click()

    Log.info('memilih blok mapenaling')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_10_pilihLantai():
    sleep(driver)
    driver.find_element(By.ID, 'lantaiForm').click()
    if Lantai == 'lantai 1':
        driver.find_element(By.XPATH, "//li[@id=\'lantaiOption-0\']").click()
    elif Lantai == 'lantai 2':
        driver.find_element(By.XPATH, "//li[@id=\'lantaiOption-1\']").click()
    Log.info('memilih lantai')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_10_pilihKamar():
    sleep(driver)
    driver.find_element(By.ID, 'kamarForm').click()
    if Kamar == 'kamar 1':
        driver.find_element(By.XPATH, "//li[@id=\'kamarOption-0\']").click()
    elif Kamar == 'kamar 2':
        driver.find_element(By.XPATH, "//li[@id=\'kamarOption-1\']").click()
    Log.info('memilih kamar')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_11_tanggalPenempatan():
    sleep(driver)
    driver.find_element(By.ID, 'tanggalMutasiForm').send_keys(TanggalPenempatanEdit)
    driver.find_element(By.ID, 'tanggalMutasiForm').send_keys(Keys.ENTER)
    Log.info('memilih tanggal penempatan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_12_Keterangan():
    sleep(driver)
    driver.find_element(By.ID, 'keteranganForm').send_keys(KeteranganEdit)
    Log.info('menginputkan keterangan')
    attach(data=driver.get_screenshot_as_png())

"""
@mark.fixture_test()
def test_13_ButtonSubmit():
    sleep(driver)
    driver.find_element(By.ID, 'submitButton').click()
    Log.info('menekan button submit ')
    attach(data=driver.get_screenshot_as_png())
"""
@mark.fixture_test()
def test_exit():
    sleep(driver)
    quit(driver)