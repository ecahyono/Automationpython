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

from Settings.setup import initDriver, loadDataPath, sleep
from Settings.login import login


Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Test_penerimaan_3_Tambahbarang.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("RUPEXEL"))

# init driver by os
@mark.fixture_penempatan
def test_Ossetup_1():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')

@mark.fixture_penempatan
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


sheetrange = wb['IndexPenerimaan']
i = 2
Carikolom       = sheetrange['A'+str(i)].value
Katkun          = sheetrange['B'+str(i)].value

@mark.fixture_penerimaan
def test_Pencariandata_4():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
	driver.find_element(By.ID, 'filterColumn').click()
	sleep(driver)
	if Carikolom == 'No Registrasi':
		driver.find_element(By. ID, 'no_reg').click()
	elif Carikolom == 'Tgl Penerimaan':
		driver.find_element(By. ID, 'tgl_penerimaan').click()
	elif Carikolom == 'Keterangan':
		driver.find_element(By. ID, 'keterangan').click()

	sleep(driver)
	if Carikolom == 'Tgl Penerimaan':
		kattgl = driver.find_element(By.XPATH, pathData['Rupelemen']['indexpenempatan']['kategoritanggal'])
		kattgl.click()
		kattgl.send_keys(Katkun)
	else:
		driver.find_element(By. ID, 'kataKunci').send_keys(Katkun)

	sleep(driver)

	driver.find_element(By.ID , 'searchButton').click()
	sleep(driver)
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))

	attach(data=driver.get_screenshot_as_png()) 
	Log.info('Melakukan Pencarian data berdasarkan kategori')

@mark.fixture_penerimaan
def test_Membukadetailbarang_5():
	sleep(driver)
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
	sleep(driver)
	driver.find_element(By. ID, 'daftarBarang0').click()
	attach(data=driver.get_screenshot_as_png()) 
	Log.info('Melakukan Pencarian data berdasarkan kategori')
	sleep(driver)

# #Kelengkapan Basan Baran ==============================================================
sheetrange1 = wb['Barangbasan']
inp = input('')
j = inp

nama_barang   = sheetrange1['A'+str(j)].value #Nama Barang
barang_temuan = sheetrange1['B'+str(j)].value #Barang Temuan
jenis_barang  = sheetrange1['C'+str(j)].value #Jenis Barang
satuan 		  = sheetrange1['D'+str(j)].value #Satuan
jumlah 		  = sheetrange1['E'+str(j)].value #Jumlah
jumlah_baik   = sheetrange1['F'+str(j)].value #Jumlah Baik
jumlah_rusak_ringan = sheetrange1['G'+str(j)].value #Jumlah Rusak Ringan
jumlah_rusak_berat  = sheetrange1['H'+str(j)].value #Jumlah Rusak Berat
Jumlahfoto          = sheetrange1['I'+str(j)].value #listjumlah foto barang
foto1  				= sheetrange1['J'+str(j)].value #Nama Foto 1
keteranfanfoto1     = sheetrange1['K'+str(j)].value #Keterangan1
foto2  				= sheetrange1['L'+str(j)].value #Nama Foto 2
keteranfanfoto2		= sheetrange1['M'+str(j)].value #Keterangan2
foto3 				= sheetrange1['N'+str(j)].value #Nama Foto 2
keteranfanfoto3 	= sheetrange1['O'+str(j)].value #Keterangan2

NomorPenelitian		= sheetrange1['P'+str(j)].value #Nomor Penelitian
tglPenelitian		= sheetrange1['Q'+str(j)].value #Tanggal Penelitian
NoskPenelitian		= sheetrange1['R'+str(j)].value #Nomor SK Peneliti
tglSkPeneliti		= sheetrange1['S'+str(j)].value #Tanggal SK Peneliti

Golongan 	= sheetrange1['T'+str(j)].value #Golongan
	
KeadaanSegelPenyita	= sheetrange1['U'+str(j)].value #Keadaan Segel Penyita
KondisiBarang 		= sheetrange1['v'+str(j)].value #Kondisi Barang
SubKondisiBarang  	= sheetrange1['W'+str(j)].value #Sub Kondisi Barang
Sifat				= sheetrange1['X'+str(j)].value #Sifat
MerekDanKondisi		= sheetrange1['Y'+str(j)].value #Merek Dan Kondisi
Berat				= sheetrange1['Z'+str(j)].value #Berat
VolumeCC			= sheetrange1['AA'+str(j)].value #Volume / CC
Panjang				= sheetrange1['AB'+str(j)].value #Panjang
Lebar				= sheetrange1['AC'+str(j)].value #Lebar
Tinggi				= sheetrange1['AD'+str(j)].value #Tinggi
Laras				= sheetrange1['AE'+str(j)].value #Laras
TipeMerek			= sheetrange1['AF'+str(j)].value #Tipe / Merek
PembuatPabrik		= sheetrange1['AG'+str(j)].value #Pembuat Pabrik
NomorPabrik			= sheetrange1['AH'+str(j)].value #Nomor Pabrik
Peluru				= sheetrange1['AI'+str(j)].value #Peluru
BahanPeledak		= sheetrange1['AJ'+str(j)].value #Bahan Peledak
SenpiDikeuarkanOleh		= sheetrange1['AK'+str(j)].value #Senpi Dikeuarkan Oleh
TglKeluar				= sheetrange1['AL'+str(j)].value #Tanggal Keluar
NomorDikeluarkan		= sheetrange1['AM'+str(j)].value #Nomor Dikeluarkan
TanggalBerlaku			= sheetrange1['AN'+str(j)].value #Tanggal Berlaku
NomorSenpi			    = sheetrange1['AO'+str(j)].value #Nomor Senpi
KomposisiBahan			= sheetrange1['AP'+str(j)].value #Komposisi Bahan
Kaliber	        = sheetrange1['AQ'+str(j)].value #Kaliber
Warna	        = sheetrange1['AR'+str(j)].value #Warna
NomorMesin	    = sheetrange1['AS'+str(j)].value #Nomor Mesin
TahunPembuatan	            = sheetrange1['AT'+str(j)].value #Tahun Pembuatan
TahunPengeluaranpenerbitan	= sheetrange1['AU'+str(j)].value #Tahun Pengeluaran / Penerbitan
NomorChasis                 = sheetrange1['AV'+str(j)].value #Nomor Chasis
TeganganDaya                = sheetrange1['AW'+str(j)].value #Tegangan Daya
MerekSumberDaya             = sheetrange1['AX'+str(j)].value #Merek Sumber Daya
Pegangan                    = sheetrange1['AY'+str(j)].value #Pegangan
TulisanHurufGambar        	= sheetrange1['AZ'+str(j)].value #Tulisan Huruf Gambar
AsalBasanDari	= sheetrange1['BA'+str(j)].value #Asal Basan Dari
PerkiraanUsia	= sheetrange1['BB'+str(j)].value #Perkiraan Usia
KadarKarat		= sheetrange1['BC'+str(j)].value #Kadar Karat
Kemasan			= sheetrange1['BD'+str(j)].value #Kemasan
Batasan			= sheetrange1['BE'+str(j)].value #Batasan
NoIMB			= sheetrange1['BF'+str(j)].value #No. IMB
IsiGedung		= sheetrange1['BG'+str(j)].value #Isi Gedung
SuratBukti		= sheetrange1['BH'+str(j)].value #Surat Bukti
BenderaNegara	= sheetrange1['BI'+str(j)].value #Bendera Negara
NoPolisi		= sheetrange1['BJ'+str(j)].value #No. Polisi
WarnaTNKB		= sheetrange1['BK'+str(j)].value #Warna TNKB
MasaBerlakuTNK	= sheetrange1['BL'+str(j)].value #Masa Berlaku TNKB
BahanBakar		= sheetrange1['BM'+str(j)].value #Bahan Bakar
CiriKhusus		= sheetrange1['BN'+str(j)].value #Ciri Khusus
HalLainnya		= sheetrange1['BO'+str(j)].value #Hal Lainnya
PemeliharaanKhusus			= sheetrange1['BP'+str(j)].value #Pemeliharaan Khusus
CatatanPemeliharaanKhusus	= sheetrange1['BQ'+str(j)].value #Catatan Pemeliharaan Khusus
RekomendasiTimPeneliti		= sheetrange1['BR'+str(j)].value #Rekomendasi Tim Peneliti

