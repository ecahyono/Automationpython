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
# pergi ke halaman tambah
def test_9_ButtonTambah_PegawaiTambah():
    driver.implicitly_wait(20)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButton"]')))
    print('.')
    print('========== Membuka Halaman Tambah ==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_5_kategori_Pegawaitambah(): # memilih kategori pegawai
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "pegawai").click()
    print('.')
    print('========== Input Kategori Pegawai  ==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
# mencari pegawai berdasarkan nama
def test_6_NamaSearch_Pegawaitambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'inputSearch')))
    driver.find_element(By.ID, 'inputSearch').send_keys('nabila')
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'tr:nth-child(1) > .el-descriptions__label')))
    driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label').click()

@mark.fixture_test()
# mencari pegawai berdasarkan nama
def test_7_InputKeperluan_Pegawaitambah():
    driver.find_element(By.XPATH, '//*[@id="inputKeperluan"]').send_keys('deskripsi')
    driver.implicitly_wait(15)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))

    print('.')
    print('========== Input pencarian berdasarkan nama   ==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_15_Button_Tambah_to_TamuDinassearch_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    print('.')
    print('========== Membuka Halaman Tambah ==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_16_kategori_TamuDinasNAMA_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "tamuDinas").click()
    print('.')
    print('========== Input kategori tamu dinas ==========')
    attach(data=driver.get_screenshot_as_png())

    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'inputSearch')))
    driver.find_element(By.ID, 'inputSearch').send_keys('a')
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label')))
    driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label').click()
    driver.find_element(By.XPATH, '//*[@id="inputKeperluan"]').send_keys('keperluan')
    print('.')
    print('========== Input tamu dinas  ==========')
    attach(data=driver.get_screenshot_as_png())



@mark.fixture_test()
# pergi ke halaman tambah
def test_7_HalamanTambah_NIP_PegawaiTambah():
    driver.implicitly_wait(20)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButton"]')))
    print('.')
    print('========== Membuka Halaman Tambah ==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
# memilih kategori pegawai dan mengisikan deskripsi
def test_8_SearchNIP_Pegawaitambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "pegawai").click()
    print('.')
    print('========== Input Jenis Keluar  ==========')
    attach(data=driver.get_screenshot_as_png())
    driver.implicitly_wait(15)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID, 'inputSearch')))
    driver.find_element(By.ID, 'inputSearch').send_keys('34')
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'tr:nth-child(1) > .el-descriptions__label')))
    driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label').click()
    driver.find_element(By.XPATH, '//*[@id="inputKeperluan"]').send_keys('deskripsi')
    driver.implicitly_wait(15)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))

    print('.')
    print('========== Input pencarian berdasarkan nama   ==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_8_membuka_halaman_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    print('.')
    print('========== Membuka Halaman Tambah ==========')
    attach(data=driver.get_screenshot_as_png())



@mark.fixture_test()
def test_17_NamaSearch_TamuDinasNIP_tambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "tamuDinas").click()
    print('.')
    print('========== Input kategori tamu dinas ==========')
    attach(data=driver.get_screenshot_as_png())

    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'inputSearch')))
    driver.find_element(By.ID, 'inputSearch').send_keys('3')
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label')))
    driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label').click()
    driver.find_element(By.XPATH, '//*[@id="inputKeperluan"]').send_keys('keperluan')
    print('.')
    print('========== Input tamu dinas  ==========')
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

    driver.close()
    driver.quit()