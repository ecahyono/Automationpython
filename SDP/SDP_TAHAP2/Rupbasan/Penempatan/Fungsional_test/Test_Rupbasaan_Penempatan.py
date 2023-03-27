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

PTN = wb['Penempatan']
u = 2
caribarang		= PTN['A'+str(u)].value #caribarang
tglpenempatan 	= PTN['B'+str(u)].value #Tanggal Penempatan
pilihtersangka  = PTN['C'+str(u)].value #Pilih Tersangka
gudang 			= PTN['D'+str(u)].value #Gudang
sektorgudang 	= PTN['E'+str(u)].value #Sektor Gudang
barisraklemari  = PTN['F'+str(u)].value #Baris/Rak/Lemari
nourut 			= PTN['G'+str(u)].value #No Urut
keterangan  	= PTN['H'+str(u)].value #Keterangan

@mark.fixture_penempatan
def test_selanjutnya1():
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By. ID, 'searchButton')))
	print('mencari Baran basan yang sudah ditempatkan')
	hold(driver)
	Log.info('Melakukan pengecekan filtering data berdasarkan kategori')
	driver.find_element(By.ID, 'filterColumn').click()
	time.sleep(1)
	driver.find_element(By. ID, 'nama_barang').click()
	driver.find_element(By. ID, 'kataKunci').send_keys(caribarang)
	print('CARI')
	driver.find_element(By.ID, 'searchButton').click()
	print('Menunggu Loading')
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penempatan
def test_PTN_003_0():
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By. ID, 'searchButton')))
	hold(driver)
	Log.info('membuka halaman tambah dengan menekan button tambah')
	driver.find_element(By. ID, 'createButton').click()
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penempatan
def test_PTN_003_1():
	Log.info('Mencari nama Barang')
	nabar = driver.find_element(By.ID, 'identity_keyword')
	nabar.click()
	nabar.send_keys(caribarang)
	print('Menunggu loading "Memuat"')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'identity_keyword-0')))
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
	driver.find_element(By.ID, "tersangkaOption-0").click()
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_penempatan
def test_PTN_003_4():
	Log.info('Memilih Gudang untuk barang')
	hold(driver)
	driver.find_element(By. ID, 'dropdownPilihGudang').click()
	if gudang == 'Gudang Umum Terbuka':
		WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'gudangOption-0')))
		driver.find_element(By.ID,'gudangOption-0').click()
	elif gudang == 'Gudang Umum Tertutup':
		WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'gudangOption-1')))
		driver.find_element(By.ID,'gudangOption-1').click()
	elif gudang == 'Gudang Berharga':
		WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'gudangOption-2')))
		driver.find_element(By.ID,'gudangOption-2').click()
	elif gudang == 'Gudang Berbahaya':
		WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'gudangOption-3')))
		driver.find_element(By.ID,'gudangOption-3').click()
	elif gudang == 'Gudang Hewan dan Tumbuhan':
		WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'gudangOption-4')))
		driver.find_element(By.ID,'gudangOption-4').click()
		# pilgud.send_keys(gudang)
		# print('Menunggu loading "Memuat"')
		# WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'gudangOption-0')))
		# driver.find_element(By.ID, "gudangOption-0").click()
	print('Menunggu loading Detail Gudang')
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, pathData['Rupelemen']['+penempatan']['descgudang'])))
	attach(data=driver.get_screenshot_as_png())	
@mark.fixture_penempatan
def test_PTN_003_5():
	Log.info('memilih sektor gudang')
	hold(driver)
	pilsek = driver.find_element(By. ID, 'dropdownSektorGudang')
	pilsek.click()
	pilsek.send_keys(sektorgudang)
	print('Menunggu loading "Memuat"')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'sektorGudangOption-0')))
	driver.find_element(By.ID, "sektorGudangOption-0").click()
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_penempatan
def test_PTN_003_6():
	Log.info('Memilih Baris dalam gudang')
	hold(driver)
	pillbar = driver.find_element(By.CSS_SELECTOR, ".el-input > #dropdownBaris")
	pillbar.click()
	pillbar.send_keys(barisraklemari)
	print('Menunggu loading "Memuat"')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'baris-0')))
	driver.find_element(By.ID, "baris-0").click()
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_penempatan
def test_PTN_003_7():
	Log.info('Memilih memilih nomer urut')
	pilnorut = driver.find_element(By.CSS_SELECTOR, ".el-input > #dropdownNoUrut")
	pilnorut.click()
	# pilnorut.send_keys(nourut)
	print('Menunggu loading "Memuat"')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'noUrut-0')))
	driver.find_element(By.ID, "noUrut-0").click()
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_penempatan
def test_PTN_003_8():
	Log.info('memasukan Ketrangan Penempatan')
	driver.find_element(By. ID, 'keterangan').send_keys(keterangan)
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_penempatan
def test_PTN_003_9():
	hold(driver)
	Log.info('menekan button submit data penempatan')
	driver.find_element(By.ID, "submitButton").click()

