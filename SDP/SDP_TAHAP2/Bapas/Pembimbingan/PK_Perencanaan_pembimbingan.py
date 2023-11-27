from src import *
from fakeoption import *
from indikator import *
from Perencanaan_pembimbingan import *
from filterperencanaanpembimbingan import *
from Program_pebimbingan import *

# init driver by os
@mark.fixture_pembimbingan
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Memasukan User name dan Password di halaman Login')
	PKbapas(driver) #Kasie BPS

@mark.fixture_pembimbingan
def testpendampingan():
	Log.info('Menambah Data Register Pendampingan')
	driver.get('http://kumbang.torche.id:32400/bapas/pembimbingan/perencanaan-pembimbingan')
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

@mark.fixture_pembimbingan
def testfiltertablepembimbing():
	filtertabel(driver)
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	klicki(driver)
	try:
		driver.find_element(By.ID, 'jenisKlienButton-0').click()
	except NoSuchElementException:
		print('Elemen ngaco ga bisa di klik')
		
	Log.info('Buka Halaman tambah Perenncanaan Pembimbingan')
	WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
	WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
	turu(driver)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

@mark.fixture_pembimbingan
def testisiform():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'dropdownKepolisian')))
	Log.info('Tambah Perencanaan Pembimbingan')
	polisi = driver.find_element(By.ID, 'dropdownKepolisian')
	polisi.click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'kepolisian0')))
	polisi.send_keys('Polres Bandung')
	polisi.send_keys(Keys.DOWN)
	polisi.send_keys(Keys.ENTER)  
	Log.info('Tambah Perencanaan Pembimbingan')
	jaksa = driver.find_element(By.ID, 'dropdownKejaksaan')
	jaksa.click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'kejaksaan0')))
	jaksa.send_keys('Kejaksaan agung')
	jaksa.send_keys(Keys.DOWN)
	jaksa.send_keys(Keys.ENTER)
	Log.info('Tambah Perencanaan Pembimbingan')
	driver.find_element(By.ID, 'dropdownSarPras').click()
	WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'Pengadilan Negeri')))
	if Radio1 == 'Pengadilan Negeri':
		driver.find_element(By.ID, 'Pengadilan Negeri').click()
		pengnegri = driver.find_element(By.ID, 'dropdownPengadilan')
		pengnegri.click()
		WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'pengadilanNegeri0')))
		pengnegri.send_keys('Bandung')
		driver.find_element(By.ID, 'pengadilanNegeri22').click()
	elif Radio1 == 'Pengadilan Tinggi':
		driver.find_element(By.ID, 'Pengadilan Tinggi').click()
		tinggi = driver.find_element(By.ID, 'dropdownPengadilanTinggi')
		tinggi.click()
		WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'pengadilanTinggi0')))
		driver.find_element(By.ID, 'pengadilanTinggi1').click()
	elif Radio1 == 'Mahkamah Agung':
		driver.find_element(By.ID, 'Mahkamah Agung').click()
		mahkam = driver.find_element(By.ID, 'dropdownMahkamahAgung')
		mahkam.click()
		WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'mahkamahAgung0')))
		driver.find_element(By.ID, 'mahkamahAgung1').click()

@mark.fixture_pembimbingan
def testisiform2():
	rencaanpembimbingan(driver)






















