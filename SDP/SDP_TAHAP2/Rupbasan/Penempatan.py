
@mark.fixture_penempatan
def test_PTN_001():
	Log.info('Mengakses menu  Penempatan dengan memilih modul Rupbasan kemudian pilih menu Penempatan')
	Penempatan(driver)
	Log.info('membuka halaman tambah dengan menekan button tambah')
	driver.find_element(By. ID, 'createButton').click()
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'cariNoReg')))
	attach(data=driver.get_screenshot_as_png())

PTN = wb['Penempatan']
u = 2

tglpenempatan 		= PTN['B'+str(u)].value #Tanggal Penempatan
pilihtersangka  	= PTN['C'+str(u)].value #Pilih Tersangka
gudang 				= PTN['D'+str(u)].value #Gudang
sektorgudang 		= PTN['E'+str(u)].value #Sektor Gudang
barisraklemari 		= PTN['F'+str(u)].value #Baris/Rak/Lemari
nourut 				= PTN['G'+str(u)].value #No Urut
keterangan  		= PTN['H'+str(u)].value #Keterangan

@mark.fixture_penempatan
def test_PTN_003_1():
	Log.info('Mencari nomor registrasi')
	noreg = driver.find_element(By.ID, 'cariNoReg')
	noreg.click()
	print('Menunggu loading "Memuat"')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'cariNoReg0')))
	# noreg.send_keys(Keys.UP)
	driver.find_element(By.ID, 'cariNoReg0').click()
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_penempatan
def test_PTN_003_1esr():
	Log.info('Mencari nama Barang')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'dropdownPilihBarang')))
	nabar = driver.find_element(By.ID, 'dropdownPilihBarang')
	nabar.click()
	nabar.send_keys(namabarang)
	print('Menunggu loading "Memuat"')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'barangOption-0')))
	driver.find_element(By.ID, 'barangOption-0').click()
	attach(data=driver.get_screenshot_as_png())
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
	print('Menunggu loading "Memuat"')
	WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.ID, 'tersangkaOption-0')))
	driver.find_element(By.ID, "tersangkaOption-0").click()
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_penempatan
def test_PTN_003_4():
	Log.info('Memilih Gudang untuk barang')
	
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
	
	Log.info('menekan button submit data penempatan')
	driver.find_element(By.ID, "submitButton").click()