@mark.fixture_penempatan
def test_PTN_004_0():
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By. ID, 'searchButton')))
	hold(driver)
	Log.info('Mengubah data Penempatan basan dan baran dengan menggunakan button (Ubah) pada kolom aksi di tabel')
	driver.find_element(By.ID,'update-0').click()

PTN_2 = wb['Penempatan']
p = 5

cabar			= PTN_2['A'+str(p)].value #Cari Barang

tglptn			= PTN_2['B'+str(p)].value #Tanggal Penempatan
piltsangka		= PTN_2['C'+str(p)].value #Pilih Tersangka
pilgudang		= PTN_2['D'+str(p)].value #Gudang
pilsektorgud	= PTN_2['E'+str(p)].value #Sektor Gudang
pilbarraklem	= PTN_2['F'+str(p)].value #Baris/Rak/Lemari
pilnourut		= PTN_2['G'+str(p)].value #No Urut
pilketerangan  	= PTN_2['H'+str(p)].value #Keterangan

@mark.fixture_penempatan
def test_PTN_004_1():
	WebDriverWait(driver, 80).until(EC.invisibility_of_element((By. XPATH, pathData['Rupelemen']['indexmutasi']['loadubah'])))
	hold(driver)
	Log.info('Mencari nama Barang')
	nabar = driver.find_element(By.ID, 'identity_keyword')
	nabar.click()
	nabar.send_keys(cabar)
	print('Menunggu loading "Memuat"')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'identity_keyword-0')))
	driver.find_element(By.CSS_SELECTOR, "#identity_keyword-0").click()
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_penempatan
def test_PTN_004_2():
	Log.info('memilih tanggal dengan format DD/MM/YYYY ')
	tglPtn = driver.find_element(By.ID, 'tgl_penempatan')
	tglPtn.click()
	tglPtn.send_keys(tglptn)
	tglPtn.send_keys(Keys.ENTER)
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_penempatan
def test_PTN_004_3():
	Log.info('pencarian tersangka barang')
	Ters = driver.find_element(By. ID, 'dropdownPilihTersangka')
	Ters.click()
	Ters.send_keys(piltsangka)
	print('Menunggu loading "Memuat"')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'tersangkaOption-0')))
	driver.find_element(By.ID, "tersangkaOption-0").click()
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_penempatan
def test_PTN_004_4():
	Log.info('Memilih Gudang untuk barang')
	pilgud = driver.find_element(By. ID, 'dropdownPilihGudang')
	pilgud.click()
	if pilgudang == 'Gudang Umum Terbuka':
		pilgud.send_keys(pilgudang)
		WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'gudangOption-0')))
		driver.find_element(By.ID,'gudangOption-0').click()
	elif pilgudang == 'Gudang Umum Tertutup':
		pilgud.send_keys(pilgudang)
		WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'gudangOption-1')))
		driver.find_element(By.ID,'gudangOption-1').click()
	elif pilgudang == 'Gudang Berharga':
		pilgud.send_keys(pilgudang)
		WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'gudangOption-2')))
		driver.find_element(By.ID,'gudangOption-2').click()
	elif pilgudang == 'Gudang Berbahaya':
		pilgud.send_keys(pilgudang)
		WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'gudangOption-3')))
		driver.find_element(By.ID,'gudangOption-3').click()
	elif pilgudang == 'Gudang Hewan dan Tumbuhan':
		pilgud.send_keys(pilgudang)
		WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'gudangOption-4')))
		driver.find_element(By.ID,'gudangOption-4').click()
	# pilgud.send_keys(pilgudang)
	# print('Menunggu loading "Memuat"')
	# WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'gudangOption-0')))
	# driver.find_element(By.ID, "gudangOption-0").click()
	# print('Menunggu loading Detail Gudang')
	WebDriverWait(driver, 80).until(EC.presence_of_element_located((By.XPATH, pathData['Rupelemen']['+penempatan']['descgudang'])))
	attach(data=driver.get_screenshot_as_png())	
