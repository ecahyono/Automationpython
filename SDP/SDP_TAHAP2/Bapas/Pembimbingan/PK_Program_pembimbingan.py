from src import *
from fakeoption import *
from indikator import *
from Perencanaan_pembimbingan import *
from filterperencanaanpembimbingan import *
from Program_pebimbingan import *
from Sesiterakhirbimbingan import *

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
def testmasuk():
	Log.info('Menambah Data Register Pendampingan')
	driver.get('http://kumbang.torche.id:32400/bapas/pembimbingan/perencanaan-pembimbingan')
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

@mark.fixture_pembimbingan
def testisiformprogrampembimbingan():
	programpembimbingan(driver)

	pilihsesi = input(' Apakah Ini sesi terakhir??? \n'
										'1. Iya \n '
										'2. Tidak \n'
										'Masukan Nomor Pilihan Anda : ')
	if pilihsesi == '1':
		driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]/div/form/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/span').click()
		sesiakhir(driver)
		perkembanganklienn(driver)
	else:
		pass

#selanjutnya
	driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div/button').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div/button[1]')))
#cetak
	driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div/button[1]').click()
	selanjut = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div/button[2]')))
	selanjut.click()

	driver.find_element(By.ID, 'pilihFoto').click()
	lamaturu(driver)
	pyautogui.write(environ.get(r'FILEPDF'))
	pyautogui.press('enter') 

	driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[4]/div/button').click()
	WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
