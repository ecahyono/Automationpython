from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
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

from Settings.setup import initDriver, loadDataPath, sleep, quit
from Settings.login import login


Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Penerimaan_5_Daftarbarang.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("RUPEXEL"))

# init driver by os
@mark.fixture_penerimaan
def test_Ossetup_1():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')

@mark.fixture_penerimaan
def test_loggin_2():
    login(driver)
    Log.info('Memasukan User name dan Password di halaman Login)')

@mark.fixture_penerimaan
def test_aksesmenuPenerimaan_3():
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    driver.implicitly_wait(5)
    driver.find_element(By.LINK_TEXT, 'Penerimaan').click()
    driver.find_element(By.XPATH, pathData['Rupelemen']['indexpenempatan']['klik']).click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Menuju Menu Penerimaan dengan mengarahkan kursor ke navigasi ''Rubasan'' kemudian sub menu ''Penerimaan''')


sheetrange = wb['IndexPenerimaan']
i = 3
Carikolom       = sheetrange['A'+str(i)].value
Katkun          = sheetrange['B'+str(i)].value

@mark.fixture_penerimaan
def test_Pencariandata_4():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
	driver.find_element(By.ID, 'filterColumn').click()
	
	if Carikolom == 'No Registrasi':
		driver.find_element(By. ID, 'no_reg').click()
	elif Carikolom == 'Tgl Penerimaan':
		driver.find_element(By. ID, 'tgl_penerimaan').click()
		kattgl = driver.find_element(By.XPATH, pathData['Rupelemen']['indexpenempatan']['kategoritanggal'])
		kattgl.click()
		kattgl.send_keys(Katkun)
	elif Carikolom == 'Keterangan':
		driver.find_element(By. ID, 'keterangan').click()
	driver.find_element(By. ID, 'kataKunci').send_keys(Katkun)

	driver.find_element(By.ID , 'searchButton').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))

	attach(data=driver.get_screenshot_as_png()) 
	Log.info('Melakukan Pencarian data berdasarkan kategori')

@mark.fixture_penerimaan
def test_Membukadetailbarang_5():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
	driver.find_element(By. ID, 'daftarBarang0').click()
	attach(data=driver.get_screenshot_as_png()) 
	Log.info('Membuka daftar barang')
	WebDriverWait(driver, 50).until(EC.invisibility_of_element_located((By.XPATH, pathData['Rupelemen']['+barang']['loadingbarang2'])))	

@mark.fixture_penerimaan
def test_pilihdetailbarang():
	print('	###S ILAHKAN MASUKAN NOMOR 1 DAN SETERUSNYA UNTUK MEMILIH DETAIL BARANG YANG AKAN LIHAT ####')
	print('ketik ### B ### jika ingin kembali ke halaman sebelumnya')
	inp = input('Ingin Melihat Detail Barang nomer:')
	while True:
		try:
			if inp == '1':
				driver.find_element(By.ID, 'buttonDetail0').click()	
				WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.XPATH, pathData['Rupelemen']['indexpenempatan']['loaddetail'])))
				Log.info('Membuka halaman detail barang Nourut' + inp)
			elif inp == '2':
				driver.find_element(By.ID, 'buttonDetail1').click()
				WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.XPATH, pathData['Rupelemen']['indexpenempatan']['loaddetail'])))
				Log.info('Membuka halaman detail barang Nourut' + inp)
			elif inp == '3':
				driver.find_element(By.ID, 'buttonDetail2') 
				WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.XPATH, pathData['Rupelemen']['indexpenempatan']['loaddetail'])))
				Log.info('Membuka halaman detail barang Nourut'  +inp)
			elif inp == '4':
				driver.find_element(By.ID, 'buttonDetail3').click()
				WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.XPATH, pathData['Rupelemen']['indexpenempatan']['loaddetail'])))
				Log.info('Membuka halaman detail barang Nourut' + inp)
			elif inp == '5':
				driver.find_element(By.ID, 'buttonDetail4').click()
				WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.XPATH, pathData['Rupelemen']['indexpenempatan']['loaddetail'])))
				Log.info('Membuka halaman detail barang Nourut' + inp)
			elif (inp == 'B'or inp == 'b'):
				driver.find_element(By.ID,'backButton').click()
			elif (inp == 'Q'or inp == 'q'):
				quit(driver)
				Log.info('menyelesaikan test dan menutup browser')
		except NoSuchElementException:
			print('Belum Ada Barang Silahkan Inputkan Barang terlebih dahulu')
			print('Detail barang dengan Nourut' + inp +'Tidak tersedia')	
			test_pilihdetailbarang()

