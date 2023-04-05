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
	oprupbasaninternal(driver)
@mark.fixture_penerimaan
def testaksesmenu():
	Log.info('Mengakses Halaman Penerimaan')
	Penerimaan(driver)
	Log.info('Mengakses Halaman Tambah')
	driver.find_element(By.ID, 'createButton').click()

penerimaan = wb['TambahubahPenerimaan']
i = 2
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
	ppenerima = driver.find_element(By.ID, 'searchPetugasPenerima')
	ppenerima.click()
	# ppenerima.send_keys(Petugaspenerima)
	WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'searchPetugasPenerima0')))
	driver.find_element(By.ID, 'searchPetugasPenerima0').click()
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
	driver.find_element(By.ID, 'searchIdentitas-00').click()
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
	# ppenerima.send_keys(SaksiPenerimaan)
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
	if platform.system() == 'Darwin':
		pyautogui.write('/Users/will/Documents/work/Automationpython/SDP/assets/FilePDF/restitusi.pdf')
	elif platform.system() == 'Windows':
		pyautogui.write(r'C:\Users\user\Documents\TRCH\Automationpython\SDP\assets\FilePDF\restitusi.pdf')
	pyautogui.press('enter')
	driver.find_element(By.ID, 'keteranganDokumen-0').send_keys(Keterangandkumen) 
@mark.fixture_penerimaan
def test_PNM_23():
	Log.info('menekan button submit')
	driver.find_element(By.ID, "submitButton").click()
	WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
###########################################################################################################################
barang = wb['Barangbasan']
y = 15

namabarang					= barang['A'+str(y)].value  
barang_temuan				= barang['B'+str(y)].value  
jenis_barang				= barang['C'+str(y)].value  
satuan						= barang['D'+str(y)].value  
jumlah_baik					= barang['E'+str(y)].value  
jumlah_rusak_ringan 		= barang['F'+str(y)].value  
jumlah_rusak_berat			= barang['G'+str(y)].value  
namafoto1					= barang['H'+str(y)].value  
keteranfanfoto1				= barang['I'+str(y)].value  
NomorPenelitian				= barang['J'+str(y)].value  
TanggalPenelitian			= barang['K'+str(y)].value  
NomorSKPeneliti				= barang['L'+str(y)].value  
TanggalSKPeneliti			= barang['M'+str(y)].value  
GOLONGAN					= barang['N'+str(y)].value  
KeadaanSegelPenyita			= barang['O'+str(y)].value  
KondisiBarang				= barang['P'+str(y)].value  
SubKondisiBarang			= barang['Q'+str(y)].value  
Sifat						= barang['R'+str(y)].value  
MerekDanKondisi				= barang['S'+str(y)].value  
Berat						= barang['T'+str(y)].value  
VolumeCC					= barang['U'+str(y)].value 
Panjang						= barang['V'+str(y)].value 
Lebar						= barang['W'+str(y)].value 
Tinggi						= barang['X'+str(y)].value 
Laras						= barang['Y'+str(y)].value 
TipeMerek					= barang['Z'+str(y)].value 
PembuatPabrik				= barang['AA'+str(y)].value 
NomorPabrik					= barang['AB'+str(y)].value 
Peluru						= barang['AC'+str(y)].value 
BahanPeledak				= barang['AD'+str(y)].value 
SenpiDikeuarkanOleh			= barang['AE'+str(y)].value 
TanggalKeluar				= barang['AF'+str(y)].value 
NomorDikeluarkan			= barang['AG'+str(y)].value 
TanggalBerlaku				= barang['AH'+str(y)].value 
NomorSenpi					= barang['AI'+str(y)].value 
KomposisiBahan				= barang['AJ'+str(y)].value 
Kaliber						= barang['AK'+str(y)].value 
Warna						= barang['AL'+str(y)].value 
NomorMesin					= barang['AM'+str(y)].value 
ThnPembuatan				= barang['AN'+str(y)].value 
TahunPengeluaranPenerbitan	= barang['AO'+str(y)].value 
NomorChasis					= barang['AP'+str(y)].value 
TeganganDaya				= barang['AQ'+str(y)].value 
MerekSumberDaya				= barang['AR'+str(y)].value 
Pengarang				    = barang['AS'+str(y)].value 
TulisanHurufGambar			= barang['AT'+str(y)].value 
AsalBasanDari				= barang['AU'+str(y)].value 
PerkiraanUsia				= barang['AV'+str(y)].value 
KadarKarat					= barang['AW'+str(y)].value 
Kemasan						= barang['AX'+str(y)].value 
Batasan						= barang['AY'+str(y)].value 
NoIMB						= barang['AZ'+str(y)].value 
IsiGedung					= barang['BA'+str(y)].value 
SuratBukti					= barang['BB'+str(y)].value 
BenderaNegara				= barang['BC'+str(y)].value 
NoPolisi					= barang['BD'+str(y)].value 
WarnaTNKB					= barang['BE'+str(y)].value 
MasaBerlakuTNKB				= barang['BF'+str(y)].value 
BahanBakar					= barang['BG'+str(y)].value 
CiriKhusus					= barang['BH'+str(y)].value 
HalLainnya					= barang['BI'+str(y)].value 
PemeliharaanKhusus			= barang['BJ'+str(y)].value 
CatatanPemeliharaanKhusus	= barang['BK'+str(y)].value 
RekomendasiTimPeneliti		= barang['BL'+str(y)].value 
Peneliti1					= barang['BM'+str(y)].value 
TanggalPenilaian			= barang['BN'+str(y)].value 
NoBAPenelitian				= barang['BO'+str(y)].value 
NilaiSatuanBarang			= barang['BP'+str(y)].value 
Keterangan					= barang['BQ'+str(y)].value 
PetugasPenilai1				= barang['BR'+str(y)].value 

