from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import os, platform, time, pytest
from os import environ, path
from pathlib import Path
import sys
import platform
from pytest import mark
from pytest_html_reporter import attach

from dotenv import load_dotenv
load_dotenv()

import unittest
if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR")) 
elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))

from Settings.setup import initDriver, loadDataPath
from Settings.login import login

@mark.fixture_penempatan
def test_Ossetup():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    print('Konfigurasi chrome driver untuk sistem operasi windows dan mac')

@mark.fixture_penempatan
def test_loggin():
    login(driver)

@mark.fixture_penempatan
def test_akses_menu_penempatan():
    nav = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['MainText'])
    ActionChains(driver).move_to_element(nav).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Penempatan').click()

    attach(data=driver.get_screenshot_as_png())

@mark.fixture_penempatan
def test_sortirdatatabel():
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    ascending = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['index']['ascenJRB'])
    ascending.click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    descending = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['index']['descenpatanbar'])
    descending.click()

    attach(data=driver.get_screenshot_as_png())

@mark.fixture_penempatan
def test_pencariandatatabel():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

    pilkat = driver.find_element(By. ID, "filterColumn")
    pilkat.click()
    pilkat.send_keys('Barang')
    pilkat.send_keys(Keys.DOWN)
    pilkat.send_keys(Keys.ENTER)

    driver.find_element(By. ID, 'kataKunci').send_keys('motor')

    driver.find_element(By. ID, 'searchButton').click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_penempatan
def test_hapuspencariandatatabel():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    filter = driver.find_element(By. ID, "filterColumn")
    ActionChains(driver).move_to_element(filter).perform()

    elemnthps = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['index']['clearkategori'])
    ActionChains(driver).move_to_element(elemnthps).perform()
    elemnthps.click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

    attach(data=driver.get_screenshot_as_png())

@mark.fixture_penempatan
def test_pilihhalaman():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    Halaman = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['index']['pilihhalmn'])
    Halaman.click()
    halaman5 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['index']['5halaman'])
    halaman5.click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    Halaman = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['index']['pilihhalmn'])
    Halaman.click()
    halaman3 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['index']['3halaman'])
    halaman3.click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

    attach(data=driver.get_screenshot_as_png())

@mark.fixture_penempatan
def test_pilihpagetabel():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    pergipage = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['index']['pergipage'])
    pergipage.clear()
    pergipage.send_keys('5')
    pergipage.send_keys(Keys.ENTER)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

    attach(data=driver.get_screenshot_as_png())
    
@mark.fixture_penempatan
def test_aksesmenu_detail():
    test_pencariandatatabel()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['index']['aksesdetail']).click()
    time.sleep(2)
    driver.find_element(By.ID, 'backButton').click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

    attach(data=driver.get_screenshot_as_png())

@mark.fixture_penempatan
def test_aksesmenu_ubah():
    test_pencariandatatabel()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['index']['aksesubah']).click()
    time.sleep(2)
    driver.find_element(By.ID, 'backButton').click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

@mark.fixture_penempatan
def test_cetakBarcode():
    test_pencariandatatabel()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    time.sleep(2)
    driver.find_element(By. ID, 'cetakBarcode').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'cetakBarcode')))
    time.sleep(2)

@mark.fixture_penempatan
def test_aksesmenu_tambah():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.ID, 'createButton').click()
    time.sleep(2)
    driver.find_element(By.ID, 'backButton').click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    time.sleep(5)

@mark.fixture_penempatan
def test_exportexcel():
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.ID, 'excelButton').click()
    driver.find_element(By.ID, 'wholeButton').click()
    time.sleep(2)
    driver.find_element(By.ID, 'thisButton').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'excelButton')))
    time.sleep(5)


#fixing besok
@mark.fixture_penempatan
def test_exportPDF():
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.ID, 'pdfButton').click()
    driver.find_element(By.ID, 'wholeButton').click()
    time.sleep(2)
    driver.find_element(By.ID, 'thisButton').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'pdfButton')))
    time.sleep(5)

@mark.fixture_penempatan
def test_printdatatable():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.ID, 'printButton').click()
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['index']['printsemua']).click()
    time.sleep(2)
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['index']['printinisaja']).click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'printButton')))
    time.sleep(5)
