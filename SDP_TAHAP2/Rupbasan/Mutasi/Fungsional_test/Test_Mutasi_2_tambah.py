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
fh = logging.FileHandler('Plusmutasi.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

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
    attach(data=driver.get_screenshot_as_png())
    Log.info('Menuju Menu Mutasi dengan mengarahkan kursor ke navigasi ''Rubasan'' kemudian sub menu ''Mutasi''')

@mark.fixture_Mutasi
def test_aksesmenu_tambah_4():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    driver.find_element(By.ID, 'createButton').click()

    attach(data=driver.get_screenshot_as_png())
    Log.info('Mengakses menu tambah')

@mark.fixture_Mutasi
def test_Pencariandataregistrasi_5():
    cari = driver.find_element(By.XPATH,  pathData['AksesMenu']['Rupbasan']['elemen']['+mutasi']['caridata'])
    cari.click()
    cari.send_keys('Nomor Registrasi Instansi')
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.ID, 'cariIdentitasPenerimaan')))
    driver.find_element(By. ID, 'cariIdentitasPenerimaan').click()
    driver.find_element(By. ID, 'findButton').click()

    attach(data=driver.get_screenshot_as_png())
    Log.info('Melakukan pencarian data berdassarkan registrasi penerimaan, kemudian menuju form tambah')

@mark.fixture_Mutasi
def test_texinput_6():
    NomorSuratMutasi = driver.find_element(By.XPATH,  pathData['AksesMenu']['Rupbasan']['elemen']['+mutasi']['NOSM'])
    NomorSuratMutasi.send_keys('NSMTestAuto@123')
    time.sleep(1)
    NomorSuratBA = driver.find_element(By.XPATH,  pathData['AksesMenu']['Rupbasan']['elemen']['+mutasi']['NOSBA'])
    NomorSuratBA.send_keys('NSBATestAuto@123')

@mark.fixture_Mutasi
def test_inputtexarea_7():
    Alamat = driver.find_element(By.XPATH,  pathData['AksesMenu']['Rupbasan']['elemen']['+mutasi']['Alamat'])
    Alamat.send_keys('AlamatestAuto@123AlamatestAuto@123AlamatestAuto@123AlamatestAuto@123AlamatestAuto@123AlamatestAuto@123AlamatestAuto@123AlamatestAuto@123AlamatestAuto@123AlamatestAuto@123AlamatestAuto@123AlamatestAuto@123AlamatestAuto@123AlamatestAuto@123AlamatestAuto@123')
    Keterangan = driver.find_element(By.XPATH,  pathData['AksesMenu']['Rupbasan']['elemen']['+mutasi']['Keterangan'])
    Keterangan.send_keys('KeteranganTestAuto@123KeteranganTestAuto@123KeteranganTestAuto@123KeteranganTestAuto@123KeteranganTestAuto@123KeteranganTestAuto@123KeteranganTestAuto@123KeteranganTestAuto@123KeteranganTestAuto@123KeteranganTestAuto@123KeteranganTestAuto@123KeteranganTes')

@mark.fixture_Mutasi
def test_inputtgl_8():
    tgl = driver.find_element(By.XPATH,  pathData['AksesMenu']['Rupbasan']['elemen']['+mutasi']['TGLSM'])
    tgl.click()
    tgl.send_keys('01/11/2022')
    tgl.send_keys(Keys.ENTER)
    
@mark.fixture_Mutasi
def test_Meresetform_8():
    reset = driver.find_element(By.ID, 'resetButton')
    reset.click()
    time.sleep(1)
    driver.find_element(By. XPATH, pathData['AksesMenu']['Rupbasan']['menu']['resetformYa']).click()
    Log.info('Mereset Form tambah Mutasi dengan Option Ya')

@mark.fixture_Mutasi
def test_input_kempali(): 
    time.sleep(1)   
    test_inputtexarea_7()
    test_texinput_6()
    test_inputtgl_8()

@mark.fixture_Mutasi
def test_dropdown_9():
    driver.find_element(By.XPATH, '//*[@id="dropdownJenisRegistrasiAkhir"]').click()
    driver.find_element(BY.XPATH, '//*[@id="dropdownJenisRegistrasiAkhir"]').click()
