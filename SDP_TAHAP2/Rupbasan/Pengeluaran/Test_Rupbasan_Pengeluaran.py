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
fh = logging.FileHandler('Test_Rupbasan_Pengeluaran.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

# init driver by os
@mark.fixture_pengeluaran
def test_00_setup():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()

@mark.fixture_pengeluaran
def test_00_loggin():
	Log.info('Memasukan User name dan Password di halaman Login')
	# login(driver)
	oprupbasanbdg(driver)

@mark.fixture_pengeluaran
def test_PLN_001():
	Log.info('Mengakses menu Penerimaan dengan memilih modul Rupbasan kemudian pilih menu Penerimaan')
	hold(driver)
	nav1 = driver.find_element(
		By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['Rupbasan'])
	ActionChains(driver).move_to_element(nav1).perform()
	driver.find_element(By.LINK_TEXT, 'Pengeluaran').click()
	driver.find_element(By.ID, 'kataKunci').click()
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_pengeluaran
def test_PLN003_1():
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
	hold(driver)
	Log.info('Membuka halaman tambah penerimaan dengan klik button tambah')
	driver.find_element(By.ID, 'createButton').click()
	attach(data=driver.get_screenshot_as_png())

wb = load_workbook(environ.get("RUPEXEL"))
luaran = wb['Pengeluaran']
r = 2  # barisexel

Tanggal_Pengeluaran			= luaran['A'+str(r)].value
NoSurat_Pengeluaran			= luaran['B'+str(r)].value
TanggalSuratPengeluaran		= luaran['C'+str(r)].value
JenisPengeluaran			= luaran['D'+str(r)].value
Pengadilan					= luaran['E'+str(r)].value
Pengadilan_tipe				= luaran['F'+str(r)].value
No_Putusan					= luaran['G'+str(r)].value
TanggalPutusan				= luaran['H'+str(r)].value
NoSurat_Perintah			= luaran['I'+str(r)].value
TanggalSuratPerintah		= luaran['J'+str(r)].value
NoBAPengeluaran				= luaran['K'+str(r)].value
NoSuratRekomendasi			= luaran['L'+str(r)].value
Caripetugasexternal			= luaran['M'+str(r)].value
Caripetugaseinternal		= luaran['N'+str(r)].value
KetaranganPengeluaranBarang	= luaran['O'+str(r)].value
Status_Saksi				= luaran['P'+str(r)].value
CariPegawaisaksi			= luaran['Q'+str(r)].value
CariNoRegistrasi			= luaran['R'+str(r)].value
Barang						= luaran['S'+str(r)].value
Keteranganbrgkeluar			= luaran['T'+str(r)].value

@mark.fixture_pengeluaran
def test_PLN003_2():
	Log.info('Tanggal_Pengeluaran')
	hold(driver)
	pln1 = driver.find_element(By.ID, 'inputTglPengeluaran')
	pln1.send_keys(Tanggal_Pengeluaran)
	pln1.send_keys(Keys.ENTER)

@mark.fixture_pengeluaran
def test_PLN003_3():
	Log.info('No. Surat Pengeluaran')
	time.sleep(1)
	driver.find_element(By.ID, 'inputNoSuratPengeluaran').send_keys(NoSurat_Pengeluaran)

@mark.fixture_pengeluaran
def test_PLN003_3():
	time.sleep(1)
	Log.info('TanggalSuratPengeluaran')
	pln1 = driver.find_element(By.ID, 'inputTglSuratPengeluaran')
	pln1.send_keys(TanggalSuratPengeluaran)
	pln1.send_keys(Keys.ENTER)

@mark.fixture_pengeluaran
def test_PLN003_4():
	time.sleep(1)
	Log.info('JenisPengeluaran')
	driver.find_element(By.ID, 'dropdownJenisPengeluaran').click()
	time.sleep(1)
	if JenisPengeluaran == 'Kepentingan penyidikan dan penuntutan tidak memerlukan lagi':
		driver.find_element(By.ID, 'jenisPengeluaran0').click()
	elif JenisPengeluaran == 'Perkara tersebut tidak jadi dituntut karena tidak cukup bukti atau bukan merupakan tindak pidana':
		driver.find_element(By.ID, 'jenisPengeluaran1').click()
	elif JenisPengeluaran == 'Perkara tersebut dikesampingkan untuk kepentingan umum atau ditutup demi hukum':
		driver.find_element(By.ID, 'jenisPengeluaran2').click()
	elif JenisPengeluaran == 'Basan yang dapat lekas rusak':
		driver.find_element(By.ID, 'jenisPengeluaran3').click()
	elif JenisPengeluaran == 'Basan yang membahayakan':
		driver.find_element(By.ID, 'jenisPengeluaran4').click()
	elif JenisPengeluaran == 'Basan yang memerlukan biaya penyimpanan yang tinggi':
		driver.find_element(By.ID, 'jenisPengeluaran5').click()
	elif JenisPengeluaran == 'Dikembalikan kepada yang berhak':
		driver.find_element(By.ID, 'jenisPengeluaran6').click()
	elif JenisPengeluaran == 'Dirampas untuk Negara untuk Dilelang':
		driver.find_element(By.ID, 'jenisPengeluaran7').click()
	elif JenisPengeluaran == 'Dirampas untuk Negara untuk Dimusnahkan':
		driver.find_element(By.ID, 'jenisPengeluaran8').click()
	elif JenisPengeluaran == 'Dirampas untuk Negara untuk Dihibahkan kepada instansi yang membutuhkan untuk dimanfaatkan':
		driver.find_element(By.ID, 'jenisPengeluaran9').click()
	elif JenisPengeluaran == 'Untuk Dihadirkan dalam Persidangan':
		driver.find_element(By.ID, 'jenisPengeluaran10').click()
	elif JenisPengeluaran == 'Penghapusan':
		driver.find_element(By.ID, 'jenisPengeluaran11').click()

@mark.fixture_pengeluaran
def test_PLN003_5():
	time.sleep(1)
	Log.info('Pengadilan')
	driver.find_element(By.ID, 'dropdownPengadilanTipe').click()
	time.sleep(1)
	if Pengadilan == 'Pengadilan Negeri':
		driver.find_element(By.ID, 'Pengadilan Negeri').click()
	elif Pengadilan == 'Pengadilan Tinggi':
		driver.find_element(By.ID, 'Pengadilan Tinggi').click()

@mark.fixture_pengeluaran
def test_PLN003_6():
	time.sleep(1)
	Log.info('Tipe Pengadilan')
	driver.find_element(By.ID, 'dropdownPengadilanTipe').click()
	time.sleep(1)
	pln2 = driver.find_element(By.XPATH, pathData['Rupelemen']['pengeluaran']['pengadilantipe'])
	pln2.send_keys(Pengadilan_tipe)
	pln2.send_keys(Keys.DOWN)
	pln2.send_keys(Keys.ENTER)

@mark.fixture_pengeluaran
def test_PLN003_7():
	time.sleep(1)
	Log.info('TNo_Putusan')
	driver.find_element(By.ID, 'inputNoSuratPerintah').send_keys(No_Putusan)

@mark.fixture_pengeluaran
def test_PLN003_8():
	time.sleep(1)
	Log.info('TanggalSuratPengeluaran')
	pln1 = driver.find_element(By.ID, 'inputTglSuratPengeluaran')
	pln1.send_keys(TanggalSuratPengeluaran)
	pln1.send_keys(Keys.ENTER)

@mark.fixture_pengeluaran
def test_PLN003_9():
	time.sleep(1)
	Log.info('NoBAPengeluaran')
	driver.find_element(By.ID, 'inputNoBaPengeluaran').send_keys(NoBAPengeluaran)

@mark.fixture_pengeluaran
def test_PLN003_10():
	time.sleep(1)
	Log.info('NoSuratRekomendasi')
	driver.find_element(By.ID, 'inputNoSuratRekomendasi').send_keys(NoSuratRekomendasi)

@mark.fixture_pengeluaran
def test_PLN003_11():
	time.sleep(1)
	Log.info('Caripetugasexternal')
	pln3 = driver.find_element(By.ID, 'searchPetugasYangMenyerahkan')
	pln3.click()
	pln3.send_keys(Caripetugasexternal)
	driver.find_element(By.ID, 'searchPetugasYangMenyerahkan0').click()

@mark.fixture_pengeluaran
def test_PLN003_12():
	time.sleep(1)
	Log.info('Caripetugaseinternal')
	pln4 = driver.find_element(By.ID, 'searchPetugasPenerima')
	pln4.click()
	pln4.send_keys(Caripetugaseinternal)
	driver.find_element(By.ID, 'searchPetugasPenerima0').click()

@mark.fixture_pengeluaran
def test_PLN003_13():
	time.sleep(1)
	Log.info('KetaranganPengeluaranBarang')
	driver.find_element(By.ID, 'inputKeterangan').send_keys(KetaranganPengeluaranBarang)

@mark.fixture_pengeluaran
def test_Pindahtab1():
	Log.info('Pindah Tab')
	hold(driver)
	driver.find_element(By.ID, 'tab-saksi_pengeluaran').click()

@mark.fixture_pengeluaran
def test_PLN_003_14():
	Log.info('Status_Saksi')
	time.sleep(1)
	if 	(Status_Saksi == 'Internal' or Status_Saksi == 'internal'):
		driver.find_element(By.ID, 'radioButtonInternal').click()
		time.sleep(1)
		pln5 = driver.find_element(By.ID, 'searchSaksi-0')
		pln5.click()
		pln5.send_keys(CariPegawaisaksi)
		time.sleep(1)
		driver.find_element(By.ID, 'searchSaksi-00').click()
	elif (Status_Saksi == 'External' or Status_Saksi == 'external'):
		driver.find_element(By.ID, 'radioButtonEksternal').click()
		time.sleep(1)
		pln5 = driver.find_element(By.ID, 'searchSaksi-0')
		pln5.click()
		pln5.send_keys(CariPegawaisaksi)
		time.sleep(1)
		driver.find_element(By.ID, 'searchSaksi-00').click()

@mark.fixture_pengeluaran
def test_Pindahtab1():
	Log.info('Pindah Tab')
	hold(driver)
	driver.find_element(By.ID, 'tab-detail_barang').click()

@mark.fixture_pengeluaran
def test_PLN_003_15():
	Log.info('CariNoRegistrasi')
	time.sleep(1)