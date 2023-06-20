from src import *
from fakeoption import *

# init driver by os
@mark.fixture_rencana
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Memasukan User name dan Password di halaman Login')
	PKbapas(driver) #Kasie BPS

@mark.fixture_rencana
def testpendampingan():
	Log.info('Menambah Data Register Pendampingan')
	driver.get('http://kumbang.torche.id:32400/bapas/pembimbingan/perencanaan-pembimbingan')
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

@mark.fixture_rencana
def testfiltertablepembimbing():
	driver.find_element(By. XPATH, "//input[@type='text']").click()
	jenisreg = WebDriverWait(driver, 25).until(EC.element_to_be_clickable(((By.ID, 'jenis_registrasi'))))
	jenisreg.click()
	Katkun = driver.find_element(By.ID, 'dropdownJenisRegistrasi')
	Katkun.click()
	Pilih = input('1. Pembimbingan Diversi \n'
		'2. Pembimbingan Penetapan Bagi Anak Berusia Kurang dari 12 Tahun \n'
		'3. Pembimbingan Penetapan Tindakan Anak \n'
		'4. Pembimbingan Pidana dengan Syarat Anak (pidana pembinaan di luar lembaga) \n'
		'5. Pembimbingan Pidana dengan Syarat Anak (pelayanan masyarakat) \n'
		'6. Pembimbingan Pidana dengan Syarat Anak (pidana pengawasan) \n'
		'7. Pembimbingan Pidana Peringatan Anak \n'
		'8. Pembimbingan Pidana Pelatihan Kerja Anak \n'
		'9. Pembimbingan Asimilasi Anak \n'
		'10. Pembimbingan CB Anak \n'
		'11. Pembimbingan CMB Anak \n'
		'12. Pembimbingan PB Anak \n'
		'13. Pembimbingan Tambahan (After Care) Anak \n'
		'14. Buku Ekspirasi Pembimbingan dan Pengawasan Anak \n'
		'15. Pidana dengan Syarat \n'
		'16. Pembimbingan Asimilasi \n'
		'17. Pembimbingan CB \n'
		'18. Pembimbingan CMB \n'
		'19. Pembimbingan PB \n'
		'20. Pembimbingan Tambahan After Care \n'
		'21. Pembimbingan dan Pengawasan (buku pembantu register) \n'
		'Masukan Nomer yang tersedia diatas--->> :')
	try:
		if Pilih =='1':
			Log.info('Pembimbingan Diversi')
			Katkun.send_keys('Pembimbingan Diversi')
		elif Pilih =='2':
			Log.info('Pembimbingan Penetapan Bagi Anak Berusia Kurang dari 12 Tahun')
			Katkun.send_keys('Pembimbingan Penetapan Bagi Anak Berusia Kurang dari 12 Tahun')
		elif Pilih =='3':
			Log.info('Pembimbingan Penetapan Tindakan Anak')
			Katkun.send_keys('Pembimbingan Penetapan Tindakan Anak')
		elif Pilih =='4':
			Log.info('Pembimbingan Pidana dengan Syarat Anak (pidana pembinaan di luar lembaga)')
			Katkun.send_keys('Pembimbingan Pidana dengan Syarat Anak (pidana pembinaan di luar lembaga)')
		elif Pilih =='5':
			Log.info('Pembimbingan Pidana dengan Syarat Anak (pelayanan masyarakat)')
			Katkun.send_keys('Pembimbingan Pidana dengan Syarat Anak (pelayanan masyarakat)')
		elif Pilih =='6':
			Log.info('Pembimbingan Pidana dengan Syarat Anak (pidana pengawasan)')
			Katkun.send_keys('Pembimbingan Pidana dengan Syarat Anak (pidana pengawasan)')
		elif Pilih =='7':
			Log.info('Pembimbingan Pidana Peringatan Anak')
			Katkun.send_keys('Pembimbingan Pidana Peringatan Anak')
		elif Pilih =='8':
			Log.info('Pembimbingan Pidana Pelatihan Kerja Anak')
			Katkun.send_keys('Pembimbingan Pidana Pelatihan Kerja Anak')
		elif Pilih =='9':
			Log.info('Pembimbingan Asimilasi Anak')
			Katkun.send_keys('Pembimbingan Asimilasi Anak')
		elif Pilih =='10':
			Log.info('Pembimbingan CB Anak')
			Katkun.send_keys('Pembimbingan CB Anak')
		elif Pilih =='11':
			Log.info('Pembimbingan CMB Anak')
			Katkun.send_keys('Pembimbingan CMB Anak')
		elif Pilih =='12':
			Log.info('Pembimbingan PB Anak')
			Katkun.send_keys('Pembimbingan PB Anak')
		elif Pilih =='13':
			Log.info('Pembimbingan Tambahan (After Care) Anak')
			Katkun.send_keys('Pembimbingan Tambahan (After Care) Anak')
		elif Pilih =='14':
			Log.info('Buku Ekspirasi Pembimbingan dan Pengawasan Anak')
			Katkun.send_keys('Buku Ekspirasi Pembimbingan dan Pengawasan Anak')
		elif Pilih =='15':
			Log.info('Pidana dengan Syarat')
			Katkun.send_keys('Pidana dengan Syarat')
		elif Pilih =='16':
			Log.info('Pembimbingan Asimilasi')
			Katkun.send_keys('Pembimbingan Asimilasi')
		elif Pilih =='17':
			Log.info('Pembimbingan CB')
			Katkun.send_keys('Pembimbingan CB')
		elif Pilih =='18':
			Log.info('Pembimbingan CMB')
			Katkun.send_keys('Pembimbingan CMB')
		elif Pilih =='19':
			Log.info('Pembimbingan PB')
			Katkun.send_keys('Pembimbingan PB')
		elif Pilih =='20':
			Log.info('Pembimbingan Tambahan After Care')
			Katkun.send_keys('Pembimbingan Tambahan After Care')
		elif Pilih =='21':
			Log.info('Pembimbingan dan Pengawasan (buku pembantu register)')
			Katkun.send_keys('Pembimbingan dan Pengawasan (buku pembantu register)')
	except NoSuchElementException:
		Log.info('ERORRRRRRRRR')
	Katkun.send_keys(Keys.DOWN)
	Katkun.send_keys(Keys.ENTER)
	driver.find_element(By.ID, "searchButton").click()	
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	time.sleep(5)
	WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.ID, 'jenisKlienButton')))
	try:
		driver.find_element(By.ID, 'jenisKlienButton').click()
	except NoSuchElementException:
		print('Elemen ngaco ga bisa di klik')
	Log.info('Buka Halaman tambah Perenncanaan Pembimbingan')
	WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
	WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
	time.sleep(1)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

