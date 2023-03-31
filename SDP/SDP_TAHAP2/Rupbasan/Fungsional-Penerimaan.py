from my_module import *
# init driver by os
@mark.fixture_penerimaan
def testconfigwebdriver():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver
	driver = initDriver()
@mark.fixture_penerimaan
def testlogin():
	Log.info('Memasukan User name dan Password di halaman Login')
	oprupbasanbdg(driver)
@mark.fixture_penerimaan
def testaksesmenu():
	Log.info('Mengakses Halaman Penerimaan')
	Penerimaan(driver)
	Log.info('Mengakses Halaman Tambah')
	driver.find_element(By.ID, 'createButton').click()

penerimaan = wb['TambahubahPenerimaan']
i = 6
JenisRegistrasi    				=penerimaan['A'+str(i)].value #Jenis Registrasi
tglPenerimaan      				=penerimaan['B'+str(i)].value #Tanggal Penerimaan
instansi           				=penerimaan['C'+str(i)].value #Instansi
NomorSuratPengantar           	=penerimaan['D'+str(i)].value #Nomor Surat Pengantar
NomorSuratPerintahPenyitaan		=penerimaan['E'+str(i)].value #Nomor Surat Perintah Penyitaan
TanggalSuratPerintahPenyitaan   =penerimaan['F'+str(i)].value #Tanggal Surat Perintah Penyitaan
PengadilanPenyita           	=penerimaan['G'+str(i)].value #Pengadilan Penyita
NomorSuratPenetapanPengadilan	=penerimaan['H'+str(i)].value #Nomor Surat Penetapan Pengadilan
tglSuratPenetapanPengadilan     =penerimaan['I'+str(i)].value #Tanggal Surat Penetapan Pengadilan
InstitusiPenempatan    			=penerimaan['J'+str(i)].value #Institusi Penempatan
Pasal         					=penerimaan['K'+str(i)].value #Pasal
KategoriPidana        			=penerimaan['L'+str(i)].value #Kategori Pidana
JenisKejahatan           		=penerimaan['M'+str(i)].value #JenisKejahatan
NoBAPenyitaan    				=penerimaan['N'+str(i)].value #NoBAPenyitaan
NoSuratPernyataan   			=penerimaan['O'+str(i)].value #No. Surat Pernyataan
Keterangan					    =penerimaan['P'+str(i)].value #Keterangan
Petugaspenerima             	=penerimaan['Q'+str(i)].value #Petugas Penerima
Namapetugasyangmenyerahkan	    =penerimaan['R'+str(i)].value #Nama Petugas yang Menyerahkan
NIPNRPPetugasyangMenyerahkan  	=penerimaan['S'+str(i)].value #NIP/NRP Petugas yang Menyerahkan
PangkatGolonganPetugas     		=penerimaan['T'+str(i)].value #Pangkat/Golongan Petugas yang Menyerahkan
JabatanPetugas            		=penerimaan['U'+str(i)].value #Jabatan Petugas yang Menyerahkan
IdentitasWBP         			=penerimaan['V'+str(i)].value #Identitas WBP
Namasaksipenyerah            	=penerimaan['W'+str(i)].value #nama Petugas Instansi yang Menyerahkan
NipNrpsaksiinstansipenyerh 		=penerimaan['X'+str(i)].value #nip Petugas Instansi yang Menyerahkan
SaksiPenerimaan        			=penerimaan['Y'+str(i)].value #Saksi Penerimaan
Keterangandkumen      			=penerimaan['Z'+str(i)].value #Keterangan Dokumen

@mark.fixture_penerimaan
def test_PNM_01():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'dropdownJenisRegistrasi')))
	Log.info('Memeilih Dropdown Jenis Registrasi')
	driver.find_element(By.ID, 'dropdownJenisRegistrasi').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'jenisRegistrasi0')))
	driver.find_element(By.XPATH, "//li[contains(.,'"+ JenisRegistrasi+"')]").click()
@mark.fixture_penerimaan
def test_PNM_02():
	Log.info('Menginput Tanggal Penerimaan')
	Tanggal_Penerimaan = driver.find_element(By.ID, 'inputTglPenerimaan')  
	Tanggal_Penerimaan.send_keys(tglPenerimaan)
	Tanggal_Penerimaan.send_keys(Keys.ENTER)