jumlhpeneliti	= sheetrange1['BS'+str(j)].value #Menentukan Jumlah Petugas Peneliti
Peneliti1		= sheetrange1['BT'+str(j)].value #Petugas1
Peneliti2		= sheetrange1['BU'+str(j)].value #Petugas2
Peneliti3		= sheetrange1['BV'+str(j)].value #Petugas3

TglPenilaian		= sheetrange1['BW'+str(j)].value #Tanggal Penilaian
NoBAPenelitian		= sheetrange1['BX'+str(j)].value #Nomor BA Penelitian
NilaiSatuanBarang	= sheetrange1['BY'+str(j)].value #Nilai Satuan Barang
Keterangan			= sheetrange1['BZ'+str(j)].value #Keterangan

jumlhpenelilai	= sheetrange1['CA'+str(j)].value #Menentukan Jumlah Petugas Peneliti
Penilai1		= sheetrange1['CB'+str(j)].value #Petugas1
Penilai2		= sheetrange1['CC'+str(j)].value #Petugas2
Penilai3		= sheetrange1['CD'+str(j)].value #Petugas3

# # #Kelengkapan Basan Baran ==============================================================
@mark.fixture_penerimaan
def test_tab_1():
	driver.find_element(By.ID, 'tab-kelengkapanBasanBaran').click()
	attach(data=driver.get_screenshot_as_png()) 
	Log.info('Melakukan Pencarian data berdasarkan kategori')

@mark.fixture_penerimaan
def test_input_1():
	WebDriverWait(driver, 50).until(EC.invisibility_of_element_located((By.XPATH, pathData['Rupelemen']['+barang']['loadingbarang'])))	
	nabar = driver.find_element(By.ID, 'nama_barang').send_keys(nama_barang) #Nama Barang
	sleep(driver)

@mark.fixture_penerimaan
def test_checkbox_1():	
	if barang_temuan == 'Iya':
		driver.find_element(By.ID, 'barang_temuan').click()
	elif barang_temuan == 'Tidak':
		print('')

@mark.fixture_penerimaan
def test_Dropdown_1():
	driver.find_element(By.ID, 'input_jenis_baran_basan').click() 
	sleep(driver)
	if jenis_barang == 'Umum Terbuka':
		driver.find_element(By.ID, 'JSB1').click()
	elif jenis_barang == 'Umum Tertutup':
		driver.find_element(By.ID, 'JSB2').click()
	elif jenis_barang == 'Berharga':
		driver.find_element(By.ID, 'JSB3').click()
	elif jenis_barang == 'Berharga':
		driver.find_element(By.ID, 'JSB4').click()
	elif jenis_barang == 'Hewan dan Tumbuhan':
		driver.find_element(By.ID, 'JSB5').click()
	sleep(driver)

@mark.fixture_penerimaan
def test_Dropdown_2():
	driver.find_element(By.ID, 'input_satuan_baran_basan').click()
	sleep(driver)
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
	elif satuan == 'Ekor':
		driver.find_element(By.ID, '10').click()
	elif satuan == 'Lain - Lain':
		driver.find_element(By.ID, 'SATUAN LAIN').click()

@mark.fixture_penerimaan
def test_input_2():
	driver.find_element(By.ID, 'jumlah').send_keys(jumlah) #jumlah
	sleep(driver)

@mark.fixture_penerimaan
def test_input_3():
	driver.find_element(By.ID, 'jumlah_baik').send_keys(jumlah_baik) #jumlah_baik
	sleep(driver)

@mark.fixture_penerimaan
def test_input_4():
	driver.find_element(By.ID, 'jumlah_rusak_ringan').send_keys(jumlah_rusak_ringan) #jumlah rusak ringan
	sleep(driver)

@mark.fixture_penerimaan
def test_input_5():
	driver.find_element(By.ID, 'jumlah_rusak_berat').send_keys(jumlah_rusak_berat) #jumlah Rusak Berat
	sleep(driver)

@mark.fixture_penerimaan
def test_jumlahfoto():
	if Jumlahfoto == 3:
		sleep(driver)
		driver.find_element(By.ID,'tambah_foto').click()
		driver.find_element(By.ID,'tambah_foto').click()
	elif Jumlahfoto == 2:
		driver.find_element(By.ID,'tambah_foto').click()
		sleep(driver)
	elif Jumlahfoto == 1:
		pass

@mark.fixture_penerimaan
def test_uploadfoto_1():
	driver.find_element(By.ID, 'pilihFoto0').click()
	sleep(driver)
	pyautogui.write(environ.get(r"FOTBRG1"))
	pyautogui.press('enter')
	# sleep(driver)
	# driver.find_element(By.ID,'namaFoto0').send_keys(foto1)
	sleep(driver)
	driver.find_element(By.ID,'keterangann0').send_keys(keteranfanfoto1)
	sleep(driver)

