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
from Settings.login import login

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('RegisterH_Verifikasi.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


sheetrange = wb['RegisterH_Verifikasi']
print(".")
print("masukan baris yang akan dibaca")
xr = input("")
i  = xr

filterColumn                                    = sheetrange['B'+str(i)].value
namaLengkap                                     = sheetrange['C'+str(i)].value
filterStatus                                    = sheetrange['D'+str(i)].value
UbahStatus                                      = sheetrange['E'+str(i)].value
keterangan                                      = sheetrange['F'+str(i)].value


@mark.fixture_test()
def test_1_setupOS_Search():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_test()
def test_2_login_Search():
    login(driver)

@mark.fixture_test()
def test_3_aksesmenu_Search():
    driver.implicitly_wait(60)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(nav1).perform()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Register H')))
    driver.find_element(By.LINK_TEXT, 'Register H').click()
    Log.info('akses menu Register H')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_4_keyword_nama():  # Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(60)
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.ID, 'filterColumn').send_keys('nama')
    driver.find_element(By.ID, 'filterColumn').click()
    Log.info(' Memilih kategori Nama ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_nama():
    sleep(driver)
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="namaLengkap"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(namaLengkap)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    Log.info('Search nama')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_6_status_dalamproses():
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'filterStatus')))
    driver.find_element(By.ID, 'filterStatus').click()
    if filterStatus == 'dalamproses':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dalamProses"]')))
        driver.find_element(By.ID, 'filterStatus').send_keys('dalam Proses')
        driver.find_element(By.ID, 'dalamProses').click()
        Log.info(' Filter status Dalam Proses ')
        attach(data=driver.get_screenshot_as_png())
    elif filterStatus == 'perbaikan':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dalamProses"]')))
        driver.find_element(By.XPATH, "//li[@id=\'perbaikan\']").click()
        Log.info('.')
        Log.info(' Filter status Dalam Proses ')
        attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_7_Click_StatusDalamProses():
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modalButton0"]')))
    driver.find_element(By.XPATH, '//*[@id="modalButton0"]').click()
    Log.info('.')
    Log.info('Click Button Status Dalam Proses')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_8_Ubah_Status_Diizinkan():
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="statusVerifikasiModal"]')))
    driver.find_element(By.XPATH, '//*[@id="statusVerifikasiModal"]').click()
    if UbahStatus == 'diizinkan':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//li[@id=\'diizinkan\'])[2]")))
        driver.find_element(By.XPATH, "(//li[@id=\'diizinkan\'])[2]").click()
        Log.info('.')
        Log.info('Ubah Status Menjadi Di Izinkan')
        attach(data=driver.get_screenshot_as_png())
    elif UbahStatus == 'perbaikan':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//li[@id=\'perbaikan\'])[2]")))
        driver.find_element(By.XPATH, "(//li[@id=\'perbaikan\'])[2]").click()
        Log.info('.')
        Log.info('Ubah Status Menjadi Di perbaikan')
        attach(data=driver.get_screenshot_as_png())
    elif UbahStatus == 'ditolak':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//li[@id=\'ditolak\'])[2]")))
        driver.find_element(By.XPATH, "(//li[@id=\'ditolak\'])[2]").click()
        Log.info('.')
        Log.info('Ubah Status Menjadi Di Tolak')
        attach(data=driver.get_screenshot_as_png())
    elif UbahStatus == 'dalamProses':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//li[@id=\'dalamProses\'])[2]")))
        driver.find_element(By.XPATH, "(//li[@id=\'dalamProses\']/span)[2]").click()
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
def test_10_SimpanButton():
    sleep(driver)
    driver.implicitly_wait(60)
    driver.find_element(By.ID, "simpanVerifikasi").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Diperbaharui\')]')))
    Log.info('.')
    Log.info('Button Simpan Verifikasi')
    attach(data=driver.get_screenshot_as_png())

# DONE
@mark.fixture_test()
def test_exit():
    quit(driver)