@mark.fixture_penerimaan
def test_PNM_BRG_1():
	Log.info('Menampilkan halaman detail penerimaan serta daftar barang baran dan basan')
	driver.find_element(By. ID, 'daftarBarangButton').click()
	try:
		wait = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//span[@class='el-table__empty-text']")))
		if wait.text == 'Tidak ada data':
			# jalankan script Anda di sini
			print('Tidak ada data yang tersedia, melanjutkan proses input Barang baru')
		else:
			WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "buttonDetail0")))
			print('Data tersedia,  menambahkan Barang di penerimaan ini')
	except NoSuchElementException:
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_2():
	Log.info('Nama barang')
	driver.find_element(By.ID, 'nama_barang').send_keys(namabarang)  # Nama Barang
@mark.fixture_penerimaan
def test_PNM_BRG_3():
	Log.info('checkbox barang temuan')
	if barang_temuan == 'Iya':
		driver.find_element(By.ID, 'barang_temuan').click()
	else:
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_4():
	Log.info('Memilih jenis barang basan')
	driver.find_element(By.ID, 'input_jenis_baran_basan').click()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'JSB1')))
	driver.find_element(By.XPATH, "//li[contains(.,'"+ jenis_barang +"')]").click()
@mark.fixture_penerimaan
def test_PNM_BRG_5():
	Log.info('Memilih satuan barang')
	driver.find_element(By.ID, 'input_satuan_baran_basan').click()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, '01')))
	driver.find_element(By.XPATH, "//li[contains(.,'"+ satuan +"')]").click()
	if  satuan == 'Lain - Lain':
		Log.info('Menginputkan satuan lain')
		driver.find_element(By.ID, 'SATUAN LAIN').click()
		driver.find_element(By.ID, 'satuan_lain').send_keys(satuan)
@mark.fixture_penerimaan
def test_PNM_BRG_6():
	Log.info('Jumlah Baik, Rusak Ringan, Rusak Berat')
	driver.find_element(By.ID, 'jumlah_baik').send_keys(jumlah_baik)  # jumlah_baik
	driver.find_element(By.ID, 'jumlah_rusak_ringan').send_keys(jumlah_rusak_ringan)  # jumlah rusak ringan
	driver.find_element(By.ID, 'jumlah_rusak_berat').send_keys(jumlah_rusak_berat)  # jumlah Rusak Berat
@mark.fixture_penerimaan
def test_PNM_BRG_9():
	Log.info('upload foto barang 1')
	driver.find_element(By.ID, 'pilihFoto0').click()
	time.sleep(3)
	if platform.system() == 'Darwin':
		pyautogui.write('/Users/will/Documents/work/Automationpython/SDP/assets/Filefoto/barang_impor.jpg')
	elif platform.system() == 'Windows':
		pyautogui.write(environ.get(r"BARANG"))
	pyautogui.press('enter')
	# driver.find_element(By.ID,'namaFoto0').send_keys(foto1)
	driver.find_element(By.ID, 'keterangann0').send_keys(keteranfanfoto1)

# Penelitian ==============================================================
def test_PNM_BRG_10():
	Log.info('pindah tab')
	driver.find_element(By.ID, 'tab-penelitian').click()
@mark.fixture_penerimaan
def test_PNM_BRG_11():
	Log.info('Nomor Penelitian')
	noPenelitian = driver.find_element(By.ID, 'noPenelitian').send_keys(NomorPenelitian)  # Nomor Penelitian
@mark.fixture_penerimaan
def test_PNM_BRG_12():
	Log.info('tanggal Penelitian')
	penelititgl = driver.find_element(By.ID, 'tglPenelitian')
	is_field = penelititgl.get_attribute("value") !=""
	if is_field :
		pass
	else : 
		penelititgl.click()
		penelititgl.send_keys(TanggalPenelitian)
		penelititgl.send_keys(Keys.ENTER)  # Tanggal Penelitian
