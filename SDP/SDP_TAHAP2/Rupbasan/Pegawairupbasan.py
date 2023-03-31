from my_module import *

# init driver by os
@mark.fixture_pegawai
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver
	# driver = initDriver()
	driver = secondaryinit()
	Log.info('Memasukan User name dan Password di halaman Login')
	# oprupbasanbdg(driver)

@mark.fixture_pegawai
def test_menmabahpetugasrupbasan():
	tambah = wb['Pegawairupbasan']
	inputbaris = 3
	for kolom in tambah.iter_rows(min_row=inputbaris, max_row=inputbaris, values_only=True):
		nip             = kolom[0] 
		nama            = kolom[1] 
		tempatlahir     = kolom[2] 
		tanggallahir    = kolom[3] 
		jeniskelamin    = kolom[4] 
		alamat          = kolom[5] 
		jabatan         = kolom[6] 
		pangkat         = kolom[7] 
		golongan        = kolom[8] 
		bagian          = kolom[9] 
		email           = kolom[10] 
		telepon         = kolom[11] 
		
		Log.info('Mengakses Halaman')
		daftarpegawai(driver)
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
		driver.find_element(By.ID, 'createButton').click()
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'Nip')))
		driver.find_element(By.ID, "Nip").send_keys(nip)
		driver.find_element(By.ID, "Nama").send_keys(nama)
		driver.find_element(By.ID, "tempatLahir").send_keys(tempatlahir)
		tgllhrpgw = driver.find_element(By.ID, "tglLahir")
		tgllhrpgw.send_keys(tanggallahir)
		tgllhrpgw.send_keys(Keys.ENTER)
		driver.find_element(By.ID, "jenisKelamin").click()
		driver.find_element(By.XPATH, "//li[contains(.,'"+ jeniskelamin+"')]").click()
		driver.find_element(By.ID, "Alamat").send_keys(alamat)
		driver.find_element(By.ID, "Jabatan").send_keys(jabatan)
		driver.find_element(By.ID, "Pangkat").send_keys(pangkat)
		driver.find_element(By.ID, "Golongan").send_keys(golongan)
		driver.find_element(By.ID, "Bagian").send_keys(bagian)
		driver.find_element(By.ID, "Email").send_keys(email)
		driver.find_element(By.ID, "Telepon").send_keys(telepon)   
		# driver.find_element(By.ID, 'submitButton').click()

