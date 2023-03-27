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
plus = wb['TambahubahPenerimaan']
i = 2  # barisexel

JenisRegistrasi		= plus['A'+str(i)].value  # Jenis Registrasi
tglPenerimaan		= plus['B'+str(i)].value  # Tanggal Penerimaan
Noregrup			= plus['C'+str(i)].value  # Nomor Registrasi Rupbasan
instansi			= plus['D'+str(i)].value  # Instansi
Noregins			= plus['E'+str(i)].value  # Nomor Registrasi Instansi
NoSIP				= plus['F'+str(i)].value  # Nomor Surat Izin Penyitaan
tglSIP				= plus['G'+str(i)].value  # Tanggal Surat Izin Penyitaan
Ppenyita			= plus['H'+str(i)].value  # Pengadilan Penyita
NoSP				= plus['I'+str(i)].value  # Nomor Surat Penyitaan
tglSP				= plus['J'+str(i)].value  # Tanggal Surat Penyitaan
pasal				= plus['K'+str(i)].value  # Pasal
NBAST				= plus['L'+str(i)].value  # No. BA Serah Terima
Keterangan			= plus['M'+str(i)].value  # Keterangan

Ptgpenerima			= plus['N'+str(i)].value  # Petugas Penerima
pilihPTG			= plus['O'+str(i)].value  # Petugas Penyrah

# tab identitas
jumlahidentitas		= plus['P'+str(i)].value  # jumlh identitas
identitas1			= plus['Q'+str(i)].value  # identitas 1
identitas2			= plus['R'+str(i)].value  # identitas 2

jumlahpenyerah		= plus['S'+str(i)].value  # jumlah penyerah
# status1			= plus['T'+str(i)].value #status1
Penyerah1			= plus['U'+str(i)].value  # penyerah1
# status2			= plus['v'+str(i)].value #Penyerah1
Penyerah2			= plus['W'+str(i)].value  # Penyerah2

jumlahsaksi			= plus['X'+str(i)].value  # jumlah saksi
statusaksi1			= plus['Y'+str(i)].value  # statussaksi1
saksi1				= plus['Z'+str(i)].value  # saksi1
statusaksi2			= plus['AA'+str(i)].value  # statussaksi2
saksi2				= plus['AB'+str(i)].value  # saksi2

# init driver by os
@mark.fixture_penerimaan
def test_00_setup():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()

@mark.fixture_penerimaan
def test_00_loggin():
	Log.info('Memasukan User name dan Password di halaman Login')
	# login(driver)
	oprupbasanbdg(driver)

@mark.fixture_penerimaan
def test_PNM_001():
	Log.info('Mengakses menu Penerimaan dengan memilih modul Rupbasan kemudian pilih menu Penerimaan')
	hold(driver)
	nav1 = driver.find_element(
		By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['Rupbasan'])
	ActionChains(driver).move_to_element(nav1).perform()
	driver.find_element(By.LINK_TEXT, 'Penerimaan').click()
	driver.find_element(By.ID, 'kataKunci').click()
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penerimaan
def test_PNM003_1():
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	hold(driver)
	Log.info('Membuka halaman tambah penerimaan dengan klik button tambah')
	driver.find_element(By.ID, 'createButton').click()
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penerimaan
def test_PNM003_2():
	time.sleep(1)
	Log.info('Memeilih Dropdown Jenis Registrasi')
	# WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.XPATH, pathData['Rupelemen']['ubahpenerimaan']['loadhalaman'])))
	# Jenis Registrasi
	driver.find_element(By.ID, 'dropdownJenisRegistrasi').click()
	time.sleep(1)
	if JenisRegistrasi == 'Register Barang Rampasan Negara':
		driver.find_element(By.ID, 'jenisRegistrasi0').click()
	elif JenisRegistrasi == 'Tingkat Penyidikan':
		driver.find_element(By.ID, 'jenisRegistrasi1').click()
	elif JenisRegistrasi == 'Tingkat Penuntutan':
		driver.find_element(By.ID, 'jenisRegistrasi2').click()
	elif JenisRegistrasi == 'Tingkat Pengadilan Negeri':
		driver.find_element(By.ID, 'jenisRegistrasi3').click()
	elif JenisRegistrasi == 'Tingkat Pengadilan Tinggi':
		driver.find_element(By.ID, 'jenisRegistrasi4').click()
	elif JenisRegistrasi == 'Tingkat Mahkamah Agung':
		driver.find_element(By.ID, 'jenisRegistrasi5').click()
	elif JenisRegistrasi == 'Register Khusus Tingkat Penyidikan':
		driver.find_element(By.ID, 'jenisRegistrasi6').click()
	elif JenisRegistrasi == 'Register Khusus Tingkat Penyidikan':
		driver.find_element(By.ID, 'jenisRegistrasi7').click()
	elif JenisRegistrasi == 'Register Khusus Tingkat Pengadilan Negeri':
		driver.find_element(By.ID, 'jenisRegistrasi8').click()
	elif JenisRegistrasi == 'Register Khusus Tingkat Pengadilan Tinggi':
		driver.find_element(By.ID, 'jenisRegistrasi9').click()
	elif JenisRegistrasi == 'Register Khusus Tingkat Mahkamah Agung':
		driver.find_element(By.ID, 'jenisRegistrasi10').click()
	attach(data=driver.get_screenshot_as_png())


@mark.fixture_penerimaan
def test_PNM003_3():
	time.sleep(1)
	Log.info('Menginput Tanggal Penerimaan')
	Tanggal_Penerimaan = driver.find_element(By.ID, 'inputTglPenerimaan')  # Tanggal Penerimaan
	Tanggal_Penerimaan.send_keys(tglPenerimaan)
	Tanggal_Penerimaan.send_keys(Keys.ENTER)
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penerimaan
def test_PNM003_4():
	time.sleep(1)
	Log.info('Menginput Nomor Registrasi Rupbasan')
	driver.find_element(By.ID, 'inputNoRegistrasi').send_keys(Noregrup)  # Nomor Registrasi Rupbasan

@mark.fixture_penerimaan
def test_PNM003_5():
	time.sleep(1)
	Log.info('Memilih Opsi instansi')
	driver.find_element(By.ID, 'dropdownInstansi').click()  # Instansi
	time.sleep(2)
	if instansi == 'POLDA JABAR':
		driver.find_element(By.ID, 'instansi0').click()
	elif instansi == 'POLRES BANDUNG':

		driver.find_element(By.ID, 'instansi3').click()
	elif instansi == 'POLRES CIMAHI':

		driver.find_element(By.ID, 'instansi10').click()
	elif instansi == 'POLRES CIREBON':

		driver.find_element(By.ID, 'instansi18').click()
	elif instansi == 'POLRES KUNINGAN':

		driver.find_element(By.ID, 'instansi21').click()
	elif instansi == 'POLRESTA SURAKARTA':

		driver.find_element(By.ID, 'instansi38').click()
	elif instansi == 'POLRES CIAMIS':

		driver.find_element(By.ID, 'instansi15').click()
	elif instansi == 'POLRES BANJAR KOTA':

		driver.find_element(By.ID, 'instansi16').click()
	elif instansi == 'POLRES MAJALENGKA':

		driver.find_element(By.ID, 'instansi19').click()
	elif instansi == 'POLRES INDRAMAYU':

		driver.find_element(By.ID, 'instansi20').click()
	elif instansi == 'POLRES JAKARTA BARAT':

		driver.find_element(By.ID, 'instansi24').click()
	attach(data=driver.get_screenshot_as_png())


@mark.fixture_penerimaan
def test_PNM003_6():
	time.sleep(1)
	Log.info('Menginput Nomor Registrasi Instansi')
	driver.find_element(By.ID, 'inputNoRegInstansi').send_keys(Noregins)  # Nomor Registrasi Instansi
	attach(data=driver.get_screenshot_as_png())


@mark.fixture_penerimaan
def test_PNM003_7():
	time.sleep(1)
	Log.info('Menginput Nomor Surat Izin Penyitaan')
	driver.find_element(By.ID, 'inputNoSuratIzinPenyitaan').send_keys(NoSIP)  # Nomor Surat Izin Penyitaan
	attach(data=driver.get_screenshot_as_png())


@mark.fixture_penerimaan
def test_PNM003_8():
	time.sleep(1)
	Log.info('Menginput Tanggal Surat Izin Penyitaan')
	Tanggal_Surat_Izin_Penyitaan = driver.find_element(By.ID, 'inputTglSuratIzinPenyitaan')  # Tanggal Surat Izin Penyitaan
	Tanggal_Surat_Izin_Penyitaan.send_keys(tglSIP)
	Tanggal_Surat_Izin_Penyitaan.send_keys(Keys.ENTER)
	attach(data=driver.get_screenshot_as_png())


@mark.fixture_penerimaan
def test_PNM003_9():
	Log.info('Memilih Opsi Pengadilan Penyita')
	driver.find_element(By.ID, 'dropdownPengadilanPenyita').click()
	time.sleep(2)
	if Ppenyita == 'Pengadilan Negeri Jakarta Utara':

		driver.find_element(By.ID, 'pengadilanNegeri2').click()
	elif Ppenyita == 'Pengadilan Negeri Bandung':

		driver.find_element(By.ID, 'pengadilanNegeri7').click()
	elif Ppenyita == 'Pengadilan Negeri Sukabumi':

		driver.find_element(By.ID, 'pengadilanNegeri9').click()
	elif Ppenyita == 'Pengadilan Negeri Tasikmalaya':

		driver.find_element(By.ID, 'pengadilanNegeri15').click()
	elif Ppenyita == 'Pengadilan Negeri Majalengka':

		driver.find_element(By.ID, 'pengadilanNegeri19').click()
	elif Ppenyita == 'Pengadilan Negeri Ciamis':

		driver.find_element(By.ID, 'pengadilanNegeri20').click()
	elif Ppenyita == 'Pengadilan Negeri Kuningan':

		driver.find_element(By.ID, 'pengadilanNegeri21').click()
	elif Ppenyita == 'Pengadilan Negeri Subang':
		driver.find_element(By.ID, 'pengadilanNegeri23').click()

	elif Ppenyita == 'Pengadilan Negeri Bangkalan':

		driver.find_element(By.ID, 'pengadilanNegeri39').click()
	elif Ppenyita == 'Pengadilan Negeri Yogyakarta':

		driver.find_element(By.ID, 'pengadilanNegeri147').click()
	elif Ppenyita == 'Pengadilan Negeri Bondowoso':

		driver.find_element(By.ID, 'pengadilanNegeri48').click()
	attach(data=driver.get_screenshot_as_png())


