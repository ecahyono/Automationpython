from Register.src import *
from Register.indikator import *
# init driver by os
@mark.fixture_penolakan
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Memasukan User name dan Password di halaman Login')
	bapasbdg(driver)

@mark.fixture_penolakan
def testpenolakan():
  Log.info('Menambah Data Register Penolakan')
  driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/penolakan')
  turu(driver)
  # WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonCari')))
  lagiloading(driver)
  driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[8]/div/div/div[2]/a/button').click()


@mark.fixture_penolakan
def testformeditpenolakan():
  lagiloading(driver)
  driver.find_element(By.ID, 'tab-2').click()
  driver.find_element(By.ID, 'uploadBeritaAcaraPenolakan').click()
  time.sleep(3)
  pyautogui.write(environ.get(r'FILEPDF'))
  pyautogui.press('enter')

  driver.find_element(By.ID, 'komen').send_keys('Komentar Upload Dokumen Penolakan')

  driver.find_element(By.ID, 'tambah_foto').click()
  namafotonya = driver.find_element(By.ID, 'namaFoto0')
  namafotonya.click()
  namafotonya.send_keys(Keys.DOWN)
  namafotonya.send_keys(Keys.ENTER)
  namafotonya = driver.find_element(By.ID, 'namaFoto1')
  namafotonya.click()
  namafotonya.send_keys(Keys.DOWN)
  namafotonya.send_keys(Keys.ENTER)

  asalsuratnya = driver.find_element(By.ID, 'dropdownSurat')
  asalsuratnya.click()
  klikasalsurat = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By. ID, 'surat0')))
  klikasalsurat.click()
  driver.find_element(By.ID, "noSurat0").send_keys('nosurat1')
  tglsuratpernth = driver.find_element(By.ID, "TglSurat0")
  tglsuratpernth.send_keys('2023-07-06')
  tglsuratpernth.send_keys(Keys.ENTER)
  driver.find_element(By.ID, 'keterangann0').send_keys('perihalsurat1')

  driver.find_element(By.ID, "noSurat1").send_keys('nosurat2')
  tglsuratpernth = driver.find_element(By.ID, "TglSurat1")
  tglsuratpernth.send_keys('2023-07-06')
  tglsuratpernth.send_keys(Keys.ENTER)
  driver.find_element(By.ID, 'keterangann1').send_keys('perihalsurat1')