@mark.fixture_penerimaan
def test_uploadfoto_2():
	driver.find_element(By.ID, 'pilihFoto1').click()
	sleep(driver)
	pyautogui.write(environ.get(r"FOTBRG1"))
	pyautogui.press('enter')
	# sleep(driver)
	# driver.find_element(By.ID,'namaFoto1').send_keys(foto2)
	driver.find_element(By.ID,'keterangann1').send_keys(keteranfanfoto2)
	sleep(driver)

@mark.fixture_penerimaan
def test_uploadfoto_3():
	driver.find_element(By.ID, 'pilihFoto2').click()
	sleep(driver)
	pyautogui.write(environ.get(r"FOTBRG1"))
	pyautogui.press('enter')
	# sleep(driver)
	# driver.find_element(By.ID,'namaFoto2').send_keys(foto3)
	driver.find_element(By.ID,'keterangann2').send_keys(keteranfanfoto3)
	sleep(driver)

# Penelitian ==============================================================
def test_tab_2():
	# WebDriverWait(driver, 50).until(EC.invisibility_of_element_located((By.XPATH, pathData['Rupelemen']['+barang']['loadingbarang'])))
	driver.find_element(By.ID, 'tab-penelitian').click()

@mark.fixture_penerimaan
def test_input_6():
	sleep(driver)
	noPenelitian = driver.find_element(By.ID, 'noPenelitian').send_keys(NomorPenelitian)#Nomor Penelitian

@mark.fixture_penerimaan
def test_date_1(): 
	sleep(driver)
	penelititgl = driver.find_element(By.ID, 'tglPenelitian')
	penelititgl.click()
	penelititgl.send_keys(tglPenelitian)
	penelititgl.send_keys(Keys.ENTER)#Tanggal Penelitian

@mark.fixture_penerimaan
def test_input_7(): 
	sleep(driver)
	driver.find_element(By.ID, 'noSkPeneliti').send_keys(NoskPenelitian)#Nomor SK Penelitian

@mark.fixture_penerimaan
def test_date_2(): 
	sleep(driver)
	skpenelititgl = driver.find_element(By.ID, 'tglSkPeneliti')
	skpenelititgl.click
	skpenelititgl.send_keys(tglSkPeneliti)
	skpenelititgl.send_keys(Keys.ENTER) #Tanggal SK Penelitian

@mark.fixture_penerimaan
def test_Dropdown_3(): #Memilih Golongan
	driver.find_element(By.ID, 'golongan').click()
	sleep(driver)
	if Golongan == 'KENDARAAN BERMOTOR':
		driver.find_element(By.ID, '021').click()
	elif Golongan == 'SENJATA API (SENPI)':
		driver.find_element(By.ID, '020').click()
	elif Golongan == 'ELEKTRONIK':
		driver.find_element(By.ID, '001').click()
	elif Golongan == 'HEWAN TERNAK':
		driver.find_element(By.ID, '030').click()
	sleep(driver)

@mark.fixture_penerimaan
def test_input_8(): #Keadaan Segel Penyita
	sleep(driver)
	driver.find_element(By.ID, 'keadaanSegel').send_keys(KeadaanSegelPenyita)

@mark.fixture_penerimaan
def test_Dropdown_4(): #Kondisi Barang
	driver.find_element(By.ID, 'kondisiBarang').click()
	sleep(driver)
	if KondisiBarang == 'Baik':
		driver.find_element(By.ID, 'KBB1').click()
	elif KondisiBarang == 'Rusak':
		driver.find_element(By.ID, 'KBB2').click()

@mark.fixture_penerimaan	
def test_Dropdown_5(): #Sub Kondisi Barang
	if KondisiBarang == 'Rusak':
		driver.find_element(By.ID,'subKondisiBarang').click()
		sleep(driver)
		if SubKondisiBarang == 'Rusak Ringan':
			driver.find_element(By.ID, 'SKB1').click()
		elif SubKondisiBarang == 'Rusak Berat':
			driver.find_element(By.ID, 'SKB2').click()
	elif KondisiBarang == 'Baik':
		pass

@mark.fixture_penerimaan
def test_input_9(): #Sifat
	sleep(driver)
	driver.find_element(By.ID, 'sifat').send_keys(Sifat)

@mark.fixture_penerimaan
def test_input_10(): #Merek Dan Kondisi
	sleep(driver)
	driver.find_element(By.ID, 'merekKondisi').send_keys(MerekDanKondisi)

@mark.fixture_penerimaan
def test_input_11(): 
	sleep(driver)
	driver.find_element(By.ID, 'berat').send_keys(Berat) #Berat

@mark.fixture_penerimaan
def test_input_12(): 
	sleep(driver)
	driver.find_element(By.ID, 'volumeCc').send_keys(VolumeCC) #Volume / CC

@mark.fixture_penerimaan
def test_input_13(): 
	sleep(driver)
	driver.find_element(By.ID, 'panjang').send_keys(Panjang) #Panjang

@mark.fixture_penerimaan
def test_input_14(): 
	sleep(driver)
	driver.find_element(By.ID, 'lebar').send_keys(Lebar) #Lebar

@mark.fixture_penerimaan
def test_input_15(): 
	sleep(driver)
	driver.find_element(By.ID, 'tinggi').send_keys(Tinggi) #Tinggi

@mark.fixture_penerimaan
def test_input_16(): 
	sleep(driver)
	driver.find_element(By.ID, 'tipeMerek').send_keys(TipeMerek) #Tipe / Merek

@mark.fixture_penerimaan
def test_input_37(): 
	sleep(driver)
	if Golongan == 'SENJATA API (SENPI)':
		driver.find_element(By.ID, 'laras').send_keys(Laras) #Laras
		driver.find_element(By.ID, 'pembuatPabrik').send_keys(PembuatPabrik) #Pembuat Pabrik
		driver.find_element(By.ID, 'nomorPabrik').send_keys(NomorPabrik) #Nomor Pabrik
		driver.find_element(By.ID, 'peluru').send_keys(Peluru) #Peluru
		driver.find_element(By.ID, 'pasDikeluarkanOleh').send_keys(SenpiDikeuarkanOleh) #Senpi Dikeuarkan Oleh
		tglexit = driver.find_element(By.ID, 'tglKeluar')
		tglexit.send_keys(TglKeluar) #Tanggal Keluar
		tglexit.send_keys(Keys.ENTER)
		driver.find_element(By.ID, 'nmr_dikeluarkan').send_keys(NomorDikeluarkan) #Nomor Dikeluarkan
		tglberlksenpi = driver.find_element(By.ID, 'tglBerlakuPasSenpi')
		tglberlksenpi.send_keys(TanggalBerlaku) #Tanggal Berlaku
		tglberlksenpi.send_keys(Keys.ENTER)
		driver.find_element(By.ID, 'nmrSenpi').send_keys(NomorSenpi) #Nomor Senpi
		driver.find_element(By.ID, 'komposisiBahan').send_keys(KomposisiBahan) #Komposisi Bahan
		driver.find_element(By.ID, 'kaliber').send_keys(Kaliber) #Kaliber
	else :
		pass

