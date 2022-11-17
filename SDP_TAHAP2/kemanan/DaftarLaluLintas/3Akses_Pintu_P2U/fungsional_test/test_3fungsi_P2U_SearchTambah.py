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
from module.template import buttonTambah, buttonSubmit, selectKategoriPegawai, selectKategoriTamuDinas, quit
import sys
from pathlib import Path
sys.path.append("/Users/will/Documents/work/Automationpython")
from Settings.setup import initDriver, loadDataPath
from Settings.login import login
from dotenv import load_dotenv
load_dotenv()
import json

# file modul

# from module.login import login


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

# ==================================================== PEGAWAI ====================================================
"""
@mark.fixture_test()
# pergi ke halaman tambah
def test_4_ButtonTambah_PegawaiTambah():
    buttonTambah(driver)


@mark.fixture_test()
def test_5_Kategori_Pegawaitambah(): # memilih kategori pegawai
    selectKategoriPegawai(driver)
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
    buttonSubmit(driver)
    print('= Click Button Submit  =')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
# pergi ke halaman tambah
def test_9_ButtonTambahNIP_PegawaiTambah():
    buttonTambah(driver)
    print('= tambah nip pegawai = ')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
# memilih kategori pegawai dan mengisikan deskripsi
def test_10_SearchNIP_Pegawaitambah():
    selectKategoriPegawai(driver)
    print('= Memilih Kategori Pegawai =')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
# Search Nip Pegawai
def test_11_SearchNIP_Pegawaitambah():
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
def test_12_InputDeskripsi_Pegawaitambah():
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="inputKeperluan"]').send_keys('deskripsi')
    print('.')
    print('= Input Deskripsi Nip =')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
# Button Submit NIP
def test_13_ButtonSubmitNip_Pegawaitambah():
    buttonSubmit(driver)
    print('= Button Submit Nip =')
    attach(data=driver.get_screenshot_as_png())

# ==================================================== TAMU DINAS ====================================================
@mark.fixture_test()
# masuk halaman tambah
def test_14_ButtonTambah_TamuDinasTambah():
    buttonTambah(driver)
    print('.')
    print('==================================================== TAMU DINAS ====================================================')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
# input kategori berdasarkan tamu dinas
def test_15_Kategori_TamuDinasNamaTambah():
    selectKategoriTamuDinas(driver)
    print('= Pilih kategori tamu dinas =')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
# input search tamu dinas
def test_16_Search_TamuDinasNAMA_TamuDinasNamaTambah():
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
def test_17_InputKeperluanTamuDinas_TamuDinasNamaTambah():
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="inputKeperluan"]').send_keys('keperluan')
    print('.')
    print('= Input Keperluan Tamu Dinas  =')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_18_ButtonSubmitTamuDinas_TamuDinasNamaTambah():
    buttonSubmit(driver)
    print('= Button Submit Tamu Dinas  =')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
# pergi ke halaman tambah
def test_19_ButtonTambah_TamuDinasNIPTambah():
    buttonTambah(driver)
    print('.')
    print('= Membuka Halaman Tambah Untuk Input Tamu Dinas =')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_20_Kategori_TamuDinasNIPTambah():
    selectKategoriTamuDinas(driver)
    print('= Input kategori tamu dinas =')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
# Input Deskripsi
def test_21_SearchNip_TamuDinasNIPTambah():
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
def test_22_InputKeperluan_TamuDinasNIPTambah():
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="inputKeperluan"]').send_keys('keperluan')
    print('.')
    print('= Input Keperluan Tamu dinas  =')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
# Button Submit tamu dinas nip
def test_23_ButtonSubmit_TamuDinasNIPTambah():
    buttonSubmit(driver)
    print('.')
    print('= Input Keperluan Tamu dinas  =')
    attach(data=driver.get_screenshot_as_png())

"""
# ==================================================== Kunjungan Onsite ====================================================
@mark.fixture_test()
# button tambah kunjungan onsite
def test_24_HalamanTambah_KunjunganOnsiteTambah():
    buttonTambah(driver)
    print('= Masuk Ke Halaman Tambah data Kunjungan Onsite  =')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
# memilih kategori berdasarkan kunjungna onsite
def test_25_SelectKategori_KunjunganOnsiteTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "kunjungan").click()
    print('.')

@mark.fixture_test()
# input katakunci berdasarkan nama
def test_27_PickNama_KunjunganOnsiteTambah():
    driver.implicitly_wait(60)
    driver.find_element(By.ID, 'pickKunjungan0').click()
@mark.fixture_test()
def test_28_submit_KunjunganOnsiteTambah():
    buttonSubmit(driver)

# ==================================================== Kunjungan Online ====================================================
@mark.fixture_test()
# button tambah kunjungan onsite
def test_29_HalamanTambah_KunjunganOnlineTambah():
    buttonTambah(driver)
    print('= Masuk Ke Halaman Tambah data Kunjungan Online  =')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
# memilih kategori berdasarkan kunjungna onsite
def test_30_SelectKategori_KunjunganOnlineTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "kunjunganOnline").click()
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
# input katakunci berdasarkan nama
def test_31_PickNama_KunjunganOnlineTambah():
    driver.implicitly_wait(60)
    driver.find_element(By.ID, 'pickKunjungan0').click()
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_32_submit_KunjunganOnlineTambah():
    buttonSubmit(driver)
    attach(data=driver.get_screenshot_as_png())


def teardown():
    quit(driver)
