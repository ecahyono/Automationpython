from distutils.archive_util import make_archive
from os import PRIO_PGRP, environ
from re import S, T
from threading import TIMEOUT_MAX
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
from pathlib import Path
#file modul
#from module.setup import initDriver, loadDataPath
#from module.login import login

sys.path.append("/Users/will/Documents/work/Automationpython")
from Settings.setup import initDriver, loadDataPath
from Settings.login import login
from dotenv import load_dotenv
load_dotenv()
import json

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
    
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Portir').click()
    print('.')
    print('==========akses menu daftar lalu lintas==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_4_sortir_5_Halaman_Index():
    #5 HALAMAN
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'5/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys('100') #Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    print('================================================================================= Menampilkan 5  ')
    attach(data=driver.get_screenshot_as_png())

    #Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_5_sortir_10_Halaman_Index():
    #10 HALAMAN
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'10/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys('2')
    time.sleep(1)
    print('.')
    print('================================================================================= Menampilkan 10  ')
    attach(data=driver.get_screenshot_as_png())


#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_6_sortir_20_Halaman_Index():
     #20 HALAMAN
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'20/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys('2')
    time.sleep(1)
    print('.')
    print('================================================================================= Menampilkan 20  ')
    attach(data=driver.get_screenshot_as_png())


#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_7_sortir_50_Halaman_Index():
    #50 HALAMAN
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'50/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys('100')
    time.sleep(1)
    print('.')
    print('================================================================================= Menampilkan 50  ')
    attach(data=driver.get_screenshot_as_png())

#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_8_sortir_100_Halaman_Index():
    #100 HALAMAN
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'100/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys('2')
    time.sleep(1)
    print('.')
    print('================================================================================= Menampilkan 100  ')
    attach(data=driver.get_screenshot_as_png())




@mark.fixture_test()
def test_4_sortir_table_cari_Semua_Portir():
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Semua\')]").click()
    print('=')
    print(' = Memilih Dropdown Semua  ')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('USER')
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.ID, 'searchButton').click()
    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5")))
    print('=')
    print(' = Input Semua  ')
    attach(data=driver.get_screenshot_as_png())




@mark.fixture_test()
def test_6_search_data_kategori_NoInduk_Index(): #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(20)
    time.sleep(1)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.ID, 'filterColumn')))
    
    driver.find_element(By.ID, 'filterColumn').send_keys('induk')
    driver.find_element(By.XPATH, '//li[contains(.,\'Nomor Induk\')]').click()
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('50120')
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()
    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5")))

    print('.')
    print('================================================================================= Search Data Form Kategori No Induk  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_7_SearchDataKategori_NoSuratPenetapan_Index(): #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(20)
    time.sleep(1)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.ID, 'filterColumn')))
    
    driver.find_element(By.ID, 'filterColumn').send_keys('Surat')
    driver.find_element(By.XPATH, '//li[contains(.,\'Nomor Surat Penetapan\')]').click()
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('NS1005')
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()
    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5")))

    print('.')
    print('================================================================================= Search Data Form Kategori No Induk  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_8_SearchDataStatus_MasukPortir_Index(): #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(20)
    time.sleep(1)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.ID, 'filterColumn').click()
    driver.find_element(By.XPATH, '//li[contains(.,\'Semua\')]').click()
    driver.find_element(By.XPATH, '//*[@id="statusColumn"]').send_keys('Masuk Portir')
    driver.find_element(By.XPATH, "//li[contains(.,\'Masuk Portir\')]").click()
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()
    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5")))

    print('.')
    print('================================================================================= Search Data Form Kategori No Induk  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_9_SearchDataStatus_KeluarKeamanan_Index(): #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(20)
    time.sleep(1)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.ID, 'filterColumn').click()
    driver.find_element(By.XPATH, '//li[contains(.,\'Semua\')]').click()
    driver.find_element(By.XPATH, '//*[@id="statusColumn"]').send_keys('keluar keamanan')
    driver.find_element(By.XPATH, "//li[contains(.,\'Keluar Keamanan\')]").click()
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()
    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5")))

    print('.')
    print('================================================================================= Search Data Form Kategori No Induk  ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_10_SearchDataStatus_KeluarPortir_Index(): #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(20)
    time.sleep(1)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.ID, 'filterColumn').click()
    driver.find_element(By.XPATH, '//li[contains(.,\'Semua\')]').click()
    driver.find_element(By.XPATH, '//*[@id="statusColumn"]').send_keys('keluar porti')
    driver.find_element(By.XPATH, "/li[contains(.,\'Keluar Portir\')]").click()
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()
    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5")))

    print('.')
    print('================================================================================= Search Data Form Kategori No Induk  ')
    attach(data=driver.get_screenshot_as_png())



@mark.fixture_test()
def test_11_SearchDataStatus_BelumKembali_Index(): #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(20)
    time.sleep(1)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.ID, 'filterColumn').click()
    driver.find_element(By.XPATH, '//li[contains(.,\'Semua\')]').click()
    driver.find_element(By.XPATH, '//*[@id="statusColumn"]').send_keys('Belum Kembali')
    driver.find_element(By.XPATH, "//li[contains(.,\'Belum Kembali\')]").click()
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()
    #WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5")))

    print('.')
    print('================================================================================= Search Data Form Kategori No Induk  ')
    attach(data=driver.get_screenshot_as_png())




def teardown():
    time.sleep(10)
    print('.')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▓▒▒▒▒▒▒▒▒▓▒')
    print('▒▒▓▓▓▓▓▓▓▓▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    driver.close()
    driver.quit()