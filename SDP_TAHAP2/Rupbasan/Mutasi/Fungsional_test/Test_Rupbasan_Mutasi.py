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

from Settings.setup import initDriver, loadDataPath, hold
from Settings.login import oprupbasanbdg

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Test_Rupbasan_Mutasi.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("RUPEXEL"))
sheetrange = wb['Mutasi']
i = 2
CariData				= sheetrange['A'+str(i)].value

NomorSuratMutasi		= sheetrange['B'+str(i)].value
TglSuratMutasi			= sheetrange['C'+str(i)].value
NoSuratBA				= sheetrange['D'+str(i)].value
JenisRegistrasiAkhir	= sheetrange['E'+str(i)].value
Alamat					= sheetrange['F'+str(i)].value
Keterangan				= sheetrange['G'+str(i)].value

# init driver by os
@mark.fixture_Mutasi
def test_Ossetup_1():
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')

@mark.fixture_Mutasi
def test_loggin_2():
	oprupbasanbdg(driver)
	Log.info('Memasukan User name dan Password di halaman Login)')

@mark.fixture_Mutasi
def test_MTS_001():
	Log.info('Mengakses menu Mutasi dengan memilih modul Rupbasan kemudian pilih menu Mutasi')
	hold(driver)
	nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['Rupbasan'])
	ActionChains(driver).move_to_element(nav1).perform()
	time.sleep(1)
	driver.find_element(By.LINK_TEXT, 'Mutasi').click()
	driver.find_element(By.ID, 'kataKunci').click()

	attach(data=driver.get_screenshot_as_png())

plus = wb['TambahubahPenerimaan']
j = 15  # barisexel
Noregrup			= plus['C'+str(j)].value  # Nomor Registrasi Rupbasan
@mark.fixture_Mutasi
def test_MTS_002():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
	hold(driver)
	Log.info('Melakukan pengecekan filtering data dengan kategori yang dipilih pada dropdown di halaman Mutasi Basan dan Baran')
	driver.find_element(By.ID, 'filterColumn').click()
	time.sleep(1)
	driver.find_element(By.ID, 'noRegistrasiRupbasan').click()
	driver.find_element(By.ID, 'kataKunci').send_keys(Noregrup)

	driver.find_element(By.ID, 'buttonSearch').click()

