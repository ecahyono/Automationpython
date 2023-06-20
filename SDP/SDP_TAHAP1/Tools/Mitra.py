from src import *
from data import *
# init driver by os
@mark.fixture_Tools
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Memasukan User name dan Password di halaman Login')
	bapasbdg(driver) #Operator BPS

@mark.fixture_Tools
def testtools1():
  Log.info('Menambah Data Register Pendampingan')
  driver.get('http://kumbang.torche.id:32400/tools/mitra')
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
  # driver.find_element(By.ID, 'createButton').click()

@mark.fixture_Tools
def testtoolstambahmitra():
	for i in range(6):
		driver.find_element(By.ID, "createButton").click()
		time.sleep(2)
		try:
			driver.find_element(By.ID, "inputNamaMitra").send_keys(NamaAlias1)                                    
			driver.find_element(By.ID, "inputPenanggungJawab").send_keys(NamaAlias2)                                                                     
			driver.find_element(By.ID, "inputAlamat").send_keys(AlamatRumah)
			provin = driver.find_element(By.ID, "selectProvinsi")
			provin.click()
			time.sleep(2)
			provin.send_keys('Jawa Barat')
			provin.send_keys(Keys.DOWN)
			provin.send_keys(Keys.ENTER)
			kota = driver.find_element(By.ID, "selectKota")
			kota.click()
			time.sleep(2)
			kota.send_keys(Keys.DOWN)
			kota.send_keys(Keys.ENTER)
			driver.find_element(By.ID, "inputNoTelepon").send_keys(Telepon)
			driver.find_element(By.ID, "inputNoHp").send_keys(Telepon)
			driver.find_element(By.ID, "inputNoHp").send_keys(AlamatRumah)
			driver.find_element(By.ID, "inputEmail").send_keys(inputEmail)
			status = driver.find_element(By.ID, "selectStatusBnsp")
			status.send_keys(Keys.DOWN)
			status.send_keys(Keys.ENTER)
			driver.find_element(By.ID, "inputAktePendirian").send_keys('Akte Pendirian')
			driver.find_element(By.ID, "inputKeterangan").send_keys('Keterangan Mitra Yang Ditambahkan Otomatis')
																	
			#Submit
			driver.find_element(By.ID, "createButton").click()
			WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'selectJenisMitra')))
			jeninya = driver.find_element(By.ID, "selectJenisMitra")
			jeninya.click()
			jeninya.send_keys(Keys.DOWN)
			jeninya.send_keys(Keys.ENTER)
			time.sleep(2)
			driver.find_element(By. XPATH, "//input[@placeholder='Masukkan Nomor Kontrak']").send_keys('Nama Kontrak')
			tanggalkontrak = driver.find_element(By. XPATH, "//input[@placeholder='Kontrak Awal']")
			tanggalkontrak.click()
			tanggalkontrak.send_keys('01/01/2023')
			tanggalkontrak.send_keys(Keys.ENTER)
			tanggalkontrak2 = driver.find_element(By. XPATH, "//input[@placeholder='Kontrak Akhir']")
			tanggalkontrak2.send_keys('30/12/2023')
			tanggalkontrak2.send_keys(Keys.ENTER)

			driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/form/div[4]/div/div/div/button').click()
			time.sleep(3)
			pyautogui.write(environ.get(r'FILEPDF'))
			pyautogui.press('enter')

			driver.find_element(By.ID, "submitButton").click()
			time.sleep(2)
			driver.find_element(By.ID, "submitButton").click()
		except NoSuchElementException:
			driver.stop()
			driver.close()
		time.sleep(5)   
		i = i + 1
	print ("Success Created")