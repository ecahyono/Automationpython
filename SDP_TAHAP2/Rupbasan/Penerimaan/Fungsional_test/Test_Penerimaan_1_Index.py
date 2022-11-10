from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from pytest_html_reporter import attach
from pytest import mark
import platform
import time
import os
import pytest
import json
import sys

from dotenv import load_dotenv
load_dotenv()

#file modul
if platform.system() == 'Darwin':
    sys.path.append('/Users/will/Documents/work/Automationpython')
elif platform.system() == 'Windows':
    sys.path.append(r'C:\Users\user\Documents\TRCH\Automationpython\Settings')

from setup import initDriver, loadDataPath
from login import login

# init driver by os
@mark.fixture_index_penerimaan
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_index_penerimaan
def test_login():
    login(driver)

@mark.fixture_index_penerimaan
def test_akses_menu():
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.LINK_TEXT, 'Penerimaan').click()
    attach(data=driver.get_screenshot_as_png())

#inputtext-Dropdown+Celarvalue button
@mark.fixture_index_penerimaan
def test_fieldinput_n_Dropdown_n_Clear_index_penerimaan():
    field = driver.find_element(By.XPATH, pathData ['buttonrupbasan']['filterabledropdownindex'])
    field.click()
    field.send_keys('Nama')
    field.send_keys(Keys.DOWN)
    field.send_keys(Keys.ENTER)
    elemnt = driver.find_element(By.XPATH, pathData ['buttonrupbasan']['clearkategori'])
    ActionChains(driver).move_to_element(elemnt).perform()
    WebDriverWait(driver, 20)
    elemnt.click()

    katkun = driver.find_element(By.XPATH, pathData ['buttonrupbasan']['maskakunci'])
    katkun.click()
    katkun.send_keys('Kata kunci @ 123')
    elemnt = driver.find_element(By.XPATH, pathData ['buttonrupbasan']['clearkatkun'])
    ActionChains(driver).move_to_element(elemnt).perform()
    WebDriverWait(driver, 20)
    elemnt.click()

    Registrasi = driver.find_element(By.XPATH, pathData ['buttonrupbasan']['dropdownJregIndex'])
    Registrasi.click()
    Registrasi.send_keys('Register Barang Rampasan Negara')
    Registrasi.send_keys(Keys.DOWN)
    Registrasi.send_keys(Keys.ENTER)
    elemnt = driver.find_element(By.XPATH, pathData ['buttonrupbasan']['clearvaluejnreg'])
    ActionChains(driver).move_to_element(elemnt).perform()
    WebDriverWait(driver, 20)
    elemnt.click()

    Instansi = driver.find_element(By.XPATH, pathData ['buttonrupbasan']['instansiindex'])
    Instansi.click()
    time.sleep(2)
    Instansi.send_keys('POLDA JABAR')
    Instansi.send_keys(Keys.DOWN)
    Instansi.send_keys(Keys.ENTER)
    elemnt = driver.find_element(By.XPATH, pathData ['buttonrupbasan']['clearvalueinstnsi'])
    ActionChains(driver).move_to_element(elemnt).perform()
    WebDriverWait(driver, 20)
    elemnt.click()

    attach(data=driver.get_screenshot_as_png())

# @mark.fixture_index_penerimaan
# def test_cari_berdasarkan_():

@mark.fixture_index_penerimaan
def test_sortirtabel():
    driver.find_element(By.XPATH, pathData ['buttonrupbasan']['ascendingtable']).click()
    # driver.find_element(By.XPATH, pathData ['buttonrupbasan']['descedingtable']).click()
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_index_penerimaan
def test_halamanpageindex():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, pathData ['buttonrupbasan']['ascendingtable'])))
    driver.find_element(By.XPATH, pathData['Other Search']['Dropdown Halaman']).click() 
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['20halaman']).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, pathData ['buttonrupbasan']['ascendingtable'])))
    driver.find_element(By.XPATH, pathData['Other Search']['Dropdown Halaman']).click() 
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['50halaman']).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, pathData ['buttonrupbasan']['ascendingtable'])))
    driver.find_element(By.XPATH, pathData['Other Search']['Dropdown Halaman']).click() 
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['100halaman']).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, pathData ['buttonrupbasan']['ascendingtable'])))
    driver.find_element(By.XPATH, pathData['Other Search']['Dropdown Halaman']).click() 
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['5halaman']).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, pathData ['buttonrupbasan']['ascendingtable'])))
    page = driver.find_element(By.XPATH, pathData['Other Search']['Pergi Ke'])
    page.send_keys(Keys.BACK_SPACE)
    page.send_keys('4')
    page.send_keys(Keys.ENTER)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, pathData ['buttonrupbasan']['ascendingtable'])))
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_index_penerimaan
def test_cetakBA():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['CetakBA']).click() 
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_index_penerimaan
def test_Buka_halaman_Ubah():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['ubah']).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, pathData ['Id Navigate Button']['Back Button'])))
    driver.find_element(By.XPATH, pathData ['Id Navigate Button']['Back Button']).click()
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_index_penerimaan
def test_Buka_halaman_tambah():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['tambah']).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, pathData ['Id Navigate Button']['Back Button'])))
    driver.find_element(By.XPATH, pathData ['Id Navigate Button']['Back Button']).click()
    attach(data=driver.get_screenshot_as_png())
    
@mark.fixture_index_penerimaan
def test_Buka_halaman_Daftarbarang():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['daftarbarang']).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, pathData ['Id Navigate Button']['Back Button'])))
    driver.find_element(By.XPATH, pathData ['Id Navigate Button']['Back Button']).click()
    attach(data=driver.get_screenshot_as_png())

# EXPORT && PRINT
@mark.fixture_index_penerimaan
def test_halaman_exportexel():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['exportexel']).click() 
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['semuhalaman']).click() 
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['Halamaninisaja']).click() 
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_index_penerimaan
def test_halaman_exportpdf():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['exportPDF']).click() 
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['PDFHalini']).click() 
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['PDFSemuaHal']).click() 
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_index_penerimaan
def test_halaman_print():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['cetak']).click() 
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['cetaksemua']).click() 
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['cetakhalinisaj']).click() 
    attach(data=driver.get_screenshot_as_png())