@mark.fixture_penerimaan
def test_PNM_03():
	Log.info('Memilih Opsi instansi')
	driver.find_element(By.ID, 'dropdownInstansi').click()  
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'instansi0')))
	driver.find_element(By.XPATH, "//li[contains(.,'"+ instansi+"')]").click()
@mark.fixture_penerimaan
def test_PNM_04():
	Log.info('Menginput Nomor Surat Perintah Penyitaan')
	driver.find_element(By.ID, 'inputNoRegInstansi').send_keys(NomorSuratPengantar)  
	Log.info('Menginput Tgl Surat Perintah Penyitaan')
	driver.find_element(By.ID, 'inputNoSuratIzinPenyitaan').send_keys(NomorSuratPerintahPenyitaan) 
@mark.fixture_penerimaan
def test_PNM_05():
	Log.info('Menginput anggal Surat Perintah Penyitaan')
	Tanggal_Penerimaan = driver.find_element(By.ID, 'inputTglSuratIzinPenyitaan')  
	Tanggal_Penerimaan.send_keys(TanggalSuratPerintahPenyitaan)
	Tanggal_Penerimaan.send_keys(Keys.ENTER)
@mark.fixture_penerimaan
def test_PNM_06():
	Log.info('Memilih Opsi Pengadilan Penyita')
	driver.find_element(By.ID, 'dropdownPengadilanPenyita').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'pengadilanNegeri0')))
	driver.find_element(By.XPATH, "//li[contains(.,'"+ PengadilanPenyita+"')]").click()
@mark.fixture_penerimaan
def test_PNM_07():
	Log.info('menginput nomor surat Penyitaan')
	driver.find_element(By.ID, 'inputNoSuratPenyitaan').send_keys(NomorSuratPenetapanPengadilan)   
@mark.fixture_penerimaan
def test_PNM_08():
	Log.info('menginput tanggal surat Penyitaan')
	Tanggal_Surat_Izin_Penyitaan = driver.find_element(By.ID, 'inputTglSuratPenyitaan')  
	Tanggal_Surat_Izin_Penyitaan.send_keys(tglSuratPenetapanPengadilan)
	Tanggal_Surat_Izin_Penyitaan.send_keys(Keys.ENTER)
@mark.fixture_penerimaan
def test_PNM_09():
	Log.info('Memilih Opsi Institusi Penempatan')
	driver.find_element(By.ID, 'dropdownInstitusiPenempatan').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'institusiPenempatan0')))
	driver.find_element(By.XPATH, "//li[contains(.,'"+ InstitusiPenempatan+"')]").click()
@mark.fixture_penerimaan
def test_PNM_10():
	Log.info('input pasal')
	driver.find_element(By.ID, 'inputPasal').send_keys(Pasal)  
@mark.fixture_penerimaan
def test_PNM_11():
	Log.info('Memilih Opsi Institusi Penempatan')
	driver.find_element(By.ID, 'dropdownKategoriPidana').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'Pidana Umum')))
	driver.find_element(By.XPATH, "//li[contains(.,'"+ KategoriPidana+"')]").click()
@mark.fixture_penerimaan
def test_PNM_12():
	Log.info('Memilih Opsi Institusi Penempatan')
	driver.find_element(By.ID, 'dropdownJenisKejahatan').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'jenisKejahatan0')))
	driver.find_element(By.XPATH, "//li[contains(.,'"+ JenisKejahatan+"')]").click()
@mark.fixture_penerimaan
def test_PNM_13():
	Log.info('input NoBAPenyitaan')
	driver.find_element(By.ID, 'inputNoBaPenyitaan').send_keys(NoBAPenyitaan)  
@mark.fixture_penerimaan
def test_PNM_14():
	Log.info('input No. Surat Pernyataan')
	driver.find_element(By.ID, 'inputNoSuratPernyataan').send_keys(NoSuratPernyataan)  
@mark.fixture_penerimaan
def test_PNM_15():
	Log.info('Input field text area')
	driver.find_element(By.ID, 'inputKeterangan').send_keys(Keterangan)