@mark.fixture_penerimaan
def test_input_38(): 
	sleep(driver)
	if Golongan == 'ELEKTRONIK':
		driver.find_element(By.ID, 'pembuatPabrik').send_keys(PembuatPabrik) #Pembuat Pabrik
		driver.find_element(By.ID, 'nomorPabrik').send_keys(NomorPabrik) #Nomor Pabrik
		tglexit = driver.find_element(By.ID, 'tglKeluar')
		tglexit.send_keys(TglKeluar) #Tanggal Keluar
		tglexit.send_keys(Keys.ENTER)
		driver.find_element(By.ID, 'nmr_dikeluarkan').send_keys(NomorDikeluarkan) #Nomor Dikeluarkan
		tglberlksenpi = driver.find_element(By.ID, 'tglBerlakuPasSenpi')
		tglberlksenpi.send_keys(TanggalBerlaku) #Tanggal Berlaku
		tglberlksenpi.send_keys(Keys.ENTER)
		# driver.find_element(By.ID, 'nmrSenpi').send_keys(NomorSenpi) #Nomor Senpi
	else :
		pass

@mark.fixture_penerimaanx
def test_date_3(): 
	sleep(driver)
	thnpembuatan = driver.find_element(By.ID, 'tahunPembuatan')
	thnpembuatan.send_keys(TahunPembuatan) #Tahun Pembuatan
	thnpembuatan.send_keys(Keys.ENTER)

@mark.fixture_penerimaanx
def test_date_4(): 
	sleep(driver)
	thnpengeluaran = driver.find_element(By.ID, 'tahunPengeluaranPenerbitan')
	thnpengeluaran.send_keys(TahunPengeluaranpenerbitan) #Tahun Pengeluaran / Penerbitan
	thnpengeluaran.send_keys(Keys.ENTER)

@mark.fixture_penerimaan
def test_input_17(): 
	sleep(driver)
	driver.find_element(By.ID, 'warna').send_keys(Warna) #Warna

@mark.fixture_penerimaan
def test_input_18(): 
	sleep(driver)
	if Golongan == 'KENDARAAN BERMOTOR':
		driver.find_element(By.ID, 'nmrMesin').send_keys(NomorMesin) #Nomor Mesin
	else:
		pass

@mark.fixture_penerimaan
def test_input_19(): 
	sleep(driver)
	if Golongan == 'KENDARAAN BERMOTOR':
		driver.find_element(By.ID, 'nmrChasis').send_keys(NomorChasis) #Nomor Chasis
	else:
		pass

@mark.fixture_penerimaan
def test_input_20(): 
	sleep(driver)
	if Golongan == 'KENDARAAN BERMOTOR':
		driver.find_element(By.ID, 'teganganDaya').send_keys(TeganganDaya) #Tegangan Daya
	else:
		pass

@mark.fixture_penerimaan
def test_input_21(): 
	sleep(driver)
	if Golongan == 'KENDARAAN BERMOTOR':
		driver.find_element(By.ID, 'merekSumberDaya').send_keys(MerekSumberDaya) #Merek Sumber Daya
	else:
		pass

@mark.fixture_penerimaan
def test_input_22(): 
	sleep(driver)
	driver.find_element(By.ID, 'asalDari').send_keys(AsalBasanDari) #Asal Basan Dari

@mark.fixture_penerimaan
def test_input_23(): 
	sleep(driver)
	driver.find_element(By.ID, 'perkiraanUsia').send_keys(PerkiraanUsia) #Perkiraan Usia

@mark.fixture_penerimaan
def test_input_24(): 
	sleep(driver)
	driver.find_element(By.ID, 'batasan').send_keys(Batasan) #Batasan

@mark.fixture_penerimaan
def test_input_25(): 
	sleep(driver)
	driver.find_element(By.ID, 'NoImb').send_keys(NoIMB) #No. IMB

@mark.fixture_penerimaan
def test_input_26(): 
	sleep(driver)
	driver.find_element(By.ID, 'isiGedung').send_keys(IsiGedung) #Isi Gedung

@mark.fixture_penerimaan
def test_input_27(): 
	sleep(driver)
	driver.find_element(By.ID, 'suratBukti').send_keys(SuratBukti) #Surat Bukti

@mark.fixture_penerimaan
def test_input_28(): 
	sleep(driver)
	driver.find_element(By.ID, 'bendera').send_keys(BenderaNegara) #Bendera Negara
	
@mark.fixture_penerimaan
def test_input_29(): 
	sleep(driver)
	if Golongan == 'KENDARAAN BERMOTOR':
		driver.find_element(By.ID, 'nomorPolisi').send_keys(NoPolisi) #No. Polisi
	else:
		pass

@mark.fixture_penerimaan
def test_input_30(): 
	sleep(driver)
	if Golongan == 'KENDARAAN BERMOTOR':
		driver.find_element(By.ID, 'warnaTnkb').send_keys(WarnaTNKB) #Warna TNKB
	else:
		pass

@mark.fixture_penerimaan
def test_input_31(): 
	sleep(driver)
	if Golongan == 'KENDARAAN BERMOTOR':
		driver.find_element(By.ID, 'masaBerlakuTnkb').send_keys(MasaBerlakuTNK) #Masa Berlaku TNKB
	else:
		pass

@mark.fixture_penerimaan
def test_input_32(): 
	sleep(driver)
	if Golongan == 'KENDARAAN BERMOTOR':
		driver.find_element(By.ID, 'bahanBakar').send_keys(BahanBakar) #Bahan Bakar
	else:
		pass

@mark.fixture_penerimaan
def test_input_33(): 
	sleep(driver)
	driver.find_element(By.ID, 'ciriKhusus').send_keys(CiriKhusus) #Ciri Khusus

@mark.fixture_penerimaan
def test_input_34(): 
	sleep(driver)
	driver.find_element(By.ID, 'halLainnya').send_keys(HalLainnya) #Hal Lainnya
	
@mark.fixture_penerimaan
def test_checkbox_2(): 
	sleep(driver)
	if PemeliharaanKhusus == 'Iya':
		driver.find_element(By.ID, 'PemeliharaanKhusus').click()
	elif PemeliharaanKhusus == 'Tidak':
		pass	

