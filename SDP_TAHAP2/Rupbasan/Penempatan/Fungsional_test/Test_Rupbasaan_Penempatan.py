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

from Settings.setup import initDriver, loadDataPath, quit, hold
from Settings.login import login, oprupbasanbdg

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Test_Rupbasaan_Penempatan.log', mode="w")
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
	Log.info('Memasukan User name dan Password di halaman Login')

@mark.fixture_penempatan
def test_PTN_001():
	hold(driver)
	Log.info('Mengakses menu  Penempatan dengan memilih modul Rupbasan kemudian pilih menu Penempatan')
	nav = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['Rupbasan'])
	ActionChains(driver).move_to_element(nav).perform()
	time.sleep(1)
	driver.find_element(By.LINK_TEXT, 'Penempatan').click()
	driver.find_element(By. ID, 'kataKunci').click()

	attach(data=driver.get_screenshot_as_png()) 

filtertable			= wb['Barangbasan']
j = 10
namabarang			= filtertable['A'+str(j)].value

@mark.fixture_penerimaan
def test_PTN_002():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	Log.info('Melakukan pengecekan filtering data berdasarkan kategori')
	hold(driver)
	driver.find_element(By.ID, 'filterColumn').click()
	time.sleep(1)
	driver.find_element(By. ID, 'nama_barang').click()
	driver.find_element(By. ID, 'kataKunci').send_keys(namabarang)
	print('CARI')
	driver.find_element(By.ID, 'searchButton').click()
	print('Menunggu Loading')
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penempatan
def test_PTN_003_0():
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By. ID, 'searchButton')))
	hold(driver)
	Log.info('membuka halaman tambah dengan menekan button tambah')
	driver.find_element(By. ID, 'createButton').click()
	attach(data=driver.get_screenshot_as_png())

PTN = wb['Penempatan']
u = 4

caribarang   	= PTN['A'+str(u)].value #Cari Barang

tglpenempatan 	= PTN['B'+str(u)].value #Tanggal Penempatan
pilihtersangka  = PTN['C'+str(u)].value #Pilih Tersangka
gudang 			= PTN['D'+str(u)].value #Gudang
sektorgudang 	= PTN['E'+str(u)].value #Sektor Gudang
barisraklemari  = PTN['F'+str(u)].value #Baris/Rak/Lemari
nourut 			= PTN['G'+str(u)].value #No Urut
keterangan  	= PTN['H'+str(u)].value #Keterangan

@mark.fixture_penempatan
def test_PTN_003_1():
	Log.info('Mencari nama Barang')
	nabar = driver.find_element(By.ID, 'identity_keyword')
	nabar.click()
	nabar.send_keys(caribarang)
	print('Menunggu loading "Memuat"')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'identity_keyword-0')))
	# hold(driver)
	driver.find_element(By.CSS_SELECTOR, "#identity_keyword-0").click()
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penempatan
def test_PTN_003_2():
	Log.info('memilih tanggal dengan format DD/MM/YYYY ')
	tglPtn = driver.find_element(By.ID, 'tgl_penempatan')
	tglPtn.click()
	tglPtn.send_keys(tglpenempatan)
	tglPtn.send_keys(Keys.ENTER)

	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penempatan
def test_PTN_003_3():
	Log.info('pencarian tersangka barang')
	Ters = driver.find_element(By. ID, 'dropdownPilihTersangka')
	Ters.click()
	Ters.send_keys(pilihtersangka)
	print('Menunggu loading "Memuat"')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'tersangkaOption-0')))
	# hold(driver)
	driver.find_element(By.ID, "tersangkaOption-0").click()
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penempatan
def test_PTN_003_4():
	Log.info('Memilih Gudang untuk barang')
	pilgud = driver.find_element(By. ID, 'dropdownPilihGudang')
	pilgud.click()
	pilgud.send_keys(gudang)
	print('Menunggu loading "Memuat"')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'gudangOption-0')))
	# hold(driver)
	driver.find_element(By.ID, "gudangOption-0").click()
	print('Menunggu loading Detail Gudang')
	WebDriverWait(driver, 80).until(EC.presence_of_element_located((By.XPATH, pathData['Rupelemen']['+penempatan']['descgudang'])))

	attach(data=driver.get_screenshot_as_png())
		
@mark.fixture_penempatan
def test_PTN_003_5():
	Log.info('memilih sektor gudang')
	pilsek = driver.find_element(By. ID, 'dropdownSektorGudang')
	pilsek.click()
	pilsek.send_keys(sektorgudang)
	print('Menunggu loading "Memuat"')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'sektorGudangOption-0')))
	# hold(driver)
	driver.find_element(By.ID, "sektorGudangOption-0").click()

	attach(data=driver.get_screenshot_as_png())
	
@mark.fixture_penempatan
def test_PTN_003_6():
	Log.info('Memilih Baris dalam gudang')
	pillbar = driver.find_element(By.ID, 'dropdownBaris')
	pillbar.click()
	pillbar.send_keys(barisraklemari)
	print('Menunggu loading "Memuat"')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'baris-0')))
	# hold(driver)
	driver.find_element(By.CSS_SELECTOR, "#baris-0").click()

	attach(data=driver.get_screenshot_as_png())
	
@mark.fixture_penempatan
def test_PTN_003_7():
	Log.info('Memilih memilih nomer urut')
	pilnorut = driver.find_element(By. ID, 'dropdownNoUrut')
	pilnorut.click()
	pilnorut.send_keys(nourut)
	print('Menunggu loading "Memuat"')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'noUrut-0')))
	# hold(driver)
	driver.find_element(By.CSS_SELECTOR, "#noUrut-0").click()

	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penempatan
def test_PTN_003_8():
	Log.info('memasukan Ketrangan Penempatan')
	driver.find_element(By. ID, 'keterangan').send_keys(keterangan)
	attach(data=driver.get_screenshot_as_png())

# @mark.fixture_penerimaan
# def test_PTN_003_9():
# 	hold(driver)
# 	Log.info('menekan button submit data penempatan')
# 	driver.find_element(By.ID, "submitButton").click()
# 	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID , 'searchButton')))