@mark.fixture_rencana
def testisiform():
	time.sleep(5)
	Log.info('Tambah Perencanaan Pembimbingan')
	polisi = driver.find_element(By.ID, 'dropdownKepolisian')
	polisi.click()
	time.sleep(2)
	polisi.send_keys('Polres Bandung')
	polisi.send_keys(Keys.DOWN)
	polisi.send_keys(Keys.ENTER)

	Log.info('Tambah Perencanaan Pembimbingan')
	jaksa = driver.find_element(By.ID, 'dropdownKejaksaan')
	jaksa.click()
	time.sleep(2)
	jaksa.send_keys('Kejaksaan agung')
	jaksa.send_keys(Keys.DOWN)
	jaksa.send_keys(Keys.ENTER)
	
	Log.info('Tambah Perencanaan Pembimbingan')
	adil = driver.find_element(By.ID, 'dropdownPengadilan')
	adil.click()
	time.sleep(2)
	adil.send_keys('PENGADILAN TINGGI BANDUNG ')
	adil.send_keys(Keys.DOWN)
	adil.send_keys(Keys.ENTER)

	driver.find_element(By.ID, 'jenisProgramKepribadianRadioButton').click()
	driver.find_element(By.ID, 'jenisProgramKemandirianRadioButton').click()

	driver.find_element(By.ID, 'bentukKegiatanIndividuRadioButton').click()
	driver.find_element(By.ID, 'bentukKegiatanKelompokRadioButton').click()

	driver.find_element(By.ID, 'uraianKegiatan').send_keys('uraianKegiatan')

	tgl_awl = driver.find_element(By.ID, 'tanggalAwalProgram')
	tgl_awl.click()
	tgl_awl.send_keys(Keys.DOWN)
	tgl_awl.send_keys(Keys.ENTER)
	tgl_akh = driver.find_element(By.ID, 'tanggalAkhirProgram')
	tgl_akh.click()
	tgl_akh.send_keys(Keys.DOWN)
	tgl_akh.send_keys(Keys.ENTER)

	mitra = driver.find_element(By.ID, 'dropdownMitra')
	mitra.click()
	mitra.send_keys(Keys.DOWN)
	mitra.send_keys(Keys.ENTER)

	driver.find_element(By.ID, 'modeAbsensiSatuKaliRadioButton').click()
	driver.find_element(By.ID, 'modeAbsensiDuaKaliRadioButton').click()
	
	driver.find_element(By.ID, 'keterangan').send_keys('keterangan')





