@mark.fixture_penerimaan
def test_PNM003_10():
	time.sleep(1)
	Log.info('menginput nomor surat Penyitaan')
	driver.find_element(By.ID, 'inputNoSuratPenyitaan').send_keys(NoSP)  # Nomor Surat Penyitaan
	attach(data=driver.get_screenshot_as_png())


@mark.fixture_penerimaan
def test_PNM003_11():
	time.sleep(1)
	Log.info('menginput tanggal surat Penyitaan')
	Tanggal_Surat_Izin_Penyitaan = driver.find_element(By.ID, 'inputTglSuratPenyitaan')  # Tanggal Surat Penyitaan
	Tanggal_Surat_Izin_Penyitaan.send_keys(tglSP)
	Tanggal_Surat_Izin_Penyitaan.send_keys(Keys.ENTER)
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penerimaan
def test_PNM003_12():
	time.sleep(1)
	Log.info('input pasal')
	driver.find_element(By.ID, 'inputPasal').send_keys(pasal)  # Pasal
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penerimaan
def test_PNM003_13():
	time.sleep(1)
	Log.info('Input field text input menggunakan varchar')
	driver.find_element(By.ID, 'inputNoBaPenyitaan').send_keys(NBAST)  # No. BA Serah Terima
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penerimaan
def test_PNM003_14():
	time.sleep(1)
	Log.info('Input field text area')
	driver.find_element(By.ID, 'inputKeterangan').send_keys(Keterangan)
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penerimaan
def test_PNM003_15():
	time.sleep(1)
	Log.info('Melakukan Pencarian data Identitas petugas Penerima')
	penerima = driver.find_element(By.ID, 'searchPetugasPenerima')  # Petugas Penerima
	penerima.click()
	penerima.send_keys(Ptgpenerima)
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchPetugasPenerima0')))
	driver.find_element(By.ID, 'searchPetugasPenerima0').click()
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penerimaan
def test_PNM003_16():
	time.sleep(1)
	Log.info('Melakukan Pencarian data Petugas yang menyerahkan')
	penyerah = driver.find_element(By.ID, 'nama_penyerah')  # Petugas Penyrah
	penyerah.send_keys()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchPetugasYangMenyerahkan0')))
	penyerah.send_keys(pilihPTG)
	driver.find_element(By.ID, 'searchPetugasYangMenyerahkan0').click()
	attach(data=driver.get_screenshot_as_png())


@mark.fixture_penerimaan
def test_PNM003_17():
	time.sleep(1)
	Log.info('Pengecekan jumlah data identitas yang akan di inputkan')
	if jumlahidentitas == 2:
		driver.find_element(By.ID, 'tambahIdentitas').click()
	elif jumlahidentitas == 1:
		print('-')
		Log.info(' menambah 1 baris status petugas')
	attach(data=driver.get_screenshot_as_png())

# tab Identitas
@mark.fixture_penerimaan
def test_PNM003_18():
	time.sleep(1)
	Log.info('Melakukan Pencarian data Identitas')
	identi1 = driver.find_element(By.ID, "searchIdentitas-0")
	identi1.click()
	identi1.send_keys(identitas1)
	driver.find_element(By. ID, 'searchIdentitas-00').click()
	attach(data=driver.get_screenshot_as_png())

	Log.info('Melakukan Pencarian data Identitas')
	identi2 = driver.find_element(By.ID, "searchIdentitas-1")
	identi2.click()
	identi2.send_keys(identitas2)
	driver.find_element(By. ID, 'searchIdentitas-10').click()
	attach(data=driver.get_screenshot_as_png())

# Tab Petugas Instansi Yng Menyerahkan
@mark.fixture_penerimaan
def test_PNM003_19():
	time.sleep(1)
	Log.info('klik tab Petugas Instansi')
	driver.find_element(By.ID, "tab-petugas_instansi").click()
	attach(data=driver.get_screenshot_as_png())


@mark.fixture_penerimaan
def test_PNM003_20():
	time.sleep(1)
	Log.info(' menambah 1 baris status petugas')
	if jumlahpenyerah == 2:
		driver.find_element(By.ID, "tambahPenyerahPenerima").click()
	elif jumlahpenyerah == 1:
		print('')
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penerimaan
def test_PNM003_21():
	time.sleep(1)
	Log.info('Memilih Petugas Instansi Yang menyerahkan pertama')
	nyerah1 = driver.find_element(By.ID, 'searchPetugasPenyerah-0')
	nyerah1.click()
	nyerah1.send_keys(Penyerah1)
	driver.find_element(By.ID, 'searchPetugasPenyerah-00').click()

	Log.info('Memilih Petugas Instansi Yang menyerahkan kedua')
	nyerah2 = driver.find_element(By.ID, 'searchPetugasPenyerah-1')
	nyerah2.click()
	time.sleep(1)
	nyerah2.send_keys(Penyerah2)
	driver.find_element(By.ID, 'searchPetugasPenyerah-10').click()
	Log.info('Melakukan Pencarian data petugas penyerah internal')

# #tab Saksi
@mark.fixture_penerimaan
def test_PNM003_22():
	time.sleep(1)
	Log.info('Klik tab Saksi Penerima')
	driver.find_element(By.ID, "tab-saksi_penerimaan").click()
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penerimaan
def test_PNM003_23():
	time.sleep(1)
	Log.info(' menambah 1 baris status petugas saksi')
	if jumlahsaksi == 2:
		driver.find_element(By.ID, "tambahSaksi").click()
	elif jumlahsaksi == 1:
		print('')
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penerimaan
def test_PNM003_24():
	time.sleep(1)
	statsaks1 = driver.find_element(By.ID, 'searchSaksi-0')
	statsaks1.click()
	statsaks1.send_keys(saksi1)
	driver.find_element(By.ID, 'searchSaksi-00').click()

	statsak2 = driver.find_element(By.ID, 'searchSaksi-1')
	statsak2.click()
	statsak2.send_keys(saksi2)
	driver.find_element(By.ID, 'searchSaksi-10').click()

	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penerimaan
def test_PNM003_25():
	hold(driver)
	Log.info('menekan button submit')
	driver.find_element(By.ID, "submitButton").click()

# @mark.fixture_penerimaan
# def test_CaridataUntukBarang():
# 	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
# 	hold(driver)
# 	Log.info('Mengecek data penerimaan yang telah dibuat dengan memfilter tabel penerimaan untuk menambah barang')
# 	driver.find_element(By.ID, 'filterColumn').click()
# 	time.sleep(1)
# 	driver.find_element(By.ID, 'no_reg').click()
# 	driver.find_element(By. ID, 'kataKunci').send_keys(Noregrup)
# 	driver.find_element(By.ID, 'searchButton').click()

@mark.fixture_penerimaan
def test_PNM_005_006():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	hold(driver)
	Log.info('[PNM-005]=>Menampilkan detail penerimaan dengan menggunakan button (Daftar Barang) pada kolom aksi di tabel')
	Log.info('[PNM-006]=>Menampilkan halaman daftar barang baran dan basan dengan menggunakan button (Daftar Barang) pada kolom aksi di tabel')
	driver.find_element(By. ID, 'daftarBarang0').click()
	attach(data=driver.get_screenshot_as_png())

# #Kelengkapan Basan Baran ==============================================================
sbarang = wb['Barangbasan']
y = 11 # barisexel

nama_barang			= sbarang['A'+str(y)].value  # Nama Barang
barang_temuan		= sbarang['B'+str(y)].value  # Barang Temuan
jenis_barang		= sbarang['C'+str(y)].value  # Jenis Barang
satuan				= sbarang['D'+str(y)].value  # Satuan
jumlah				= sbarang['E'+str(y)].value  # Jumlah
jumlah_baik			= sbarang['F'+str(y)].value  # Jumlah Baik
jumlah_rusak_ringan = sbarang['G'+str(y)].value  # Jumlah Rusak Ringan
jumlah_rusak_berat	= sbarang['H'+str(y)].value  # Jumlah Rusak Berat
Jumlahfoto			= sbarang['I'+str(y)].value  # listjumlah foto barang
foto1				= sbarang['J'+str(y)].value  # Nama Foto 1
keteranfanfoto1		= sbarang['K'+str(y)].value  # Keterangan1
foto2				= sbarang['L'+str(y)].value  # Nama Foto 2
keteranfanfoto2		= sbarang['M'+str(y)].value  # Keterangan2
foto3				= sbarang['N'+str(y)].value  # Nama Foto 2
keteranfanfoto3		= sbarang['O'+str(y)].value  # Keterangan2

NomorPenelitian		= sbarang['P'+str(y)].value  # Nomor Penelitian
tglPenelitian		= sbarang['Q'+str(y)].value  # Tanggal Penelitian
NoskPenelitian		= sbarang['R'+str(y)].value  # Nomor SK Peneliti
tglSkPeneliti		= sbarang['S'+str(y)].value  # Tanggal SK Peneliti

Golongan			= sbarang['T'+str(y)].value  # Golongan

