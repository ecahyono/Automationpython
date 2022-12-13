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
fh = logging.FileHandler('2VerifikasiPenghuniBaru.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrange = wb['VerifikasiPenghuniBaru']
print('.')
print('masukan baris ke berapa yang akan di baca !!!')
i  = input('')

filter                                  = sheetrange['B'+str(i)].value
namaWbp                                 = sheetrange['C'+str(i)].value
noRegis                                 = sheetrange['D'+str(i)].value
blok                                    = sheetrange['E'+str(i)].value
kamar                                   = sheetrange['F'+str(i)].value
statusVerifikasi                        = sheetrange['G'+str(i)].value
BlokMapenaling                          = sheetrange['H'+str(i)].value
Ubahstatus                              = sheetrange['I'+str(i)].value

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
def test_3_AksesMenu_ManajemenPenghuniBaru():
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
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'filterColumn')))
    driver.find_element(By.ID, 'filterColumn').click()
    time.sleep(1)
    # sleep(driver)
    if filter == 'Nama':
        driver.find_element(By.XPATH, "//li[@id=\'identitas_nama_lengkap\']").click()

    elif filter == 'No Registrasi':
        driver.find_element(By.XPATH, "//li[@id=\'perkara_nmr_reg_gol\']").click()

    elif filter == 'Blok':
        driver.find_element(By.XPATH, "//li[@id=\'blok_deskripsi\']").click()

    elif filter == 'Kamar':
        driver.find_element(By.XPATH, "//li[@id=\'kamar_no_kamar\']").click()

    elif filter == 'Status':
        driver.find_element(By.ID, 'statusVerifikasi').click()
        if statusVerifikasi == 'Dalam Proses':
            driver.find_element(By.XPATH, "//li[contains(.,\'Dalam Proses\')]").click()

        elif statusVerifikasi == 'Perbaikan':
            driver.find_element(By.XPATH, "//li[contains(.,\'Perbaikan\')]").click()

@mark.fixture_test()
def test_5_ButtonSearch():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.ID, 'searchButton').click()

@mark.fixture_test()
def test_6_clickbuttonDalamProses():
    #sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#verifikasi-0 > span')))
    driver.find_element(By.CSS_SELECTOR, '#verifikasi-0 > span').click()

@mark.fixture_test()
def test_7_Verifikasi():
    #sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#submitButton > span')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="status_verifikasi"]')))
    driver.find_element(By.XPATH, '//*[@id="status_verifikasi"]').click()
    #sleep(driver)
    if UbahStatus == 'Diizinkan':
        driver.find_element(By.XPATH, '//*[@id="status_verifikasi"]').send_keys('Diizinkan')
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//li[@id=\'diizinkan\']")))
        driver.find_element(By.XPATH, "//li[@id=\'diizinkan\']").click()
        Log.info('Ubah Status Menjadi Di Izinkan')
        attach(data=driver.get_screenshot_as_png())
    elif UbahStatus == 'Perbaikan':
        driver.find_element(By.XPATH, '//*[@id="status_verifikasi"]').send_keys('Perbaikan')
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//li[@id=\'perbaikan\']")))
        driver.find_element(By.XPATH, "//li[@id=\'perbaikan\']").click()
        Log.info('Ubah Status Menjadi Di perbaikan')
        attach(data=driver.get_screenshot_as_png())
    elif UbahStatus == 'Ditolak':
        driver.find_element(By.XPATH, '//*[@id="status_verifikasi"]').send_keys('Ditolak')
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//li[@id=\'ditolak\']")))
        driver.find_element(By.XPATH, "//li[@id=\'ditolak\']").click()
        Log.info('Ubah Status Menjadi Di Tolak')
        attach(data=driver.get_screenshot_as_png())
    elif UbahStatus == 'DalamProses':
        driver.find_element(By.XPATH, '//*[@id="status_verifikasi"]').send_keys('DalamProses')
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//li[@id=\'dalam_proses\']/span")))
        driver.find_element(By.XPATH, "//li[@id=\'dalam_proses\']/span").click()
        Log.info('Ubah Status Menjadi Dalam Proses')
        attach(data=driver.get_screenshot_as_png())


#ubah status belum ada id
@mark.fixture_test()
def test_exit():
    quit(driver)