@mark.fixture_penerimaan
def test_inputarea_1(): 
	sleep(driver)
	if PemeliharaanKhusus == 'Iya':
		driver.find_element(By.ID, 'catatanPemeliharaanKhusus').send_keys(CatatanPemeliharaanKhusus) #Catatan Pemeliharaan Khusus
	elif PemeliharaanKhusus == 'Tidak':
		pass

@mark.fixture_penerimaan
def test_inputarea_2(): 
	sleep(driver)
	driver.find_element(By.ID, 'rekomendasiTimPeneliti').send_keys(RekomendasiTimPeneliti) #Rekomendasi Tim Peneliti

sheetrange2 = wb['Golongankendaraanbermotor']
k = 3

KunciKontak         	= sheetrange2['A'+str(k)].value
jmlhKunciKontak     	= sheetrange2['B'+str(k)].value
konKunciKontak			= sheetrange2['C'+str(k)].value
RemoteKunci         	= sheetrange2['D'+str(k)].value
jmlhRemoteKunci     	= sheetrange2['E'+str(k)].value
konRemoteKunc			= sheetrange2['F'+str(k)].value
CentralLock         	= sheetrange2['G'+str(k)].value
jmlhCentralLock     	= sheetrange2['H'+str(k)].value
konCentralLoc			= sheetrange2['I'+str(k)].value
PowerWindow         	= sheetrange2['J'+str(k)].value
jmlhPowerWindow     	= sheetrange2['K'+str(k)].value
PowerWindo				= sheetrange2['L'+str(k)].value
Spion           		= sheetrange2['M'+str(k)].value
jmlhSpion           	= sheetrange2['N'+str(k)].value
konSpion				= sheetrange2['O'+str(k)].value
Wiper               	= sheetrange2['P'+str(k)].value
jmlhWiper         		= sheetrange2['Q'+str(k)].value
konWiper				= sheetrange2['R'+str(k)].value
LampuDepan          	= sheetrange2['S'+str(k)].value
jmlhLampuDepan      	= sheetrange2['T'+str(k)].value
konLampuDepan			= sheetrange2['U'+str(k)].value
SeinDepan           	= sheetrange2['V'+str(k)].value
jmlhSeinDepan       	= sheetrange2['W'+str(k)].value
konSeinDepan			= sheetrange2['X'+str(k)].value
LampuBelakang       	= sheetrange2['Y'+str(k)].value
jmlhLampuBelakang   	= sheetrange2['Z'+str(k)].value
konLampuBelakang		= sheetrange2['AA'+str(k)].value
SeinBelakang        	= sheetrange2['AB'+str(k)].value
jmlhSeinBelakang  		= sheetrange2['AC'+str(k)].value
konSeinBelakang			= sheetrange2['AD'+str(k)].value
LampuVariasi        	= sheetrange2['AE'+str(k)].value
jmlhLampuVariasi 		= sheetrange2['AF'+str(k)].value
konLampuVariasi			= sheetrange2['AG'+str(k)].value
PintuKanan	        	= sheetrange2['AH'+str(k)].value
jmlhPintuKanan	    	= sheetrange2['AI'+str(k)].value
konPintuKanan			= sheetrange2['AJ'+str(k)].value
PintuKiri	       		= sheetrange2['AK'+str(k)].value
jmlhPintuKiri	   		= sheetrange2['AL'+str(k)].value
konPintuKiri			= sheetrange2['AM'+str(k)].value
BodyBelakang	    	= sheetrange2['AN'+str(k)].value
jmlhBodyBelakang		= sheetrange2['AO'+str(k)].value
konBodyBelakang			= sheetrange2['AP'+str(k)].value
BumperDepan	      		= sheetrange2['AQ'+str(k)].value
jmlhBumperDepan	  		= sheetrange2['AR'+str(k)].value
konBumperDepan			= sheetrange2['AS'+str(k)].value
BumperBelakang	    	= sheetrange2['AT'+str(k)].value
jmlhBumperBelakang		= sheetrange2['AU'+str(k)].value
konBumperBelakang		= sheetrange2['AV'+str(k)].value
Accu	    			= sheetrange2['AW'+str(k)].value
jmlhAccu	     		= sheetrange2['AX'+str(k)].value
konAccu					= sheetrange2['AY'+str(k)].value
Speedometer	      		= sheetrange2['AZ'+str(k)].value
jmlhSpeedometer	   		= sheetrange2['BA'+str(k)].value
konSpeedometer			= sheetrange2['BB'+str(k)].value
Jok	         			= sheetrange2['BC'+str(k)].value
jmlhJok	          		= sheetrange2['BD'+str(k)].value
konJok					= sheetrange2['BE'+str(k)].value
AC	         			= sheetrange2['BF'+str(k)].value
jmlhAC	      			= sheetrange2['BG'+str(k)].value
konAC					= sheetrange2['BH'+str(k)].value
AudioSound	       		= sheetrange2['BI'+str(k)].value
jmlhAudioSound	   		= sheetrange2['BJ'+str(k)].value
konAudioSound			= sheetrange2['BK'+str(k)].value
KarpetBawah	    		= sheetrange2['BL'+str(k)].value
jmlhKarpetBawah	 		= sheetrange2['BM'+str(k)].value
konKarpetBawah			= sheetrange2['BN'+str(k)].value
VelgBanRodaDepan   		= sheetrange2['BO'+str(k)].value
jmlhVelgBanRodaDepan	= sheetrange2['BP'+str(k)].value
konVelgBanRodaDepan		= sheetrange2['BQ'+str(k)].value
VelgBanRodaBelakang	   	= sheetrange2['BR'+str(k)].value
jmlhVelgBanRodaBelakang	= sheetrange2['BS'+str(k)].value
konVelgBanRodaBelakang	= sheetrange2['BT'+str(k)].value
BanSerep	           	= sheetrange2['BU'+str(k)].value
jmlhBanSerep	       	= sheetrange2['BV'+str(k)].value
konBanSerep				= sheetrange2['BW'+str(k)].value
Dongkrak	           	= sheetrange2['BX'+str(k)].value
jumlhDongkrak	       	= sheetrange2['BY'+str(k)].value
konDongkrak				= sheetrange2['BZ'+str(k)].value
KunciKunci	           	= sheetrange2['CA'+str(k)].value
jmlhKunciKunci	       	= sheetrange2['CB'+str(k)].value
konKunciKunci			= sheetrange2['CC'+str(k)].value
LogoTulisan	           	= sheetrange2['CD'+str(k)].value
jmlhLogoTulisan	       	= sheetrange2['CE'+str(k)].value
konLogoTulisan			= sheetrange2['CF'+str(k)].value
Mesin	          	   	= sheetrange2['CG'+str(k)].value
jmlhMesin	       	   	= sheetrange2['CH'+str(k)].value
konMesin				= sheetrange2['CI'+str(k)].value
STNK          		   	= sheetrange2['CJ'+str(k)].value
jmlhSTNK          	   	= sheetrange2['CK'+str(k)].value
konSTNK					= sheetrange2['CL'+str(k)].value