KeadaanSegelPenyita = sbarang['U'+str(y)].value  # Keadaan Segel Penyita
KondisiBarang		= sbarang['v'+str(y)].value  # Kondisi Barang
SubKondisiBarang	= sbarang['W'+str(y)].value  # Sub Kondisi Barang
Sifat				= sbarang['X'+str(y)].value  # Sifat
MerekDanKondisi		= sbarang['Y'+str(y)].value  # Merek Dan Kondisi
Berat				= sbarang['Z'+str(y)].value  # Berat
VolumeCC			= sbarang['AA'+str(y)].value  # Volume / CC
Panjang				= sbarang['AB'+str(y)].value  # Panjang
Lebar				= sbarang['AC'+str(y)].value  # Lebar
Tinggi				= sbarang['AD'+str(y)].value  # Tinggi
Laras				= sbarang['AE'+str(y)].value  # Laras
TipeMerek			= sbarang['AF'+str(y)].value  # Tipe / Merek
PembuatPabrik		= sbarang['AG'+str(y)].value  # Pembuat Pabrik
NomorPabrik			= sbarang['AH'+str(y)].value  # Nomor Pabrik
Peluru				= sbarang['AI'+str(y)].value  # Peluru
BahanPeledak		= sbarang['AJ'+str(y)].value  # Bahan Peledak
SenpiDikeuarkanOleh = sbarang['AK'+str(y)].value  # Senpi Dikeuarkan Oleh
TglKeluar			= sbarang['AL'+str(y)].value  # Tanggal Keluar
NomorDikeluarkan	= sbarang['AM'+str(y)].value  # Nomor Dikeluarkan
TanggalBerlaku		= sbarang['AN'+str(y)].value  # Tanggal Berlaku
NomorSenpi			= sbarang['AO'+str(y)].value  # Nomor Senpi
KomposisiBahan		= sbarang['AP'+str(y)].value  # Komposisi Bahan
Kaliber				= sbarang['AQ'+str(y)].value  # Kaliber
Warna				= sbarang['AR'+str(y)].value  # Warna
NomorMesin			= sbarang['AS'+str(y)].value  # Nomor Mesin
TahunPembuatan		= sbarang['AT'+str(y)].value  # Tahun Pembuatan
# Tahun Pengeluaran / Penerbitan
TahunPengeluaranpenerbitan	= sbarang['AU'+str(y)].value
NomorChasis					= sbarang['AV'+str(y)].value  # Nomor Chasis
TeganganDaya				= sbarang['AW'+str(y)].value  # Tegangan Daya
MerekSumberDaya				= sbarang['AX'+str(y)].value  # Merek Sumber Daya
Pegangan					= sbarang['AY'+str(y)].value  # Pegangan
TulisanHurufGambar			= sbarang['AZ'+str(y)].value  # Tulisan Huruf Gambar
AsalBasanDari				= sbarang['BA'+str(y)].value  # Asal Basan Dari
PerkiraanUsia				= sbarang['BB'+str(y)].value  # Perkiraan Usia
KadarKarat					= sbarang['BC'+str(y)].value  # Kadar Karat
Kemasan					= sbarang['BD'+str(y)].value  # Kemasan
Batasan					= sbarang['BE'+str(y)].value  # Batasan
NoIMB					= sbarang['BF'+str(y)].value  # No. IMB
IsiGedung				= sbarang['BG'+str(y)].value  # Isi Gedung
SuratBukti				= sbarang['BH'+str(y)].value  # Surat Bukti
BenderaNegara		= sbarang['BI'+str(y)].value  # Bendera Negara
NoPolisi			= sbarang['BJ'+str(y)].value  # No. Polisi
WarnaTNKB			= sbarang['BK'+str(y)].value  # Warna TNKB
MasaBerlakuTNK		= sbarang['BL'+str(y)].value  # Masa Berlaku TNKB
BahanBakar			= sbarang['BM'+str(y)].value  # Bahan Bakar
CiriKhusus			= sbarang['BN'+str(y)].value  # Ciri Khusus
HalLainnya			= sbarang['BO'+str(y)].value  # Hal Lainnya
PemeliharaanKhusus	= sbarang['BP'+str(y)].value  # Pemeliharaan Khusus
# Catatan Pemeliharaan Khusus
CatatanPemeliharaanKhusus	= sbarang['BQ'+str(y)].value
RekomendasiTimPeneliti		= sbarang['BR'+str(y)].value  # Rekomendasi Tim Peneliti

# Menentukan Jumlah Petugas Peneliti
jumlhpeneliti	= sbarang['BS'+str(y)].value
Peneliti1		= sbarang['BT'+str(y)].value  # Petugas1
Peneliti2		= sbarang['BU'+str(y)].value  # Petugas2
Peneliti3		= sbarang['BV'+str(y)].value  # Petugas3

TglPenilaian		= sbarang['BW'+str(y)].value  # Tanggal Penilaian
NoBAPenelitian		= sbarang['BX'+str(y)].value  # Nomor BA Penelitian
NilaiSatuanBarang	= sbarang['BY'+str(y)].value  # Nilai Satuan Barang
Keterangan			= sbarang['BZ'+str(y)].value  # Keterangan

# Menentukan Jumlah Petugas Peneliti
jumlhpenelilai	= sbarang['CA'+str(y)].value
Penilai1		= sbarang['CB'+str(y)].value  # Petugas1
Penilai2		= sbarang['CC'+str(y)].value  # Petugas2
Penilai3		= sbarang['CD'+str(y)].value  # Petugas3

@mark.fixture_penerimaan
def test_PNM_007_0():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	Log.info('Menambahkan data baran dan basan dengan menginputkan data di halaman daftar barang kemudian klik button simpan')
	hold(driver)
	driver.find_element(By.ID, 'tab-kelengkapanBasanBaran').click()
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_penerimaan
def test_PNM_007_1():
	time.sleep(1)
	Log.info('Nama barang')
	nabar = driver.find_element(By.ID, 'nama_barang').send_keys(nama_barang)  # Nama Barang

@mark.fixture_penerimaan
def test_PNM_007_2():
	time.sleep(1)
	Log.info('checkbox barang temuan')
	if barang_temuan == 'Iya':
		driver.find_element(By.ID, 'barang_temuan').click()
	elif barang_temuan == 'Tidak':
		print('')

@mark.fixture_penerimaan
def test_PNM_007_3():
	time.sleep(1)
	Log.info('Memilih jenis barang basan')
	driver.find_element(By.ID, 'input_jenis_baran_basan').click()
	if jenis_barang == 'Umum Terbuka':
		driver.find_element(By.ID, 'JSB1').click()
	elif jenis_barang == 'Umum Tertutup':
		driver.find_element(By.ID, 'JSB2').click()
	elif jenis_barang == 'Berharga':
		driver.find_element(By.ID, 'JSB3').click()
	elif jenis_barang == 'Berbahaya':
		driver.find_element(By.ID, 'JSB4').click()
	elif jenis_barang == 'Hewan dan Tumbuhan':
		driver.find_element(By.ID, 'JSB5').click()

@mark.fixture_penerimaan
def test_PNM_007_4():
	time.sleep(1)
	Log.info('Memilih satuan barang')
	driver.find_element(By.ID, 'input_satuan_baran_basan').click()
	if satuan == 'Unit':
		driver.find_element(By.ID, '01').click()
	elif satuan == 'Buah':
		driver.find_element(By.ID, '02').click()
	elif satuan == 'Pasang':
		driver.find_element(By.ID, '03').click()
	elif satuan == 'Lembar':
		driver.find_element(By.ID, '04').click()
	elif satuan == 'Keping':
		driver.find_element(By.ID, '05').click()
	elif satuan == 'Batang':
		driver.find_element(By.ID, '06').click()
	elif satuan == 'Bungkus':
		driver.find_element(By.ID, '07').click()
	elif satuan == 'Potong':
		driver.find_element(By.ID, '08').click()
	elif satuan == 'Tablet':
		driver.find_element(By.ID, '09').click()
	elif satuan == 'Ekor':
		driver.find_element(By.ID, '10').click()
	elif satuan == 'Rim':
		driver.find_element(By.ID, '11').click()
	elif satuan == 'Karat':
		driver.find_element(By.ID, '12').click()
	elif satuan == 'Botol':
		driver.find_element(By.ID, '13').click()
	elif satuan == 'Butir':
		driver.find_element(By.ID, '14').click()
	elif satuan == 'Roll':
		driver.find_element(By.ID, '15').click()
	elif satuan == 'Dus':
		driver.find_element(By.ID, '16').click()
	elif satuan == 'Karung':
		driver.find_element(By.ID, '17').click()
	elif satuan == 'Koli':
		driver.find_element(By.ID, '18').click()
	elif satuan == 'Sak':
		driver.find_element(By.ID, '19').click()
	elif satuan == 'Bal':
		driver.find_element(By.ID, '20').click()
	elif satuan == 'Kaleng':
		driver.find_element(By.ID, '21').click()
	elif satuan == 'Set':
		driver.find_element(By.ID, '22').click()
	elif satuan == 'Slop':
		driver.find_element(By.ID, '23').click()
	elif satuan == 'Gulung Gram':
		driver.find_element(By.ID, '24').click()
	elif satuan == 'Ton':
		driver.find_element(By.ID, '25').click()
	elif satuan == 'Kg':
		driver.find_element(By.ID, '26').click()
	elif satuan == 'Gram':
		driver.find_element(By.ID, '27').click()
	elif satuan == 'Mili':
		driver.find_element(By.ID, '28').click()
	elif satuan == 'Meter':
		driver.find_element(By.ID, '29').click()
	elif satuan == 'M2':
		driver.find_element(By.ID, '30').click()
	elif satuan == 'M3':
		driver.find_element(By.ID, '31').click()
	elif satuan == 'Inchi':
		driver.find_element(By.ID, '32').click()
	elif satuan == 'Cc':
		driver.find_element(By.ID, '33').click()
	elif satuan == 'Liter':
		driver.find_element(By.ID, '34').click()
	elif satuan == 'Lusin':
		driver.find_element(By.ID, '35').click()
	elif satuan == 'Lain - Lain':
		driver.find_element(By.ID, 'SATUAN LAIN').click()

@mark.fixture_penerimaan
def test_PNM_007_6():
	time.sleep(1)
	Log.info('Jumlah Baik')
	driver.find_element(By.ID, 'jumlah_baik').send_keys(jumlah_baik)  # jumlah_baik