@mark.fixture_Mutasi
def test_MTS_003():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
	hold(driver)
	Log.info('Mengakses halaman Cari Data dengan menekan button Tambah pada main grid')
	driver.find_element(By.ID, 'createButton').click()
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_Mutasi
def test_MTS_004():
	Log.info('Melakukan pencarian data registrasi penerimaan dengan menginputkan No. Registrasi Instansi lalu klik data hasil pencarian')
	hold(driver)
	cari = driver.find_element(By.ID, 'searchData')
	cari.click()
	cari.send_keys(CariData)
	WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.ID, 'searchOptions-0')))
	driver.find_element(By. ID, 'searchOptions-0').click()
	time.sleep(1)
	driver.find_element(By. ID, 'findButton').click()
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_Mutasi
def test_MTS_005_0():
	# WebDriverWait(driver, 40).until(EC.invisibility_of_element((By.ID, 'findButton-0')))
	hold(driver)
	Log.info('Menambahkan data Mutasi penerimaan basan dan baran dengan menekan button Cari di halaman Cari Data lalu menginputkan data Mutasi pada form Tambah kemudian submit data')
	Nosur = driver.find_element(By.ID, 'no_surat')
	Nosur.send_keys(NomorSuratMutasi)
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_Mutasi
def test_MTS_005_1():
	Log.info('Mengisi Tanggal Surat Mutasi')
	tgl = driver.find_element(By.ID, 'tgl_surat')
	tgl.click()
	tgl.send_keys(TglSuratMutasi)
	tgl.send_keys(Keys.ENTER)
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_Mutasi
def test_MTS_005_2():
	Log.info('Mengisi Nomor Surat BA')
	NoBA = driver.find_element(By.ID, 'no_ba')
	NoBA.send_keys(NoSuratBA)
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_Mutasi
def test_MTS_005_3():
	Log.info('Mengisi Jenis Registrasi Akhir')
	driver.find_element(By.ID,'dropdownJenisRegistrasiAkhir').click()
	if JenisRegistrasiAkhir == 'Register Barang Rampasan Negara':
		driver.find_element(By.ID,'dropdownJenisRegistrasiAkhirOption-0').click()
	elif JenisRegistrasiAkhir == 'Tingkat Penyidikan':
		driver.find_element(By.ID,'dropdownJenisRegistrasiAkhirOption-1').click()
	elif JenisRegistrasiAkhir =='Tingkat Penuntutan':
		driver.find_element(By.ID,'dropdownJenisRegistrasiAkhirOption-2').click()
	elif JenisRegistrasiAkhir =='Tingkat Pengadilan Negeri':
		driver.find_element(By.ID,'dropdownJenisRegistrasiAkhirOption-3').click()
	elif JenisRegistrasiAkhir =='Tingkat Pengadilan Tinggi':
		driver.find_element(By.ID,'dropdownJenisRegistrasiAkhirOption-4').click()
	elif JenisRegistrasiAkhir =='Tingkat Mahkamah Agung':
		driver.find_element(By.ID,'dropdownJenisRegistrasiAkhirOption-5').click()
	elif JenisRegistrasiAkhir =='Register Khusus Tingkat Penyidikan':
		driver.find_element(By.ID,'dropdownJenisRegistrasiAkhirOption-6').click()
	elif JenisRegistrasiAkhir =='Register Khusus Tingkat Penuntutan':
		driver.find_element(By.ID,'dropdownJenisRegistrasiAkhirOption-7').click()
	elif JenisRegistrasiAkhir =='Register Khusus Tingkat Pengadilan Negeri':
		driver.find_element(By.ID,'dropdownJenisRegistrasiAkhirOption-8').click()
	elif JenisRegistrasiAkhir =='Register Khusus Tingkat Pengadilan Tinggi':
		driver.find_element(By.ID,'dropdownJenisRegistrasiAkhirOption-9').click()
	elif JenisRegistrasiAkhir =='Register Khusus Tingkat Mahkamah Agung':
		driver.find_element(By.ID,'dropdownJenisRegistrasiAkhirOption-10').click()
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_Mutasi
def test_MTS_005_4():
	Log.info('Menginputkan alamat')
	Almt = driver.find_element(By.ID, 'alamat')
	Almt.send_keys(Alamat)
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_Mutasi
def test_MTS_005_5():
	Log.info('Menginputkan Keterangan')
	Ket = driver.find_element(By.ID,'keterangan')
	Ket.send_keys(Keterangan)
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_Mutasi
def test_MTS_005_6():
	hold(driver)
	Log.info('klik tombol simpan untuk Menambahkan data Mutasi')
	driver.find_element(By.ID,'submitButton').click()
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_Mutasi
def test_mencaridata():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
	hold(driver)
	Log.info('Melakukan pengecekan filtering data dengan kategori yang dipilih pada dropdown di halaman Mutasi Basan dan Baran')
	driver.find_element(By.ID, 'filterColumn').click()
	time.sleep(1)
	driver.find_element(By.ID, 'noSuratMutasi').click()
	driver.find_element(By.ID, 'kataKunci').send_keys(NomorSuratMutasi)
	driver.find_element(By.ID, 'buttonSearch').click()
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_Mutasi
def test_MTS_006():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
	hold(driver)
	Log.info('Menampilkan detail mutasi dengan menggunakan button (Detail) pada kolom aksi di tabel')
	driver.find_element(By.ID, 'detail-0').click()
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_Mutasi
def test_Kembalihome():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
	hold(driver)
	driver.find_element(By.ID, 'backButton').click()

	Log.info('Kembali ke Helaman Utama')
@mark.fixture_Mutasi
def test_selanjutnya():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
	Log.info('mencaridata')
	test_mencaridata()

@mark.fixture_Mutasi
def test_MTS_007():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
	hold(driver)
	Log.info('Penecekan Cetak BA')
	driver.find_element(By.ID, 'cetakBarcode-0').click()

sheetrange = wb['Mutasi']
l = 3
NoSMtas			= sheetrange['B'+str(l)].value
TglNoSMtas		= sheetrange['C'+str(l)].value
NoSBA			= sheetrange['D'+str(l)].value
JenisRegAkhir	= sheetrange['E'+str(l)].value
Almt			= sheetrange['F'+str(l)].value
Ketrn			= sheetrange['G'+str(l)].value
@mark.fixture_Mutasi
def test_MTS_008_0():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'cetakBarcode-0')))
	driver.find_element(By.ID, 'kataKunci').clear()
	test_mencaridata()
	hold(driver)
	Log.info('Mengubah Mutasi dengan menekan button Ubah')
	driver.find_element(By.ID, "update-0").click()
