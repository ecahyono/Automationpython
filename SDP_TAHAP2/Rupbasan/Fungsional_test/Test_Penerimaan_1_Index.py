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

from module.setup import initDriver, loadDataPath
from module.login import login

# init driver by os
@mark.fixture_index_penerimaan
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_index_penerimaan
def test_2_login():
    login(driver)

@mark.fixture_index_penerimaan
def test_3_akses_menu():
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.LINK_TEXT, 'Penerimaan').click()
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_index_penerimaan
def test_sortirtabel():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['buttonrupbasan']['daftarbarang'])))
    driver.find_element(By.XPATH, pathData ['buttonrupbasan']['ascendingtable']).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['buttonrupbasan']['daftarbarang'])))
    driver.find_element(By.XPATH, pathData ['buttonrupbasan']['descendingtable']).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['buttonrupbasan']['daftarbarang'])))

@mark.fixture_index_penerimaan
def test_halaman_cetakBA():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['CetakBA']).click() 
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_index_penerimaan
def test_halaman_exportexel():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['exportexel']).click() 
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_index_penerimaan
def test_halaman_exportexelsemuahal():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['excelsemuhalaman']).click() 
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_index_penerimaan
def test_halaman_exportexelhalinisaj():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['excelHalamaninisaja']).click() 
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_index_penerimaan
def test_halaman_exportpdf():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['exportPDF']).click() 
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_index_penerimaan
def test_halaman_pdfsemuahal():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['pdfsemuaH']).click() 
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_index_penerimaan
def test_halaman_pdfhalinisaj():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['pdfhinisaj']).click() 
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_index_penerimaan
def test_halaman_print():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['cetak']).click() 
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_index_penerimaan
def test_halaman_printsemuahal():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['cetaksemua']).click() 
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_index_penerimaan
def test_halaman_printhalinisaj():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['cetakhalinisaj']).click() 
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_index_penerimaan
def test_pageindex20hal():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['buttonrupbasan']['daftarbarang'])))
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['pilihpage']).click() 
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['20halaman']).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['buttonrupbasan']['daftarbarang'])))
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_index_penerimaan
def test_pageindex50hal():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['buttonrupbasan']['daftarbarang'])))
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['pilihpage']).click() 
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['50halaman']).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['buttonrupbasan']['daftarbarang'])))
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_index_penerimaan
def test_pageindex100hal():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['buttonrupbasan']['daftarbarang'])))
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['pilihpage']).click() 
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['100halaman']).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['buttonrupbasan']['daftarbarang'])))
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_index_penerimaan
def test_pageindex5hal():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['buttonrupbasan']['daftarbarang'])))
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['pilihpage']).click() 
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['5halaman']).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['buttonrupbasan']['daftarbarang'])))
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_index_penerimaan
def test_pergikepage():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, pathData ['buttonrupbasan']['daftarbarang'])))
    driver.find_element(By.XPATH, pathData['Other Search']['Pergi Ke']).send_keys(Keys.BACK_SPACE)
    time.sleep(3)
    driver.find_element(By.XPATH, pathData['Other Search']['Pergi Ke']).send_keys('4')
    driver.find_element(By.XPATH, pathData['Other Search']['Pergi Ke']).send_keys(Keys.ENTER)

@mark.fixture_index_penerimaan
def test_Buka_halaman_Ubah():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['ubah']).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['Id Navigate Button']['Back Button'])))
    driver.find_element(By.XPATH, pathData ['Id Navigate Button']['Back Button']).click()
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_index_penerimaan
def test_Buka_halaman_tambah():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['tambah']).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['Id Navigate Button']['Back Button'])))
    driver.find_element(By.XPATH, pathData ['Id Navigate Button']['Back Button']).click()
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_index_penerimaan
def test_Buka_halaman_Daftarbarang():
    driver.find_element(By.XPATH, pathData['buttonrupbasan']['daftarbarang']).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['Id Navigate Button']['Back Button'])))
    driver.find_element(By.XPATH, pathData ['Id Navigate Button']['Back Button']).click()
    attach(data=driver.get_screenshot_as_png())
