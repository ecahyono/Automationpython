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
def test_2_login_HalamanEdit():
    login(driver)


#AKSES MENU 
@mark.fixture_test()
def test_3_akses_menu_HalamanEdit():
    
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Daftar Lalu Lintas').click()
    print('.')
    print('==========akses menu daftar lalu lintas==========')
    attach(data=driver.get_screenshot_as_png())

# MENAKAN BUTTON UBAH
@mark.fixture_test()
def test_4_Click_ButtonUbah_HalamanEdit():
    driver.implicitly_wait(30)
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    driver.find_element(By.CSS_SELECTOR, ".text-green-500 .h-5").click()
    time.sleep(5)
    
    print('.')
    print('=================================================================================Click Button Update Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5__sortir_detil_wbp_HalamanEdit():
    WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tab-0"]')))
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-0"]')))
    driver.execute_script("window.scrollTo(0,1462.5)")
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-0"]').click()
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
def test_6_detile_perkara_HalamanEdit():

    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tab-registrasi"]')))
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-registrasi"]')))
    driver.execute_script("window.scrollTo(0,1462.5)")
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
#MEMUAT ULANG HALAMAN WEB
@mark.fixture_test()
def test_7_Muat_Ulang_HalamanEdit():
    driver.implicitly_wait(10)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonReset"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonReset"]').click()
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click() 
    time.sleep(10)
    print('.')
    print('=================================================================================Click Button Muat Ulang Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png()) 


#MENEGEDIT DESKRIPSI
@mark.fixture_test()
def test_8_Ubah_Deskripsi_HalamanEdit():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="deskripsi"]')))
    driver.find_element(By.XPATH, '//*[@id="deskripsi"]').clear()
    driver.find_element(By.XPATH, '//*[@id="deskripsi"]').send_keys('deskripsi baru')
    print('.')
    print('=================================================================================Ubah Deskripsi Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png()) 
"""
@mark.fixture_test()

#MENGEDIT TANGGAL KELUAR
def test_Ubah_Tanggal_Keluar_Edit():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "keluarKeamanan")))
    driver.find_element(By.ID, "keluarKeamanan").clear()
    driver.find_element(By.ID, "keluarKeamanan").send_keys(Keys.ENTER)
    print('.')
    print('=================================================================================Ubah Tanggal Keluar Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png()) 


#MENGEDIT TANGGAL KEMBALI
@mark.fixture_test()
def test_Ubah_Tanggal_kembali_Edit():
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').clear()
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').send_keys(Keys.ENTER)
    print('.')
    print('=================================================================================Ubah Tanggal Kembali Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png()) 
    time.sleep(10)

#MENGEDIT JENIS KELUAR
@mark.fixture_test()
def test_Ubah_Jenis_Keluar_Edit():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jenisKeluar"]')))
    driver.find_element(By.XPATH, '//*[@id="jenisKeluar"]').clear()

    time.sleep(10)

    print('.')
    print('=================================================================================Ubah Jenis Keluar Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png())
"""



#CLOSE 
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
