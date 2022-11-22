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

# file modul
# from module.setup import initDriver, loadDataPath
# from module.login import login

sys.path.append("/Users/will/Documents/work/Automationpython")
from Settings.setup import initDriver, loadDataPath
from Settings.login import login
from dotenv import load_dotenv

load_dotenv()
import json

@mark.fixture_test()
def test_1_SetupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_test()
def test_2_Login():
    login(driver)

@mark.fixture_test()
def test_3_Akses_menu_index():
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Akses Pintu P2U').click()
    print('.')
    print('=akses menu daftar lalu lintas=')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_4_Search_nama_Index(): #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(30) 
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="searchButton"]'))) 
    #BUTTON CARI
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]'))) 
    #BUTTON CARI
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys('nama') 
    #KETIK NAMA
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama Lengkap\')]").click() 
    #PILIH DROPDOWN NAMA LENGKAP
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys("a")
    #KETIK GALIH DI FORM MASUKAN KATA KUNCI
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()  
    #KLIK BUTTON CARI
    print('.')
    print('=Search nama=')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_Search_nomorID_Index(): #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(30) 
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="searchButton"]'))) 
    #BUTTON CARI
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]'))) 
    #BUTTON CARI
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys('Nomor') 
    #KETIK NOMOR
    driver.find_element(By.XPATH, "//li[contains(.,\'Nomor Identitas\')]").click() 
    #PILIH DROPDOWN NOMOR IDENTITAS
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys("31") 
    #KETIK GALIH DI FORM MASUKAN KATA KUNCI
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click() 
    #KLIK BUTTON CARI

    print('.')
    print('=Search Identitas=')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_6_Search_Pegawai_kategori_Index(): #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(30) 
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="searchButton"]'))) 
    #BUTTON CARI
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]'))) 
    #BUTTON CARI
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').send_keys('Kategori') 
    #KETIK NOMOR
    driver.find_element(By.XPATH, "//li[contains(.,\'Kategori\')]").click() 
    #PILIH DROPDOWN NOMOR IDENTITAS
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys("pegawai") 
    #KETIK GALIH DI FORM MASUKAN KATA KUNCI
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click() 
    #KLIK BUTTON CARI
    print('.')
    print('=Search Pegawai=')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_7_Search_keperluan_Index(): #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(30) 
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="searchButton"]'))) 
    #BUTTON CARI
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]'))) 
    #BUTTON CARI
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').send_keys('Keperluan') 
    #KETIK NOMOR
    driver.find_element(By.XPATH, "//li[contains(.,\'Keperluan\')]").click() 
    #PILIH DROPDOWN NOMOR IDENTITAS
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys("Test")
    
    #KETIK GALIH DI FORM MASUKAN KATA KUNCI
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click() 
    #KLIK BUTTON CARI
    print('.')
    print('=Search Keperluan=')
    attach(data=driver.get_screenshot_as_png())




#Mengosongkan kata kunci dan kategori dengan klik button clear value
@mark.fixture_test()
def test_8_Clik_clear_value_Index():
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, '//*[@id="filterColumn"]')
    actions = ActionChains(driver)
    actions.move_to_element(nav1).perform()
    element2 = driver.find_element(By.CSS_SELECTOR, ".el-select__caret:nth-child(2) > svg")
    time.sleep(1)
    actions2 = ActionChains(driver)
    actions2.move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-select__caret:nth-child(2) > svg").click()
    print('.')
    print('=Clear Value Button=')
    attach(data=driver.get_screenshot_as_png())

    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('tessssst') #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci yang tidak sesuai lalu data table yang ditampilkan kosong
    time.sleep(0.5)
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, '//*[@id="kataKunci"]')
    actions = ActionChains(driver)
    actions.move_to_element(nav1).perform()
    element2 = driver.find_element(By.CSS_SELECTOR, ".el-input__clear > svg")
    time.sleep(1)
    actions2 = ActionChains(driver)
    actions2.move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-input__clear > svg").click()
    print('.')
    print('=Clear Value Button=')
    attach(data=driver.get_screenshot_as_png())



#SORTIR TABLE HALAMAN INDEX
@mark.fixture_test()
def test_9_Sortir_data_table_NoInduk_Index():
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, "//span/i[2]").click()
    print('.')
    print('=Sortir No Induk=')
    attach(data=driver.get_screenshot_as_png())
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, "//th[3]/div/span").click()
    print('.')
    print('=Sortir Nama=')
    attach(data=driver.get_screenshot_as_png())
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, "//th[4]/div").click()
    print('.')
    print('=Sortir Jenis=')
    attach(data=driver.get_screenshot_as_png())
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, "//th[5]/div/span/i").click()
    print('.')
    print('=Sortir Tanggal Keluar=')
    attach(data=driver.get_screenshot_as_png())
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, "//th[6]/div/span/i").click()
    print('.')
    print('=Sortir No Tanggal Kembali=')
    attach(data=driver.get_screenshot_as_png())

#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_10_Sortir_5_Halaman_Index():
    #5 HALAMAN
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke1']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'5/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys('100')
    # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    print('= Menampilkan 5  ')
    attach(data=driver.get_screenshot_as_png())


#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_11_Sortir_10_Halaman_Index():
    #10 HALAMAN
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke1']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'10/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys('2')
    time.sleep(1)
    print('.')
    print('= Menampilkan 10  ')
    attach(data=driver.get_screenshot_as_png())


#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_12_Sortir_20_Halaman_Index():
     #20 HALAMAN
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke1']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'20/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys('2')
    time.sleep(1)
    print('.')
    print('= Menampilkan 20  ')
    attach(data=driver.get_screenshot_as_png())


#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_13_Sortir_50_Halaman_Index():
    #50 HALAMAN
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke1']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'50/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys('2')
    time.sleep(1)
    print('.')
    print('= Menampilkan 50  ')
    attach(data=driver.get_screenshot_as_png())

#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_14_Sortir_100_Halaman_Index():
    #100 HALAMAN
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke1']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'100/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys('2')
    time.sleep(1)
    print('.')
    print('= Menampilkan 100  ')
    attach(data=driver.get_screenshot_as_png())


 #Membuka halaman Tambah Data / Cari Identitas melalui klik tombol tambah

#Membuka halaman detail melalui klik tombol aksi icon detail

#Membuka form ubah melalui klik tombol aksi icon uba



#Melakukan export data tabel ke excel
@mark.fixture_test()
def test_15_Export_exel_Index():
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div[1]/button').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div[1]/div/div/div/div[2]/div/button[2]').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil mengunduh file\')]')))
    print('.')
    print('= Export Excel   ')
    attach(data=driver.get_screenshot_as_png())




#Melakukan export data tabel ke pdf
@mark.fixture_test()
def test_16_Export_pdf_Index():
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[5]/div[2]/button').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[5]/div[2]/div/div/div/div[2]/div/button[2]').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil mengunduh file\')]')))
    print('.')
    print('= Export PDF    ')
    attach(data=driver.get_screenshot_as_png())



#Melakukan cetak
@mark.fixture_test()
def test_17_Cetak_Index():
    time.sleep(1)
    driver.implicitly_wait(30)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="printButton"]').click()
    driver.find_element(By.XPATH, '//*[@id="printButton"]/div/div/div/div[2]/div/button[2]').click()


    print('.')
    print('= Cetak ')
    attach(data=driver.get_screenshot_as_png())



def teardown():
    time.sleep(9)
    print('.')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▓▒▒▒▒▒▒▒▒▓▒')
    print('▒▒▓▓▓▓▓▓▓▓▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')


    # DONE SUKSES
    driver.close()
    driver.quit()

    