@mark.fixture_penerimaan
def test_PNM_007_7():
	time.sleep(1)
	Log.info('Jumlah rusak ringan')
	driver.find_element(By.ID, 'jumlah_rusak_ringan').send_keys(jumlah_rusak_ringan)  # jumlah rusak ringan

@mark.fixture_penerimaan
def test_PNM_007_8():
	time.sleep(1)
	Log.info('Jumlah rusak berat')
	driver.find_element(By.ID, 'jumlah_rusak_berat').send_keys(jumlah_rusak_berat)  # jumlah Rusak Berat

@mark.fixture_penerimaan
def test_PNM_007_9():
	time.sleep(1)
	Log.info('Jumlah foto')
	if Jumlahfoto == 3:
		driver.find_element(By.ID, 'tambah_foto').click()
		driver.find_element(By.ID, 'tambah_foto').click()
	elif Jumlahfoto == 2:
		driver.find_element(By.ID, 'tambah_foto').click()

	elif Jumlahfoto == 1:
		pass

@mark.fixture_penerimaan
def test_PNM_007_10():
	time.sleep(1)
	Log.info('upload foto barang 1')
	driver.find_element(By.ID, 'pilihFoto0').click()
	time.sleep(3)
	pyautogui.write(environ.get(r"FOTBRG1"))
	pyautogui.press('enter')
	#
	# driver.find_element(By.ID,'namaFoto0').send_keys(foto1)
	driver.find_element(By.ID, 'keterangann0').send_keys(keteranfanfoto1)

@mark.fixture_penerimaan
def test_PNM_007_11():
	time.sleep(1)
	Log.info('upload foto barang 2')
	driver.find_element(By.ID, 'pilihFoto1').click()
	time.sleep(3)
	pyautogui.write(environ.get(r"FOTBRG1"))
	pyautogui.press('enter')
	#
	# driver.find_element(By.ID,'namaFoto1').send_keys(foto2)
	driver.find_element(By.ID, 'keterangann1').send_keys(keteranfanfoto2)

@mark.fixture_penerimaan
def test_PNM_007_12():
	time.sleep(1)
	Log.info('upload foto barang 3')
	driver.find_element(By.ID, 'pilihFoto2').click()
	time.sleep(3)
	pyautogui.write(environ.get(r"FOTBRG1"))
	pyautogui.press('enter')
	#
	# driver.find_element(By.ID,'namaFoto2').send_keys(foto3)
	driver.find_element(By.ID, 'keterangann2').send_keys(keteranfanfoto3)

# Penelitian ==============================================================
def test_PNM_007_13():
	time.sleep(1)
	Log.info('pindah tab')
	hold(driver)
	# WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.XPATH, pathData['Rupelemen']['+barang']['loadingbarang'])))
	driver.find_element(By.ID, 'tab-penelitian').click()

@mark.fixture_penerimaan
def test_PNM_007_14():
	time.sleep(1)
	Log.info('Nomor Penelitian')
	noPenelitian = driver.find_element(By.ID, 'noPenelitian').send_keys(
		NomorPenelitian)  # Nomor Penelitian

@mark.fixture_penerimaan
def test_PNM_007_15():
	time.sleep(1)
	Log.info('tanggal Penelitian')
	penelititgl = driver.find_element(By.ID, 'tglPenelitian')
	penelititgl.click()
	penelititgl.send_keys(tglPenelitian)
	penelititgl.send_keys(Keys.ENTER)  # Tanggal Penelitian

@mark.fixture_penerimaan
def test_PNM_007_16():
	time.sleep(1)
	Log.info('no SK penelitian')
	driver.find_element(By.ID, 'noSkPeneliti').send_keys(NoskPenelitian)  # Nomor SK Penelitian

@mark.fixture_penerimaan
def test_PNM_007_17():
	time.sleep(1)
	Log.info('Tanggal SK Penelitian')
	skpenelititgl = driver.find_element(By.ID, 'tglSkPeneliti')
	skpenelititgl.click
	skpenelititgl.send_keys(tglSkPeneliti)
	skpenelititgl.send_keys(Keys.ENTER)  # Tanggal SK Penelitian

@mark.fixture_penerimaan
def test_PNM_007_18():
	time.sleep(1)  # Memilih Golongan
	Log.info('Memilih Golongan')
	hold(driver)
	driver.find_element(By.ID, 'golongan').click()
	if Golongan == 'ELEKTRONIK':
		driver.find_element(By.ID, '001').click()
	elif Golongan == 'MEKANIK':
		driver.find_element(By.ID, '002').click()
	elif Golongan == 'ALAT KOMUNIKASI':
		driver.find_element(By.ID, '003').click()
	elif Golongan == 'MEBEL':
		driver.find_element(By.ID, '004').click()
	elif Golongan == 'MAKANAN':
		driver.find_element(By.ID, '005').click()
	elif Golongan == 'MINUMAN TIDAK BERALKOHOL':
		driver.find_element(By.ID, '006').click()
	elif Golongan == 'MINUMAN BERALKOHOL':
		driver.find_element(By.ID, '007').click()
	elif Golongan == 'TEKSTIL':
		driver.find_element(By.ID, '008').click()
	elif Golongan == 'KAYU':
		driver.find_element(By.ID, '009').click()
	elif Golongan == 'LOGAM/LOGAM BERHARGA':
		driver.find_element(By.ID, '010').click()
	elif Golongan == 'BATU PERMATA':
		driver.find_element(By.ID, '011').click()
	elif Golongan == 'MATA UANG':
		driver.find_element(By.ID, '012').click()
	elif Golongan == 'SURAT BERHARGA':
		driver.find_element(By.ID, '013').click()
	elif Golongan == 'OBAT-OBATAN':
		driver.find_element(By.ID, '014').click()
	elif Golongan == 'NAPZA':
		driver.find_element(By.ID, '015').click()
	elif Golongan == 'KIMIA':
		driver.find_element(By.ID, '016').click()
	elif Golongan == 'KOSMETIK':
		driver.find_element(By.ID, '017').click()
	elif Golongan == 'BAHAN PELEDAK':
		driver.find_element(By.ID, '018').click()
	elif Golongan == 'SENJATA TAJAM (SAJAM)':
		driver.find_element(By.ID, '019').click()
	elif Golongan == 'SENJATA API (SENPI)':
		driver.find_element(By.ID, '020').click()
	elif Golongan == 'KENDARAAN BERMOTOR':
		driver.find_element(By.ID, '021').click()
	elif Golongan == 'KENDARAAN TIDAK BERMOTOR':
		driver.find_element(By.ID, '022').click()
	elif Golongan == 'ANGKUTAN (DARAT/LAUT/UDARA)':
		driver.find_element(By.ID, '023').click()
	elif Golongan == 'ALAT BANGUNAN':
		driver.find_element(By.ID, '024').click()
	elif Golongan == 'ALAT PERTANIAN':
		driver.find_element(By.ID, '025').click()
	elif Golongan == 'BAHAN BANGUNAN':
		driver.find_element(By.ID, '026').click()
	elif Golongan == 'MINYAK':
		driver.find_element(By.ID, '027').click()
	elif Golongan == 'TANAMAN':
		driver.find_element(By.ID, '028').click()
	elif Golongan == 'IKAN':
		driver.find_element(By.ID, '029').click()
	elif Golongan == 'HEWAN TERNAK':
		driver.find_element(By.ID, '030').click()
	elif Golongan == 'BINATANG':
		driver.find_element(By.ID, '031').click()
	elif Golongan == 'MACAM KARET':
		driver.find_element(By.ID, '032').click()
	elif Golongan == 'BAHAN DASAR KULIT':
		driver.find_element(By.ID, '033').click()
	elif Golongan == 'KACA/PECAH BELAH':
		driver.find_element(By.ID, '034').click()
	elif Golongan == 'PLASTIK':
		driver.find_element(By.ID, '035').click()
	elif Golongan == 'HIASAN':
		driver.find_element(By.ID, '036').click()
	elif Golongan == 'ASESORIS':
		driver.find_element(By.ID, '037').click()
	elif Golongan == 'PERHIASAN':
		driver.find_element(By.ID, '038').click()
	elif Golongan == 'KASET':
		driver.find_element(By.ID, '039').click()
	elif Golongan == 'KERTAS':
		driver.find_element(By.ID, '040').click()
	elif Golongan == 'PUSTAKA':
		driver.find_element(By.ID, '041').click()
	elif Golongan == 'PUPUK':
		driver.find_element(By.ID, '042').click()
	elif Golongan == 'BUAH':
		driver.find_element(By.ID, '043').click()
	elif Golongan == 'TABUNG BERISI GAS':
		driver.find_element(By.ID, '044').click()
	elif Golongan == 'TABUNG KOSONG':
		driver.find_element(By.ID, '045').click()
	elif Golongan == 'PENGUKUR WAKTU':
		driver.find_element(By.ID, '046').click()
	elif Golongan == 'SAYURAN':
		driver.find_element(By.ID, '047').click()
	elif Golongan == 'BUMBU':
		driver.find_element(By.ID, '048').click()
	elif Golongan == 'LOGAM':
		driver.find_element(By.ID, '049').click()
	elif Golongan == 'BATU-BATUAN':
		driver.find_element(By.ID, '050').click()
	elif Golongan == 'HASIL TAMBANG':
		driver.find_element(By.ID, '051').click()
	elif Golongan == 'Lain - Lain':
		driver.find_element(By.ID, 'BASAN LAIN').click()

@mark.fixture_penerimaan
def test_PNM_007_19():
	time.sleep(1)  # Keadaan Segel Penyita
	Log.info('Keadaan Segel Penyita')
	driver.find_element(By.ID, 'keadaanSegel').send_keys(KeadaanSegelPenyita)

