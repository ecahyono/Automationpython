from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pytest_html_reporter import attach
import os, platform, time, pytest
from selenium import webdriver
from os import environ, path
from pathlib import Path
from pytest import mark
import platform
import logging
import sys

from dotenv import load_dotenv
load_dotenv()

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR")) 
elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))

from Settings.setup import initDriver, loadDataPath
from Settings.login import login

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('result.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

# init driver by os
@mark.fixture_penempatan
def test_Ossetup_1():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')

@mark.fixture_penempatan
def test_loggin_2():
    login(driver)
    Log.info('Memasukan User name dan Password di halaman Login)')

@mark.fixture_penerimaan
def test_akses_menu_3():
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.LINK_TEXT, 'Penerimaan').click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Menuju Menu penempatan dengan mengarahkan kursor ke navigasi ''Rubasan'' kemudian sub menu ''pemermpatan''')

#inputtext-Dropdown+Celarvalue button
@mark.fixture_penerimaan
def test_fieldinput_Dropdown_ClearVB():
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, pathData['Other Search']['Search Button'])))
    field = driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['filterabledropdownindex'])
    field.click()
    field.send_keys('No Registrasi')
    field.send_keys(Keys.DOWN)
    field.send_keys(Keys.ENTER)

    elemnt = driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['clearkategori'])
    ActionChains(driver).move_to_element(elemnt).perform()
    WebDriverWait(driver, 25)
    elemnt.click()

    katkun = driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['maskakunci'])
    katkun.click()
    katkun.send_keys('Kata kunci @ 123')

    elemnt = driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['clearkatkun'])
    ActionChains(driver).move_to_element(elemnt).perform()
    WebDriverWait(driver, 25)
    elemnt.click()

    Registrasi = driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['dropdownJregIndex'])
    Registrasi.click()
    time.sleep(2)
    Registrasi.send_keys('Register Barang Rampasan Negara')
    Registrasi.send_keys(Keys.DOWN)
    Registrasi.send_keys(Keys.ENTER)

    elemnt = driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['clearvaluejnreg'])
    ActionChains(driver).move_to_element(elemnt).perform()
    WebDriverWait(driver, 25)
    elemnt.click()

    Instansi = driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['instansiindex'])
    Instansi.click()
    time.sleep(2)
    Instansi.send_keys('POLDA JABAR')
    Instansi.send_keys(Keys.DOWN)
    Instansi.send_keys(Keys.ENTER)

    elemnt = driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['clearvalueinstnsi'])
    ActionChains(driver).move_to_element(elemnt).perform()
    WebDriverWait(driver, 25)
    elemnt.click()

    attach(data=driver.get_screenshot_as_png())

@mark.fixture_penerimaan
def test_sortir_tabel():
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupbasan']['indexrupbasan']['ascendingtable'])))
    driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['ascendingtable']).click()
    # driver.find_element(By.XPATH, pathData ['Rupbasan']['indexrupbasan']['descedingtable']).click()
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupbasan']['indexrupbasan']['ascendingtable'])))
    attach(data=driver.get_screenshot_as_png())
    time.sleep(2)
# EXPORT && PRINT
@mark.fixture_penerimaan
def test_ExportDanCetak():
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, pathData['Other Search']['Search Button'])))
    driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['exportPDF']).click()    
    driver.find_element(By.ID, 'wholeButton').click() 
    driver.find_element(By.ID, 'thisButton').click()    
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupbasan']['indexrupbasan']['exportPDF'])))

    driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['exportexel']).click() 
    driver.find_element(By.ID, 'wholeButton').click() 
    driver.find_element(By.ID, 'thisButton').click() 
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupbasan']['indexrupbasan']['exportexel'])))

    driver.find_element(By.ID, 'printButton').click() 
    driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['cetaksemua']).click() 
    driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['cetakhalinisaj']).click() 
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.ID, 'printButton')))
    attach(data=driver.get_screenshot_as_png())
    time.sleep(2)
@mark.fixture_penerimaan
def test_halamanpage():
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupbasan']['indexrupbasan']['ascendingtable'])))
    driver.find_element(By.XPATH, pathData['Other Search']['Dropdown Halaman']).click() 
    driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['5halaman']).click()
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupbasan']['indexrupbasan']['ascendingtable'])))
    page = driver.find_element(By.XPATH, pathData['Other Search']['Pergi Ke'])
    page.send_keys(Keys.BACK_SPACE)
    page.send_keys('15')
    page.send_keys(Keys.ENTER)
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, pathData['Other Search']['Search Button'])))
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_penerimaan
def test_cari_Datatable():
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupbasan']['indexrupbasan']['ascendingtable'])))
    field = driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['filterabledropdownindex'])
    field.click()
    field.send_keys('No Registrasi')
    field.send_keys(Keys.DOWN)
    field.send_keys(Keys.ENTER)

    katkun = driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['maskakunci'])
    katkun.click()
    katkun.send_keys('NRP/1002')

    driver.find_element(By.XPATH, pathData['Other Search']['Search Button']).click()
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, pathData['Other Search']['Search Button'])))
    time.sleep(2)
@mark.fixture_penerimaan
def test_cetakBA():
    driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['CetakBA']).click() 
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupbasan']['indexrupbasan']['CetakBA'])))
    attach(data=driver.get_screenshot_as_png())
    time.sleep(2)
@mark.fixture_penerimaan
def test_Buka_halaman_Ubah():
    driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['ubah']).click()
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.ID, 'backButton')))
    driver.find_element(By.ID, 'backButton').click()
    attach(data=driver.get_screenshot_as_png())
    time.sleep(2)
@mark.fixture_penerimaan
def test_Buka_halaman_Daftarbarang():
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupbasan']['indexrupbasan']['ascendingtable'])))
    field = driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['filterabledropdownindex'])
    field.click()
    field.send_keys('No Registrasi')
    field.send_keys(Keys.DOWN)
    field.send_keys(Keys.ENTER)

    katkun = driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['maskakunci'])
    katkun.click()
    katkun.send_keys('NRP/1002')

    driver.find_element(By.XPATH, pathData['Other Search']['Search Button']).click()
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, pathData['Other Search']['Search Button'])))

    time.sleep(2)

    driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['daftarbarang']).click()
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupbasan']['ubahpenerimaan']['tab'])))
    driver.find_element(By.ID, 'backButton').click()
    attach(data=driver.get_screenshot_as_png())
    time.sleep(2)

@mark.fixture_penerimaan
def test_Buka_halaman_tambah():
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, pathData['Other Search']['Search Button'])))
    driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['tambah']).click()
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.ID, 'backButton')))
    driver.find_element(By.ID, 'backButton').click()
    attach(data=driver.get_screenshot_as_png())
    time.sleep(2)   
