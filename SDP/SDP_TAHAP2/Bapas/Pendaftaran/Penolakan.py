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
def testpendampingan():
  Log.info('Menambah Data Register Penolakan')
  driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/penolakan')
  turu(driver)
  # WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonCari')))
  driver.find_element(By.ID, 'createButton').click()

@mark.fixture_penolakan
def testcaridatawbp():
  try:
    Log.info('Memilih WBP')
    elem1 = driver.find_element(By. ID, "upt")
    elem1.click()
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.ID, 'upt0')))
    textupt ='Lapas Kelas II A Bogor'
    elem1.send_keys(textupt)
    klikupt = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,'"+textupt+"')]")))
    klikupt.click()
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('Memilih WBP')
    elem1 = driver.find_element(By. ID, "nama")
    elem1.click()
    awal = time.time()
    wbpnya = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "nama0")))
    akhir = time.time()
    lamatunggu = awal - akhir
    Log.info("Waktu yang dibutuhkan: {:.2f} detik".format(abs(lamatunggu)))
    wbpnya.click()
  except NoSuchElementException:
    driver.close()
    driver.quit()

  try:  
    Log.info('Melakukan pencarian data WBP')
    driver.find_element(By.ID, 'findButton').click()
    lagiloading(driver)
  except NoSuchElementException:
    driver.close()
    driver.quit()

@mark.fixture_penolakan
def testformtambahpenolakan():
  driver.find_element(By.ID, 'noPenolakan').send_keys('No-PNL/00')
  driver.find_element(By.ID, 'asalSurat').send_keys('Bandung')
  driver.find_element(By.ID, 'noSurat').send_keys('SRT-No-PNL/00')
  tglsur = driver.find_element(By.ID, 'tglSurat')
  tglsur.click()
  tglsur.send_keys('01/07/2023')
  tglsur.send_keys(Keys.ENTER)
  tgltolak = driver.find_element(By.ID, 'tglPendampingan')
  tgltolak.click()
  tgltolak.send_keys('06/07/2023')
  tgltolak.send_keys(Keys.ENTER)

  alasan = driver.find_element(By.ID, 'alasanPenolakan')
  alasan.click()
  driver.find_element(By.ID, '=tidakMemenuhi').click()
  driver.find_element(By.ID, 'detailPenolakan').send_keys('Ditolak Karena Data WBP/APH tidak Memenuhi syarat')
  simpandatanya(driver)