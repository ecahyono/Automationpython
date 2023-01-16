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
import pyautogui
import platform
import logging
from pytest import mark
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
@mark.fixture_penerimaan
def test_00_setup():
	# Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()

@mark.fixture_penerimaan
def test_00_loggin():
	# Log.info('Memasukan User name dan Password di halaman Login')
	# login(driver)
	oprupbasanbdg(driver)

@mark.fixture_penerimaan
def test_PNM_001():
	# Log.info('Mengakses menu Penerimaan dengan memilih modul Rupbasan kemudian pilih menu Penerimaan')
	nav1 = driver.find_element(By.ID, "RUP00")
	ActionChains(driver).move_to_element(nav1).perform()
	driver.find_element(By.LINK_TEXT, 'Penerimaan').click()
	driver.find_element(By.ID, 'kataKunci').click()

plus = wb['TambahubahPenerimaan']
sbarang = wb['Barangbasan']

@mark.fixture_penerimaan
def test_PNM003_2():
	i = 77
	y = 77 # barisexel  
	while i <= len(plus['A']):

		JenisRegistrasi		= plus['A'+str(i)].value  # Jenis Registrasi
		tglPenerimaan		= plus['B'+str(i)].value  # Tanggal Penerimaan
		Noregrup			= plus['C'+str(i)].value  # Nomor Registrasi Rupbasan
		instansi			= plus['D'+str(i)].value  # Instansi
		Noregins			= plus['E'+str(i)].value  # Nomor Surat Pengantar
		NoSIP				= plus['F'+str(i)].value  # Nomor Surat Perintah Penyitaan
		tglSIP				= plus['G'+str(i)].value  # Tanggal Surat Perintah Penyitaan
		Ppenyita			= plus['H'+str(i)].value  # Pengadilan Penyita
		NoSP				= plus['I'+str(i)].value  # Nomor Surat Penetapan Pengadilan
		tglSP				= plus['J'+str(i)].value  # Tanggal Surat Penetapan Pengadilan
		pasal				= plus['K'+str(i)].value  # Pasal
		NBAST				= plus['L'+str(i)].value  # Kategori Pidana
		kejahatan			= plus['M'+str(i)].value  # Jenis Kejahatan
		NOBApenyitaan			= plus['N'+str(i)].value  # No. BA Penyitaan
		nosuratpernyataan			= plus['O'+str(i)].value  # No. Surat Pernyataan
		Keteranganpenerimaan		= plus['P'+str(i)].value  # Keterangan

		# tab identitas
		Ptgpenerima			= plus['Q'+str(i)].value  # Petugas Penerima

		NamaPetugasyangMenyerahkan = plus['R'+str(i)].value
		nippetugaspenyerah		= plus['S'+str(i)].value  # jumlah penyerah
		Jabatanpetugas			= plus['T'+str(i)].value #status1
		pangktPenyerah1			= plus['U'+str(i)].value  # penyerah1

		identitaspenerimaan		= plus['v'+str(i)].value #Penyerah1

		petugasinstansipenyerah			= plus['W'+str(i)].value  # Penyerah2
		NIKpetugasinstansipenyerah			= plus['X'+str(i)].value  # jumlah 
		
		saksipenerimaan			= plus['Y'+str(i)].value  # statussaksi1
		saksi1				= plus['Z'+str(i)].value  # saksi1
		statusaksi2			= plus['AA'+str(i)].value  # statussaksi2
		saksi2				= plus['AB'+str(i)].value  # saksi2

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

		WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
		driver.find_element(By.ID, 'createButton').click()
		try:
			# Jenis Registrasi
			jenisrasi = driver.find_element(By.ID, 'dropdownJenisRegistrasi')
			jenisrasi.click()
			jenisrasi.send_keys(JenisRegistrasi)
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisRegistrasi0')))
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
			elif JenisRegistrasi == 'Register Khusus Tingkat Penuntutan':
				driver.find_element(By.ID, 'jenisRegistrasi7').click()
			elif JenisRegistrasi == 'Register Khusus Tingkat Pengadilan Negeri':
				driver.find_element(By.ID, 'jenisRegistrasi8').click()
			elif JenisRegistrasi == 'Register Khusus Tingkat Pengadilan Tinggi':
				driver.find_element(By.ID, 'jenisRegistrasi9').click()
			elif JenisRegistrasi == 'Register Khusus Tingkat Mahkamah Agung':
				driver.find_element(By.ID, 'jenisRegistrasi10').click()

			Tanggal_Penerimaan = driver.find_element(By.ID, 'inputTglPenerimaan')  # Tanggal Penerimaan
			Tanggal_Penerimaan.send_keys(tglPenerimaan)
			Tanggal_Penerimaan.send_keys(Keys.ENTER)

			driver.find_element(By.ID, 'inputNoRegistrasi').send_keys(Noregrup)  # Nomor Registrasi Rupbasan

			pilihinstansi = driver.find_element(By.ID, 'dropdownInstansi')
			pilihinstansi.click()  # Instansi
			pilihinstansi.send_keys(instansi)
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'instansi0')))
			if instansi == 'POLDA JABAR':
				driver.find_element(By.ID, 'instansi0').click()
			elif instansi == 'POLRES BANDUNG':
				driver.find_element(By.ID, 'instansi3').click()
			elif instansi == 'KEJAKSAAN NEGERI BANDUNG':
				driver.find_element(By.ID, 'instansi590').click()
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
			elif instansi == 'PENGADILAN TINGGI BANDUNG':
				driver.find_element(By.ID, 'instansi938').click()
			elif instansi == 'PENGADILAN NEGERI BANDUNG':
				driver.find_element(By.ID, 'instansi989').click()
			elif instansi == 'POLRES INDRAMAYU':
				driver.find_element(By.ID, 'instansi20').click()
			elif instansi == 'POLRES JAKARTA BARAT':
				driver.find_element(By.ID, 'instansi24').click()
			elif instansi == 'POLRES KOTA BESAR BANDUNG':
				driver.find_element(By.ID, 'instansi2').click()
			elif instansi == 'PENGADILAN NEGERI BALE BANDUNG':
				driver.find_element(By.ID, 'instansi1007').click()


			# Log.info('Menginput Nomor Registrasi Instansi')
			driver.find_element(By.ID, 'inputNoRegInstansi').send_keys(Noregins)  # Nomor Registrasi Instansi

			# Log.info('Menginput Nomor Surat Izin Penyitaan')
			driver.find_element(By.ID, 'inputNoSuratIzinPenyitaan').send_keys(NoSIP)  # Nomor Surat Izin Penyitaan

			# Log.info('Menginput Tanggal Surat Izin Penyitaan')
			Tanggal_Surat_Izin_Penyitaan = driver.find_element(By.ID, 'inputTglSuratIzinPenyitaan')  # Tanggal Surat Izin Penyitaan
			Tanggal_Surat_Izin_Penyitaan.send_keys(tglSIP)
			Tanggal_Surat_Izin_Penyitaan.send_keys(Keys.ENTER)

			# Log.info('Memilih Opsi Pengadilan Penyita')
			driver.find_element(By.ID, 'dropdownPengadilanPenyita').click()
			
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
			# Log.info('menginput nomor surat Penyitaan')
			driver.find_element(By.ID, 'inputNoSuratPenyitaan').send_keys(NoSP)  # Nomor Surat Penyitaan
			# Log.info('menginput tanggal surat Penyitaan')
			Tanggal_Surat_Izin_Penyitaan = driver.find_element(By.ID, 'inputTglSuratPenyitaan')  # Tanggal 
			Tanggal_Surat_Izin_Penyitaan.send_keys(tglSP)
			Tanggal_Surat_Izin_Penyitaan.send_keys(Keys.ENTER)
			# Log.info('input pasal')
			driver.find_element(By.ID, 'inputPasal').send_keys(pasal)  # Pasal
		
			driver.find_element(By.ID, 'dropdownKategoriPidana').click()
			if NBAST == 'Pidana Umum': 
				driver.find_element(By.ID, 'Pidana Umum').click()
			elif NBAST == 'Pidana Khusus': 
				driver.find_element(By.ID, 'Pidana Khusus').click()

			imputkejahatan = driver.find_element(By.ID, 'dropdownJenisKejahatan')
			imputkejahatan.click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisKejahatan0')))
			imputkejahatan.send_keys(kejahatan)
			if kejahatan == 'Kemanan Negara/ Makar/ Politik':
				driver.find_element(By.ID,'jenisKejahatan0').click()
			elif kejahatan == 'Terhadap Kepala Negara':
				driver.find_element(By.ID,'jenisKejahatan1').click()
			elif kejahatan == 'Terhadap Ketertiban':
				driver.find_element(By.ID,'jenisKejahatan2').click()
			elif kejahatan == 'Pembakaran':
				driver.find_element(By.ID,'jenisKejahatan3').click()
			elif kejahatan == 'Penyuapan':
				driver.find_element(By.ID,'jenisKejahatan4').click()
			elif kejahatan == 'Mata Uang':
				driver.find_element(By.ID,'jenisKejahatan5').click()
			elif kejahatan == 'Memalsu Materai / Surat':
				driver.find_element(By.ID,'jenisKejahatan6').click()
			elif kejahatan == 'Kesusilaan':
				driver.find_element(By.ID,'jenisKejahatan7').click()
			elif kejahatan == 'Melakukan Perjudian Ilegal Secara Online dan Offline':
				driver.find_element(By.ID,'jenisKejahatan8').click()
			elif kejahatan == 'Penculikan':
				driver.find_element(By.ID,'jenisKejahatan9').click()
			elif kejahatan == 'Penganiayaan':
				driver.find_element(By.ID,'jenisKejahatan10').click()
			elif kejahatan == 'Pencurian-1':
				driver.find_element(By.ID,'jenisKejahatan11').click()
			elif kejahatan == 'Perampokan':
				driver.find_element(By.ID,'jenisKejahatan12').click()
			elif kejahatan == 'Memeras / Mengancam':
				driver.find_element(By.ID,'jenisKejahatan13').click()
			elif kejahatan == 'Penggelapan':
				driver.find_element(By.ID,'jenisKejahatan14').click()
			elif kejahatan == 'Penipuan':
				driver.find_element(By.ID,'jenisKejahatan15').click()
			elif kejahatan == 'Desersi':
				driver.find_element(By.ID,'jenisKejahatan16').click()
			elif kejahatan == 'Perbankan':
				driver.find_element(By.ID,'jenisKejahatan17').click()
			elif kejahatan == 'Penadahan':
				driver.find_element(By.ID,'jenisKejahatan18').click()
			elif kejahatan == 'Migas':
				driver.find_element(By.ID,'jenisKejahatan19').click()
			elif kejahatan == 'Subversi':
				driver.find_element(By.ID,'jenisKejahatan20').click()
			elif kejahatan == 'Narkotika':
				driver.find_element(By.ID,'jenisKejahatan21').click()
			elif kejahatan == 'Korupsi':
				driver.find_element(By.ID,'jenisKejahatan22').click()

			driver.find_element(By.ID, 'inputNoBaPenyitaan').send_keys(NOBApenyitaan)
			driver.find_element(By.ID, 'inputNoSuratPernyataan').send_keys(nosuratpernyataan)
			driver.find_element(By.ID, 'inputKeterangan').send_keys(Keteranganpenerimaan)
			# Log.info('Melakukan Pencarian data Identitas petugas Penerima')
			penerima = driver.find_element(By.ID, 'searchPetugasPenerima')  # Petugas Penerima
			penerima.click()
			penerima.send_keys(Ptgpenerima)
			time.sleep(2)
			WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchPetugasPenerima0')))
			driver.find_element(By.ID, 'searchPetugasPenerima0').click()

			# Log.info('Melakukan Pencarian data Petugas yang menyerahkan')
			driver.find_element(By.ID, 'nama_penyerah').send_keys(NamaPetugasyangMenyerahkan)
			driver.find_element(By.ID, 'nip_penyerah').send_keys(nippetugaspenyerah)
			driver.find_element(By.ID, 'jabatan_penyerah').send_keys(Jabatanpetugas)
			driver.find_element(By.ID, 'pangkat_penyerah').send_keys(pangktPenyerah1)

		# tab Identitas
			# Log.info('Melakukan Pencarian data Identitas')
			identi1 = driver.find_element(By.ID, "searchIdentitas-0")
			identi1.click()
			identi1.send_keys(identitaspenerimaan)
			time.sleep(1)
			WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchIdentitas-00')))
			driver.find_element(By. ID, 'searchIdentitas-00').click()

		# Tab Petugas Instansi Yng Menyerahkan
			# Log.info('klik tab Petugas Instansi')
			driver.find_element(By.ID, "tab-petugas_instansi").click()
			# Log.info('Memilih Petugas Instansi Yang menyerahkan pertama')
			driver.find_element(By.ID, 'nama_menyerahkan-0').send_keys(petugasinstansipenyerah)
			driver.find_element(By.ID, 'nip_menyerahkan-0').send_keys(NIKpetugasinstansipenyerah)

		# #tab Saksi
			# Log.info('Klik tab Saksi Penerima')
			driver.find_element(By.ID, "tab-saksi_penerimaan").click()

			statsaks1 = driver.find_element(By.ID, 'searchSaksi-0')
			statsaks1.click()
			statsaks1.send_keys(saksipenerimaan)
			time.sleep(2)
			driver.find_element(By.ID, 'searchSaksi-00').click()

		# #tab Dokumen
			# Log.info('Klik tab Saksi Penerima')
			driver.find_element(By.ID, "tab-dokumen_files").click()

			driver.find_element(By.ID, "pilihDokumenFile0").click()
			time.sleep(3)
			pyautogui.write(environ.get(r"FILEPDF"))
			pyautogui.press('enter')

			time.sleep(2)
			driver.find_element(By.ID, "submitButton").click()

			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
			driver.find_element(By. ID, 'daftarBarangButton').click()

			# #Kelengkapan Basan Baran ==============================================================

			time.sleep(1)
			driver.find_element(By.ID, 'tab-kelengkapanBasanBaran').click()

			nabar = driver.find_element(By.ID, 'nama_barang').send_keys(nama_barang)  # Nama Barang

			# Log.info('checkbox barang temuan')
			if barang_temuan == 'Iya':
				driver.find_element(By.ID, 'barang_temuan').click()
			elif barang_temuan == 'Tidak':
				print('')

			# Log.info('Memilih jenis barang basan')
			driver.find_element(By.ID, 'input_jenis_baran_basan').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'JSB1')))
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

			time.sleep(1)
			# Log.info('Memilih satuan barang')
			driver.find_element(By.ID, 'input_satuan_baran_basan').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, '01')))
			driver.find_element(By.ID, 'input_satuan_baran_basan').send_keys(satuan)
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

			# Log.info('Jumlah Baik')
			driver.find_element(By.ID, 'jumlah_baik').send_keys(jumlah_baik)  # jumlah_baik
			# Log.info('Jumlah rusak ringan')
			driver.find_element(By.ID, 'jumlah_rusak_ringan').send_keys(jumlah_rusak_ringan)  # jumlah rusak ringan
			# Log.info('Jumlah rusak berat')
			driver.find_element(By.ID, 'jumlah_rusak_berat').send_keys(jumlah_rusak_berat)  # jumlah Rusak Berat

			# Log.info('upload foto barang 1')
			driver.find_element(By.ID, 'pilihFoto0').click()
			time.sleep(3)
			pyautogui.write(environ.get(r"BARANG"))
			pyautogui.press('enter')
			#
			# driver.find_element(By.ID,'namaFoto0').send_keys(foto1)
			driver.find_element(By.ID, 'keterangann0').send_keys(keteranfanfoto1)