@mark.fixture_penerimaan
def test_submitdataKendaraan():
	sleep(driver)
	if Golongan == 'KENDARAAN BERMOTOR':
		if KunciKontak == 'Ada':
			driver.find_element(By.ID,'ketersediaan10').click()
			driver.find_element(By.ID,'jumlah10').send_keys(jmlhKunciKontak)
			driver.find_element(By.ID,'kondisi10').send_keys(konKunciKontak)
		elif KunciKontak == 'Tidak':
			driver.find_element(By.ID,'jumlah10').send_keys('-')
			driver.find_element(By.ID,'kondisi10').send_keys('-')

		if RemoteKunci == 'Ada':
			driver.find_element(By.ID,'ketersediaan11').click()
			driver.find_element(By.ID,'jumlah11').send_keys(jmlhRemoteKunci)
			driver.find_element(By.ID,'kondisi11').send_keys(konRemoteKunci)
		elif RemoteKunci == 'Tidak':
			driver.find_element(By.ID,'jumlah11').send_keys('-')
			driver.find_element(By.ID,'kondisi11').send_keys('-')

		if CentralLock == 'Ada':
			driver.find_element(By.ID,'ketersediaan12').click()
			driver.find_element(By.ID,'jumlah12').send_keys(jmlhCentralLock)
			driver.find_element(By.ID,'kondisi12').send_keys(konCentralLock)
		elif CentralLock == 'Tidak':
			driver.find_element(By.ID,'jumlah12').send_keys('-')
			driver.find_element(By.ID,'kondisi12').send_keys('-')

		if PowerWindow == 'Ada':
			driver.find_element(By.ID,'ketersediaan13').click()
			driver.find_element(By.ID,'jumlah13').send_keys(jmlhPowerWindow)
			driver.find_element(By.ID,'kondisi13').send_keys(konPowerWindow)
		elif PowerWindow == 'Tidak':
			driver.find_element(By.ID,'jumlah13').send_keys('-')
			driver.find_element(By.ID,'kondisi13').send_keys('-')

		if Spion == 'Ada':
			driver.find_element(By.ID,'ketersediaan14').click()
			driver.find_element(By.ID,'jumlah14').send_keys(jmlhSpion)
			driver.find_element(By.ID,'kondisi14').send_keys(konSpion)
		elif Spion == 'Tidak':
			driver.find_element(By.ID,'jumlah14').send_keys('-')
			driver.find_element(By.ID,'kondisi14').send_keys('-')

		if Wiper == 'Ada':
			driver.find_element(By.ID,'ketersediaan15').click()
			driver.find_element(By.ID,'jumlah15').send_keys(jmlhWiper)
			driver.find_element(By.ID,'kondisi15').send_keys(konWiper)
		elif Wiper == 'Tidak':
			driver.find_element(By.ID,'jumlah15').send_keys('-')
			driver.find_element(By.ID,'kondisi15').send_keys('-')

		if LampuDepan == 'Ada':
			driver.find_element(By.ID,'ketersediaan16').click()
			driver.find_element(By.ID,'jumlah16').send_keys(jmlhLampuDepan)
			driver.find_element(By.ID,'kondisi16').send_keys(konLampuDepan)
		elif LampuDepan == 'Tidak':
			driver.find_element(By.ID,'jumlah16').send_keys('-')
			driver.find_element(By.ID,'kondisi16').send_keys('-')

		if SeinDepan == 'Ada':
			driver.find_element(By.ID,'ketersediaan17').click()
			driver.find_element(By.ID,'jumlah17').send_keys(jmlhSeinDepan)
			driver.find_element(By.ID,'kondisi17').send_keys(konSeinDepan)
		elif SeinDepan == 'Tidak':
			driver.find_element(By.ID,'jumlah17').send_keys('-')
			driver.find_element(By.ID,'kondisi17').send_keys('-')

		if LampuBelakang == 'Ada':
			driver.find_element(By.ID,'ketersediaan18').click()
			driver.find_element(By.ID,'jumlah18').send_keys(jmlhLampuBelakang)
			driver.find_element(By.ID,'kondisi18').send_keys(konLampuBelakang)
		elif LampuBelakang == 'Tidak':
			driver.find_element(By.ID,'jumlah18').send_keys('-')
			driver.find_element(By.ID,'kondisi18').send_keys('-')

		if SeinBelakang == 'Ada':
			driver.find_element(By.ID,'ketersediaan19').click()
			driver.find_element(By.ID,'jumlah19').send_keys(jmlhSeinBelakang)
			driver.find_element(By.ID,'kondisi19').send_keys(konSeinBelakang)
		elif SeinBelakang == 'Tidak':
			driver.find_element(By.ID,'jumlah19').send_keys('-')
			driver.find_element(By.ID,'kondisi19').send_keys('-')

		if LampuVariasi == 'Ada':
			driver.find_element(By.ID,'ketersediaan110').click()
			driver.find_element(By.ID,'jumlah110').send_keys(jmlhLampuVariasi)
			driver.find_element(By.ID,'kondisi110').send_keys(konLampuVariasi)
		elif LampuVariasi == 'Tidak':
			driver.find_element(By.ID,'jumlah110').send_keys('-')
			driver.find_element(By.ID,'kondisi110').send_keys('-')

		if PintuKanan == 'Ada':
			driver.find_element(By.ID,'ketersediaan111').click()
			driver.find_element(By.ID,'jumlah111').send_keys(jmlhPintuKanan)
			driver.find_element(By.ID,'kondisi111').send_keys(konPintuKanan)
		elif PintuKanan == 'Tidak':
			driver.find_element(By.ID,'jumlah111').send_keys('-')
			driver.find_element(By.ID,'kondisi111').send_keys('-')

		if PintuKiri == 'Ada':
			driver.find_element(By.ID,'ketersediaan112').click()
			driver.find_element(By.ID,'jumlah112').send_keys(jmlhPintuKiri)
			driver.find_element(By.ID,'kondisi112').send_keys(konPintuKiri)
		elif PintuKiri == 'Tidak':
			driver.find_element(By.ID,'jumlah112').send_keys('-')
			driver.find_element(By.ID,'kondisi112').send_keys('-')

		if BodyBelakang == 'Ada':
			driver.find_element(By.ID,'ketersediaan113').click()
			driver.find_element(By.ID,'jumlah113').send_keys(jmlhBodyBelakang)
			driver.find_element(By.ID,'kondisi113').send_keys(konBodyBelakang)
		elif BodyBelakang == 'Tidak':
			driver.find_element(By.ID,'jumlah113').send_keys('-')
			driver.find_element(By.ID,'kondisi113').send_keys('-')

		if BumperDepan == 'Ada':
			driver.find_element(By.ID,'ketersediaan114').click()
			driver.find_element(By.ID,'jumlah114').send_keys(jmlhBumperDepan)
			driver.find_element(By.ID,'kondisi114').send_keys(konBumperDepan)
		elif BumperDepan == 'Tidak':
			driver.find_element(By.ID,'jumlah114').send_keys('-')
			driver.find_element(By.ID,'kondisi114').send_keys('-')

		if BumperBelakang == 'Ada':
			driver.find_element(By.ID,'ketersediaan20').click()
			driver.find_element(By.ID,'jumlah20').send_keys(jmlhBumperBelakang)
			driver.find_element(By.ID,'kondisi20').send_keys(konBumperBelakang)
		elif BumperBelakang == 'Tidak':
			driver.find_element(By.ID,'jumlah20').send_keys('-')
			driver.find_element(By.ID,'kondisi20').send_keys('-')

		if Accu == 'Ada':
			driver.find_element(By.ID,'ketersediaan21').click()
			driver.find_element(By.ID,'jumlah21').send_keys(jmlhAccu)
			driver.find_element(By.ID,'kondisi21').send_keys(konAccu)
		elif Accu == 'Tidak':
			driver.find_element(By.ID,'jumlah21').send_keys('-')
			driver.find_element(By.ID,'kondisi21').send_keys('-')

		if Speedometer == 'Ada':
			driver.find_element(By.ID,'ketersediaan22').click()
			driver.find_element(By.ID,'jumlah22').send_keys(jmlhSpeedometer)
			driver.find_element(By.ID,'kondisi22').send_keys(konSpeedometer)
		elif Speedometer == 'Tidak':
			driver.find_element(By.ID,'jumlah22').send_keys('-')
			driver.find_element(By.ID,'kondisi22').send_keys('-')

		if Jok == 'Ada':
			driver.find_element(By.ID,'ketersediaan23').click()
			driver.find_element(By.ID,'jumlah23').send_keys(jmlhJok)
			driver.find_element(By.ID,'kondisi23').send_keys(konJok)
		elif Jok == 'Tidak':
			driver.find_element(By.ID,'jumlah23').send_keys('-')
			driver.find_element(By.ID,'kondisi23').send_keys('-')

		if AC == 'Ada':
			driver.find_element(By.ID,'ketersediaan24').click()
			driver.find_element(By.ID,'jumlah24').send_keys(jmlhAC)
			driver.find_element(By.ID,'kondisi24').send_keys(konAC)
		elif AC == 'Tidak':
			driver.find_element(By.ID,'jumlah24').send_keys('-')
			driver.find_element(By.ID,'kondisi24').send_keys('-')

		if AudioSound == 'Ada':
			driver.find_element(By.ID,'ketersediaan25').click()
			driver.find_element(By.ID,'jumlah25').send_keys(jmlhAudioSound)
			driver.find_element(By.ID,'kondisi25').send_keys(konAudioSound)
		elif AudioSound == 'Tidak':
			driver.find_element(By.ID,'jumlah25').send_keys('-')
			driver.find_element(By.ID,'kondisi25').send_keys('-')

		if KarpetBawah == 'Ada':
			driver.find_element(By.ID,'ketersediaan26').click()
			driver.find_element(By.ID,'jumlah26').send_keys(jmlhKarpetBawah)
			driver.find_element(By.ID,'kondisi26').send_keys(konKarpetBawah)
		elif KarpetBawah == 'Tidak':
			driver.find_element(By.ID,'jumlah26').send_keys('-')
			driver.find_element(By.ID,'kondisi26').send_keys('-')

		if VelgBanRodaDepan == 'Ada':
			driver.find_element(By.ID,'ketersediaan27').click()
			driver.find_element(By.ID,'jumlah27').send_keys(jmlhVelgBanRodaDepan)
			driver.find_element(By.ID,'kondisi27').send_keys(konVelgBanRodaDepan)
		elif VelgBanRodaDepan == 'Tidak':
			driver.find_element(By.ID,'jumlah27').send_keys('-')
			driver.find_element(By.ID,'kondisi27').send_keys('-')

		if VelgBanRodaBelakang == 'Ada':
			driver.find_element(By.ID,'ketersediaan28').click()
			driver.find_element(By.ID,'jumlah28').send_keys(jmlhVelgBanRodaBelakang)
			driver.find_element(By.ID,'kondisi28').send_keys(konVelgBanRodaBelakang)
		elif VelgBanRodaBelakang == 'Tidak':
			driver.find_element(By.ID,'jumlah28').send_keys('-')
			driver.find_element(By.ID,'kondisi28').send_keys('-')

		if BanSerep == 'Ada':
			driver.find_element(By.ID,'ketersediaan29').click()
			driver.find_element(By.ID,'jumlah29').send_keys(jmlhBanSerep)
			driver.find_element(By.ID,'kondisi29').send_keys(konBanSerep)
		elif BanSerep == 'Tidak':
			driver.find_element(By.ID,'jumlah29').send_keys('-')
			driver.find_element(By.ID,'kondisi29').send_keys('-')

		if Dongkrak == 'Ada':
			driver.find_element(By.ID,'ketersediaan210').click()
			driver.find_element(By.ID,'jumlah210').send_keys(jmlhDongkrak)
			driver.find_element(By.ID,'kondisi210').send_keys(konDongkrak)
		elif Dongkrak == 'Tidak':
			driver.find_element(By.ID,'jumlah210').send_keys('-')
			driver.find_element(By.ID,'kondisi210').send_keys('-')

		if KunciKunci == 'Ada':
			driver.find_element(By.ID,'ketersediaan211').click()
			driver.find_element(By.ID,'jumlah211').send_keys(jmlhKunciKunci)
			driver.find_element(By.ID,'kondisi211').send_keys(konKunciKunci)
		elif KunciKunci == 'Tidak':
			driver.find_element(By.ID,'jumlah211').send_keys('-')
			driver.find_element(By.ID,'kondisi211').send_keys('-')

		if LogoTulisan == 'Ada':
			driver.find_element(By.ID,'ketersediaan212').click()
			driver.find_element(By.ID,'jumlah212').send_keys(jmlhLogoTulisan)
			driver.find_element(By.ID,'kondisi212').send_keys(konLogoTulisan)
		elif LogoTulisan == 'Tidak':
			driver.find_element(By.ID,'jumlah212').send_keys('-')
			driver.find_element(By.ID,'kondisi212').send_keys('-')

		if Mesin == 'Ada':
			driver.find_element(By.ID,'ketersediaan213').click()
			driver.find_element(By.ID,'jumlah213').send_keys(jmlhMesin)
			driver.find_element(By.ID,'kondisi213').send_keys(konMesin)
		elif Mesin == 'Tidak':
			driver.find_element(By.ID,'jumlah213').send_keys('-')
			driver.find_element(By.ID,'kondisi213').send_keys('-')

		if STNK == 'Ada':
			driver.find_element(By.ID,'ketersediaan214').click()
			driver.find_element(By.ID,'jumlah214').send_keys(jmlhSTNK)
			driver.find_element(By.ID,'kondisi214').send_keys(konSTNK)
		elif STNK == 'Tidak':
			driver.find_element(By.ID,'jumlah214').send_keys('-')
			driver.find_element(By.ID,'kondisi214').send_keys('-')
	else:
		pass

