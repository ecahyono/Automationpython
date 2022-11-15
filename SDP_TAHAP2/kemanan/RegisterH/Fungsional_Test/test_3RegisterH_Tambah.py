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
def test_1_setupOS_Search():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_test()
def test_2_login_Search():
    login(driver)

@mark.fixture_test()
def test_3_aksesmenu_Search():
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Register H').click()
    print('.')
    print('==========akses menu daftar lalu lintas==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_4_membuka_halaman_tambah_index_Search():
    driver.implicitly_wait(60)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, 'createButton').click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="backButton"]')))
    print('.')
    print('================================================================================= Membuka Halaman Tambah  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_search_data_kategori_nama_HalamanTambah():  # Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(60)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'filterColumn')))

    time.sleep(1)
    driver.find_element(By.ID, 'filterColumn').send_keys('nama')
    driver.find_element(By.ID, 'filterColumn').click()

    driver.find_element(By.XPATH, '//*[@id="nama"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('WILLLD BINTI eko cah cah ge')
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    print('.')
    print('')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_6_ClickButton_Daftarkan_HalamanTambah():  # Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="view0"]')))
    time.sleep(0.5)
    driver.find_element(By.XPATH,'//*[@id="view0"]').click()
    print('.')
    print('')
    attach(data=driver.get_screenshot_as_png())




@mark.fixture_test()
def test_7_InputNoSurat_HalamanTambah():
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="noSurat"]').send_keys('srt001/01')
    print('.')
    print('')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_8_InputTanggalSurat_HalamanTambah():
    driver.implicitly_wait(60)
    driver.find_element(By.ID, 'tanggalSurat').send_keys('24/11/2022')
    driver.find_element(By.ID, 'tanggalSurat').send_keys(Keys.ENTER)
    print('.')
    print('')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_9_InputTanggalMulai_HalamanTambah():
    driver.implicitly_wait(60)
    driver.find_element(By.ID, 'tanggalMulai').send_keys('24/11/2022')
    driver.find_element(By.ID, 'tanggalMulai').send_keys(Keys.ENTER)
    print('.')
    print('')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_10_InputLamaPerasingan_HalamanTambah():
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH,'//*[@id="lamaPengasingan"]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="lamaPengasingan"]/div/input').send_keys('3')

    print('.')
    print('')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_11_InputAlasan_HalamanTambah():
    driver.implicitly_wait(60)
    driver.find_element(By.ID, 'alasan').send_keys('berantem')

    print('.')
    print('')
    attach(data=driver.get_screenshot_as_png())

