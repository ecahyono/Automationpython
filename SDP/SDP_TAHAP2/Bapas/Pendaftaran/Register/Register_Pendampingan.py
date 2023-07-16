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
  driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/register-pendampingan')
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonCari')))
  driver.find_element(By.ID, 'createButton').click()

@mark.fixture_pendampingan
def testdatawbppendampingan():
  try:
    Log.info('Memilih UPT')
    elem = driver.find_element(By. ID, "upt")
    elem.click()
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.ID, 'upt0')))
    elem.send_keys(UPTOdamping)
    klikupt = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,'"+UPTOdamping+"')]")))
    klikupt.click()
    # driver.find_element(By.XPATH, "//li[contains(.,'"+UPTO+"')]").click()
  except NoSuchElementException:
    Log.getloger
    driver.close()
    driver.quit()

  try:
    Log.info('Memilih WBP')
    elem1 = driver.find_element(By. ID, "nama")
    elem1.click()
    elem1.send_keys(Namanoinduk)
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
    kop = time.time()
    WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='el-descriptions__cell el-descriptions__content is-bordered-content' and text()='"+Namanoinduk+"']")))
    kip = time.time()
    tungguload = kop - kip
    Log.info("Waktu yang dibutuhkan: {:.2f} detik".format(abs(tungguload)))
    time.sleep(4)
  except NoSuchElementException:
    Log.info('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

@mark.fixture_pendampingan
def testformtambahpendampingan1():
  try:
    Log.info('memelihi Jenis Pendampingan')
    fildjenreg = driver.find_element(By.ID, 'dropdownJenisRegistrasi')
    fildjenreg.click()
    jenisregpen = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By. ID, 'jenisRegistrasi0')))
    driver.find_element(By.XPATH, "//li[contains(.,'"+ JenisPNP+"')]").click()
  except NoSuchElementException:
    Log.info('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()
@mark.fixture_pendampingan
def testformtambahpendampingan2():
  try:
    Log.info('memelihi Kelompok usia')
    if Kelusia == 'Anak':
      driver.find_element(By.ID, 'anak').click()
    elif Kelusia == 'Dewasa':
      driver.find_element(By.ID, 'dewasa').click()
  except NoSuchElementException:
    Log.info('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()
@mark.fixture_pendampingan
def testformtambahpendampingan3():
  try:
    Log.info('memelihi Petugas Pendamping')
    pk = driver.find_element(By.ID, 'searchPetugasPenerima')
    pk.click()
    pk.send_keys(Petpk)
    time.sleep(2)
    petpknya = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "searchPetugasPenerima0")))
    petpknya.click()
  except NoSuchElementException:
    Log.info('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()
@mark.fixture_pendampingan
def testformtambahpendampingan4():
  try:
    Log.info('UPload surat Perintah')
    driver.find_element(By.ID, 'pilihFoto0').click()
    time.sleep(3)
    pyautogui.write(environ.get(r'FILEPDF'))
    pyautogui.press('enter')
  except NoSuchElementException:
    Log.info('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()
@mark.fixture_pendampingan
def testformtambahpendampingan5():
  try:
    Log.info('deskripsi surat Perintah')
    driver.find_element(By.ID, 'dropdownSurat').click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By. ID, 'surat0')))
    driver.find_element(By.XPATH, "//li[contains(.,'"+ asalsurat1+"')]").click()
    Log.info('input Nomer surat')
    driver.find_element(By.ID, "noSurat0").send_keys(nosurat1)
    Log.info('pilih tanggal surat')
    tglsuratpernth = driver.find_element(By.ID, "TglSurat0")
    tglsuratpernth.click()
    tglsuratpernth.send_keys(tglsurat1)
    tglsuratpernth.send_keys(Keys.ENTER)
    Log.info('input Perihal surat')
    driver.find_element(By.ID, 'keterangann0').send_keys(perihalsurat1)
  except NoSuchElementException:
    Log.info('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()
@mark.fixture_pendampingan
def testformtambahpendampingan6():
  try:
    Log.info('Upload surat permintaan pendampingan')
    driver.find_element(By.ID, 'pilihFoto1').click()
    time.sleep(3)
    pyautogui.write(environ.get(r'FILEPDF'))
    pyautogui.press('enter')
  except NoSuchElementException:
    Log.info('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

  try:
    Log.info('deskripsi spermintaan pendampingan')
    driver.find_element(By.ID, 'noSurat1').send_keys(nosurat1)
    tgl2 = driver.find_element(By.ID, 'TglSurat1')
    tgl2.send_keys(tglsurat1)
    tgl2.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'keterangann1').send_keys(perihalsurat2)
  
  except NoSuchElementException:
    Log.info('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()
@mark.fixture_pendampingan
def testformtambahpendampingan7():
  Log.info('Menambah Dokumen')
  driver.find_element(By.ID, 'tambah_foto').click()
  namafotonya = driver.find_element(By.ID, 'namaFoto2')
  namafotonya.click()
  namafotonya.send_keys(Keys.DOWN)
  namafotonya.send_keys(Keys.ENTER)
  try:
    Log.info('Upload surat permintaan pendampingan')
    driver.find_element(By.ID, 'pilihFoto2').click()
    time.sleep(3)
    pyautogui.write(environ.get(r'FILEPDF'))
    pyautogui.press('enter')
  except NoSuchElementException:
    Log.info('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

  try:
    Log.info('deskripsi spermintaan pendampingan')
    driver.find_element(By.ID, 'noSurat2').send_keys(nosurat1)
    tgl2 = driver.find_element(By.ID, 'TglSurat2')
    tgl2.send_keys(tglsurat1)
    tgl2.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'keterangann2').send_keys(perihalsurat2)
  
  except NoSuchElementException:
    Log.info('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

def SimpanRegister(driver):
  try:
    Log.info('Buton simmpan di tekan')
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.ID,'submitButton').click()
    Log.info('menunggu Index Me-Load Data')
    pendingstart = time.time()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'buttonCari')))
    pendingend = time.time()
    lamatunggu = pendingstart - pendingend
    Log.info("Waktu yang dibutuhkan: {:.2f} detik".format(abs(lamatunggu)))
  except NoSuchElementException:
    driver.close()
    driver.quit()