@mark.fixture_penerimaan
def test_PNM_BRG_13():
	Log.info('no SK penelitian')
	driver.find_element(By.ID, 'noSkPeneliti').send_keys(NomorSKPeneliti)  # Nomor SK Penelitian
@mark.fixture_penerimaan
def test_PNM_BRG_14():
	Log.info('Tanggal SK Penelitian')
	skpenelititgl = driver.find_element(By.ID, 'tglSkPeneliti')
	is_field = skpenelititgl.get_attribute("value") !=""
	if is_field :
		pass
	else : 
		skpenelititgl.click()
		skpenelititgl.send_keys(tglSkPeneliti)
		skpenelititgl.send_keys(Keys.ENTER)  # Tanggal SK Penelitian
@mark.fixture_penerimaan
def test_PNM_BRG_15():
	# Memilih Golongan
	Log.info('Memilih Golongan')
	driver.find_element(By.ID, 'golongan').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, '001')))
	driver.find_element(By.XPATH, "//li[contains(.,'"+ GOLONGAN +"')]").click()
	if GOLONGAN == 'Lain - Lain':
		driver.find_element(By.ID, 'BASAN LAIN').click()
@mark.fixture_penerimaan
def test_PNM_BRG_16():
	# Kondisi Barang
	Log.info('Kondisi Barang')
	driver.find_element(By.ID, 'kondisiBarang').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'KBB1')))
	driver.find_element(By.XPATH, "//li[contains(.,'"+ KondisiBarang +"')]").click()
	Log.info('Sub Kondisi Barang')
	if KondisiBarang == 'Rusak':
		driver.find_element(By.ID, 'subKondisiBarang').click()
		WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'SKB1')))
		driver.find_element(By.XPATH, "//li[contains(.,'"+ SubKondisiBarang +"')]").click()
	elif KondisiBarang == 'Baik':
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_17():
	try:
		Log.info('input Keadaan segel Penyita')
		driver.find_element(By.ID, 'keadaanSegel').send_keys(KeadaanSegelPenyita)
		Log.info('Input sifat')
		driver.find_element(By.ID, 'sifat').send_keys(Sifat)
		Log.info('input merek dan kondisi')
		driver.find_element(By.ID, 'merekKondisi').send_keys(MerekDanKondisi)
		Log.info('input berat')
		driver.find_element(By.ID, 'berat').send_keys(Berat)  # Berat
		Log.info('input volime')
		driver.find_element(By.ID, 'volumeCc').send_keys(VolumeCC)  # Volume / CC
		Log.info('input panjang')
		driver.find_element(By.ID, 'panjang').send_keys(Panjang)  # Panjang
		Log.info('input lebar')
		driver.find_element(By.ID, 'lebar').send_keys(Lebar)  # Lebar
		Log.info('input Tinggi')
		driver.find_element(By.ID, 'tinggi').send_keys(Tinggi)  # Tinggi
	except NoSuchElementException:
		print('fieldinputan tidak ada untuk Golongan ini')
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_18():
	try :
		Log.info('Input Tipe / Merek')
		tipedanmerek = driver.find_element(By.ID, 'tipeMerek').send_keys(TipeMerek)  # Tipe / Merek
	except NoSuchElementException:
		print('fieldinputan tidak ada untuk Golongan ini')
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_19():
	try:
		Log.info('input Laras')
		driver.find_element(By.ID, 'laras').send_keys(Laras)  # Laras
	except NoSuchElementException:
		print('fieldinputan tidak ada untuk Golongan ini')
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_20():
	try:
		Log.info('input Pembuat Pabrik')
		driver.find_element(By.ID, 'pembuatPabrik').send_keys(PembuatPabrik)  # Pembuat Pabrik
		driver.find_element(By.ID, 'nomorPabrik').send_keys(NomorPabrik)  # Nomor Pabrik
	except NoSuchElementException:
		print('fieldinputan tidak ada untuk Golongan ini')
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_21():
	try:
		Log.info('Nomor Peluru')
		driver.find_element(By.ID, 'peluru').send_keys(Peluru)  
	except NoSuchElementException:
		print('fieldinputan tidak ada untuk Golongan ini')
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_22():
	try:
		Log.info('Nomor Bahan Peledak')
		driver.find_element(By.ID, 'bahanPeledak').send_keys(BahanPeledak)  
	except NoSuchElementException:
		print('fieldinputan tidak ada untuk Golongan ini')
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_23():
	try:
		Log.info('input No Dikeluarkan oleh')
		driver.find_element(By.ID, 'pasDikeluarkanOleh').send_keys(SenpiDikeuarkanOleh) #Nomor Senpi
		Log.info('Nomor Nosenpi')
		driver.find_element(By.ID, 'nmrSenpi').send_keys(NomorSenpi)  
	except NoSuchElementException:
		print('fieldinputan tidak ada untuk Golongan ini')
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_weds():
	try:
		Log.info('input Komposisi Bahan')
		driver.find_element(By.ID, 'komposisiBahan').send_keys(KomposisiBahan)  # Warna
	except NoSuchElementException:
		print('fieldinputan tidak ada untuk Golongan ini')
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_sef():
	try:
		Log.info('input warna')
		driver.find_element(By.ID, 'warna').send_keys(Warna)  # Warna
	except NoSuchElementException:
		print('fieldinputan tidak ada untuk Golongan ini')
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_fsef():
	try:
		Log.info('input NomorMesin')
		driver.find_element(By.ID, 'nmrMesin').send_keys(NomorMesin)  # Nomor Mesin
		Log.info('input NomorChasis')
		driver.find_element(By.ID, 'nmrChasis').send_keys(NomorChasis)  # Nomor Chasis
		Log.info('input TeganganDaya')
		driver.find_element(By.ID, 'teganganDaya').send_keys(TeganganDaya)  # Tegangan Daya
		Log.info('input MerekSumberDaya')
		driver.find_element(By.ID, 'merekSumberDaya').send_keys(MerekSumberDaya)  # Merek Sumber Daya
	except NoSuchElementException:
		print('fieldinputan tidak ada untuk Golongan ini')
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_sd():
	try:
		Log.info('input AsalBasanDari')
		driver.find_element(By.ID, 'asalDari').send_keys(AsalBasanDari)  # Asal Basan Dari
		Log.info('input PerkiraanUsia')
		driver.find_element(By.ID, 'perkiraanUsia').send_keys(PerkiraanUsia)  # Perkiraan Usia
		Log.info('input Batasan')
		driver.find_element(By.ID, 'batasan').send_keys(Batasan)  # Batasan
		Log.info('input NoIMB')
		driver.find_element(By.ID, 'NoImb').send_keys(NoIMB)  # No. IMB
		Log.info('input IsiGedung')
		driver.find_element(By.ID, 'isiGedung').send_keys(IsiGedung)  # Isi Gedung
		Log.info('input SuratBukti')
		driver.find_element(By.ID, 'suratBukti').send_keys(SuratBukti)  # Surat Bukti
		Log.info('input BenderaNegara')
		driver.find_element(By.ID, 'bendera').send_keys(BenderaNegara)  # Bendera Negara
	except NoSuchElementException:
		print('fieldinputan tidak ada untuk Golongan ini')
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_qw():
	try:
		Log.info('input KadarKarat')
		driver.find_element(By.ID, 'kadarKarat').send_keys(KadarKarat)  # Kadar Karat
	except NoSuchElementException:
		print('fieldinputan tidak ada untuk Golongan ini')
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_qopw():
	try:
		Log.info('Nomor Dikeluarkan')
		driver.find_element(By.ID, 'nmr_dikeluarkan').send_keys(NomorDikeluarkan)  # Nomor Dikeluarkan
	except NoSuchElementException:
		print('fieldinputan tidak ada untuk Golongan ini')
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_kiuj():
	try:
		Log.info('input Kemasan')
		driver.find_element(By.ID, 'kemasan').send_keys(Kemasan)  # Kemasan
	except NoSuchElementException:
		print('fieldinputan tidak ada untuk Golongan ini')
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_22hg():
	try :
		Log.info('input Tanggal Keluar')
		tglexit = driver.find_element(By.ID, 'tglKeluar')
		is_field = tglexit.get_attribute("value") !=""
		if is_field :
			pass
		else :  
			tglexit.send_keys(TglKeluar)  # Tanggal Keluar
			tglexit.send_keys(Keys.ENTER)

		Log.info('input Tanggal Berlaku')
		tglberlksenpi = driver.find_element(By.ID, 'tglBerlakuPasSenpi')
		is_field = tglberlksenpi.get_attribute("value") !=""
		if is_field :
			pass
		else :  
			tglberlksenpi.send_keys(TanggalBerlaku)  # Tanggal Berlaku
			tglberlksenpi.send_keys(Keys.ENTER)
	except NoSuchElementException:
		print('fieldinputan tidak ada untuk Golongan ini')
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_22hgfdc():
	try:
		Log.info('input Tahun Pembuatan')
		pembuatanthn = driver.find_element(By.ID, 'tahunPembuatan')
		pembuatanthn.click()
		pembuatanthn.send_keys(ThnPembuatan)  # Tahun Pembuatan
		pembuatanthn.send_keys(Keys.ENTER)
	except NoSuchElementException:
		print('fieldinputan tidak ada untuk Golongan ini')
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_286fhg():	
	try:
		Log.info('input Tahun Penerbitan')
		thnpengeluaran = driver.find_element(By.ID, 'tahunPengeluaranPenerbitan')
		thnpengeluaran.click()
		thnpengeluaran.send_keys(TahunPengeluaranPenerbitan)
		thnpengeluaran.send_keys(Keys.ENTER)
	except NoSuchElementException:
		print('fieldinputan tidak ada untuk Golongan ini')
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_30():
	if GOLONGAN == 'KENDARAAN BERMOTOR':
		Log.info('input No. Polisi')
		driver.find_element(By.ID, 'nomorPolisi').send_keys(NoPolisi)  # No. Polisi
		Log.info('input Warna TNKB')
		driver.find_element(By.ID, 'warnaTnkb').send_keys(WarnaTNKB)  # Warna TNKB
		Log.info('input Masa Berlaku TNKB')
		driver.find_element(By.ID, 'masaBerlakuTnkb').send_keys(MasaBerlakuTNKB)  # Masa Berlaku TNKB
		Log.info('input BahanBakar')
		driver.find_element(By.ID, 'bahanBakar').send_keys(BahanBakar)  # Bahan Bakar
	else:
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_31():
	Log.info('input CiriKhusus')
	driver.find_element(By.ID, 'ciriKhusus').send_keys(CiriKhusus)  # Ciri Khusus
	Log.info('input HalLainnya')
	driver.find_element(By.ID, 'halLainnya').send_keys(HalLainnya)  # Hal Lainnya
	Log.info('input PemeliharaanKhusus')
	if (PemeliharaanKhusus == 'Iya' or PemeliharaanKhusus == 'iya'):
		driver.find_element(By.ID, 'PemeliharaanKhusus').click()
		driver.find_element(By.ID, 'catatanPemeliharaanKhusus').send_keys(CatatanPemeliharaanKhusus)  # Catatan Pemeliharaan Khusus
	elif (PemeliharaanKhusus == 'Tidak' or PemeliharaanKhusus == 'tidak'):
		pass
	driver.find_element(By.ID, 'rekomendasiTimPeneliti').send_keys(RekomendasiTimPeneliti)  # Rekomendasi Tim Peneliti