@mark.fixture_penempatan
def test_PTN_004_5():
	Log.info('memilih sektor gudang')
	pilsek = driver.find_element(By. ID, 'dropdownSektorGudang')
	pilsek.click()
	pilsek.send_keys(pilsektorgud)
	print('Menunggu loading "Memuat"')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'sektorGudangOption-0')))
	driver.find_element(By.ID, "sektorGudangOption-0").click()
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_penempatan
def test_PTN_004_6():
	Log.info('Memilih Baris dalam gudang')
	pillbar = driver.find_element(By.CSS_SELECTOR, ".el-input > #dropdownBaris")
	pillbar.click()
	pillbar.send_keys(pilbarraklem)
	print('Menunggu loading "Memuat"')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'baris-0')))
	driver.find_element(By.ID, "baris-0").click()
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_penempatan
def test_PTN_004_7():
	Log.info('Memilih memilih nomer urut')
	pilnorut = driver.find_element(By.CSS_SELECTOR, ".el-input > #dropdownNoUrut")
	pilnorut.click()
	pilnorut.send_keys(pilnourut)
	print('Menunggu loading "Memuat"')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'noUrut-0')))
	driver.find_element(By.ID, "noUrut-0").click()
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_penempatan
def test_PTN_004_8():
	Log.info('memasukan Ketrangan Penempatan')
	driver.find_element(By. ID, 'keterangan').send_keys(pilketerangan)
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_penempatan
def test_PTN_004_9():
	hold(driver)
	Log.info('menekan button submit data penempatan')
	driver.find_element(By.ID, "submitButton").click()

@mark.fixture_penempatan
def test_selanjutnya2():
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By. ID, 'searchButton')))
	print('mencari Baran basan yang sudah ditempatkan')
	hold(driver)
	Log.info('Melakukan pengecekan filtering data berdasarkan kategori')
	hold(driver)
	driver.find_element(By.ID, 'filterColumn').click()
	time.sleep(1)
	driver.find_element(By. ID, 'nama_barang').click()
	driver.find_element(By. ID, 'kataKunci').send_keys(cabar)
	print('CARI')
	driver.find_element(By.ID, 'searchButton').click()
	print('Menunggu Loading')
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penempatan
def test_PTN_005_0():
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By. ID, 'searchButton')))
	print('mencari Baran basan yang sudah ditempatkan')
	hold(driver)
	Log.info('Pengecekan Detail Penempatan')
	driver.find_element(By.ID, 'detail-0').click()

@mark.fixture_penempatan
def test_PTN_005_1():
	WebDriverWait(driver, 80).until(EC.invisibility_of_element((By. XPATH, pathData['Rupelemen']['indexmutasi']['loadubah'])))
	Log.info('Menampilkan detail Penempatan dengan menggunakan button (Detail) pada kolom aksi di tabel')
	hold(driver)
	driver.find_element(By.ID, 'backButton-0').click()
	print('Kembali he halaman Utama')

@mark.fixture_penempatan
def test_PTN_006():
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By. ID, 'searchButton')))
	test_selanjutnya2()
	Log.info('Pengecekan Cetak Barcode')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By. ID, 'searchButton')))
	driver.find_element(By.ID, 'cetakBarcode-0').click()
	Log.info('Mencetak barcode dengan menekan Button Cetak Barcode')

@mark.fixture_penempatan
def test_PTN_007():
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By. ID, 'cetakBarcode-0')))
	hold(driver)
	driver.find_element(By.ID, 'kataKunci').click()
	driver.find_element(By.ID, 'kataKunci').click()
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	hold(driver)
	Log.info('Menampilkan dropdown jumlah data yang dipilih oleh pengguna dan ditampilkan pada main grid')
	driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
	time.sleep(1)
	driver.find_element(By.XPATH, '//div[5]/div/div/div[1]/ul/li[1]').click()  # 3 Halaman
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penempatan
def test_PTN_008():
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	Log.info('Menampilkan jumlah data yang sesuai dengan total halaman yang dipilih')
	pass

@mark.fixture_penempatan
def test_PTN_009():
	hold(driver)
	Log.info('Menampilkan halaman sebelumnya dan selanjutnya menggunakan navigasi button ')
	pergi = driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke'])
	time.sleep(2)
	pergi.click()
	pergi.send_keys('3')
	pergi.send_keys(Keys.ENTER)

@mark.fixture_penempatan
def test_PTN_011():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	hold(driver)
	Log.info('Berhasil mencetak data penerimaan sesuai dengan total halaman yang dipilih dengan format PDF (.pdf)')
	driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportPDF']).click()
	# driver.find_element(By.ID, 'wholeButton').click()
	time.sleep(1)
	driver.find_element(By.ID, 'thisButton').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportPDF'])))
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penempatan
def test_PTN_010():
	hold(driver)
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) dengan menekan Button Export Excel')
	driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportexcel']).click()
	# driver.find_element(By.ID, 'wholeButton').click()
	time.sleep(1)
	driver.find_element(By.ID, 'thisButton').click()
	WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportexcel'])))
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penempatan
def test_PTN_012():
	hold(driver)
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) yang terhubung langsung dengan perangkat tambahan (printer)')
	driver.find_element(By.ID, 'printButton').click()
	time.sleep(1)
	driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['cetakinisaja']).click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'printButton')))
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_Mutasi
def test_tutupweb():
	hold(driver)
	Log.info('menyelesaikan test penerimaan dan menutup browser')
	driver.quit()