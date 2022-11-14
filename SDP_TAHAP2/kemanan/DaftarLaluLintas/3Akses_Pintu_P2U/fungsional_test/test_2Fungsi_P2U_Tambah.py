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

from dotenv import load_dotenv
load_dotenv()
#file modul
from module.setup import initDriver, loadDataPath
from module.login import login

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
    
    driver.implicitly_wait(15)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Akses Pintu P2U').click()
    print('.')
    print('==========akses menu daftar lalu lintas==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_4_membuka_halaman_tambah():
    driver.implicitly_wait(20)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButton"]')))
    print('.')
    print('========== Membuka Halaman Tambah ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_kategori_Pegawai_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "pegawai").click()
    print('.')
    print('========== Input Jenis Keluar  ==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_6_NamaSearch_Pegawai_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'inputSearch')))
    driver.find_element(By.ID, 'inputSearch').send_keys('nabila')
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'tr:nth-child(1) > .el-descriptions__label')))
    driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label').click()
    driver.find_element(By.XPATH, '//*[@id="inputKeperluan"]').send_keys('deskripsi')
    driver.implicitly_wait(15)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))

    print('.')
    print('========== Input pencarian berdasarkan nama   ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_8_membuka_halaman_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    print('.')
    print('========== Membuka Halaman Tambah ==========')
    attach(data=driver.get_screenshot_as_png())


"""


@mark.fixture_test()
def test_9_NipSearch_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'inputSearch')))
    driver.find_element(By.ID, 'inputSearch').click()
    driver.find_element(By.ID, 'inputSearch').send_keys('3460')
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'tr:nth-child(1) > .el-descriptions__label')))
    driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label').click()
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'inputKeperluan')))
    driver.find_element(By.ID, 'inputKeperluan').send_keys('new input keperluan')
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
  
    print('.')
    print('========== Input pencarian berdasarkan Nip  ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_10_input_nip_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'inputNip')))
    driver.find_element(By.ID, 'inputNip').send_keys('7321377')

    print('.')
    print('========== Input nip ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_11_input_namaLengkap_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'inputNama')))
    driver.find_element(By.ID, 'inputNama').send_keys('new input nama')
    print('.')
    print('========== Input nama lengkap ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_12_input_Jabatan_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'inputJabatan')))
    driver.find_element(By.ID, 'inputJabatan').send_keys('new input jabatan')
    print('.')
    print('========== Input Jabatan ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_13_input_keperluan_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'inputKeperluan')))
    driver.find_element(By.ID, 'inputKeperluan').send_keys('new input keperluan')
    print('.')
    print('========== Input nip ==========')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    print('========== button tambah new input ( tidak get data dari pencarian) ==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_15_Button_Tambah_to_TamuDinassearch_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    print('.')
    print('========== Membuka Halaman Tambah ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_16_kategori_TamuDinasNAMA_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "tamuDinas").click()
    print('.')
    print('========== Input kategori tamu dinas ==========')
    attach(data=driver.get_screenshot_as_png())

    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'inputSearch')))
    driver.find_element(By.ID, 'inputSearch').send_keys('a')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label')))
    driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label').click()
    driver.find_element(By.XPATH, '//*[@id="inputKeperluan"]').send_keys('keperluan')
    print('.')
    print('========== Input tamu dinas  ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_17_NamaSearch_TamuDinasNIP_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "tamuDinas").click()
    print('.')
    print('========== Input kategori tamu dinas ==========')
    attach(data=driver.get_screenshot_as_png())

    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'inputSearch')))
    driver.find_element(By.ID, 'inputSearch').send_keys('3')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label')))
    driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label').click()
    driver.find_element(By.XPATH, '//*[@id="inputKeperluan"]').send_keys('keperluan')
    print('.')
    print('========== Input tamu dinas  ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_18_NamaSearch_TamuDinasNIP_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "tamuDinas").click()
    print('.')
    print('========== Input kategori tamu dinas ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_19_input_nip_tamuDinas_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'inputNip')))
    driver.find_element(By.ID, 'inputNip').send_keys('7321377')
    
    print('.')
    print('========== Input nip ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_20_input_nip_tamuDinas_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'inputNama')))
    driver.find_element(By.ID, 'inputNama').send_keys('input nama tamu dinas')
    
    print('.')
    print('========== Input nip ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_21_Instansi_TamuDinasNIP_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputInstansiId"]')))
    driver.find_element(By.XPATH, '//*[@id="inputInstansiId"]').click()
    driver.find_element(By.ID, "optionInstansi0").click()
    print('.')
    print('========== Input kategori tamu dinas ==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_21_input_nip_tamuDinas_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'inputJabatan')))
    driver.find_element(By.ID, 'inputJabatan').send_keys('input jabatan ')
    
    print('.')
    print('========== Input nip ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_22_input_nip_tamuDinas_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'inputKeperluan')))
    driver.find_element(By.ID, 'inputKeperluan').send_keys('input keperluan test ')
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    
    print('.')
    print('========== Input nip ==========')
    attach(data=driver.get_screenshot_as_png())

"""



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

    print('░░▄███▄███▄')
    print('░░█████████')
    print('░░▒▀█████▀░')
    print('░░▒░░▀█▀')
    print('░░▒░░█░')
    print('░░▒░█')
    print('░░░█')
    print('░░█░░░░███████')
    print('░██░░░██▓▓███▓██▒')
    print('██░░░█▓▓▓▓▓▓▓█▓████')
    print('██░░██▓▓▓(◐)▓█▓█▓█')
    print('███▓▓▓█▓▓▓▓▓█▓█▓▓▓▓█')
    print('▀██▓▓█░██▓▓▓▓██▓▓▓▓▓█')
    print('░▀██▀░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█')
    print('░░░░▒░░░█▓▓▓▓▓█▓▓▓▓▓▓█')
    print('░░░░▒░░░█▓▓▓▓█▓█▓▓▓▓▓█')
    print('░▒░░▒░░░█▓▓▓█▓▓▓█▓▓▓▓█')
    print('░▒░░▒░░░█▓▓▓█░░░█▓▓▓█')
    print('░▒░░▒░░██▓██░░░██▓▓██')
    driver.close()
    driver.quit()

    