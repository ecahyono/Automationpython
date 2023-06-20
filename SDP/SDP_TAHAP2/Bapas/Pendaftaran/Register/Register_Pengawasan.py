from src import *
from fakeoption  import *

# init driver by os
@mark.fixture_pengawasan
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Memasukan User name dan Password di halaman Login')
	bapasbdg(driver) #Operator BPS

@mark.fixture_pengawasan
def testpengawasan():
  Log.info('Menambah Data Register pengawasan')
  driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/register-pengawasan/')
  # WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonCari')))
  driver.find_element(By.ID, 'createButton').click()

@mark.fixture_pengawasan
def testcaridatawbp():
  try:
    Log.info('Memilih UPT')
    elem = driver.find_element(By. ID, "upt")
    elem.click()
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.ID, 'upt0')))
    elem.send_keys(UPTOawas)
    klikupt = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,'"+UPTOawas+"')]")))
    klikupt.click()
  except NoSuchElementException:
    Log.getloger
    driver.close()
    driver.quit()

  try:
    Log.info('Memilih WBP')
    elem1 = driver.find_element(By. ID, "nama")
    elem1.click()
    elem1.send_keys(NoregNamapengawasan)
    awal = time.time()
    wbpnya = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "nama0")))
    akhir = time.time()
    lamatunggu = awal - akhir
    Log.info("Waktu yang dibutuhkan: {:.2f} detik".format(abs(lamatunggu)))
    wbpnya.click()
  except NoSuchElementException:
    driver.close()
    driver.quit()

  try:  
    Log.info('Melakukan pencarian data WBP, menunggu loading detail WBP')
    driver.find_element(By.ID, 'findButton').click()
    kop = time.time()
    WebDriverWait(driver, 55).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='el-descriptions__cell el-descriptions__content is-bordered-content' and text()='"+NoregNamapengawasan+"']")))
    kip = time.time()
    tungguload = kop - kip
    Log.info("Waktu yang dibutuhkan: {:.2f} detik".format(abs(tungguload)))
  except NoSuchElementException:
    driver.close()
    driver.quit()

@mark.fixture_pendampingan
def testformtambahpengawasan():
  try:
    Log.info('memelihi Jenis Klien')
    jereg = driver.find_element(By.ID, 'dropdownJenisRegistrasi')
    jereg.click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "jenisRegistrasi0")))
    jereg.send_keys(jenispengawasn)
    driver.find_element(By.XPATH, "//li[contains(.,'"+jenispengawasn+"')]").click()
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('memelihi Petugas Pendamping')
    pk = driver.find_element(By.ID, 'searchPetugasPenerima')
    pk.send_keys(CariPetugaspengawsan)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "searchPetugasPenerima0")))
    driver.find_element(By.ID, 'searchPetugasPenerima0').click()
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')
  
  try:
    Log.info('UPload surat Perintah')
    driver.find_element(By.ID, 'pilihFoto0').click()
    time.sleep(3)
    pyautogui.write(environ.get(r'FILEPDF'))
    pyautogui.press('enter')
  except NoSuchElementException:
    driver.close()
    driver.quit()

  try:
    Log.info('input Nomer surat')
    driver.find_element(By.ID, "noSurat0").send_keys(nosurat1)
    Log.info('pilih tanggal surat')
    tglsuratpernth = driver.find_element(By.ID, "TglSurat0")
    tglsuratpernth.send_keys(tglsurat1)
    tglsuratpernth.send_keys(Keys.ENTER)
    Log.info('input Perihal surat')
    driver.find_element(By.ID, 'keterangann0').send_keys(perihalsurat1)
  except NoSuchElementException:
    print('eror')

@mark.fixture_pendampingan
def testmenyimpanhasilinput():
  try: 
    Log.info('menuimpan Register Pengawasan')
    driver.find_element(By.ID, 'submitButton').click()
  except NoSuchElementException:
    print ('gagal simpan')