@mark.fixture_penerimaan
def test_jumlahPneliti():
	if jumlhpeneliti == 3:
		driver.find_element(By.ID, 'tambahPeneliti').click()
		driver.find_element(By.ID, 'tambahPeneliti').click()
	elif jumlhpeneliti == 2:
		driver.find_element(By.ID, 'tambahPeneliti').click()
	elif jumlhpeneliti == 1:
		pass

@mark.fixture_penerimaan
def test_Dropdown_6():
	if jumlhpeneliti == 3 :
		ptgs1 = driver.find_element(By.ID, 'cariPeneliti0')
		ptgs1.click()
		ptgs1.send_keys('PEGWAI001')
		driver.find_element(By.ID, 'cariPeneliti00').click()
		sleep(driver)

		ptgs2 = driver.find_element(By.ID, 'cariPeneliti1')
		ptgs2.click()
		ptgs2.send_keys('PEGWAI002')
		driver.find_element(By.ID, 'cariPeneliti10').click()
		sleep(driver)

		ptgs2 = driver.find_element(By.ID, 'cariPeneliti2')
		ptgs2.click()
		ptgs2.send_keys('PEGWAI003')
		driver.find_element(By.ID, 'cariPeneliti20').click()
		sleep(driver)

	elif jumlhpeneliti == 2 :
		ptgs1 = driver.find_element(By.ID, 'cariPeneliti0')
		ptgs1.click()
		ptgs1.send_keys('PEGWAI001')
		driver.find_element(By.ID, 'cariPeneliti00').click()

		ptgs2 = driver.find_element(By.ID, 'cariPeneliti1')
		ptgs2.click()
		ptgs2.send_keys('PEGWAI002')
		driver.find_element(By.ID, 'cariPeneliti10').click()
		sleep(driver)

	elif jumlhpeneliti == 1 :
		ptgs1 = driver.find_element(By.ID, 'cariPeneliti0')
		ptgs1.click()
		ptgs1.send_keys('PEGWAI001')
		driver.find_element(By.ID, 'cariPeneliti00').click()