gmotor = wb['Golongankendaraanbermotor']
g = 3  # barisexel

KunciKontak					= gmotor['A'+str(g)].value
jmlhKunciKontak				= gmotor['B'+str(g)].value
konKunciKontak				= gmotor['C'+str(g)].value
RemoteKunci					= gmotor['D'+str(g)].value
jmlhRemoteKunci				= gmotor['E'+str(g)].value
konRemoteKunc				= gmotor['F'+str(g)].value
CentralLock					= gmotor['G'+str(g)].value
jmlhCentralLock				= gmotor['H'+str(g)].value
konCentralLoc				= gmotor['I'+str(g)].value
PowerWindow					= gmotor['J'+str(g)].value
jmlhPowerWindow				= gmotor['K'+str(g)].value
PowerWindo					= gmotor['L'+str(g)].value
Spion						= gmotor['M'+str(g)].value
jmlhSpion					= gmotor['N'+str(g)].value
konSpion					= gmotor['O'+str(g)].value
Wiper						= gmotor['P'+str(g)].value
jmlhWiper					= gmotor['Q'+str(g)].value
konWiper					= gmotor['R'+str(g)].value
LampuDepan					= gmotor['S'+str(g)].value
jmlhLampuDepan				= gmotor['T'+str(g)].value
konLampuDepan				= gmotor['U'+str(g)].value
SeinDepan					= gmotor['V'+str(g)].value
jmlhSeinDepan				= gmotor['W'+str(g)].value
konSeinDepan				= gmotor['X'+str(g)].value
LampuBelakang				= gmotor['Y'+str(g)].value
jmlhLampuBelakang			= gmotor['Z'+str(g)].value
konLampuBelakang			= gmotor['AA'+str(g)].value
SeinBelakang				= gmotor['AB'+str(g)].value
jmlhSeinBelakang			= gmotor['AC'+str(g)].value
konSeinBelakang				= gmotor['AD'+str(g)].value
LampuVariasi				= gmotor['AE'+str(g)].value
jmlhLampuVariasi			= gmotor['AF'+str(g)].value
konLampuVariasi				= gmotor['AG'+str(g)].value
PintuKanan					= gmotor['AH'+str(g)].value
jmlhPintuKanan				= gmotor['AI'+str(g)].value
konPintuKanan				= gmotor['AJ'+str(g)].value
PintuKiri					= gmotor['AK'+str(g)].value
jmlhPintuKiri				= gmotor['AL'+str(g)].value
konPintuKiri				= gmotor['AM'+str(g)].value
BodyBelakang				= gmotor['AN'+str(g)].value
jmlhBodyBelakang			= gmotor['AO'+str(g)].value
konBodyBelakang				= gmotor['AP'+str(g)].value
BumperDepan					= gmotor['AQ'+str(g)].value
jmlhBumperDepan				= gmotor['AR'+str(g)].value
konBumperDepan				= gmotor['AS'+str(g)].value
BumperBelakang				= gmotor['AT'+str(g)].value
jmlhBumperBelakang			= gmotor['AU'+str(g)].value
konBumperBelakang			= gmotor['AV'+str(g)].value
Accu						= gmotor['AW'+str(g)].value
jmlhAccu					= gmotor['AX'+str(g)].value
konAccu						= gmotor['AY'+str(g)].value
Speedometer					= gmotor['AZ'+str(g)].value
jmlhSpeedometer				= gmotor['BA'+str(g)].value
konSpeedometer				= gmotor['BB'+str(g)].value
Jok							= gmotor['BC'+str(g)].value
jmlhJok						= gmotor['BD'+str(g)].value
konJok						= gmotor['BE'+str(g)].value
AC							= gmotor['BF'+str(g)].value
jmlhAC						= gmotor['BG'+str(g)].value
konAC						= gmotor['BH'+str(g)].value
AudioSound					= gmotor['BI'+str(g)].value
jmlhAudioSound				= gmotor['BJ'+str(g)].value
konAudioSound				= gmotor['BK'+str(g)].value
KarpetBawah					= gmotor['BL'+str(g)].value
jmlhKarpetBawah				= gmotor['BM'+str(g)].value
konKarpetBawah				= gmotor['BN'+str(g)].value
VelgBanRodaDepan			= gmotor['BO'+str(g)].value
jmlhVelgBanRodaDepan		= gmotor['BP'+str(g)].value
konVelgBanRodaDepan			= gmotor['BQ'+str(g)].value
VelgBanRodaBelakang			= gmotor['BR'+str(g)].value
jmlhVelgBanRodaBelakang		= gmotor['BS'+str(g)].value
konVelgBanRodaBelakang		= gmotor['BT'+str(g)].value
BanSerep					= gmotor['BU'+str(g)].value
jmlhBanSerep				= gmotor['BV'+str(g)].value
konBanSerep					= gmotor['BW'+str(g)].value
Dongkrak					= gmotor['BX'+str(g)].value
jumlhDongkrak				= gmotor['BY'+str(g)].value
konDongkrak					= gmotor['BZ'+str(g)].value
KunciKunci					= gmotor['CA'+str(g)].value
jmlhKunciKunci				= gmotor['CB'+str(g)].value
konKunciKunci				= gmotor['CC'+str(g)].value
LogoTulisan					= gmotor['CD'+str(g)].value
jmlhLogoTulisan				= gmotor['CE'+str(g)].value
konLogoTulisan				= gmotor['CF'+str(g)].value
Mesin						= gmotor['CG'+str(g)].value
jmlhMesin					= gmotor['CH'+str(g)].value
konMesin					= gmotor['CI'+str(g)].value
STNK						= gmotor['CJ'+str(g)].value
jmlhSTNK					= gmotor['CK'+str(g)].value
konSTNK						= gmotor['CL'+str(g)].value


