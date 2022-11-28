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
#file module
#from module.setup import initDriver, loadDataPath
#from module.login import login

sys.path.append("/Users/will/Documents/work/Automationpython")
from Settings.setup import initDriver, loadDataPath
from Settings.login import login
from dotenv import load_dotenv
load_dotenv()
import json

@mark.fixture_test()
def test_1_setupOS_HalamanTambah():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_test()
def test_2_login_HalamanTambah():
    login(driver)

@mark.fixture_test()
def test_3_akses_menu_HalamanTambah():
    driver.implicitly_wait(60)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Daftar Lalu Lintas').click()
    print('=')
    print(' = akses menu daftar lalu lintas')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_4_membuka_halaman_HalamanTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5 > path")))
    #WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="backButton"]')))
    #driver.find_element(By.XPATH, '//*[@id="backButton"]').click()
    print('=')
    print(' = Membuka Halaman Tambah  ')
    attach(data=driver.get_screenshot_as_png())



@mark.fixture_test()
def test_5_sortir_table_cari_nama_HalamanTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    time.sleep(0.4)
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
    print('=')
    print(' = Memilih Dropdown Nama  ')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('TEST BIN ayah')
    #driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('Wildan Cahyono')
    print('=')
    print(' = Input Nama  ')

    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    print('=')
    print(' = Click Button Cari  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_6_Click_Button_Detile_HalamanTambah():
    driver.implicitly_wait(60)
    time.sleep(2)
    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.CSS_SELECTOR, ".h-5 > path").click()
    print('=')
    print(' = Click Button Update  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_7_Click_Button_Tambah_WBP_HalamanTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, 'createButton').click()
    print('=')
    print(' = Click Button Tambah WBP  ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()    
def test_8_sortir_detil_wbp_HalamanTambah():
    WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tab-0"]')))
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-0"]')))
    driver.execute_script("window.scrollTo(0,1462.5)")
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[3]/div').click()
    driver.find_element(By.XPATH, '//*[@id="tab-1"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-2"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-3"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-4"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-5"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-6"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-7"]').click()

    print('=')
    print(' = Detile WBP')

@mark.fixture_test()
def test_9_detile_perkara_HalamanTambah():

    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tab-registrasi"]')))
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-registrasi"]')))
    driver.execute_script("window.scrollTo(0,1462.5)")
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[3]/div').click()
    driver.find_element(By.XPATH, '//*[@id="tab-registrasi"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-sidang"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-tahanan_rumah"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-meninggal_dunia"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-mutasi_upt"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-pm"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-pembebasan"]').click()
    print('=')
    print(' = Detile Perkara')

@mark.fixture_test()
def test_10_Input_JenisKeluar_HalamanTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jenisKeluar"]')))
    driver.find_element(By.XPATH, '//*[@id="jenisKeluar"]').send_keys("asimilasi")
    driver.find_element(By.XPATH, "//li[contains(.,\'Asimilasi\')]").click()
    print('=')
    print(' = Input Jenis Keluar  ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_11_Input_Tanggal_Keluar_HalamanTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="keluarKeamanan"]')))
    driver.find_element(By.XPATH, '//*[@id="keluarKeamanan"]').send_keys('24/12/2018')
    driver.find_element(By.XPATH, '//*[@id="keluarKeamanan"]').send_keys(Keys.ENTER)

    print('=')
    print(' = Input Tanggal Keluar  ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_12_Input_Deskripsi_HalamanTambah():
    driver.implicitly_wait(60)
    driver.execute_script("window.scrollTo(0,1462.5)")
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#deskripsi')))
    driver.find_element(By.CSS_SELECTOR, "#deskripsi").click()
    driver.find_element(By.CSS_SELECTOR, "#deskripsi").send_keys("koookok")
    print('=')
    print(' = Input Deskripsi Behasil ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_13_Input_Tanggal_Harus_Kembali_HalamanTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tanggalKembali"]')))
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').send_keys('29/12/2018 12:00:00')
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').send_keys(Keys.ENTER)
    print('=')
    print(' = Input Tanggal Harus Kembali  ')
    attach(data=driver.get_screenshot_as_png())
    
@mark.fixture_test()
def test_14_tambah_Pengwal_HalamanTambah():
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="addPengawal"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="addPengawal"]').click()
    print('=')
    print(' = Input tambah pengawal  ')
    attach(data=driver.get_screenshot_as_png())



@mark.fixture_test()
def test_15_JenisPengawal_HalamanTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jenis0"]')))
    driver.find_element(By.XPATH, '//*[@id="jenis0"]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Internal\')]").click()
    print('=')
    print(' = Input tambah Jenis pengawal  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_16_NamaPengawalInternal_HalamanTambah():
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="pengawalInternal0"]').click
    driver.find_element(By.XPATH, '//*[@id="pengawalInternal0"]').send_keys('robi')
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="optionPengawal00"]')))
    driver.find_element(By.XPATH, '//*[@id="optionPengawal00"]').click()
    print('=')
    print(' = Input nama pengawal Internal  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_17_JenisPengawalEksternal_HalamanTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jenis1"]')))
    driver.find_element(By.XPATH, '//*[@id="jenis1"]').click()
    driver.find_element(By.CSS_SELECTOR, "#Eksternal1").click()
    print('=')
    print(' = Input tambah Jenis pengawal  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_18_NamaPengawalEksternal_HalamanTambah():
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="pengawal1"]').click
    driver.find_element(By.XPATH, '//*[@id="pengawal1"]').send_keys('rehan')
    time.sleep(1)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, "//td[contains(.,'operator')]")))
    time.sleep(0.4)
    driver.find_element(By.XPATH, "//td[contains(.,'operator')]").click()
    print('=')
    print(' = Input nama pengawal Enternal  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_19_ButtonSubmitInternal_HalamanTambah():
    driver.implicitly_wait(60)
    time.sleep(3)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSubmit"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSubmit"]').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    print('=')
    print(' = Menekan Button Submit  ')
    attach(data=driver.get_screenshot_as_png())
 





def teardown():
    time.sleep(5)
    print('=')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▓▒▒▒▒▒▒▒▒▓▒')
    print('▒▒▓▓▓▓▓▓▓▓▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')


    driver.close()
    driver.quit()