# Penilaian ==============================================================
def test_tab_3():
	# WebDriverWait(driver, 50).until(EC.invisibility_of_element_located((By.XPATH, pathData['Rupelemen']['+barang']['loadingbarang'])))
	driver.find_element(By.ID, 'tab-penilaian').click()

@mark.fixture_penerimaanx
def test_date_5(): 
	tglpenilai = driver.find_element(By.ID, 'tglPenilaian') #Tanggal Penilaian
	tglpenilai.send_keys(TglPenilaian)	
	tglpenilai.send_keys(Keys.ENTER)

@mark.fixture_penerimaan
def test_input_35():#Nomor BA Penelitian
	driver.find_element(By.ID,'noBaPenelitian').send_keys(NoBAPenelitian) 

@mark.fixture_penerimaan
def test_input_36():#Nilai Satuan Barang
	driver.find_element(By.ID,'nilaiSatuan').send_keys(NilaiSatuanBarang) 

@mark.fixture_penerimaan
def test_inputarea_3():#Keterangan
	driver.find_element(By.ID,'keterangan').send_keys(Keterangan) 

@mark.fixture_penerimaan
def test_jumlahPenilai():
	if jumlhpeneliti == 3:
		driver.find_element(By.ID, 'tambahPenilai').click()
		driver.find_element(By.ID, 'tambahPenilai').click()
	elif jumlhpeneliti == 2:
		driver.find_element(By.ID, 'tambahPenilai').click()
	elif jumlhpeneliti == 1:
		pass

@mark.fixture_penerimaan
def test_Dropdown_7():
	if jumlhpeneliti == 3 :
		peneliti1 = driver.find_element(By.ID, 'cariPenilai0')
		peneliti1.click()
		peneliti1.send_keys('PEGWAI001')
		driver.find_element(By.ID, 'cariPenilai00').click()
		sleep(driver)

		peneliti2 = driver.find_element(By.ID, 'cariPenilai1')
		peneliti2.click()
		peneliti2.send_keys('PEGWAI002')
		driver.find_element(By.ID, 'cariPenilai10').click()
		sleep(driver)

		peneliti2 = driver.find_element(By.ID, 'cariPenilai2')
		peneliti2.click()
		peneliti2.send_keys('PEGWAI003')
		driver.find_element(By.ID, 'cariPenilai20').click()
		sleep(driver)

	elif jumlhpeneliti == 2 :
		peneliti1 = driver.find_element(By.ID, 'cariPenilai0')
		peneliti1.click()
		peneliti1.send_keys('PEGWAI001')
		driver.find_element(By.ID, 'cariPenilai00').click()
		sleep(driver)

		peneliti2 = driver.find_element(By.ID, 'cariPenilai1')
		peneliti2.click()
		peneliti2.send_keys('PEGWAI002')
		driver.find_element(By.ID, 'cariPenilai10').click()
		sleep(driver)

	elif jumlhpeneliti == 1 :
		peneliti1 = driver.find_element(By.ID, 'cariPenilai0')
		peneliti1.click()
		peneliti1.send_keys('PEGWAI001')
		driver.find_element(By.ID, 'cariPenilai00').click()
		sleep(driver)

@mark.fixture_penerimaan
def test_submitdata_21():
    driver.find_element(By.ID,'submitButton').click()