# Penelitian ==============================================================
			# Log.info('pindah tab')
			# WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.XPATH, pathData['Rupelemen']['+barang']['loadingbarang'])))
			driver.find_element(By.ID, 'tab-penelitian').click()

			# Log.info('Nomor Penelitian')
			noPenelitian = driver.find_element(By.ID, 'noPenelitian').send_keys(NomorPenelitian)  # Nomor Penelitian

			# Log.info('tanggal Penelitian')
			penelititgl = driver.find_element(By.ID, 'tglPenelitian')
			penelititgl.click()
			penelititgl.send_keys(tglPenelitian)
			penelititgl.send_keys(Keys.ENTER)  # Tanggal Penelitian

			# Log.info('no SK penelitian')
			driver.find_element(By.ID, 'noSkPeneliti').send_keys(NoskPenelitian)  # Nomor SK Penelitian

			# Log.info('Tanggal SK Penelitian')
			skpenelititgl = driver.find_element(By.ID, 'tglSkPeneliti')
			skpenelititgl.click
			skpenelititgl.send_keys(tglSkPeneliti)
			skpenelititgl.send_keys(Keys.ENTER)  # Tanggal SK Penelitian
			# Memilih Golongan
			# Log.info('Memilih Golongan')
			driver.find_element(By.ID, 'golongan').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, '001')))
			driver.find_element(By.ID, 'golongan').send_keys(Golongan)
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
 # Keadaan Segel Penyita
			# Log.info('Keadaan Segel Penyita')
			driver.find_element(By.ID, 'keadaanSegel').send_keys(KeadaanSegelPenyita)
 # Kondisi Barang
			# Log.info('Kondisi Barang')
			driver.find_element(By.ID, 'kondisiBarang').click()
			if KondisiBarang == 'Baik':
				driver.find_element(By.ID, 'KBB1').click()
			elif KondisiBarang == 'Rusak':
				driver.find_element(By.ID, 'KBB2').click()
 # Sub Kondisi Barang
			# Log.info('Sub Kondisi Barang')
			if KondisiBarang == 'Rusak':
				driver.find_element(By.ID, 'subKondisiBarang').click()
				if SubKondisiBarang == 'Rusak Ringan':
					driver.find_element(By.ID, 'SKB1').click()
				elif SubKondisiBarang == 'Rusak Berat':
					driver.find_element(By.ID, 'SKB2').click()
			elif KondisiBarang == 'Baik':
				pass
 # Sifat
			# Log.info('Input sifat')
			driver.find_element(By.ID, 'sifat').send_keys(Sifat)
 # Merek Dan Kondisi
			# Log.info('input merek dan kondisi')
			driver.find_element(By.ID, 'merekKondisi').send_keys(MerekDanKondisi)
			# Log.info('input berat')
			driver.find_element(By.ID, 'berat').send_keys(Berat)  # Berat

			# Log.info('input volime')
			driver.find_element(By.ID, 'volumeCc').send_keys(VolumeCC)  # Volume / CC

			# Log.info('input panjang')
			driver.find_element(By.ID, 'panjang').send_keys(Panjang)  # Panjang

			# Log.info('input lebar')
			driver.find_element(By.ID, 'lebar').send_keys(Lebar)  # Lebar
			# Log.info('input tinggi')
			driver.find_element(By.ID, 'tinggi').send_keys(Tinggi)  # Tinggi

			# Log.info('input tipemerek')
			if Golongan == 'HEWAN TERNAK':
				pass
			else:
				driver.find_element(By.ID, 'tipeMerek').send_keys(
					TipeMerek)  # Tipe / Merek
			# Log.info('input yang jenis golongan senjata api')
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

			# Log.info('input yang jenis golongan elektronik')
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

			# Log.info('input tahunPembuatan')
			if (Golongan == 'KENDARAAN BERMOTOR' or Golongan == 'SENJATA API (SENPI)' or Golongan == 'Lain - Lain'):
				thnpembuatan = driver.find_element(By.ID, 'tahunPembuatan')
				thnpembuatan.send_keys(TahunPembuatan)  # Tahun Pembuatan
				thnpembuatan.send_keys(Keys.ENTER)
			else:
				pass

			# Log.info('input tahunPengeluaranPenerbitan')
			if (Golongan == 'KENDARAAN BERMOTOR' or Golongan == 'SENJATA API (SENPI)' or Golongan == 'Lain - Lain'):
				thnpengeluaran = driver.find_element(
					By.ID, 'tahunPengeluaranPenerbitan')
				# Tahun Pengeluaran / Penerbitan
				thnpengeluaran.send_keys(TahunPengeluaranpenerbitan)
				thnpengeluaran.send_keys(Keys.ENTER)
			else:
				pass

			# Log.info('input warna')
			if (Golongan == 'KENDARAAN BERMOTOR' or Golongan == 'SENJATA API (SENPI)'):
				driver.find_element(By.ID, 'warna').send_keys(Warna)  # Warna
			else:
				pass

			# Log.info('input NomorMesin')
			if Golongan == 'KENDARAAN BERMOTOR':
				driver.find_element(By.ID, 'nmrMesin').send_keys(
					NomorMesin)  # Nomor Mesin
			else:
				pass

			# Log.info('input NomorChasis')
			if Golongan == 'KENDARAAN BERMOTOR':
				driver.find_element(By.ID, 'nmrChasis').send_keys(
					NomorChasis)  # Nomor Chasis
			else:
				pass

			# Log.info('input TeganganDaya')
			if Golongan == 'KENDARAAN BERMOTOR':
				driver.find_element(By.ID, 'teganganDaya').send_keys(
					TeganganDaya)  # Tegangan Daya
			else:
				pass

			# Log.info('input MerekSumberDaya')
			if Golongan == 'KENDARAAN BERMOTOR':
				driver.find_element(By.ID, 'merekSumberDaya').send_keys(
					MerekSumberDaya)  # Merek Sumber Daya
			else:
				pass

			# Log.info('input AsalBasanDari')
			driver.find_element(By.ID, 'asalDari').send_keys(
				AsalBasanDari)  # Asal Basan Dari

			# Log.info('input PerkiraanUsia')
			driver.find_element(By.ID, 'perkiraanUsia').send_keys(
				PerkiraanUsia)  # Perkiraan Usia

			# Log.info('input Kemasan')
			if Golongan == 'BATU PERMATA':
				driver.find_element(By.ID, 'kadarKarat').send_keys(
					KadarKarat)  # Kadar Karat
				driver.find_element(By.ID, 'kemasan').send_keys(Kemasan)  # Kemasan
			else:
				pass

			# Log.info('input Batasan')
			driver.find_element(By.ID, 'batasan').send_keys(Batasan)  # Batasan


			# Log.info('input NoIMB')
			driver.find_element(By.ID, 'NoImb').send_keys(NoIMB)  # No. IMB

			# Log.info('input IsiGedung')
			driver.find_element(By.ID, 'isiGedung').send_keys(IsiGedung)  # Isi Gedung



			# Log.info('input SuratBukti')
			driver.find_element(By.ID, 'suratBukti').send_keys(SuratBukti)  # Surat Bukti

			# Log.info('input BenderaNegara')
			driver.find_element(By.ID, 'bendera').send_keys(BenderaNegara)  # Bendera Negara

			# Log.info('input NoPolisi')
			if Golongan == 'KENDARAAN BERMOTOR':
				driver.find_element(By.ID, 'nomorPolisi').send_keys(NoPolisi)  # No. Polisi
			else:
				pass

			# Log.info('input WarnaTNKB')
			if Golongan == 'KENDARAAN BERMOTOR':
				driver.find_element(By.ID, 'warnaTnkb').send_keys(WarnaTNKB)  # Warna TNKB
			else:
				pass

			# Log.info('input MasaBerlakuTNK')
			if Golongan == 'KENDARAAN BERMOTOR':
				driver.find_element(By.ID, 'masaBerlakuTnkb').send_keys(MasaBerlakuTNK)  # Masa Berlaku TNKB
			else:
				pass

			# Log.info('input BahanBakar')
			if Golongan == 'KENDARAAN BERMOTOR':
				driver.find_element(By.ID, 'bahanBakar').send_keys(BahanBakar)  # Bahan Bakar
			else:
				pass

			# Log.info('input CiriKhusus')
			driver.find_element(By.ID, 'ciriKhusus').send_keys(CiriKhusus)  # Ciri Khusus


			# Log.info('input HalLainnya')
			driver.find_element(By.ID, 'halLainnya').send_keys(HalLainnya)  # Hal Lainnya


			# Log.info('input PemeliharaanKhusus')
			if (PemeliharaanKhusus == 'Iya' or PemeliharaanKhusus == 'iya'):
				driver.find_element(By.ID, 'PemeliharaanKhusus').click()
			elif (PemeliharaanKhusus == 'Tidak' or PemeliharaanKhusus == 'tidak'):
				pass


			# Log.info('input catatanPemeliharaanKhusus')
			if (PemeliharaanKhusus == 'Iya' or PemeliharaanKhusus == 'iya'):
				driver.find_element(By.ID, 'catatanPemeliharaanKhusus').send_keys(CatatanPemeliharaanKhusus)  # Catatan Pemeliharaan Khusus
			elif (PemeliharaanKhusus == 'Tidak' or PemeliharaanKhusus == 'tidak'):
				pass

			# Log.info('input RekomendasiTimPeneliti')
			driver.find_element(By.ID, 'rekomendasiTimPeneliti').send_keys(RekomendasiTimPeneliti)  # Rekomendasi Tim Peneliti

			driver.find_element(By.ID,'namaFotoTambahan0').send_keys(foto1)
			driver.find_element(By.ID, 'keteranganTambahan0').send_keys(keteranfanfoto1)

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

			ptgs1 = driver.find_element(By.ID, 'cariPeneliti0')
			ptgs1.click()
			time.sleep(1)
			ptgs1.send_keys(Peneliti1)
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'cariPeneliti00')))
			driver.find_element(By.ID, 'cariPeneliti00').click()

		# Penilaian ==============================================================:
			# Log.info('pindah tab')
			# WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.XPATH, pathData['Rupelemen']['+barang']['loadingbarang'])))
			driver.find_element(By.ID, 'tab-penilaian').click()

			# Log.info('input tglPenilaian')
			tglpenilai = driver.find_element(By.ID, 'tglPenilaian')  
			tglpenilai.send_keys(TglPenilaian)# Tanggal Penilaian
			tglpenilai.send_keys(Keys.ENTER)
  # Nomor BA Penelitian
			# Log.info('input NoBAPenelitian')
			driver.find_element(By.ID, 'noBaPenelitian').send_keys(NoBAPenelitian)

  # Nilai Satuan Barang
			# Log.info('input NilaiSatuanBarang')
			nilaisatbar = driver.find_element(By.XPATH, '//*[@id="nilaiSatuan"]/div/input')
			nilaisatbar.clear()
			nilaisatbar.send_keys(NilaiSatuanBarang)

  # Keterangan
			# Log.info('input Keterangan')
			driver.find_element(By.ID, 'keterangan').send_keys(Keterangan)

			penlai1 = driver.find_element(By.ID, 'cariPenilai0')
			penlai1.click()
			penlai1.send_keys(Penilai1)
			time.sleep(2)
			driver.find_element(By.ID, 'cariPenilai00').click()


			# submit data tambah barang
			driver.find_element(By.ID, 'submitButton').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

		except TimeoutException:
			print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!LOADING TERLALU LAMA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
			pass
		i = i + 1
		y = y + 1
	print ('Success Created')
