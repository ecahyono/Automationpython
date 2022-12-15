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
from openpyxl import load_workbook

from dotenv import load_dotenv
load_dotenv()

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR")) 
elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))

from Settings.setup import initDriver, loadDataPath, quit, sleep
from Settings.login import login, oprupbasanbdg

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('TF2_Penempatan_tambah.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("RUPEXEL"))
sheetrange1 = wb['Penempatan']
j = 2

caribarang   	= sheetrange1['A'+str(j)].value #Cari Barang
tglpenempatan 	= sheetrange1['B'+str(j)].value #Tanggal Penempatan
pilihtersangka  = sheetrange1['C'+str(j)].value #Pilih Tersangka
gudang 			= sheetrange1['D'+str(j)].value #Gudang
sektorgudang 	= sheetrange1['E'+str(j)].value #Sektor Gudang
barisraklemari  = sheetrange1['F'+str(j)].value #Baris/Rak/Lemari
nourut 			= sheetrange1['G'+str(j)].value #No Urut
keterangan  	= sheetrange1['H'+str(j)].value #Keterangan

@mark.fixture_penempatan
def test_Ossetup_1():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')

@mark.fixture_penempatan
def test_loggin_2():
    # login(driver)
    oprupbasanbdg(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Memasukan User name dan Password di halaman Login)')

@mark.fixture_penempatan
def test_akses_menu_penempatan_3():
    nav = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['Rupbasan'])
    ActionChains(driver).move_to_element(nav).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Penempatan').click()
    driver.find_element(By. ID, 'kataKunci').click()
    attach(data=driver.get_screenshot_as_png()) 
    Log.info('mengakses menu penempatan')

@mark.fixture_penempatan
def test_aksesmenu_tambah_4():
    WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By. ID, 'searchButton')))
    driver.find_element(By. ID, 'createButton').click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('membuka halaman tambah dengan menekan button tambah')

@mark.fixture_penempatan
def test_tambah_1():
	# sleep(driver)
	barang = driver.find_element(By.ID, 'identity_keyword')
	barang.click()
	barang.send_keys(caribarang)
	WebDriverWait(driver, 80).until(EC.presence_of_element_located((By.ID, 'identity_keyword-0')))
	driver.find_element(By.ID, 'identity_keyword-0').click()

	attach(data=driver.get_screenshot_as_png())
	Log.info('Memilih value, kemudian mengosongkan pilihan dengan clear button value, lalu ditampilkan validation message jika mandatory')

@mark.fixture_penempatan
def test_tambah_2():
	# sleep(driver)
	tgl = driver.find_element(By.ID, 'tgl_penempatan')
	tgl.click()
	tgl.send_keys(tglpenempatan)
	tgl.send_keys(Keys.ENTER)

	attach(data=driver.get_screenshot_as_png())
	Log.info('memilih tanggal dengan format DD/MM/YYYY ')

@mark.fixture_penempatan
def test_tambah_3():
    # sleep(driver)
    Tersangka = driver.find_element(By. ID, 'dropdownPilihTersangka')
    Tersangka.click()
    Tersangka.send_keys(pilihtersangka)
    WebDriverWait(driver, 80).until(EC.presence_of_element_located((By.ID, 'tersangkaOption-0')))
    driver.find_element(By.ID,'tersangkaOption-0').click()

@mark.fixture_penempatan
def test_tambah_4():
    # sleep(driver)
    gud = driver.find_element(By. ID, 'dropdownPilihGudang')
    gud.click()
    gud.send_keys(gudang)
    WebDriverWait(driver, 80).until(EC.presence_of_element_located((By.ID, 'gudangOption-0')))
    driver.find_element(By. ID, 'gudangOption-0').click()
    WebDriverWait(driver, 80).until(EC.presence_of_element_located((By.XPATH, pathData['Rupelemen']['+penempatan']['descgudang'])))

    attach(data=driver.get_screenshot_as_png())
    Log.info('Memilih value, kemudian mengosongkan pilihan dengan clear button value, lalu ditampilkan validation message jika mandatory')
		
@mark.fixture_penempatan
def test_tambah_5():
    # sleep(driver)
    sekgud = driver.find_element(By. ID, 'dropdownSektorGudang')
    sekgud.click()
    sekgud.send_keys(sektorgudang)
    WebDriverWait(driver, 80).until(EC.presence_of_element_located((By.ID, 'sektorGudangOption-0')))
    driver.find_element(By. ID, 'sektorGudangOption-0').click()

    attach(data=driver.get_screenshot_as_png())
    Log.info('memilih sektor gudang')
		
@mark.fixture_penempatan
def test_tambah_6():
    # sleep(driver)
    barisrk = driver.find_element(By.ID, 'dropdownBaris')
    barisrk.click()
    # send_keys(barisraklemari)
    WebDriverWait(driver, 80).until(EC.presence_of_element_located((By.ID, 'baris-0')))
    driver.find_element(By.ID,'baris-0').click()

    attach(data=driver.get_screenshot_as_png())
    Log.info('Memilih value, kemudian mengosongkan pilihan dengan clear button value, lalu ditampilkan validation message jika mandatory')
	
@mark.fixture_penempatan
def test_tambah_7():
    # sleep(driver)
    norutgud = driver.find_element(By. ID, 'dropdownNoUrut').click()
    # norutgud.send_keys(nourut)
    WebDriverWait(driver, 80).until(EC.presence_of_element_located((By.ID, 'noUrut-0')))
    driver.find_element(By. ID, 'noUrut-0').click()

    attach(data=driver.get_screenshot_as_png())
    Log.info('Memilih value, kemudian mengosongkan pilihan dengan clear button value, lalu ditampilkan validation message jika mandatory')

@mark.fixture_penempatan
def test_inputtextarea_1():
    # sleep(driver)
    driver.find_element(By. ID, 'keterangan').send_keys(keterangan)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Input field menggunakan varchar, value indicatornya sesuai ')

@mark.fixture_penerimaan
def test_SubmitDatapenempatan():
    sleep(driver)    
    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
    Log.info('menekan button submit')

@mark.fixture_penerimaan
def keluar():
    sleep(driver)
    quit(driver)
    Log.info('menyelesaikan test dan menutup browser')