@mark.fixture_penerimaan
def test_PNM_BRG_33():
	if (GOLONGAN == 'KENDARAAN BERMOTOR' or GOLONGAN == 'ANGKUTAN (DARAT/LAUT/UDARA)'):
		if KunciKontak == 'Ada':
			driver.find_element(By.ID, 'ketersediaan10').click()
			driver.find_element(By.ID, 'jumlah10').send_keys(jmlhKunciKontak)
			driver.find_element(By.ID, 'kondisi10').send_keys(konKunciKontak)
		else:
			pass
		if RemoteKunci == 'Ada':
			driver.find_element(By.ID, 'ketersediaan11').click()
			driver.find_element(By.ID, 'jumlah11').send_keys(jmlhRemoteKunci)
			driver.find_element(By.ID, 'kondisi11').send_keys(konRemoteKunci)
		else:
			pass
		if CentralLock == 'Ada':
			driver.find_element(By.ID, 'ketersediaan12').click()
			driver.find_element(By.ID, 'jumlah12').send_keys(jmlhCentralLock)
			driver.find_element(By.ID, 'kondisi12').send_keys(konCentralLock)
		else:
			pass
		if PowerWindow == 'Ada':
			driver.find_element(By.ID, 'ketersediaan13').click()
			driver.find_element(By.ID, 'jumlah13').send_keys(jmlhPowerWindow)
			driver.find_element(By.ID, 'kondisi13').send_keys(konPowerWindow)
		else:
			pass
		if Spion == 'Ada':
			driver.find_element(By.ID, 'ketersediaan14').click()
			driver.find_element(By.ID, 'jumlah14').send_keys(jmlhSpion)
			driver.find_element(By.ID, 'kondisi14').send_keys(konSpion)
		else:
			pass
		if Wiper == 'Ada':
			driver.find_element(By.ID, 'ketersediaan15').click()
			driver.find_element(By.ID, 'jumlah15').send_keys(jmlhWiper)
			driver.find_element(By.ID, 'kondisi15').send_keys(konWiper)
		else:
			pass
		if LampuDepan == 'Ada':
			driver.find_element(By.ID, 'ketersediaan16').click()
			driver.find_element(By.ID, 'jumlah16').send_keys(jmlhLampuDepan)
			driver.find_element(By.ID, 'kondisi16').send_keys(konLampuDepan)
		else:
			pass
		if SeinDepan == 'Ada':
			driver.find_element(By.ID, 'ketersediaan17').click()
			driver.find_element(By.ID, 'jumlah17').send_keys(jmlhSeinDepan)
			driver.find_element(By.ID, 'kondisi17').send_keys(konSeinDepan)
		else:
			pass
		if LampuBelakang == 'Ada':
			driver.find_element(By.ID, 'ketersediaan18').click()
			driver.find_element(By.ID, 'jumlah18').send_keys(jmlhLampuBelakang)
			driver.find_element(By.ID, 'kondisi18').send_keys(konLampuBelakang)
		else:
			pass
		if SeinBelakang == 'Ada':
			driver.find_element(By.ID, 'ketersediaan19').click()
			driver.find_element(By.ID, 'jumlah19').send_keys(jmlhSeinBelakang)
			driver.find_element(By.ID, 'kondisi19').send_keys(konSeinBelakang)
		else:
			pass
		if LampuVariasi == 'Ada':
			driver.find_element(By.ID, 'ketersediaan110').click()
			driver.find_element(By.ID, 'jumlah110').send_keys(jmlhLampuVariasi)
			driver.find_element(By.ID, 'kondisi110').send_keys(konLampuVariasi)
		else:
			pass
		if PintuKanan == 'Ada':
			driver.find_element(By.ID, 'ketersediaan111').click()
			driver.find_element(By.ID, 'jumlah111').send_keys(jmlhPintuKanan)
			driver.find_element(By.ID, 'kondisi111').send_keys(konPintuKanan)
		else:
			pass
		if PintuKiri == 'Ada':
			driver.find_element(By.ID, 'ketersediaan112').click()
			driver.find_element(By.ID, 'jumlah112').send_keys(jmlhPintuKiri)
			driver.find_element(By.ID, 'kondisi112').send_keys(konPintuKiri)
		else:
			pass
		if BodyBelakang == 'Ada':
			driver.find_element(By.ID, 'ketersediaan113').click()
			driver.find_element(By.ID, 'jumlah113').send_keys(jmlhBodyBelakang)
			driver.find_element(By.ID, 'kondisi113').send_keys(konBodyBelakang)
		else:
			pass
		if BumperDepan == 'Ada':
			driver.find_element(By.ID, 'ketersediaan114').click()
			driver.find_element(By.ID, 'jumlah114').send_keys(jmlhBumperDepan)
			driver.find_element(By.ID, 'kondisi114').send_keys(konBumperDepan)
		else:
			pass
		if BumperBelakang == 'Ada':
			driver.find_element(By.ID, 'ketersediaan20').click()
			driver.find_element(By.ID, 'jumlah20').send_keys(jmlhBumperBelakang)
			driver.find_element(By.ID, 'kondisi20').send_keys(konBumperBelakang)
		else:
			pass
		if Accu == 'Ada':
			driver.find_element(By.ID, 'ketersediaan21').click()
			driver.find_element(By.ID, 'jumlah21').send_keys(jmlhAccu)
			driver.find_element(By.ID, 'kondisi21').send_keys(konAccu)
		else:
			pass
		if Speedometer == 'Ada':
			driver.find_element(By.ID, 'ketersediaan22').click()
			driver.find_element(By.ID, 'jumlah22').send_keys(jmlhSpeedometer)
			driver.find_element(By.ID, 'kondisi22').send_keys(konSpeedometer)
		else:
			pass
		if Jok == 'Ada':
			driver.find_element(By.ID, 'ketersediaan23').click()
			driver.find_element(By.ID, 'jumlah23').send_keys(jmlhJok)
			driver.find_element(By.ID, 'kondisi23').send_keys(konJok)
		else:
			pass
		if AC == 'Ada':
			driver.find_element(By.ID, 'ketersediaan24').click()
			driver.find_element(By.ID, 'jumlah24').send_keys(jmlhAC)
			driver.find_element(By.ID, 'kondisi24').send_keys(konAC)
		else:
			pass
		if AudioSound == 'Ada':
			driver.find_element(By.ID, 'ketersediaan25').click()
			driver.find_element(By.ID, 'jumlah25').send_keys(jmlhAudioSound)
			driver.find_element(By.ID, 'kondisi25').send_keys(konAudioSound)
		else:
			pass
		if KarpetBawah == 'Ada':
			driver.find_element(By.ID, 'ketersediaan26').click()
			driver.find_element(By.ID, 'jumlah26').send_keys(jmlhKarpetBawah)
			driver.find_element(By.ID, 'kondisi26').send_keys(konKarpetBawah)
		else:
			pass
		if VelgBanRodaDepan == 'Ada':
			driver.find_element(By.ID, 'ketersediaan27').click()
			driver.find_element(By.ID, 'jumlah27').send_keys(jmlhVelgBanRodaDepan)
			driver.find_element(By.ID, 'kondisi27').send_keys(konVelgBanRodaDepan)
		else:
			pass
		if VelgBanRodaBelakang == 'Ada':
			driver.find_element(By.ID, 'ketersediaan28').click()
			driver.find_element(By.ID, 'jumlah28').send_keys(jmlhVelgBanRodaBelakang)
			driver.find_element(By.ID, 'kondisi28').send_keys(konVelgBanRodaBelakang)
		else:
			pass
		if BanSerep == 'Ada':
			driver.find_element(By.ID, 'ketersediaan29').click()
			driver.find_element(By.ID, 'jumlah29').send_keys(jmlhBanSerep)
			driver.find_element(By.ID, 'kondisi29').send_keys(konBanSerep)
		else:
			pass
		if Dongkrak == 'Ada':
			driver.find_element(By.ID, 'ketersediaan210').click()
			driver.find_element(By.ID, 'jumlah210').send_keys(jmlhDongkrak)
			driver.find_element(By.ID, 'kondisi210').send_keys(konDongkrak)
		else:
			pass
		if KunciKunci == 'Ada':
			driver.find_element(By.ID, 'ketersediaan211').click()
			driver.find_element(By.ID, 'jumlah211').send_keys(jmlhKunciKunci)
			driver.find_element(By.ID, 'kondisi211').send_keys(konKunciKunci)
		else:
			pass
		if LogoTulisan == 'Ada':
			driver.find_element(By.ID, 'ketersediaan212').click()
			driver.find_element(By.ID, 'jumlah212').send_keys(jmlhLogoTulisan)
			driver.find_element(By.ID, 'kondisi212').send_keys(konLogoTulisan)
		else:
			pass
		if Mesin == 'Ada':
			driver.find_element(By.ID, 'ketersediaan213').click()
			driver.find_element(By.ID, 'jumlah213').send_keys(jmlhMesin)
			driver.find_element(By.ID, 'kondisi213').send_keys(konMesin)
		else:
			pass
		if STNK == 'Ada':
			driver.find_element(By.ID, 'ketersediaan214').click()
			driver.find_element(By.ID, 'jumlah214').send_keys(jmlhSTNK)
			driver.find_element(By.ID, 'kondisi214').send_keys(konSTNK)
		else:
			pass
	else:
		pass
