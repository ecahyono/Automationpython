from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
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
from openpyxl import load_workbook

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
fh = logging.FileHandler('Mutasi_4_Detail.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("RUPEXEL"))
sheetrange1 = wb['IndexMutasi']
j = 2
pilihkategori    = sheetrange1['A'+str(j)].value
Katkun			 = sheetrange1['B'+str(j)].value
# init driver by os
@mark.fixture_Mutasi
def test_Ossetup_1():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')

@mark.fixture_Mutasi
def test_loggin_2():
    login(driver)
    Log.info('Memasukan User name dan Password di halaman Login)')

@mark.fixture_Mutasi
def test_aksesmenuPenerimaan_3():
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.LINK_TEXT, 'Mutasi').click()
    driver.find_element(By.XPATH, pathData['Rupelemen']['indexpenempatan']['klik']).click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Menuju Menu Mutasi dengan mengarahkan kursor ke navigasi ''Rubasan'' kemudian sub menu ''Mutasi''')

@mark.fixture_Mutasi
def test_pencariandatatabel_4():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    driver.find_element(By.ID, 'filterColumn').click()
    time.sleep(2)
    if pilihkategori == 'No Registrasi Rupbasan':
        driver.find_element(By.ID, 'noRegistrasiRupbasan').click()
    elif pilihkategori == 'Nama Identitas':
        driver.find_element(By.ID, 'namaIdentitas').click()
    elif pilihkategori == 'No Surat Mutasi':
        driver.find_element(By.ID, 'noSuratMutasi').click()
    elif pilihkategori == 'Jenis Registrasi Awal':
        driver.find_element(By.ID, 'noSuratMutasi').click()
    elif pilihkategori == 'Jenis Registrasi Akhir':
        driver.find_element(By.ID, 'noSuratMutasi').click()
    elif pilihkategori == 'Tgl Surat':
        driver.find_element(By.ID, 'tglSurat').click()
        # driver.implicitly_wait(10)
        driver.find_element(By.ID, 'tglSurat').send_keys(Katkun)
        
    if (pilihkategori == 'No Registrasi Rupbasan'or pilihkategori == 'Nama Identitas' or pilihkategori == 'No Surat Mutasi' or pilihkategori == 'Jenis Registrasi Awal' or pilihkategori == 'Jenis Registrasi Akhir'):
        driver.find_element(By.ID, 'kataKunci').send_keys(Katkun)
    else:
        pass

    driver.find_element(By.ID, 'buttonSearch').click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))    
    attach(data=driver.get_screenshot_as_png())
    Log.info('Melakukan pencarian data berdasarkan kategori')

@mark.fixture_Mutasi
def test_aksesmenu_detail_11():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    driver.find_element(By.XPATH, pathData['Rupelemen']['indexmutasi']['detailmutasi']).click()

    attach(data=driver.get_screenshot_as_png())
    Log.info('Membuka halaman Detail')