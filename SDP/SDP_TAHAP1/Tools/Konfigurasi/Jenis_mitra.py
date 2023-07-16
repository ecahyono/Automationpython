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
  driver.get('http://kumbang.torche.id:32400/tools/daftar-referensi/jenis-mitra')
  # WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
  # driver.find_element(By.ID, 'createButton').click()

@mark.fixture_Tools
def testtoolstambahjenismitra():
	for i in range(6):
		driver.find_element(By.ID, "createButton").click()
		time.sleep(2)
		try:
			driver.find_element(By. XPATH, "//input[@placeholder='Masukkan Jenis Mitra']").send_keys(jenis_mitra)
			driver.find_element(By. XPATH, "//textarea[@placeholder='Masukkan Catatan']").send_keys(CacatTubuh)
		except NoSuchElementException:
			print('Tidak ada element')
		driver.find_element(By.ID, "submitButton").click()
	print ("Success Created")