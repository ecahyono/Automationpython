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
import pyautogui
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

from Settings.setup import initDriver, loadDataPath, sleep, quit, hold
from Settings.login import login, oprupbasanbdg


Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Rupbasan_Penerimaan.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("RUPEXEL"))

# init driver by os
@mark.fixture_rupbasan
def test_00_setup():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()

@mark.fixture_rupbasan
def test_00_loggin():
	Log.info('Memasukan User name dan Password di halaman Login')
	oprupbasanbdg(driver)

@mark.fixture_rupbasan
def test_GDG_001():
	Log.info('Mengakses menu Gudang dengan memilih modul Lain - Lain kemudian pilih menu Parameter lalu pilih submenu Gudang')
	hold(driver)
	element = driver.find_element(By.XPATH, '//*[@id="app"]/div/nav/ul/li[2]/div')
	actions = ActionChains(driver)
	time.sleep(2)
	actions.move_to_element(element).perform()

	element2 = driver.find_element(By.XPATH, '//div[3]/div/ul/li[1]/div[1]')
	actions2 = ActionChains(driver)
	time.sleep(2)
	actions2.move_to_element(element2).perform()
	driver.find_element(By.LINK_TEXT, "Gudang").click()

gudang = wb['Gudang']
o = 6
namgud			= gudang['A'+str(o)].value
JGudang 		= gudang['B'+str(o)].value
Alm 			= gudang['C'+str(o)].value
Prov			= gudang['D'+str(o)].value
Kotkab		  	= gudang['E'+str(o)].value
luas 			= gudang['F'+str(o)].value
quant 			= gudang['G'+str(o)].value
ket 			= gudang['H'+str(o)].value
Nama			= gudang['I'+str(o)].value
jmlh			= gudang['J'+str(o)].value
rangan		  	= gudang['K'+str(o)].value

@mark.fixture_rupbasan
def test_GDG_002():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	hold(driver)
	Log.info('Melakukan pengecekan filtering data berdasarkan kategori')
	driver.find_element(By.ID, 'formfilterColumn').click()
	time.sleep(1)
	driver.find_element(By. XPATH, '//div[4]/div/div/div[1]/ul/li[1]').click()
	driver.find_element(By. ID, 'kataKunci').send_keys(JGudang)
	driver.find_element(By.ID, 'searchButton').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_rupbasan
def test_GDG_003():
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	hold(driver)
	Log.info('Menambahkan data gudang dengan menggunakan button tambah lalu menginputkan data gudang pada form')
	driver.find_element(By.ID, 'createButton').click()
	attach(data=driver.get_screenshot_as_png())

	driver.find_element(By.ID, 'namaGudang').send_keys(namgud)

	gd = driver.find_element(By.ID, 'jenisGudang')
	gd.click()
	if JGudang == 'Gudang Umum Terbuka':
		driver.find_element(By.ID,'JG01').click()
	elif JGudang == 'Gudang Umum Tertutup':
		driver.find_element(By.ID,'JG02').click()
	elif JGudang == 'Gudang Berharga':
		driver.find_element(By.ID,'JG03').click()
	elif JGudang == 'Gudang Berbahaya':
		driver.find_element(By.ID,'JG04').click()
	elif JGudang == 'Gudang Hewan dan Tumbuhan':
		driver.find_element(By.ID,'JG05').click()

	driver.find_element(By.ID, 'alamat').send_keys(Alm)

	vinsi = driver.find_element(By.ID,'provinsi')
	vinsi.send_keys(Prov)
	if Prov == 'Jawa Barat':
		driver.find_element(By.ID,'12').click()
	elif Prov == 'DKI Jakarta':
		driver.find_element(By.ID,'11').click()

	paten = driver.find_element(By.ID,'kotaKabupaten')
	paten.send_keys(Kotkab)
	if Kotkab == 'Bandung':
		driver.find_element(By.ID,'122').click()
	elif Kotkab == 'Jakarta Pusat':
		driver.find_element(By.ID,'116').click()
			
	driver.find_element(By.ID, 'luas').send_keys(luas)
	driver.find_element(By.ID, 'kapasitasGudang').send_keys(quant)

	foto = driver.find_element(By.ID, 'pilihFoto').click()
	time.sleep(3)
	pyautogui.typewrite(environ.get(r"GUDANG"))
	pyautogui.press('enter')

	driver.find_element(By.ID, 'keterangan').send_keys(ket)

	driver.find_element(By.ID, 'nama0').send_keys(Nama)
	driver.find_element(By.ID, 'jumlah0').send_keys(jmlh)
	driver.find_element(By.ID, 'keterangan0').send_keys(rangan)

	Log.info('kemudian submit data')
	hold(driver)		
	driver.find_element(By.ID, 'submitButton').click()
	

