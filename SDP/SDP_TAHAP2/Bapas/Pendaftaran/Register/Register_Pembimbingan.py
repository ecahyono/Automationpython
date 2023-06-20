from src import *
from fakeoption import *

# init driver by os
@mark.fixture_pendampingan
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Memasukan User name dan Password di halaman Login')
	bapasbdg(driver) #Operator BPS

@mark.fixture_pendampingan
def testpendampingan():
  Log.info('Menambah Data Register Pendampingan')
  driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/register-pembimbingan')
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonCari')))
  driver.find_element(By.ID, 'createButton').click()

@mark.fixture_pendampingan
def testcaridatawbp():
  try:
    Log.info('Memilih UPT')
    elem = driver.find_element(By. ID, "upt")
    elem.click()
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.ID, 'upt0')))
    elem.send_keys(UPTObimbingan)
    klikupt = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,'"+UPTObimbingan+"')]")))
    klikupt.click()
  except NoSuchElementException:
    Log.getloger
    driver.close()
    driver.quit()

  try:
    Log.info('Memilih WBP')
    elem1 = driver.find_element(By. ID, "nama")
    elem1.click()
    elem1.send_keys(NoregNamabimbingan)
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
    Log.info('Melakukan pencarian data WBP, menunggu loading detail WBP')
    driver.find_element(By.ID, 'findButton').click()
    kop = time.time()
    WebDriverWait(driver, 35).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='el-descriptions__cell el-descriptions__content is-bordered-content' and text()='"+NoregNamabimbingan+"']")))
    kip = time.time()
    tungguload = kop - kip
    Log.info("Waktu yang dibutuhkan: {:.2f} detik".format(abs(tungguload)))
  except NoSuchElementException:
    driver.close()
    driver.quit()

@mark.fixture_pendampingan
def testformtambahpendampingan():
  try:
    Log.info('memelihi Jenis Klien')
    jereg = driver.find_element(By.ID, 'dropdownJenisRegistrasi')
    jereg.click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "jenisRegistrasi0")))
    jereg.send_keys(jenisKlienPembimbingan)
    driver.find_element(By.XPATH, "//li[contains(.,'"+jenisKlienPembimbingan+"')]").click()
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('memelihi Dasar Pembimbingan')
    driver.find_element(By.ID, 'dropdownDasarPembimbingan').click()
    WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//li[contains(.,'"+ DasarPembimbingan+"')]").click()
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('Tgl awal Bimbingan')
    tglaawal = driver.find_element(By. ID, "tglAwalBimbingan")
    tglaawal.click()
    tglaawal.send_keys(TglAwalBimbingan)
    tglaawal.send_keys(Keys.ENTER)
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('Tgl Akir nimbingan')
    tglakhir = driver.find_element(By. ID, "tglAkhirBimbingan")
    tglakhir.click()
    tglakhir.send_keys(TglAkhirBimbignan)
    tglakhir.send_keys(Keys.ENTER)
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('memelihi Petugas Pendamping')
    pk = driver.find_element(By.ID, 'searchPetugasPenerima')
    pk.send_keys(CariPetugasPembimbingan)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "searchPetugasPenerima0")))
    driver.find_element(By.ID, 'searchPetugasPenerima0').click()
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')
  
  try:
    Log.info('Upload SuratDasarPembimbingan')
    driver.find_element(By.ID, 'pilihFoto0').click()
    time.sleep(3)
    pyautogui.write(environ.get(r'FILEPDF'))
    pyautogui.press('enter')
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('deskripsi SuratDasarPembimbingan')
    driver.find_element(By.ID, 'dropdownSurat').click()
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.ID, 'surat0')))
    driver.find_element(By.ID, 'dropdownSurat').send_keys(AsalsuratPembimbingan)
    driver.find_element(By.XPATH, "//li[contains(.,'"+ AsalsuratPembimbingan+"')]").click()
    Log.info('input Nomer surat')
    driver.find_element(By.ID, "noSurat0").send_keys(Nosurat1Pembimbingan)
    Log.info('pilih tanggal surat')
    tglsuratpernth = driver.find_element(By.ID, "TglSurat0")
    tglsuratpernth.send_keys(tglsuratPembimbingan)
    tglsuratpernth.send_keys(Keys.ENTER)
    Log.info('input Perihal surat')
    driver.find_element(By.ID, 'keterangann0').send_keys(Perihalsurat1Pembimbingan)
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('Upload SuratPengantarPenyerahan')
    driver.find_element(By.ID, 'pilihFoto1').click()
    time.sleep(3)
    pyautogui.write(environ.get(r'FILEPDF'))
    pyautogui.press('enter')
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('Upload SuratPengantarPenyerahan')
    driver.find_element(By.ID, 'pilihFoto2').click()
    time.sleep(3)
    pyautogui.write(environ.get(r'FILEPDF'))
    pyautogui.press('enter')
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('Upload SuratPengantarPenyerahan')
    driver.find_element(By.ID, 'pilihFoto3').click()
    time.sleep(3)
    pyautogui.write(environ.get(r'FILEPDF'))
    pyautogui.press('enter')
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('Upload SuratPengantarPenyerahan')
    driver.find_element(By.ID, 'pilihFoto4').click()
    time.sleep(3)
    pyautogui.write(environ.get(r'FILEPDF'))
    pyautogui.press('enter')
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('deskripsi SuratPengantarPenyerahan')
    driver.find_element(By.ID, "noSurat1").send_keys(Nosurat1Pembimbingan)
    ltg1 = driver.find_element(By.ID, "TglSurat1")
    ltg1.send_keys(tglsuratPembimbingan)
    ltg1.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'keterangann1').send_keys(Perihalsurat1Pembimbingan)
    
    driver.find_element(By.ID, "noSurat2").send_keys(Nosurat1Pembimbingan)
    ltg2 = driver.find_element(By.ID, "TglSurat2")
    ltg2.send_keys(tglsuratPembimbingan)
    ltg2.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'keterangann2').send_keys(Perihalsurat1Pembimbingan)
    
    driver.find_element(By.ID, "noSurat3").send_keys(Nosurat1Pembimbingan)
    ltg3 = driver.find_element(By.ID, "TglSurat3")
    ltg3.send_keys(tglsuratPembimbingan)
    ltg3.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'keterangann3').send_keys(Perihalsurat1Pembimbingan)
    
    driver.find_element(By.ID, "noSurat4").send_keys(Nosurat1Pembimbingan)
    ltg3 = driver.find_element(By.ID, "TglSurat4")
    ltg3.send_keys(tglsuratPembimbingan)
    ltg3.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'keterangann3').send_keys(Perihalsurat1Pembimbingan)
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

