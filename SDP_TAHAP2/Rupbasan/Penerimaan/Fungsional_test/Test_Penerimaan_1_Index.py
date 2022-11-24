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
from Settings.setup import createlog 
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
    global driver, pathData, Log
    driver = initDriver()
    pathData = loadDataPath()
    log = createlog
    Log('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')

@mark.fixture_penempatan
def test_loggin_2():
    login(driver)
    Log('Memasukan User name dan Password di halaman Login)')

@mark.fixture_penerimaan
def test_aksesmenuPenerimaan_3():
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.LINK_TEXT, 'Penerimaan').click()
    attach(data=driver.get_screenshot_as_png())
    Log('Menuju Menu Penerimaan dengan mengarahkan kursor ke navigasi ''Rubasan'' kemudian sub menu ''Penerimaan''')

@mark.fixture_penerimaan
def test_PencarianData_4():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['tombolcari'])))
    kategori = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['pilkategori'])
    kategori.click()
    kategori.send_keys('No Registrasi')
    kategori.send_keys(Keys.DOWN)
    kategori.send_keys(Keys.ENTER)

    katkun = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['katkun'])
    katkun.click()
    katkun.send_keys('NRP1001')
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['tombolcari']).click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['tombolcari'])))
    attach(data=driver.get_screenshot_as_png())
    Log('Melakukan Pencarian data berdasarkan kategori')

@mark.fixture_penerimaan
def test_menghapusfieldpencarian_5():
    filter = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['pilkategori'])
    ActionChains(driver).move_to_element(filter).perform()

    elemnthps = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['hpskolom'])
    ActionChains(driver).move_to_element(elemnthps).perform()
    elemnthps.click()

    attach(data=driver.get_screenshot_as_png())
    Log('Melakukan Pencarian data berdasarkan kategori')

@mark.fixture_penerimaan
def test_caridatadenganjenisregistrasi_6():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['tombolcari'])))
    Jreg = driver.find_element(By. ID, 'input_jenis_registrasi_baran_basan')
    Jreg.click()
    time.sleep(2)
    Jreg.send_keys('Tingkat Penyidikan')
    Jreg.send_keys(Keys.DOWN)
    Jreg.send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['tombolcari']).click()
    
    field = driver.find_element(By. ID, 'input_jenis_registrasi_baran_basan')
    ActionChains(driver).move_to_element(field).perform()
    elem = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['clearJREG'])
    ActionChains(driver).move_to_element(elem).perform()
    elem.click()

    attach(data=driver.get_screenshot_as_png())
    Log('Melakukan Pencarian data berdasarkan kategori')

@mark.fixture_penerimaan
def test_SortirDataTabel_7():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['tombolcari'])))
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['ascending']).click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['tombolcari'])))
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['descending']).click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['tombolcari'])))

    attach(data=driver.get_screenshot_as_png())
    Log('Melakukan Pencarian data berdasarkan kategori')

@mark.fixture_penerimaan
def test_membukahalamanedit_8():
    test_PencarianData_4() #Yang digunakan NOREG NRP1001
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['tombolcari'])))
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['hlmnedit']).click()
    
    attach(data=driver.get_screenshot_as_png())
    Log('Akses menu halaman edit Penerimaan')

@mark.fixture_penerimaan
def test_kembalikehalamansebelumnya_9():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'backButton')))
    driver.find_element(By.ID, 'backButton').click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['tombolcari'])))

@mark.fixture_penerimaan
def test_membukahalamanDetail_10():
    test_PencarianData_4() #Yang digunakan NOREG NRP1001
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['tombolcari'])))
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['hlmndetail']).click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'backButton')))

    test_kembalikehalamansebelumnya_9()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['tombolcari'])))

    attach(data=driver.get_screenshot_as_png())
    Log('Akses menu halama detail Penerimaan')

@mark.fixture_penerimaan
def test_CetakBA_11():
    test_PencarianData_4()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['tombolcari'])))
    cetak = driver.find_element(By. XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['CetakBA'])
    cetak.click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['CetakBA'])))
    attach(data=driver.get_screenshot_as_png())
    Log('Akses menu halama Tambah Penerimaan')

@mark.fixture_penerimaan
def test_pilihpagehalaman_12(): #kasus 5 data tabel per halaman
    test_menghapusfieldpencarian_5()
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['tombolcari']).click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['tombolcari'])))
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['pilhalaman']).click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//div[15]/div/div/div[1]/ul/li[1]').click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['tombolcari'])))
    attach(data=driver.get_screenshot_as_png())
    Log('Menampilkan jumlah data yang sesuai dengan total halaman yang dipilih')

@mark.fixture_penerimaan
def test_pergikepagehalaman_13():
    pergi = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['peegikepage'])
    pergi.clear()
    pergi.send_keys('8')
    pergi.send_keys(Keys.ENTER)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['tombolcari'])))
    
    attach(data=driver.get_screenshot_as_png())
    Log('Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir')

@mark.fixture_penerimaan
def test_exportPDF_14():
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['exportPDF']).click()
    driver.find_element(By.ID, 'wholeButton').click()
    driver.find_element(By.ID, 'thisButton').click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['exportPDF'])))
    attach(data=driver.get_screenshot_as_png())
    Log('Export data tabel dengan format PDF')

@mark.fixture_penerimaan
def test_exportexcel_15():
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['exportexcel']).click()
    driver.find_element(By.ID, 'wholeButton').click()
    driver.find_element(By.ID, 'thisButton').click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['exportexcel'])))
    attach(data=driver.get_screenshot_as_png())
    Log('Export data Tabel dengan format Excel')

@mark.fixture_penerimaan
def test_printhalamn_16():
    driver.find_element(By.ID,'printButton').click()
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['cetaksemua']).click()
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['idxpenerimaan']['cetakinisaja']).click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'printButton')))
    attach(data=driver.get_screenshot_as_png())
    Log('Print Data Tabel')

@mark.fixture_penerimaan
def test_membukahalamanTambah():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'printButton')))
    driver.find_element(By. ID, 'createButton').click
    attach(data=driver.get_screenshot_as_png())
    Log('Akses menu halama Tambah Penerimaan')