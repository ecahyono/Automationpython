from src import *
# init driver by os
@mark.fixture_penerimaan
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Memasukan User name dan Password di halaman Login')
	bapasbdg(driver)

A = wb['Register Pembimbingan']
g = 2  # barisexel
Namanoinduk                  = A['A'+str(g)].value
NomorSurat                   = A['B'+str(g)].value
TanggalSuratPenolakan       = A['C'+str(g)].value
JenisAlasanPenolakan        = A['D'+str(g)].value
DetilAlasanPenolakan        = A['E'+str(g)].value

@mark.fixture_pendampingan
def testpendampingan():
  Log.info('Menambah Data Register Penolakan')
  driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/penolakan/create')

@mark.fixture_pengawasan
def testcaridatawbp():
  try:
    Log.info('Memilih WBP')
    elem1 = driver.find_element(By. XPATH, "//input[@placeholder='Cari berdasarkan Nama / No Induk']")
    elem1.click()
    elem1.send_keys(Namanoinduk)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*/text()[normalize-space(.)='"+Namanoinduk+"']/parent::*")))
    driver.find_element(By.XPATH, "//*/text()[normalize-space(.)='"+Namanoinduk+"']/parent::*").click()
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:  
    Log.info('Melakukan pencarian data WBP')
    driver.find_element(By.ID, 'findButton').click()
    time.sleep(4)
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  