@mark.fixture_penerimaan
def test_PNM_16():
	Log.info('Melakukan Pencarian data Identitas petugas Penerima')
	try :
		ppenerima = driver.find_element(By.ID, 'searchPetugasPenerima')
		ppenerima.click()
		ppenerima.send_keys(Petugaspenerima)
		WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'searchPetugasPenerima0')))
		driver.find_element(By.XPATH, "//li[contains(.,'"+ Petugaspenerima +"')]").click()
	except NoSuchElementException: 
		Log.info("Element not found, Data petugas belum di tambahkan")
		is_running = True
		while is_running:
			try:
				subprocess.run(["pytest", "Pegawairupbasan.py"], check=True)
				# setelah pytest selesai dijalankan, ulangi proses mencari elemen
				handles = driver.window_handles
				# alihkan fokus kembali ke tab awal
				driver.switch_to.window(handles[0])
				# jalankan script pada tab awal
				# ...
				is_running = False
			except:
				WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchPetugasPenerima')))
				ppenerima = driver.find_element(By.ID, 'searchPetugasPenerima')
				ppenerima.click()
				ppenerima.send_keys(Petugaspenerima)
				WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchPetugasPenerima0')))
				driver.find_element(By.XPATH, "//li[contains(.,'"+ Petugaspenerima +"')]").click()
@mark.fixture_penerimaan
def test_PNM_17():
	Log.info('Melakukan Pencarian data Petugas yang menyerahkan')
	driver.find_element(By.ID, 'nama_penyerah'	 ).send_keys(Namapetugasyangmenyerahkan) 
	driver.find_element(By.ID, 'nip_penyerah'	 ).send_keys(NIPNRPPetugasyangMenyerahkan) 
	driver.find_element(By.ID, 'pangkat_penyerah').send_keys(PangkatGolonganPetugas) 
	driver.find_element(By.ID, 'jabatan_penyerah').send_keys(JabatanPetugas) 
@mark.fixture_penerimaan
def test_PNM_18():
	Log.info('Melakukan Pencarian data Identitas WBP')
	tahanan = driver.find_element(By.ID, 'searchIdentitas-0')
	tahanan.click()
	WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'searchIdentitas-00')))
	driver.find_element(By.XPATH, "//li[contains(.,'"+ IdentitasWBP +"')]").click()
@mark.fixture_penerimaan
def test_PNM_19():		
	Log.info('klik tab Petugas Instansi yang Menyerahkan')
	driver.find_element(By.ID, "tab-petugas_instansi").click()
	Log.info('input data  Petugas Instansi Yang menyerahkan')
	driver.find_element(By.ID, 'nama_menyerahkan-0').send_keys(Namasaksipenyerah) 
	driver.find_element(By.ID, 'nip_menyerahkan-0' ).send_keys(NipNrpsaksiinstansipenyerh) 
@mark.fixture_penerimaan
def test_PNM_20():	
	Log.info('Klik tab Saksi Penerima')
	driver.find_element(By.ID, "tab-saksi_penerimaan").click()
	Log.info('melakukan pencarian data petugas saksi penerimaan')
@mark.fixture_penerimaan
def test_PNM_21():	
	ppenerima = driver.find_element(By.ID, 'searchSaksi-0')
	ppenerima.click()
	ppenerima.send_keys(SaksiPenerimaan)
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchSaksi-00')))
	driver.find_element(By.ID, 'searchSaksi-00').click()
@mark.fixture_penerimaan
def test_PNM_22():	
	Log.info('Klik tab Dokument')
	driver.find_element(By.ID, "tab-dokumen_files").click()
	Log.info('melakukan Verifikasi dokumen yang diupload')
	driver.find_element(By.ID, "verifikasi").click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'simpanVerifikasi')))
	inputpasswordverif = driver.find_element(By.ID, 'passwordVerifikasi')
	is_filled = inputpasswordverif.get_attribute("value") !=""
	if is_filled :
		pass
	else:
		inputpasswordverif.send_keys(environ.get("PASSSPV"))
	driver.find_element(By.ID, "simpanVerifikasi").click()
	WebDriverWait(driver, 50).until_not(EC.presence_of_element_located((By.ID, "simpanVerifikasi")))
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'pilihDokumenFile0')))
	driver.find_element(By.ID, "pilihDokumenFile0").click()
	time.sleep(3)
	pyautogui.write(r'C:\Users\user\Documents\TRCH\Automationpython\SDP\assets\FilePDF\restitusi.pdf')
	pyautogui.press('enter')
	driver.find_element(By.ID, 'keteranganDokumen-0').send_keys(Keterangandkumen) 
@mark.fixture_penerimaan
def test_PNM_23():
	Log.info('menekan button submit')
	driver.find_element(By.ID, "submitButton").click()
	WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
#############################################################################################################################
# barang = wb['Barangbasan']
# y = 2