ubhgudang = wb['Gudang']
a = 5
ubhnamgud		= ubhgudang['A'+str(a)].value
ubhAlm 			= ubhgudang['C'+str(a)].value
ubhProv			= ubhgudang['D'+str(a)].value
ubhKotkab		= ubhgudang['E'+str(a)].value
ubhluas 		= ubhgudang['F'+str(a)].value
ubhquant 		= ubhgudang['G'+str(a)].value
ubhket 			= ubhgudang['H'+str(a)].value

@mark.fixture_rupbasan
def test_GDG_004():
	WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	Log.info('Mengubah data gudang dengan menggunakan button (Ubah) pada kolom aksi di tabel kemudian ubah data di form')
	hold(driver)

	# driver.find_element(By.CSS_SELECTOR, ".h-5").click()
	driver.find_element(By.ID, 'updateButton-125').click()

	hold(driver)
	driver.find_element(By.ID, 'namaGudang').send_keys(ubhnamgud)
	driver.find_element(By.ID, 'alamat').send_keys(ubhAlm)

	vinsi = driver.find_element(By.ID,'provinsi')
	vinsi.send_keys(ubhProv)
	if Prov == 'Jawa Barat':
		driver.find_element(By.ID,'12').click()
	elif Prov == 'DKI Jakarta':
		driver.find_element(By.ID,'11').click()

	paten = driver.find_element(By.ID,'kotaKabupaten')
	paten.send_keys(ubhKotkab)
	if Kotkab == 'Bandung':
		driver.find_element(By.ID,'122').click()
	elif Kotkab == 'Jakarta Pusat':
		driver.find_element(By.ID,'116').click()
			
	driver.find_element(By.ID, 'luas').send_keys(ubhluas)
	driver.find_element(By.ID, 'kapasitasGudang').send_keys(ubhquant)
	driver.find_element(By.ID, 'keterangan').send_keys('Update' + ubhket)

	Log.Info('kemudian klik button ubah')
	hold(driver)		
	driver.find_element(By.ID, 'submitButton').click()

@mark.fixture_rupbasan
def test_GDG_005():
	WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	Log.info('Menampilkan detail gudang dengan menggunakan button (Detail) pada kolom aksi di tabel')
	hold(driver)
	driver.find_element(By.CSS_SELECTOR, ".h-5").click()
	hold(driver)
	driver.find_element(By.ID, "backButton").click()

@mark.fixture_rupbasan
def test_GDG_006():
	WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	Log.info('Menampilkan dropdown jumlah data yang dipilih oleh pengguna dan ditampilkan pada main grid')
	hold(driver)
	time.sleep(1)
	driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
	driver.find_element(By.XPATH, '//div[5]/div/div/div[1]/ul/li[1]').click()  # 5 Halaman
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_rupbasan
def test_GDG_007():
	WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	Log.info('Menampilkan jumlah Total perhalaman di main grid')
	hold(driver)
	pass

@mark.fixture_rupbasan
def test_GDG_008():
	Log.info('Menampilkan halaman sebelumnya dan selanjutnya menggunakan navigasi button ')
	hold(driver)
	pergi = driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke'])
	time.sleep(2)
	pergi.clear()
	pergi.send_keys('3')
	pergi.send_keys(Keys.ENTER)
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

@mark.fixture_rupbasan
def test_GDG_010():
	Log.info('Berhasil mencetak data penerimaan sesuai dengan total halaman yang dipilih dengan format PDF (.pdf)')
	hold(driver)
	driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportPDF']).click()
	# driver.find_element(By.ID, 'wholeButton').click()
	time.sleep(1)
	driver.find_element(By.ID, 'thisButton').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportPDF'])))
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_rupbasan
def test_GDG_009():
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) dengan menekan Button Export Excel')
	hold(driver)
	driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportexcel']).click()
	# driver.find_element(By.ID, 'wholeButton').click()
	time.sleep(1)
	driver.find_element(By.ID, 'thisButton').click()
	WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportexcel'])))
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_rupbasan
def test_GDG_011():
	hold(driver)
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) yang terhubung langsung dengan perangkat tambahan (printer)')
	driver.find_element(By.ID, 'printButton').click()
	time.sleep(1)
	driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['cetakinisaja']).click()
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_rupbasan
def test_SKG_001():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'printButton')))
	Log.info('Mengakses menu Sektor Gudang dengan memilih modul Lain - Lain kemudian pilih menu Parameter lalu pilih submenu Sektor Gudang')
	hold(driver)
	element = driver.find_element(By.XPATH, '//*[@id="app"]/div/nav/ul/li[2]/div')
	actions = ActionChains(driver)
	time.sleep(1)
	actions.move_to_element(element).perform()
	element2 = driver.find_element(By.XPATH, '//div[3]/div/ul/li[1]/div[1]')
	actions2 = ActionChains(driver)
	time.sleep(1)
	actions2.move_to_element(element2).perform()

	driver.find_element(By.LINK_TEXT, "Sektor Gudang").click()

@mark.fixture_rupbasan
def test_SKG_001():
	WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'searchButton')))