@mark.fixture_penerimaan
def test_PNM_007_20():
	time.sleep(1)  # Kondisi Barang
	Log.info('Kondisi Barang')
	driver.find_element(By.ID, 'kondisiBarang').click()
	if KondisiBarang == 'Baik':
		driver.find_element(By.ID, 'KBB1').click()
	elif KondisiBarang == 'Rusak':
		driver.find_element(By.ID, 'KBB2').click()

@mark.fixture_penerimaan
def test_PNM_007_21():
	time.sleep(1)  # Sub Kondisi Barang
	Log.info('Sub Kondisi Barang')
	if KondisiBarang == 'Rusak':
		driver.find_element(By.ID, 'subKondisiBarang').click()
		if SubKondisiBarang == 'Rusak Ringan':
			driver.find_element(By.ID, 'SKB1').click()
		elif SubKondisiBarang == 'Rusak Berat':
			driver.find_element(By.ID, 'SKB2').click()
	elif KondisiBarang == 'Baik':
		pass

@mark.fixture_penerimaan
def test_PNM_007_22():
	time.sleep(1)  # Sifat
	Log.info('Input sifat')
	driver.find_element(By.ID, 'sifat').send_keys(Sifat)

@mark.fixture_penerimaan
def test_PNM_007_23():
	time.sleep(1)  # Merek Dan Kondisi
	Log.info('input merek dan kondisi')
	driver.find_element(By.ID, 'merekKondisi').send_keys(MerekDanKondisi)

@mark.fixture_penerimaan
def test_PNM_007_24():
	time.sleep(1)
	Log.info('input berat')
	driver.find_element(By.ID, 'berat').send_keys(Berat)  # Berat

@mark.fixture_penerimaan
def test_PNM_007_25():
	time.sleep(1)
	Log.info('input volime')
	driver.find_element(By.ID, 'volumeCc').send_keys(VolumeCC)  # Volume / CC

@mark.fixture_penerimaan
def test_PNM_007_26():
	time.sleep(1)
	Log.info('input panjang')
	driver.find_element(By.ID, 'panjang').send_keys(Panjang)  # Panjang

@mark.fixture_penerimaan
def test_PNM_007_27():
	time.sleep(1)
	Log.info('input lebar')
	driver.find_element(By.ID, 'lebar').send_keys(Lebar)  # Lebar

@mark.fixture_penerimaan
def test_PNM_007_28():
	time.sleep(1)
	Log.info('input tinggi')
	driver.find_element(By.ID, 'tinggi').send_keys(Tinggi)  # Tinggi

@mark.fixture_penerimaan
def test_PNM_007_29():
	time.sleep(1)
	Log.info('input tipemerek')
	if Golongan == 'HEWAN TERNAK':
		pass
	else:
		driver.find_element(By.ID, 'tipeMerek').send_keys(
			TipeMerek)  # Tipe / Merek

@mark.fixture_penerimaan
def test_PNM_007_30():
	time.sleep(1)
	Log.info('input yang jenis golongan senjata api')
	if Golongan == 'SENJATA API (SENPI)':
		driver.find_element(By.ID, 'laras').send_keys(Laras)  # Laras
		driver.find_element(By.ID, 'pembuatPabrik').send_keys(PembuatPabrik)  # Pembuat Pabrik
		driver.find_element(By.ID, 'nomorPabrik').send_keys(NomorPabrik)  # Nomor Pabrik
		driver.find_element(By.ID, 'peluru').send_keys(Peluru)  # Peluru
		driver.find_element(By.ID, 'pasDikeluarkanOleh').send_keys(SenpiDikeuarkanOleh)  # Senpi Dikeuarkan Oleh
		tglexit = driver.find_element(By.ID, 'tglKeluar')
		tglexit.send_keys(TglKeluar)  # Tanggal Keluar
		tglexit.send_keys(Keys.ENTER)
		driver.find_element(By.ID, 'nmr_dikeluarkan').send_keys(NomorDikeluarkan)  # Nomor Dikeluarkan
		tglberlksenpi = driver.find_element(By.ID, 'tglBerlakuPasSenpi')
		tglberlksenpi.send_keys(TanggalBerlaku)  # Tanggal Berlaku
		tglberlksenpi.send_keys(Keys.ENTER)
		driver.find_element(By.ID, 'nmrSenpi').send_keys(NomorSenpi)  # Nomor Senpi
		driver.find_element(By.ID, 'komposisiBahan').send_keys(KomposisiBahan)  # Komposisi Bahan
		driver.find_element(By.ID, 'kaliber').send_keys(Kaliber)  # Kaliber
	else:
		pass

@mark.fixture_penerimaan
def test_PNM_007_31():
	time.sleep(1)
	Log.info('input yang jenis golongan elektronik')
	if (Golongan == 'ELEKTRONIK' or Golongan == 'PERHIASAN'):
		driver.find_element(By.ID, 'pembuatPabrik').send_keys(PembuatPabrik)  # Pembuat Pabrik
		driver.find_element(By.ID, 'nomorPabrik').send_keys(NomorPabrik)  # Nomor Pabrik
		tglexit = driver.find_element(By.ID, 'tglKeluar')
		tglexit.send_keys(TglKeluar)  # Tanggal Keluar
		tglexit.send_keys(Keys.ENTER)
		driver.find_element(By.ID, 'nmr_dikeluarkan').send_keys(NomorDikeluarkan)  # Nomor Dikeluarkan
		tglberlksenpi = driver.find_element(By.ID, 'tglBerlakuPasSenpi')
		tglberlksenpi.send_keys(TanggalBerlaku)  # Tanggal Berlaku
		tglberlksenpi.send_keys(Keys.ENTER)
		# driver.find_element(By.ID, 'nmrSenpi').send_keys(NomorSenpi) #Nomor Senpi
	else:
		pass

@mark.fixture_penerimaanx
def test_PNM_007_32():
	time.sleep(1)
	Log.info('input tahunPembuatan')
	if (Golongan == 'KENDARAAN BERMOTOR' or Golongan == 'SENJATA API (SENPI)' or Golongan == 'Lain - Lain'):
		thnpembuatan = driver.find_element(By.ID, 'tahunPembuatan')
		thnpembuatan.send_keys(TahunPembuatan)  # Tahun Pembuatan
		thnpembuatan.send_keys(Keys.ENTER)
	else:
		pass

@mark.fixture_penerimaanx
def test_PNM_007_33():
	time.sleep(1)
	Log.info('input tahunPengeluaranPenerbitan')
	if (Golongan == 'KENDARAAN BERMOTOR' or Golongan == 'SENJATA API (SENPI)' or Golongan == 'Lain - Lain'):
		thnpengeluaran = driver.find_element(
			By.ID, 'tahunPengeluaranPenerbitan')
		# Tahun Pengeluaran / Penerbitan
		thnpengeluaran.send_keys(TahunPengeluaranpenerbitan)
		thnpengeluaran.send_keys(Keys.ENTER)
	else:
		pass

@mark.fixture_penerimaan
def test_PNM_007_34():
	time.sleep(1)
	Log.info('input warna')
	if (Golongan == 'KENDARAAN BERMOTOR' or Golongan == 'SENJATA API (SENPI)'):
		driver.find_element(By.ID, 'warna').send_keys(Warna)  # Warna
	else:
		pass

@mark.fixture_penerimaan
def test_PNM_007_35():
	time.sleep(1)
	Log.info('input NomorMesin')
	if Golongan == 'KENDARAAN BERMOTOR':
		driver.find_element(By.ID, 'nmrMesin').send_keys(
			NomorMesin)  # Nomor Mesin
	else:
		pass

@mark.fixture_penerimaan
def test_PNM_007_36():
	time.sleep(1)
	Log.info('input NomorChasis')
	if Golongan == 'KENDARAAN BERMOTOR':
		driver.find_element(By.ID, 'nmrChasis').send_keys(
			NomorChasis)  # Nomor Chasis
	else:
		pass

@mark.fixture_penerimaan
def test_PNM_007_37():
	time.sleep(1)
	Log.info('input TeganganDaya')
	if Golongan == 'KENDARAAN BERMOTOR':
		driver.find_element(By.ID, 'teganganDaya').send_keys(
			TeganganDaya)  # Tegangan Daya
	else:
		pass

@mark.fixture_penerimaan
def test_PNM_007_38():
	time.sleep(1)
	Log.info('input MerekSumberDaya')
	if Golongan == 'KENDARAAN BERMOTOR':
		driver.find_element(By.ID, 'merekSumberDaya').send_keys(
			MerekSumberDaya)  # Merek Sumber Daya
	else:
		pass

@mark.fixture_penerimaan
def test_PNM_007_39():
	time.sleep(1)
	Log.info('input AsalBasanDari')
	driver.find_element(By.ID, 'asalDari').send_keys(
		AsalBasanDari)  # Asal Basan Dari

@mark.fixture_penerimaan
def test_PNM_007_40():
	time.sleep(1)
	Log.info('input PerkiraanUsia')
	driver.find_element(By.ID, 'perkiraanUsia').send_keys(
		PerkiraanUsia)  # Perkiraan Usia

@mark.fixture_penerimaan
def test_PNM_007_41():
	time.sleep(1)
	Log.info('input Kemasan')
	if Golongan == 'BATU PERMATA':
		driver.find_element(By.ID, 'kadarKarat').send_keys(
			KadarKarat)  # Kadar Karat
		driver.find_element(By.ID, 'kemasan').send_keys(Kemasan)  # Kemasan
	else:
		pass

@mark.fixture_penerimaan
def test_PNM_007_42():
	time.sleep(1)
	Log.info('input Batasan')
	driver.find_element(By.ID, 'batasan').send_keys(Batasan)  # Batasan


@mark.fixture_penerimaan
def test_PNM_007_44():
	time.sleep(1)
	Log.info('input NoIMB')
	driver.find_element(By.ID, 'NoImb').send_keys(NoIMB)  # No. IMB

@mark.fixture_penerimaan
def test_PNM_007_45():
	time.sleep(1)
	Log.info('input IsiGedung')
	driver.find_element(By.ID, 'isiGedung').send_keys(IsiGedung)  # Isi Gedung


