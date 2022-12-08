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

from Settings.setup import initDriver, loadDataPath, sleep, quit
from Settings.login import login


Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Penerimaan_1_IndexPenerimaan.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("RUPEXEL"))
sheetrange = wb['IndexPenerimaan']
i = 2

Carikolom       = sheetrange['A'+str(i)].value
Katkun          = sheetrange['B'+str(i)].value
Registrasi      = sheetrange['C'+str(i)].value
instansi        = sheetrange['D'+str(i)].value


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
    driver.find_element(By.LINK_TEXT, 'Penerimaan').click()
    driver.find_element(By.XPATH, pathData['Rupelemen']['indexpenempatan']['klik']).click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Menuju Menu Penerimaan dengan mengarahkan kursor ke navigasi ''Rubasan'' kemudian sub menu ''Penerimaan''')

@mark.fixture_penerimaan
def test_PencarianData_3():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
	driver.find_element(By.ID, 'filterColumn').click()
	
	if Carikolom == 'No Registrasi':
		driver.find_element(By. ID, 'no_reg').click()
	elif Carikolom == 'Tgl Penerimaan':
		driver.find_element(By. ID, 'tgl_penerimaan').click()
	elif Carikolom == 'Keterangan':
		driver.find_element(By. ID, 'keterangan').click()
	
	if Carikolom == 'Tgl Penerimaan':
		kattgl = driver.find_element(By.XPATH, pathData['Rupelemen']['indexpenempatan']['kategoritanggal'])
		kattgl.click()
		kattgl.send_keys(Katkun)
	else:
		driver.find_element(By. ID, 'kataKunci').send_keys(Katkun)

	driver.find_element(By.ID , 'searchButton').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))

	attach(data=driver.get_screenshot_as_png()) 
	Log.info('Melakukan Pencarian data berdasarkan kategori')

@mark.fixture_penerimaan
def test_menghapusfieldpencarian_4():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
    filter = driver.find_element(By.ID, 'filterColumn')
    ActionChains(driver).move_to_element(filter).perform()

    elemnthps = driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['clearkolom'])
    ActionChains(driver).move_to_element(elemnthps).perform()
    elemnthps.click()

    attach(data=driver.get_screenshot_as_png())
    Log.info('Melakukan Pencarian data berdasarkan kategori')

@mark.fixture_penerimaan
def test_caridatadenganjenisinstasi_5():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
    driver.find_element(By. ID, 'input_jenis_instansi_baran_basan').click()
    driver.find_element(By.ID, '201507090006').click()
    driver.find_element(By.ID , 'searchButton').click()

    field = driver.find_element(By.ID, 'input_jenis_instansi_baran_basan')
    ActionChains(driver).move_to_element(field).perform()
    elem = driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['clearistansi'])
    ActionChains(driver).move_to_element(elem).perform()
    elem.click()
    
    attach(data=driver.get_screenshot_as_png())
    Log.info('Melakukan Pencarian data berdasarkan instansi')

@mark.fixture_penerimaan
def test_caridatadenganjenisregistrasi_6():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
    driver.find_element(By. ID, 'input_jenis_registrasi_baran_basan').click()
    driver.find_element(By.ID, 'RBS1').click()
    driver.find_element(By.ID , 'searchButton').click()

    field = driver.find_element(By.ID, 'input_jenis_registrasi_baran_basan')
    ActionChains(driver).move_to_element(field).perform()
    elemins = driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['clearJREG'])
    ActionChains(driver).move_to_element(elemins).perform()
    elemins.click()

    attach(data=driver.get_screenshot_as_png())
    Log.info('Melakukan Pencarian data berdasarkan kategori')

# @mark.fixture_penerimaan
# def test_SortirDataTabel_7():
#     WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
#     driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['ascending']).click()
#     WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
#     driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['descending']).click()
#     WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))

#     attach(data=driver.get_screenshot_as_png())
#     Log.info('Melakukan Pencarian data berdasarkan kategori')

@mark.fixture_penerimaan
def test_membukahalamanedit_8():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
    test_PencarianData_3()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
    driver.find_element(By.CSS_SELECTOR, '.h-5').click()

    attach(data=driver.get_screenshot_as_png())
    Log.info('Akses menu halaman edit Penerimaan')

@mark.fixture_penerimaan
def test_kembalihalaman_9():
	WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.XPATH, pathData['Rupelemen']['ubahpenerimaan']['loadhalaman'])))
	# 
	driver.find_element(By.ID, 'backButton').click()
	
	attach(data=driver.get_screenshot_as_png())
	Log.info('Akses menu halaman edit Penerimaan')

@mark.fixture_penerimaan
def test_membukahalamanDetail_10():
	test_PencarianData_3()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
	
	driver.find_element(By. ID, 'daftarBarang0').click()
	attach(data=driver.get_screenshot_as_png()) 
	Log.info('Membuka daftar barang')

	test_kembalihalaman_9()

	attach(data=driver.get_screenshot_as_png())
	Log.info('Akses menu halama detail Penerimaan')

@mark.fixture_penerimaan
def test_CetakBA_11():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
	test_PencarianData_3()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))

	cetak = driver.find_element(By. ID, 'cetakBA0').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'cetakBA0')))

	# test_menghapusfieldpencarian_4()
	
	attach(data=driver.get_screenshot_as_png())
	Log.info('Akses menu halama Tambah Penerimaan')

@mark.fixture_penerimaan
def test_CetakSPTJM_12():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'cetakBA0')))
	driver.find_element(By. ID, 'cetakSPTJM0').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'cetakSPTJM0')))

	attach(data=driver.get_screenshot_as_png())
	Log.info('Akses menu halama Tambah Penerimaan')

@mark.fixture_penerimaan
def test_pilihpagehalaman_13(): #kasus 5 data tabel per halaman
    test_menghapusfieldpencarian_4()
    driver.find_element(By.ID , 'searchButton').click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))

    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//div[15]/div/div/div[1]/ul/li[1]').click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
    attach(data=driver.get_screenshot_as_png())
    Log.info('Menampilkan jumlah data yang sesuai dengan total halaman yang dipilih')

@mark.fixture_penerimaan
def test_pergikepagehalaman_14():
    pergi = driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke'])
    pergi.clear()
    pergi.send_keys('8')
    pergi.send_keys(Keys.ENTER)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
    
    attach(data=driver.get_screenshot_as_png())
    Log.info('Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir')

@mark.fixture_penerimaan
def test_exportPDF_15():
    driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportPDF']).click()
    driver.find_element(By.ID, 'wholeButton').click()
    driver.find_element(By.ID, 'thisButton').click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportPDF'])))
    attach(data=driver.get_screenshot_as_png())
    Log.info('Export data tabel dengan format PDF')

@mark.fixture_penerimaan
def test_exportexcel_16():
    driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportexcel']).click()
    driver.find_element(By.ID, 'wholeButton').click()
    driver.find_element(By.ID, 'thisButton').click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportexcel'])))
    attach(data=driver.get_screenshot_as_png())
    Log.info('Export data Tabel dengan format Excel')

@mark.fixture_penerimaan
def test_printhalamn_17():
    driver.find_element(By.ID,'printButton').click()
    driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['cetaksemua']).click()
    driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['cetakinisaja']).click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'printButton')))
    attach(data=driver.get_screenshot_as_png())
    Log.info('Print Data Tabel')

@mark.fixture_penerimaan
def test_membukahalamanTambah_18():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'printButton')))
    driver.find_element(By. ID, 'createButton').click
    attach(data=driver.get_screenshot_as_png())
    Log.info('Akses menu halama Tambah Penerimaan')
	
@mark.fixture_penerimaan
def test_penutup_19():
	quit(driver)
	Log.info('menyelesaikan tes dan menutup browser')