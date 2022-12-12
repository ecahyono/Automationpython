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
from Settings.login import login, loginOperator, loginSPV

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('2Verifikasi.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrange = wb['2Verifikasi']
print('.')
print('masukan baris ke berapa yang akan di baca !!!')
i  = input('')

filter                                  = sheetrange['B'+str(i)].value
namaBlok                                = sheetrange['C'+str(i)].value
status                                  = sheetrange['D'+str(i)].value
jumlahlantai                            = sheetrange['E'+str(i)].value
semua                                   = sheetrange['F'+str(i)].value
UbahStatus                              = sheetrange['G'+str(i)].value




@mark.fixture_test()
def test_1_SetupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Login')


@mark.fixture_test()
def test_2_Login():
    loginSPV(driver)
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
    driver.find_element(By.LINK_TEXT, 'Manajemen Blok dan Kamar').click()
    print('.')
    Log.info('Manajemen Blok Dan Kamar')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_4_ClickButtonTambah_PemetaanBlock():
    driver.implicitly_wait(30)
    #sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.border:nth-child(1)')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    print('.')
    Log.info('Click Button Tambah halaman Pemetaan Block')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_searchData_DalamProses():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'filterColumn')))
    time.sleep(1)
    if filter == 'status':
        driver.find_element(By.ID, 'filterColumn').send_keys('Status')
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#status_verifikasi > span')))
        driver.find_element(By.CSS_SELECTOR, '#status_verifikasi > span').click()
        driver.find_element(By.ID, 'kataKuncuStatusVerifikasi').click()
        driver.find_element(By.XPATH, "//li[contains(.,\'Dalam Proses\')]").click()
    elif filter == 'blok':
        driver.find_element(By.ID, 'kataKunci').send_keys(namaBlok)

    elif filter == 'jumlahlantai':
        driver.find_element(By.ID, 'kataKunci').send_keys(jumlahlantai)

    elif filter == 'semua':
        driver.find_element(By.ID, 'kataKunci').send_keys(semua)

    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
@mark.fixture_test()
def test_6_clickbuttonDalamProses():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, '#verifikasi-0 > span').click()

@mark.fixture_test()
def test_7_Verifikasi():
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="status_verifikasi"]')))
    driver.find_element(By.XPATH, '//*[@id="status_verifikasi"]').click()
    if UbahStatus == 'Diizinkan':
        driver.find_element(By.XPATH, '//*[@id="status_verifikasi"]').send_keys('Diizinkan')
        driver.find_element(By.XPATH, "//li[contains(.,\'Diizinkan\')]").click()
        Log.info('.')
        Log.info('Ubah Status Menjadi Di Izinkan')
        attach(data=driver.get_screenshot_as_png())
    elif UbahStatus == 'Perbaikan':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//li[@id=\'perbaikan\'])[2]")))
        driver.find_element(By.XPATH, "//li[contains(.,\'Perbaikan\')]").click()
        Log.info('.')
        Log.info('Ubah Status Menjadi Di perbaikan')
        attach(data=driver.get_screenshot_as_png())
    elif UbahStatus == 'Ditolak':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//li[@id=\'ditolak\'])[2]")))
        driver.find_element(By.XPATH, "(//li[@id=\'Ditolak\'])[2]").click()
        Log.info('.')
        Log.info('Ubah Status Menjadi Di Tolak')
        attach(data=driver.get_screenshot_as_png())
    elif UbahStatus == 'DalamProses':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//li[@id=\'dalamProses\'])[2]")))
        driver.find_element(By.XPATH, "(//li[@id=\'DalamProses\']/span)[2]").click()
        Log.info('.')
        Log.info('Ubah Status Menjadi Dalam Proses')
        attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_9_InputKeterangan():
    sleep(driver)
    driver.implicitly_wait(60)
    driver.find_element(By.ID, "keterangan").click()
    driver.find_element(By.ID, "keterangan").send_keys(keterangan)
    Log.info('.')
    Log.info('Input Keterangan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_exit():
    quit(driver)