@mark.fixture_penerimaan
def test_PNM_007_46():
	time.sleep(1)
	Log.info('input SuratBukti')
	driver.find_element(By.ID, 'suratBukti').send_keys(SuratBukti)  # Surat Bukti

@mark.fixture_penerimaan
def test_PNM_007_47():
	time.sleep(1)
	Log.info('input BenderaNegara')
	driver.find_element(By.ID, 'bendera').send_keys(BenderaNegara)  # Bendera Negara

@mark.fixture_penerimaan
def test_PNM_007_48():
	time.sleep(1)
	Log.info('input NoPolisi')
	if Golongan == 'KENDARAAN BERMOTOR':
		driver.find_element(By.ID, 'nomorPolisi').send_keys(NoPolisi)  # No. Polisi
	else:
		pass

@mark.fixture_penerimaan
def test_PNM_007_49():
	time.sleep(1)
	Log.info('input WarnaTNKB')
	if Golongan == 'KENDARAAN BERMOTOR':
		driver.find_element(By.ID, 'warnaTnkb').send_keys(WarnaTNKB)  # Warna TNKB
	else:
		pass

@mark.fixture_penerimaan
def test_PNM_007_50():
	time.sleep(1)
	Log.info('input MasaBerlakuTNK')
	if Golongan == 'KENDARAAN BERMOTOR':
		driver.find_element(By.ID, 'masaBerlakuTnkb').send_keys(MasaBerlakuTNK)  # Masa Berlaku TNKB
	else:
		pass

@mark.fixture_penerimaan
def test_PNM_007_51():
	time.sleep(1)
	Log.info('input BahanBakar')
	if Golongan == 'KENDARAAN BERMOTOR':
		driver.find_element(By.ID, 'bahanBakar').send_keys(BahanBakar)  # Bahan Bakar
	else:
		pass

@mark.fixture_penerimaan
def test_PNM_007_52():
	time.sleep(1)
	Log.info('input CiriKhusus')
	driver.find_element(By.ID, 'ciriKhusus').send_keys(CiriKhusus)  # Ciri Khusus

@mark.fixture_penerimaan
def test_PNM_007_53():
	time.sleep(1)
	Log.info('input HalLainnya')
	driver.find_element(By.ID, 'halLainnya').send_keys(HalLainnya)  # Hal Lainnya

@mark.fixture_penerimaan
def test_PNM_007_54():
	time.sleep(1)
	Log.info('input PemeliharaanKhusus')
	if (PemeliharaanKhusus == 'Iya' or PemeliharaanKhusus == 'iya'):
		driver.find_element(By.ID, 'PemeliharaanKhusus').click()
	elif (PemeliharaanKhusus == 'Tidak' or PemeliharaanKhusus == 'tidak'):
		pass

@mark.fixture_penerimaan
def test_PNM_007_55():
	time.sleep(1)
	Log.info('input catatanPemeliharaanKhusus')
	if (PemeliharaanKhusus == 'Iya' or PemeliharaanKhusus == 'iya'):
		driver.find_element(By.ID, 'catatanPemeliharaanKhusus').send_keys(CatatanPemeliharaanKhusus)  # Catatan Pemeliharaan Khusus
	elif (PemeliharaanKhusus == 'Tidak' or PemeliharaanKhusus == 'tidak'):
		pass

@mark.fixture_penerimaan
def test_PNM_007_56():
	time.sleep(1)
	Log.info('input RekomendasiTimPeneliti')
	driver.find_element(By.ID, 'rekomendasiTimPeneliti').send_keys(RekomendasiTimPeneliti)  # Rekomendasi Tim Peneliti

gmotor = wb['Golongankendaraanbermotor']
g = 3  # barisexel

KunciKontak			= gmotor['A'+str(g)].value
jmlhKunciKontak		= gmotor['B'+str(g)].value
konKunciKontak		= gmotor['C'+str(g)].value
RemoteKunci			= gmotor['D'+str(g)].value
jmlhRemoteKunci		= gmotor['E'+str(g)].value
konRemoteKunc		= gmotor['F'+str(g)].value
CentralLock			= gmotor['G'+str(g)].value
jmlhCentralLock		= gmotor['H'+str(g)].value
konCentralLoc		= gmotor['I'+str(g)].value
PowerWindow			= gmotor['J'+str(g)].value
jmlhPowerWindow		= gmotor['K'+str(g)].value
PowerWindo			= gmotor['L'+str(g)].value
Spion				= gmotor['M'+str(g)].value
jmlhSpion			= gmotor['N'+str(g)].value
konSpion			= gmotor['O'+str(g)].value
Wiper				= gmotor['P'+str(g)].value
jmlhWiper			= gmotor['Q'+str(g)].value
konWiper			= gmotor['R'+str(g)].value
LampuDepan			= gmotor['S'+str(g)].value
jmlhLampuDepan		= gmotor['T'+str(g)].value
konLampuDepan		= gmotor['U'+str(g)].value
SeinDepan			= gmotor['V'+str(g)].value
jmlhSeinDepan		= gmotor['W'+str(g)].value
konSeinDepan		= gmotor['X'+str(g)].value
LampuBelakang		= gmotor['Y'+str(g)].value
jmlhLampuBelakang	= gmotor['Z'+str(g)].value
konLampuBelakang	= gmotor['AA'+str(g)].value
SeinBelakang		= gmotor['AB'+str(g)].value
jmlhSeinBelakang	= gmotor['AC'+str(g)].value
konSeinBelakang		= gmotor['AD'+str(g)].value
LampuVariasi		= gmotor['AE'+str(g)].value
jmlhLampuVariasi	= gmotor['AF'+str(g)].value
konLampuVariasi		= gmotor['AG'+str(g)].value
PintuKanan			= gmotor['AH'+str(g)].value
jmlhPintuKanan		= gmotor['AI'+str(g)].value
konPintuKanan		= gmotor['AJ'+str(g)].value
PintuKiri			= gmotor['AK'+str(g)].value
jmlhPintuKiri		= gmotor['AL'+str(g)].value
konPintuKiri		= gmotor['AM'+str(g)].value
BodyBelakang		= gmotor['AN'+str(g)].value
jmlhBodyBelakang	= gmotor['AO'+str(g)].value
konBodyBelakang		= gmotor['AP'+str(g)].value
BumperDepan			= gmotor['AQ'+str(g)].value
jmlhBumperDepan		= gmotor['AR'+str(g)].value
konBumperDepan		= gmotor['AS'+str(g)].value
BumperBelakang		= gmotor['AT'+str(g)].value
jmlhBumperBelakang	= gmotor['AU'+str(g)].value
konBumperBelakang	= gmotor['AV'+str(g)].value
Accu				= gmotor['AW'+str(g)].value
jmlhAccu			= gmotor['AX'+str(g)].value
konAccu				= gmotor['AY'+str(g)].value
Speedometer			= gmotor['AZ'+str(g)].value
jmlhSpeedometer		= gmotor['BA'+str(g)].value
konSpeedometer		= gmotor['BB'+str(g)].value
Jok					= gmotor['BC'+str(g)].value
jmlhJok				= gmotor['BD'+str(g)].value
konJok				= gmotor['BE'+str(g)].value
AC					= gmotor['BF'+str(g)].value
jmlhAC				= gmotor['BG'+str(g)].value
konAC				= gmotor['BH'+str(g)].value
AudioSound			= gmotor['BI'+str(g)].value
jmlhAudioSound		= gmotor['BJ'+str(g)].value
konAudioSound		= gmotor['BK'+str(g)].value
KarpetBawah			= gmotor['BL'+str(g)].value
jmlhKarpetBawah		= gmotor['BM'+str(g)].value
konKarpetBawah		= gmotor['BN'+str(g)].value
VelgBanRodaDepan	= gmotor['BO'+str(g)].value
jmlhVelgBanRodaDepan		= gmotor['BP'+str(g)].value
konVelgBanRodaDepan			= gmotor['BQ'+str(g)].value
VelgBanRodaBelakang			= gmotor['BR'+str(g)].value
jmlhVelgBanRodaBelakang		= gmotor['BS'+str(g)].value
konVelgBanRodaBelakang		= gmotor['BT'+str(g)].value
BanSerep			= gmotor['BU'+str(g)].value
jmlhBanSerep		= gmotor['BV'+str(g)].value
konBanSerep			= gmotor['BW'+str(g)].value
Dongkrak			= gmotor['BX'+str(g)].value
jumlhDongkrak		= gmotor['BY'+str(g)].value
konDongkrak			= gmotor['BZ'+str(g)].value
KunciKunci			= gmotor['CA'+str(g)].value
jmlhKunciKunci		= gmotor['CB'+str(g)].value
konKunciKunci		= gmotor['CC'+str(g)].value
LogoTulisan			= gmotor['CD'+str(g)].value
jmlhLogoTulisan		= gmotor['CE'+str(g)].value
konLogoTulisan		= gmotor['CF'+str(g)].value
Mesin			= gmotor['CG'+str(g)].value
jmlhMesin		= gmotor['CH'+str(g)].value
konMesin		= gmotor['CI'+str(g)].value
STNK			= gmotor['CJ'+str(g)].value
jmlhSTNK		= gmotor['CK'+str(g)].value
konSTNK			= gmotor['CL'+str(g)].value


