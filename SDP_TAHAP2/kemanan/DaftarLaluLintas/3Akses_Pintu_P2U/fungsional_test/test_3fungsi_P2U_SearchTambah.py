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
sys.path.append("/Users/will/Documents/work/Automationpython")
from Settings.setup import initDriver, loadDataPath, buttonTambah
from Settings.login import login
from dotenv import load_dotenv

load_dotenv()
import json


@mark.fixture_test()
def test_1_setupOS_Search_Tambah():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()


@mark.fixture_test()
def test_2_login_SearchTambah():
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
    driver.find_element(By.LINK_TEXT, 'Akses Pintu P2U').click()
    print('.')
    print('= akses menu daftar lalu lintas =')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
# pergi ke halaman tambah
def test_4_ButtonTambah_PegawaiTambah():
    buttonTambah(driver)


@mark.fixture_test()
def test_5_kategori_Pegawaitambah(): # memilih kategori pegawai
    driver.implicitly_wait(60)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "pegawai").click()
    print('.')
    print('= Input Kategori Pegawai  =')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
# mencari pegawai berdasarkan nama
def test_6_NamaSearch_Pegawaitambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'inputSearch')))
    driver.find_element(By.ID, 'inputSearch').send_keys('nabila')
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'tr:nth-child(1) > .el-descriptions__label')))
    driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label').click()
    print('.')
    print('= Input pencarian berdasarkan nama   =')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
# Input Deskripsi
def test_7_InputKeperluan_Pegawaitambah():
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="inputKeperluan"]').send_keys('deskripsi')
    print('.')
    print('= Input Keperluan =')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
# Submit inputan
def test_8_ButtonSubmit_Pegawaitambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))

    print('.')
    print('= Click Button Submit  =')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
# pergi ke halaman tambah
def test_9_ButtonTambahNIP_PegawaiTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButton"]')))
    print('.')
    print('==================================================== PEGAWAI ====================================================')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
# memilih kategori pegawai dan mengisikan deskripsi
def test_9_SearchNIP_Pegawaitambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "pegawai").click()
    print('.')
    print('= Memilih Kategori Pegawai =')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
# Search Nip Pegawai
def test_10_SearchNIP_Pegawaitambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'inputSearch')))
    driver.find_element(By.ID, 'inputSearch').send_keys('34')
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'tr:nth-child(1) > .el-descriptions__label')))
    driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label').click()
    print('.')
    print('= Search Nip =')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
# memilih kategori pegawai dan mengisikan deskripsi
def test_11_InputDeskripsi_Pegawaitambah():
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="inputKeperluan"]').send_keys('deskripsi')
    print('.')
    print('= Input Deskripsi Nip =')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
# Button Submit NIP
def test_12_ButtonSubmitNip_Pegawaitambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))

    print('.')
    print('= Button Submit Nip =')
    attach(data=driver.get_screenshot_as_png())

# ==================================================== TAMU DINAS ====================================================
@mark.fixture_test()
# masuk halaman tambah
def test_13_ButtonTambah_TamuDinasTambah():
    buttonTambah(driver)
    print('.')
    print('==================================================== TAMU DINAS ====================================================')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
# input kategori berdasarkan tamu dinas
def test_14_kategori_TamuDinasNamaTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "tamuDinas").click()
    print('.')
    print('= Pilih kategori tamu dinas =')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
# input search tamu dinas
def test_11_Search_TamuDinasNAMA_TamuDinasNamaTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'inputSearch')))
    driver.find_element(By.ID, 'inputSearch').send_keys('a')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label')))
    driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label').click()
    print('.')
    print('= Input Search Tamu Dinas berdasarkan nama  =')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
# Input Deskripsi keperluan tamu dinas
def test_12_InputKeperluanTamuDinas_TamuDinasNamaTambah():
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="inputKeperluan"]').send_keys('keperluan')
    print('.')
    print('= Input Keperluan Tamu Dinas  =')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_13_ButtonSubmitTamuDinas_TamuDinasNamaTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    print('.')
    print('= Button Submit Tamu Dinas  =')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
# pergi ke halaman tambah
def test_14_ButtonTambah_TamuDinasNIPTambah():
    buttonTambah(driver)
    print('.')
    print('= Membuka Halaman Tambah Untuk Input Tamu Dinas =')
    attach(data=driver.get_screenshot_as_png())




@mark.fixture_test()
def test_15_Kategori_TamuDinasNIPTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "tamuDinas").click()
    print('.')
    print('= Input kategori tamu dinas =')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
# Input Deskripsi
def test_16_SearchNip_TamuDinasNIPTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'inputSearch')))
    driver.find_element(By.ID, 'inputSearch').send_keys('3')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label')))
    driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label').click()
    print('.')
    print('= Search Nip tamu dinas =')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
# Input Deskripsi
def test_17_InputKeperluan_TamuDinasNIPTambah():
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="inputKeperluan"]').send_keys('keperluan')
    print('.')
    print('= Input Keperluan Tamu dinas  =')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
# Button Submit tamu dinas nip
def test_18_ButtonSubmit_TamuDinasNIPTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    print('.')
    print('= Input Keperluan Tamu dinas  =')
    attach(data=driver.get_screenshot_as_png())


# ==================================================== Kunjungan Onsite ====================================================
@mark.fixture_test()
def test_19_HalamanTambah_Onsitetambah():
    buttonTambah(driver)



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

    driver.close()
    driver.quit()