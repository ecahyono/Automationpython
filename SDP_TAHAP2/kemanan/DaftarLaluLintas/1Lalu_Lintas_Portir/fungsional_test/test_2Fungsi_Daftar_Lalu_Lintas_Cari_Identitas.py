from distutils.archive_util import make_archive
# from os import PRIO_PGRP, environ
# from re import S, T
# from threading import TIMEOUT_MAX
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

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR"))
    sys.path.append("/Users/will/Documents/work/Automationpython")
elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))

from Settings.setup import initDriver, loadDataPath, quit
from Settings.login import login

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('result.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


@mark.fixture_test()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_test()
def test_2_login():
    login(driver)

@mark.fixture_test()
def test_3_akses_menu_index():
    driver.implicitly_wait(60)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Daftar Lalu Lintas').click()
    print('.')
    Log.info('akses menu daftar lalu lintas')
    attach(data=driver.get_screenshot_as_png())


#==============++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++===================

#HALAMAN CARI
#Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai 
#Halaman Manajemen Administrasi Keamanan - Cari Identitas

 #Membuka halaman Tambah Data / Cari Identitas melalui klik tombol tambah
@mark.fixture_test()
def test_4_membuka_halaman_tambah_index():
    driver.implicitly_wait(60)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, 'createButton').click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5 > path")))
    #WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="backButton"]')))
    #driver.find_element(By.XPATH, '//*[@id="backButton"]').click()
    print('.')
    Log.info('Membuka Halaman Tambah')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_5_Button_Next_Prev():
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.CSS_SELECTOR, ".btn-next svg").click()
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".btn-prev svg").click()
    Log.info('button next search data')


@mark.fixture_test()
def test_6_sortir_table_cari_noreg_cari_identitas():

    driver.implicitly_wait(60)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, '//*[@id="nomorReg"]').click()
    print('.')
    Log.info(' Memilih Dropdown Noregis  ')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('123')
    print('.')
    Log.info('Input Noregis  ')

    driver.implicitly_wait(60)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    print('.')
    Log.info('Click Button Cari ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_7_sortir_table_cari_nama_cari_identitas():
    driver.implicitly_wait(60)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
    print('.')
    Log.info('Memilih Dropdown Nama  ')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('WILLLD BINTI eko cah cah ge')
    print('.')
    Log.info('Input Nama  ')

    driver.implicitly_wait(60)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    print('.')
    Log.info('Click Button Cari')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_8_sortir_table_cari_JenisKejahatan_cari_identitas():
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, '//*[@id="jenisKejahatan"]').click()
    print('.')
    Log.info('Memilih Dropdown Jenis Kejahatan  ')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('Korupsi')
    print('.')
    Log.info('Input katakunci  ')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    print('.')
    Log.info('Click Button Cari')
    attach(data=driver.get_screenshot_as_png())
    
@mark.fixture_test()
def test_9_search_data_aktif_cari_identitas():
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, '//*[@id="semua"]').click()
    driver.find_element(By.XPATH, '//*[@id="dataAktif"]/span[1]/span').click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="dataAktif"]/span[1]/span').click()
    print('.')
    Log.info(' Search Data Aktiv  ')
    attach(data=driver.get_screenshot_as_png())
    
@mark.fixture_test()
def test_10_search_residivis_cari_identitas():
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, '//*[@id="semua"]').click()
    driver.find_element(By.XPATH, '//*[@id="residivis"]/span[1]/span').click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="residivis"]/span[1]/span').click()
    print('.')
    Log.info(' Search Residivis  ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_11_Sortir_5_Halaman_cari_identitas():
    #5 HALAMAN
    driver.implicitly_wait(60)
    driver.execute_script("window.scrollTo(0,326)")
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '(//input[@type=\'text\'])[3]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'5/halaman\')]").click()
    driver.find_element(By.XPATH, '//input[@type=\'number\']').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, "//input[@type=\'number\']").send_keys("2") #Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 5 halaman cari  ')
    attach(data=driver.get_screenshot_as_png())



@mark.fixture_test()
def test_12_sortir_10_Halaman_cari_identitas():
    #10 HALAMAN
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '(//input[@type=\'text\'])[3]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'10/halaman\')]").click()
    driver.find_element(By.XPATH, '//input[@type=\'number\']').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//input[@type=\'number\']').send_keys('3') #Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 10 halaman cari ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_13_sortir_20_Halaman_cari_identitas():
    #20 HALAMAN
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '(//input[@type=\'text\'])[3]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'20/halaman\')]").click()
    driver.find_element(By.XPATH, '//input[@type=\'number\']').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//input[@type=\'number\']').send_keys('3') #Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 20 halaman cari ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_14_sortir_50_Halaman_cari_identitas():
    #50 HALAMAN
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '(//input[@type=\'text\'])[3]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'50/halaman\')]").click()
    driver.find_element(By.XPATH, '//input[@type=\'number\']').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//input[@type=\'number\']').send_keys('3') #Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 50 halaman cari ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_15_sortir_100_Halaman_cari_identitas():
    #100 HALAMAN
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '(//input[@type=\'text\'])[3]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'100/halaman\')]").click()
    driver.find_element(By.XPATH, '//input[@type=\'number\']').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//input[@type=\'number\']').send_keys('3') #Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info('Menampilkan 100 halaman cari ')
    attach(data=driver.get_screenshot_as_png())





def teardown():
    quit(driver)
    