@mark.fixture_penerimaan
def test_PNM_007_35_1():
	time.sleep(1)
	if (Golongan == 'KENDARAAN BERMOTOR' or Golongan == 'ANGKUTAN (DARAT/LAUT/UDARA)'):
		if KunciKontak == 'Ada':
			driver.find_element(By.ID, 'ketersediaan10').click()
			driver.find_element(By.ID, 'jumlah10').send_keys(jmlhKunciKontak)
			driver.find_element(By.ID, 'kondisi10').send_keys(konKunciKontak)
		elif KunciKontak == 'Tidak':
			driver.find_element(By.ID, 'jumlah10').send_keys('-')
			driver.find_element(By.ID, 'kondisi10').send_keys('-')

		if RemoteKunci == 'Ada':
			driver.find_element(By.ID, 'ketersediaan11').click()
			driver.find_element(By.ID, 'jumlah11').send_keys(jmlhRemoteKunci)
			driver.find_element(By.ID, 'kondisi11').send_keys(konRemoteKunci)
		elif RemoteKunci == 'Tidak':
			driver.find_element(By.ID, 'jumlah11').send_keys('-')
			driver.find_element(By.ID, 'kondisi11').send_keys('-')

		if CentralLock == 'Ada':
			driver.find_element(By.ID, 'ketersediaan12').click()
			driver.find_element(By.ID, 'jumlah12').send_keys(jmlhCentralLock)
			driver.find_element(By.ID, 'kondisi12').send_keys(konCentralLock)
		elif CentralLock == 'Tidak':
			driver.find_element(By.ID, 'jumlah12').send_keys('-')
			driver.find_element(By.ID, 'kondisi12').send_keys('-')

		if PowerWindow == 'Ada':
			driver.find_element(By.ID, 'ketersediaan13').click()
			driver.find_element(By.ID, 'jumlah13').send_keys(jmlhPowerWindow)
			driver.find_element(By.ID, 'kondisi13').send_keys(konPowerWindow)
		elif PowerWindow == 'Tidak':
			driver.find_element(By.ID, 'jumlah13').send_keys('-')
			driver.find_element(By.ID, 'kondisi13').send_keys('-')

		if Spion == 'Ada':
			driver.find_element(By.ID, 'ketersediaan14').click()
			driver.find_element(By.ID, 'jumlah14').send_keys(jmlhSpion)
			driver.find_element(By.ID, 'kondisi14').send_keys(konSpion)
		elif Spion == 'Tidak':
			driver.find_element(By.ID, 'jumlah14').send_keys('-')
			driver.find_element(By.ID, 'kondisi14').send_keys('-')

		if Wiper == 'Ada':
			driver.find_element(By.ID, 'ketersediaan15').click()
			driver.find_element(By.ID, 'jumlah15').send_keys(jmlhWiper)
			driver.find_element(By.ID, 'kondisi15').send_keys(konWiper)
		elif Wiper == 'Tidak':
			driver.find_element(By.ID, 'jumlah15').send_keys('-')
			driver.find_element(By.ID, 'kondisi15').send_keys('-')

		if LampuDepan == 'Ada':
			driver.find_element(By.ID, 'ketersediaan16').click()
			driver.find_element(By.ID, 'jumlah16').send_keys(jmlhLampuDepan)
			driver.find_element(By.ID, 'kondisi16').send_keys(konLampuDepan)
		elif LampuDepan == 'Tidak':
			driver.find_element(By.ID, 'jumlah16').send_keys('-')
			driver.find_element(By.ID, 'kondisi16').send_keys('-')

		if SeinDepan == 'Ada':
			driver.find_element(By.ID, 'ketersediaan17').click()
			driver.find_element(By.ID, 'jumlah17').send_keys(jmlhSeinDepan)
			driver.find_element(By.ID, 'kondisi17').send_keys(konSeinDepan)
		elif SeinDepan == 'Tidak':
			driver.find_element(By.ID, 'jumlah17').send_keys('-')
			driver.find_element(By.ID, 'kondisi17').send_keys('-')

		if LampuBelakang == 'Ada':
			driver.find_element(By.ID, 'ketersediaan18').click()
			driver.find_element(By.ID, 'jumlah18').send_keys(jmlhLampuBelakang)
			driver.find_element(By.ID, 'kondisi18').send_keys(konLampuBelakang)
		elif LampuBelakang == 'Tidak':
			driver.find_element(By.ID, 'jumlah18').send_keys('-')
			driver.find_element(By.ID, 'kondisi18').send_keys('-')

		if SeinBelakang == 'Ada':
			driver.find_element(By.ID, 'ketersediaan19').click()
			driver.find_element(By.ID, 'jumlah19').send_keys(jmlhSeinBelakang)
			driver.find_element(By.ID, 'kondisi19').send_keys(konSeinBelakang)
		elif SeinBelakang == 'Tidak':
			driver.find_element(By.ID, 'jumlah19').send_keys('-')
			driver.find_element(By.ID, 'kondisi19').send_keys('-')

		if LampuVariasi == 'Ada':
			driver.find_element(By.ID, 'ketersediaan110').click()
			driver.find_element(By.ID, 'jumlah110').send_keys(jmlhLampuVariasi)
			driver.find_element(By.ID, 'kondisi110').send_keys(konLampuVariasi)
		elif LampuVariasi == 'Tidak':
			driver.find_element(By.ID, 'jumlah110').send_keys('-')
			driver.find_element(By.ID, 'kondisi110').send_keys('-')

		if PintuKanan == 'Ada':
			driver.find_element(By.ID, 'ketersediaan111').click()
			driver.find_element(By.ID, 'jumlah111').send_keys(jmlhPintuKanan)
			driver.find_element(By.ID, 'kondisi111').send_keys(konPintuKanan)
		elif PintuKanan == 'Tidak':
			driver.find_element(By.ID, 'jumlah111').send_keys('-')
			driver.find_element(By.ID, 'kondisi111').send_keys('-')

		if PintuKiri == 'Ada':
			driver.find_element(By.ID, 'ketersediaan112').click()
			driver.find_element(By.ID, 'jumlah112').send_keys(jmlhPintuKiri)
			driver.find_element(By.ID, 'kondisi112').send_keys(konPintuKiri)
		elif PintuKiri == 'Tidak':
			driver.find_element(By.ID, 'jumlah112').send_keys('-')
			driver.find_element(By.ID, 'kondisi112').send_keys('-')

		if BodyBelakang == 'Ada':
			driver.find_element(By.ID, 'ketersediaan113').click()
			driver.find_element(By.ID, 'jumlah113').send_keys(jmlhBodyBelakang)
			driver.find_element(By.ID, 'kondisi113').send_keys(konBodyBelakang)
		elif BodyBelakang == 'Tidak':
			driver.find_element(By.ID, 'jumlah113').send_keys('-')
			driver.find_element(By.ID, 'kondisi113').send_keys('-')

		if BumperDepan == 'Ada':
			driver.find_element(By.ID, 'ketersediaan114').click()
			driver.find_element(By.ID, 'jumlah114').send_keys(jmlhBumperDepan)
			driver.find_element(By.ID, 'kondisi114').send_keys(konBumperDepan)
		elif BumperDepan == 'Tidak':
			driver.find_element(By.ID, 'jumlah114').send_keys('-')
			driver.find_element(By.ID, 'kondisi114').send_keys('-')

		if BumperBelakang == 'Ada':
			driver.find_element(By.ID, 'ketersediaan20').click()
			driver.find_element(By.ID, 'jumlah20').send_keys(
				jmlhBumperBelakang)
			driver.find_element(By.ID, 'kondisi20').send_keys(
				konBumperBelakang)
		elif BumperBelakang == 'Tidak':
			driver.find_element(By.ID, 'jumlah20').send_keys('-')
			driver.find_element(By.ID, 'kondisi20').send_keys('-')

		if Accu == 'Ada':
			driver.find_element(By.ID, 'ketersediaan21').click()
			driver.find_element(By.ID, 'jumlah21').send_keys(jmlhAccu)
			driver.find_element(By.ID, 'kondisi21').send_keys(konAccu)
		elif Accu == 'Tidak':
			driver.find_element(By.ID, 'jumlah21').send_keys('-')
			driver.find_element(By.ID, 'kondisi21').send_keys('-')

		if Speedometer == 'Ada':
			driver.find_element(By.ID, 'ketersediaan22').click()
			driver.find_element(By.ID, 'jumlah22').send_keys(jmlhSpeedometer)
			driver.find_element(By.ID, 'kondisi22').send_keys(konSpeedometer)
		elif Speedometer == 'Tidak':
			driver.find_element(By.ID, 'jumlah22').send_keys('-')
			driver.find_element(By.ID, 'kondisi22').send_keys('-')

		if Jok == 'Ada':
			driver.find_element(By.ID, 'ketersediaan23').click()
			driver.find_element(By.ID, 'jumlah23').send_keys(jmlhJok)
			driver.find_element(By.ID, 'kondisi23').send_keys(konJok)
		elif Jok == 'Tidak':
			driver.find_element(By.ID, 'jumlah23').send_keys('-')
			driver.find_element(By.ID, 'kondisi23').send_keys('-')

		if AC == 'Ada':
			driver.find_element(By.ID, 'ketersediaan24').click()
			driver.find_element(By.ID, 'jumlah24').send_keys(jmlhAC)
			driver.find_element(By.ID, 'kondisi24').send_keys(konAC)
		elif AC == 'Tidak':
			driver.find_element(By.ID, 'jumlah24').send_keys('-')
			driver.find_element(By.ID, 'kondisi24').send_keys('-')

		if AudioSound == 'Ada':
			driver.find_element(By.ID, 'ketersediaan25').click()
			driver.find_element(By.ID, 'jumlah25').send_keys(jmlhAudioSound)
			driver.find_element(By.ID, 'kondisi25').send_keys(konAudioSound)
		elif AudioSound == 'Tidak':
			driver.find_element(By.ID, 'jumlah25').send_keys('-')
			driver.find_element(By.ID, 'kondisi25').send_keys('-')

		if KarpetBawah == 'Ada':
			driver.find_element(By.ID, 'ketersediaan26').click()
			driver.find_element(By.ID, 'jumlah26').send_keys(jmlhKarpetBawah)
			driver.find_element(By.ID, 'kondisi26').send_keys(konKarpetBawah)
		elif KarpetBawah == 'Tidak':
			driver.find_element(By.ID, 'jumlah26').send_keys('-')
			driver.find_element(By.ID, 'kondisi26').send_keys('-')

		if VelgBanRodaDepan == 'Ada':
			driver.find_element(By.ID, 'ketersediaan27').click()
			driver.find_element(By.ID, 'jumlah27').send_keys(
				jmlhVelgBanRodaDepan)
			driver.find_element(By.ID, 'kondisi27').send_keys(
				konVelgBanRodaDepan)
		elif VelgBanRodaDepan == 'Tidak':
			driver.find_element(By.ID, 'jumlah27').send_keys('-')
			driver.find_element(By.ID, 'kondisi27').send_keys('-')

		if VelgBanRodaBelakang == 'Ada':
			driver.find_element(By.ID, 'ketersediaan28').click()
			driver.find_element(By.ID, 'jumlah28').send_keys(
				jmlhVelgBanRodaBelakang)
			driver.find_element(By.ID, 'kondisi28').send_keys(
				konVelgBanRodaBelakang)
		elif VelgBanRodaBelakang == 'Tidak':
			driver.find_element(By.ID, 'jumlah28').send_keys('-')
			driver.find_element(By.ID, 'kondisi28').send_keys('-')

		if BanSerep == 'Ada':
			driver.find_element(By.ID, 'ketersediaan29').click()
			driver.find_element(By.ID, 'jumlah29').send_keys(jmlhBanSerep)
			driver.find_element(By.ID, 'kondisi29').send_keys(konBanSerep)
		elif BanSerep == 'Tidak':
			driver.find_element(By.ID, 'jumlah29').send_keys('-')
			driver.find_element(By.ID, 'kondisi29').send_keys('-')

		if Dongkrak == 'Ada':
			driver.find_element(By.ID, 'ketersediaan210').click()
			driver.find_element(By.ID, 'jumlah210').send_keys(jmlhDongkrak)
			driver.find_element(By.ID, 'kondisi210').send_keys(konDongkrak)
		elif Dongkrak == 'Tidak':
			driver.find_element(By.ID, 'jumlah210').send_keys('-')
			driver.find_element(By.ID, 'kondisi210').send_keys('-')

		if KunciKunci == 'Ada':
			driver.find_element(By.ID, 'ketersediaan211').click()
			driver.find_element(By.ID, 'jumlah211').send_keys(jmlhKunciKunci)
			driver.find_element(By.ID, 'kondisi211').send_keys(konKunciKunci)
		elif KunciKunci == 'Tidak':
			driver.find_element(By.ID, 'jumlah211').send_keys('-')
			driver.find_element(By.ID, 'kondisi211').send_keys('-')

		if LogoTulisan == 'Ada':
			driver.find_element(By.ID, 'ketersediaan212').click()
			driver.find_element(By.ID, 'jumlah212').send_keys(jmlhLogoTulisan)
			driver.find_element(By.ID, 'kondisi212').send_keys(konLogoTulisan)
		elif LogoTulisan == 'Tidak':
			driver.find_element(By.ID, 'jumlah212').send_keys('-')
			driver.find_element(By.ID, 'kondisi212').send_keys('-')

		if Mesin == 'Ada':
			driver.find_element(By.ID, 'ketersediaan213').click()
			driver.find_element(By.ID, 'jumlah213').send_keys(jmlhMesin)
			driver.find_element(By.ID, 'kondisi213').send_keys(konMesin)
		elif Mesin == 'Tidak':
			driver.find_element(By.ID, 'jumlah213').send_keys('-')
			driver.find_element(By.ID, 'kondisi213').send_keys('-')

		if STNK == 'Ada':
			driver.find_element(By.ID, 'ketersediaan214').click()
			driver.find_element(By.ID, 'jumlah214').send_keys(jmlhSTNK)
			driver.find_element(By.ID, 'kondisi214').send_keys(konSTNK)
		elif STNK == 'Tidak':
			driver.find_element(By.ID, 'jumlah214').send_keys('-')
			driver.find_element(By.ID, 'kondisi214').send_keys('-')
	else:
		pass