@mark.fixture_Mutasi
def test_MTS_008_1():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupelemen']['indexmutasi']['loadubah']))) 
	Log.info('Menunggu Loading')
	hold(driver)
	srat = driver.find_element(By.ID, 'no_surat')
	srat.clear()
	srat.send_keys(NoSMtas)
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_Mutasi
def test_MTS_008_2():
	Log.info('Mengisi Tanggal Surat Mutasi')
	tglsur = driver.find_element(By.ID, 'tgl_surat')
	tglsur.clear()
	tglsur.send_keys(TglSuratMutasi)
	tglsur.send_keys(Keys.ENTER)
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_Mutasi
def test_MTS_008_3():
	Log.info('Mengisi Nomor Surat BA')
	NoBA2 = driver.find_element(By.ID, 'no_ba')
	NoBA2.clear()
	NoBA2.send_keys(NoSuratBA)
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_Mutasi
def test_MTS_008_4():
	Log.info('Mengisi Jenis Registrasi Akhir')
	jreg = driver.find_element(By.ID,'jenisRegistrasiAkhir').click()
	time.sleep(1)
	if JenisRegAkhir == 'Register Barang Rampasan Negara':
		# jreg.send_keys(JenisRegAkhir)
		driver.find_element(By.ID,'jenisRegistrasiAkhir-0').click()
	elif JenisRegAkhir == 'Tingkat Penyidikan':
		# jreg.send_keys(JenisRegAkhir)
		driver.find_element(By.ID,'jenisRegistrasiAkhir-1').click()
	elif JenisRegAkhir =='Tingkat Penuntutan':
		# jreg.send_keys(JenisRegAkhir)
		driver.find_element(By.ID,'jenisRegistrasiAkhir-2').click()
	elif JenisRegAkhir =='Tingkat Pengadilan Negeri':
		# jreg.send_keys(JenisRegAkhir)
		driver.find_element(By.ID,'jenisRegistrasiAkhir-3').click()
	elif JenisRegAkhir =='Tingkat Pengadilan Tinggi':
		# jreg.send_keys(JenisRegAkhir)
		driver.find_element(By.ID,'jenisRegistrasiAkhir-4').click()
	elif JenisRegAkhir =='Tingkat Mahkamah Agung':
		# jreg.send_keys(JenisRegAkhir)
		driver.find_element(By.ID,'jenisRegistrasiAkhir-5').click()
	elif JenisRegAkhir =='Register Khusus Tingkat Penyidikan':
		# jreg.send_keys(JenisRegAkhir)
		driver.find_element(By.ID,'jenisRegistrasiAkhir-6').click()
	elif JenisRegAkhir =='Register Khusus Tingkat Penuntutan':
		# jreg.send_keys(JenisRegAkhir)
		driver.find_element(By.ID,'jenisRegistrasiAkhir-7').click()
	elif JenisRegAkhir =='Register Khusus Tingkat Pengadilan Negeri':
		# jreg.send_keys(JenisRegAkhir)
		driver.find_element(By.ID,'jenisRegistrasiAkhir-8').click()
	elif JenisRegAkhir =='Register Khusus Tingkat Pengadilan Tinggi':
		# jreg.send_keys(JenisRegAkhir)
		driver.find_element(By.ID,'jenisRegistrasiAkhir-9').click()
	elif JenisRegAkhir =='Register Khusus Tingkat Mahkamah Agung':
		# jreg.send_keys(JenisRegAkhir)
		driver.find_element(By.ID,'jenisRegistrasiAkhir-10').click()
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_Mutasi
def test_MTS_008_5():
	Log.info('Menginputkan alamat')
	Almt2 = driver.find_element(By.ID, 'alamat')
	Almt2.clear()
	Almt2.send_keys(Almt)
@mark.fixture_Mutasi
def test_MTS_008_6():
	Log.info('Menginputkan Keterangan')
	KeKetrn = driver.find_element(By.XPATH,'//*[@id="keterangan"]') #ID NYA SAMA JADI TIDAK TERPANGGIL
	KeKetrn.clear()
	KeKetrn.send_keys(Ketrn)
@mark.fixture_Mutasi
def test_MTS_008_6():
	hold(driver)
	Log.info('klik tombol simpan untuk Menambahkan data Mutasi')
	driver.find_element(By.ID,'submitButton').click()

@mark.fixture_Mutasi
def test_MTS_009():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
	Log.info('Pengecekan jumlah data per-halaman ')
	pass

@mark.fixture_Mutasi
def test_MTS_010():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
	hold(driver)
	Log.info('Menampilkan dropdown jumlah data yang dipilih oleh pengguna dan ditampilkan pada main grid')
	driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
	time.sleep(1)
	driver.find_element(By.XPATH, '//div[5]/div/div/div[1]/ul/li[1]').click()  # 3 Halaman
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_Mutasi
def test_MTS_011():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
	hold(driver)
	Log.info('Menampilkan halaman sebelumnya dan selanjutnya menggunakan navigasi button ')
	pergi = driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke'])
	time.sleep(2)
	pergi.clear()
	pergi.send_keys('3')
	pergi.send_keys(Keys.ENTER)
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))

@mark.fixture_Mutasi
def test_MTS_013():
	hold(driver)
	Log.info('Berhasil mencetak data penerimaan sesuai dengan total halaman yang dipilih dengan format PDF (.pdf)')
	driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportPDF']).click()
	# driver.find_element(By.ID, 'wholeButton').click()
	time.sleep(1)
	driver.find_element(By.ID, 'thisButton').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportPDF'])))
	attach(data=driver.get_screenshot_as_png())


@mark.fixture_Mutasi
def test_MTS_012():
	hold(driver)
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) dengan menekan Button Export Excel')
	driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportexcel']).click()
	# driver.find_element(By.ID, 'wholeButton').click()
	time.sleep(1)
	driver.find_element(By.ID, 'thisButton').click()
	WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportexcel'])))
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_Mutasi
def test_MTS_014():
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