# nama_barang					= barang['A'+str(y)].value  
# barang_temuan					= barang['B'+str(y)].value  
# jenis_barang					= barang['C'+str(y)].value  
# satuan						= barang['D'+str(y)].value  
# jumlah_baik					= barang['E'+str(y)].value  
# jumlah_rusak_ringan 			= barang['F'+str(y)].value  
# jumlah_rusak_berat			= barang['G'+str(y)].value  
# namafoto1						= barang['H'+str(y)].value  
# keteranfanfoto1				= barang['I'+str(y)].value  
# NomorPenelitian				= barang['J'+str(y)].value  
# TanggalPenelitian				= barang['K'+str(y)].value  
# NomorSKPeneliti				= barang['L'+str(y)].value  
# TanggalSKPeneliti				= barang['M'+str(y)].value  
# GOLONGAN						= barang['N'+str(y)].value  
# KeadaanSegelPenyita			= barang['O'+str(y)].value  
# KondisiBarang					= barang['P'+str(y)].value  
# SubKondisiBarang				= barang['Q'+str(y)].value  
# Sifat							= barang['R'+str(y)].value  
# MerekDanKondisi				= barang['S'+str(y)].value  
# Berat							= barang['T'+str(y)].value  
# VolumeCC						= barang['U'+str(y)].value 
# Panjang						= barang['V'+str(y)].value 
# Lebar							= barang['W'+str(y)].value 
# Tinggi						= barang['X'+str(y)].value 
# Laras							= barang['Y'+str(y)].value 
# TipeMerek						= barang['Z'+str(y)].value 
# PembuatPabrik					= barang['AA'+str(y)].value 
# NomorPabrik					= barang['AB'+str(y)].value 
# Peluru						= barang['AC'+str(y)].value 
# BahanPeledak					= barang['AD'+str(y)].value 
# SenpiDikeuarkanOleh			= barang['AE'+str(y)].value 
# TanggalKeluar					= barang['AF'+str(y)].value 
# NomorDikeluarkan				= barang['AG'+str(y)].value 
# TanggalBerlaku				= barang['AH'+str(y)].value 
# NomorSenpi					= barang['AI'+str(y)].value 
# KomposisiBahan				= barang['AJ'+str(y)].value 
# Kaliber						= barang['AK'+str(y)].value 
# Warna							= barang['AL'+str(y)].value 
# NomorMesin					= barang['AM'+str(y)].value 
# TahunPembuatan				= barang['AN'+str(y)].value 
# TahunPengeluaranPenerbitan	= barang['AO'+str(y)].value 
# NomorChasis					= barang['AP'+str(y)].value 
# TeganganDaya					= barang['AQ'+str(y)].value 
# MerekSumberDaya				= barang['AR'+str(y)].value 
# Pegangan				    	= barang['AS'+str(y)].value 
# TulisanHurufGambar			= barang['AT'+str(y)].value 
# AsalBasanDari					= barang['AU'+str(y)].value 
# PerkiraanUsia					= barang['AV'+str(y)].value 
# KadarKarat					= barang['AW'+str(y)].value 
# Kemasan						= barang['AX'+str(y)].value 
# Batasan						= barang['AY'+str(y)].value 
# NoIMB							= barang['AZ'+str(y)].value 
# IsiGedung						= barang['BA'+str(y)].value 
# SuratBukti					= barang['BB'+str(y)].value 
# BenderaNegara					= barang['BC'+str(y)].value 
# NoPolisi						= barang['BD'+str(y)].value 
# WarnaTNKB						= barang['BE'+str(y)].value 
# MasaBerlakuTNKB				= barang['BF'+str(y)].value 
# BahanBakar					= barang['BG'+str(y)].value 
# CiriKhusus					= barang['BH'+str(y)].value 
# HalLainnya					= barang['BI'+str(y)].value 
# PemeliharaanKhusus			= barang['BJ'+str(y)].value 
# CatatanPemeliharaanKhusus		= barang['BK'+str(y)].value 
# RekomendasiTimPeneliti		= barang['BL'+str(y)].value 
# Petugas1						= barang['BM'+str(y)].value 
# TanggalPenilaian				= barang['BN'+str(y)].value 
# NomorBAPenelitian				= barang['BO'+str(y)].value 
# NilaiSatuanBarang				= barang['BP'+str(y)].value 
# Keterangan					= barang['BQ'+str(y)].value 
# PetugasPenilai1				= barang['BR'+str(y)].value 
































