@mark.fixture_penerimaan
def test_PNM_BRG_dfnbhtr():
	Log.info('pencarian para prtugas peneliti')
	ptgs1 = driver.find_element(By.ID, 'cariPeneliti0')
	ptgs1.click()
	# ptgs1.send_keys(Peneliti1)
	WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'cariPeneliti00')))
	driver.find_element(By.ID, 'cariPeneliti00').click()

# Penilaian ==============================================================
def test_PNM_BRG_54efg():
	Log.info('pindah tab')
	driver.find_element(By.ID, 'tab-penilaian').click()

	Log.info('input tglPenilaian')
	tglpenilai = driver.find_element(By.ID, 'tglPenilaian') 
	is_field = tglpenilai.get_attribute("value") !=""
	if is_field :
		pass
	else :  
		tglpenilai.send_keys(TglPenilaian)# Tanggal Penilaian
		tglpenilai.send_keys(Keys.ENTER)

	Log.info('input NoBAPenelitian')
	driver.find_element(By.ID, 'noBaPenelitian').send_keys(NoBAPenelitian)

	Log.info('input NilaiSatuanBarang')
	driver.find_element(By.ID, 'nilaiTaksirSatuanBarang').send_keys(NilaiSatuanBarang)

	Log.info('input Keterangan')
	driver.find_element(By.ID, 'keterangan').send_keys(Keterangan)

	Log.info('pencarian prtugas penilai')
	penlai1 = driver.find_element(By.ID, 'cariPenilai0')
	penlai1.click()
	# penlai1.send_keys(PetugasPenilai1)
	WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'cariPenilai00')))
	driver.find_element(By.ID, 'cariPenilai00').click()

@mark.fixture_penerimaan
def test_PNM_BRG_36r():# submit data tambah barang
	Log.info('submit data')
	driver.find_element(By.ID, 'submitButton').click()
	WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'message_1')))
	driver.refresh()