@mark.fixture_penerimaan
def test_PNM_007_57():
	time.sleep(1)
	Log.info('tambah jumlah peneliti')
	if jumlhpeneliti == 3:
		driver.find_element(By.ID, 'tambahPeneliti').click()
		driver.find_element(By.ID, 'tambahPeneliti').click()
	elif jumlhpeneliti == 2:
		driver.find_element(By.ID, 'tambahPeneliti').click()
	elif jumlhpeneliti == 1:
		pass


@mark.fixture_penerimaan
def test_PNM_007_58():
	time.sleep(1)
	Log.info('pencarian para prtugas peneliti')
	if jumlhpeneliti == 3:
		ptgs1 = driver.find_element(By.ID, 'cariPeneliti0')
		ptgs1.click()
		ptgs1.send_keys(Peneliti1)
		driver.find_element(By.ID, 'cariPeneliti00').click()

		ptgs2 = driver.find_element(By.ID, 'cariPeneliti1')
		ptgs2.click()
		ptgs2.send_keys(Peneliti2)
		driver.find_element(By.ID, 'cariPeneliti10').click()

		ptgs2 = driver.find_element(By.ID, 'cariPeneliti2')
		ptgs2.click()
		ptgs2.send_keys(Peneliti3)
		driver.find_element(By.ID, 'cariPeneliti20').click()

	elif jumlhpeneliti == 2:
		ptgs1 = driver.find_element(By.ID, 'cariPeneliti0')
		ptgs1.click()
		ptgs1.send_keys(Peneliti1)
		driver.find_element(By.ID, 'cariPeneliti00').click()

		ptgs2 = driver.find_element(By.ID, 'cariPeneliti1')
		ptgs2.click()
		ptgs2.send_keys(Peneliti2)
		driver.find_element(By.ID, 'cariPeneliti10').click()

	elif jumlhpeneliti == 1:
		ptgs1 = driver.find_element(By.ID, 'cariPeneliti0')
		ptgs1.click()
		ptgs1.send_keys(Peneliti1)
		driver.find_element(By.ID, 'cariPeneliti00').click()

# Penilaian ==============================================================
def test_PNM_007_59():
	time.sleep(1)
	hold(driver)
	Log.info('pindah tab')
	# WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.XPATH, pathData['Rupelemen']['+barang']['loadingbarang'])))
	driver.find_element(By.ID, 'tab-penilaian').click()


@mark.fixture_penerimaanx
def test_PNM_007_60():
	time.sleep(1)
	Log.info('input tglPenilaian')
	tglpenilai = driver.find_element(By.ID, 'tglPenilaian')  
	tglpenilai.send_keys(TglPenilaian)# Tanggal Penilaian
	tglpenilai.send_keys(Keys.ENTER)

@mark.fixture_penerimaan
def test_PNM_007_61():
	time.sleep(1)  # Nomor BA Penelitian
	Log.info('input NoBAPenelitian')
	driver.find_element(By.ID, 'noBaPenelitian').send_keys(NoBAPenelitian)

@mark.fixture_penerimaan
def test_PNM_007_62():
	time.sleep(1)  # Nilai Satuan Barang
	Log.info('input NilaiSatuanBarang')
	driver.find_element(By.ID, 'nilaiSatuan').send_keys(NilaiSatuanBarang)

@mark.fixture_penerimaan
def test_PNM_007_63():
	time.sleep(1)  # Keterangan
	Log.info('input Keterangan')
	driver.find_element(By.ID, 'keterangan').send_keys(Keterangan)

@mark.fixture_penerimaan
def test_PNM_007_67():
	time.sleep(1)
	Log.info('tambah jumlah petugas penilai')
	if jumlhpeneliti == 3:
		driver.find_element(By.ID, 'tambahPenilai').click()
		driver.find_element(By.ID, 'tambahPenilai').click()
	elif jumlhpeneliti == 2:
		driver.find_element(By.ID, 'tambahPenilai').click()
	elif jumlhpeneliti == 1:
		pass

@mark.fixture_penerimaan
def test_PNM_007_68():
	time.sleep(1)
	Log.info('pencarian prtugas penilai')
	if jumlhpenelilai == 3:
		penlai1 = driver.find_element(By.ID, 'cariPenilai0')
		penlai1.click()
		penlai1.send_keys(Penilai1)
		driver.find_element(By.ID, 'cariPenilai00').click()

		penlai2 = driver.find_element(By.ID, 'cariPenilai1')
		penlai2.click()
		penlai2.send_keys(Penilai2)
		driver.find_element(By.ID, 'cariPenilai10').click()

		penlai2 = driver.find_element(By.ID, 'cariPenilai2')
		penlai2.click()
		penlai2.send_keys(Penilai3)
		driver.find_element(By.ID, 'cariPenilai20').click()

	elif jumlhpenelilai == 2:
		penlai1 = driver.find_element(By.ID, 'cariPenilai0')
		penlai1.click()
		penlai1.send_keys(Penilai1)
		driver.find_element(By.ID, 'cariPenilai00').click()

		penlai2 = driver.find_element(By.ID, 'cariPenilai1')
		penlai2.click()
		penlai2.send_keys(Penilai2)
		driver.find_element(By.ID, 'cariPenilai10').click()

	elif jumlhpenelilai == 1:
		penlai1 = driver.find_element(By.ID, 'cariPenilai0')
		penlai1.click()
		penlai1.send_keys(Penilai1)
		driver.find_element(By.ID, 'cariPenilai00').click()

@mark.fixture_penerimaan
def test_PNM_007_69():# submit data tambah barang
	hold(driver)
	Log.info('submit data')
	driver.find_element(By.ID, 'submitButton').click()
	WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

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

@mark.fixture_penempatan
def test_PTN_003_0():
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By. ID, 'searchButton')))
	hold(driver)
	Log.info('membuka halaman tambah dengan menekan button tambah')
	driver.find_element(By. ID, 'createButton').click()
	attach(data=driver.get_screenshot_as_png())

PTN = wb['Penempatan']
u = 2

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
	nabar.send_keys(nama_barang)
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
	WebDriverWait(driver, 80).until(EC.presence_of_element_located((By.XPATH, pathData['Rupelemen']['+penempatan']['descgudang'])))
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
	# pillbar.send_keys(barisraklemari)
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
