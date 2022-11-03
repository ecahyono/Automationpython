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

def test_3_akses_menu_index():
    
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


@mark.fixture_test()
def test_4_membuka_halaman_tambah():
    driver.implicitly_wait(10)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5 > path")))
    #WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="backButton"]')))
    #driver.find_element(By.XPATH, '//*[@id="backButton"]').click()
    print('.')
    print('================================================================================= Membuka Halaman Tambah  ')
    attach(data=driver.get_screenshot_as_png())



@mark.fixture_test()
def test_5_sortir_table_cari_nama_Tambah():
    driver.implicitly_wait(20)
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/label/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
    print('.')
    print('================================================================================= Memilih Dropdown Nama  ')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div/input')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div/input').send_keys('WILLLD BINTI eko cah cah ge')
    print('.')
    print('================================================================================= Input Nama  ')

    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button').click()
    print('.')
    print('==========Click Button Cari  ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_6_Click_Button_Detile_Tambah():
    driver.implicitly_wait(10)
    time.sleep(2)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.CSS_SELECTOR, ".h-5 > path").click()
    print('.')
    print('==========Click Button Update  ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_7_Click_Button_Tambah_WBP_Tambah():
    driver.implicitly_wait(10)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div/div[2]/button').click()
    print('.')
    print('==========Click Button Tambah WBP  ==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_8_sortir_detil_wbp_Tambah():
    WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tab-0"]')))
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-0"]')))
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

    print('.')
    print('================================================================================= Detile WBP')

@mark.fixture_test()
def test_9_detile_perkara_Tambah():

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tab-registrasi"]')))
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-registrasi"]')))
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
    print('.')
    print('================================================================================= Detile Perkara')



@mark.fixture_test()
def test_Input_Tanggal_Keluar_Tambah():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="keluarKeamanan"]')))
    driver.find_element(By.XPATH, '//*[@id="keluarKeamanan"]').send_keys('24/12/2018')
    driver.find_element(By.XPATH, '//*[@id="keluarKeamanan"]').send_keys(Keys.ENTER)

    print('.')
    print('========== Input Tanggal Keluar  ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_Input_Tanggal_Harus_Kembali_Tambah():
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').send_keys('29/12/2018')
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').send_keys(Keys.ENTER)
    print('.')
    print('========== Input Tanggal Harus Kembali  ==========')
    attach(data=driver.get_screenshot_as_png())
    

@mark.fixture_test()
def test_Input_Jenis_Keluar_Tambah():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jenisKeluar"]')))
    driver.find_element(By.XPATH, '//*[@id="jenisKeluar"]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Mutasi Keluar\')]").click()
    print('.')
    print('========== Input Jenis Keluar  ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_Input_Deskripsi_Tambah():
    driver.implicitly_wait(10)
    driver.execute_script("window.scrollTo(0,1462.5)")
    driver.find_element(By.CSS_SELECTOR, "#deskripsi").click()
    driver.find_element(By.CSS_SELECTOR, "#deskripsi").send_keys("koookok")
    print('.')
    print('========== Input Deskripsi Behasil ==========')
    attach(data=driver.get_screenshot_as_png())
"""
@mark.fixture_test()
def test_Input_katakunci_Tambah():
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
    print('================================================================================= Click Clear Value Button Kata Kunci dan inputan data tidak sesuai  ')
    attach(data=driver.get_screenshot_as_png())
"""



@mark.fixture_test()
def test_Button_Submit_Tambah():
    driver.implicitly_wait(10)
    time.sleep(3)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSubmit"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSubmit"]').click()
    print('.')
    print('========== Menekan Button Submit  ==========')
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
