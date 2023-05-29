from src import *
from regisdanverif import *

# init driver by os
@mark.fixture_pendampingan
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Memasukan User name dan Password di halaman Login')
	bapasbdg(driver) #Operator BPS

A = wb['Register Litmas']
UPTO            = A['A'+str(litmas)].value
Namanoinduk     = A['B'+str(litmas)].value
JenisPNP        = A['C'+str(litmas)].value
Petpk           = A['E'+str(litmas)].value
suratperintah   = A['F'+str(litmas)].value
asalsurat1      = A['G'+str(litmas)].value
nosurat1        = A['H'+str(litmas)].value
tglsurat1       = A['I'+str(litmas)].value
perihalsurat1   = A['J'+str(litmas)].value
permintaanpenp  = A['K'+str(litmas)].value
nosurat2        = A['L'+str(litmas)].value
tglsurat2       = A['M'+str(litmas)].value
perihalsurat2   = A['N'+str(litmas)].value


@mark.fixture_pendampingan
def testlitmas():
  Log.info('Menambah Data Register Pendampingan')
  # register_litmas(driver)
  driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/register-litmas')
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonCari')))
  driver.find_element(By.ID, 'createButton').click()

@mark.fixture_pendampingan
def testcaridatawbp():
  try:
    Log.info('Memilih UPT')
    elem = driver.find_element(By. ID, "upt")
    elem.click()
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.ID, 'upt0')))
    elem.send_keys(UPTO)
    klikupt = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,'"+UPTO+"')]")))
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
    # driver.find_element(By.XPATH, "//*/text()[normalize-space(.)='"+Namanoinduk+"']/parent::*").click()
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
  except NoSuchElementException:
    driver.close()
    driver.quit()

@mark.fixture_pendampingan
def testformtambahpendampingan():
  try:
    Log.info('memelihi Jenis Litmas')
    driver.find_element(By.ID, 'dropdownJenisRegistrasi').click()
    driver.find_element(By.XPATH, "//li[contains(.,'"+ JenisPNP+"')]").click()
  except NoSuchElementException:
    driver.close()
    driver.quit()

  try:
    Log.info('memelihi Petugas Pendamping')
    pk = driver.find_element(By.ID, 'searchPetugasPenerima')
    pk.click()
    pk.send_keys(Petpk)
    petg = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "searchPetugasPenerima0")))
    petg .click()
  except NoSuchElementException:
    driver.close()
    driver.quit()

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
    Log.info('deskripsi surat Perintah')
    asalsuratnya = driver.find_element(By.ID, 'dropdownSurat')
    asalsuratnya.click()
    klikasalsurat = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By. ID, 'surat0')))
    klikasalsurat.click()
    Log.info('input Nomer surat')
    driver.find_element(By.ID, "noSurat0").send_keys(nosurat1)
    Log.info('pilih tanggal surat')
    tglsuratpernth = driver.find_element(By.ID, "tglSurat0")
    tglsuratpernth.send_keys(tglsurat1)
    tglsuratpernth.send_keys(Keys.ENTER)
    Log.info('input Perihal surat')
    driver.find_element(By.ID, 'keterangann0').send_keys(perihalsurat1)
  except NoSuchElementException:
    driver.close()
    driver.quit()

  try:
    Log.info('Upload surat permintaan pendampingan')
    driver.find_element(By.ID, 'pilihFoto1').click()
    time.sleep(3)
    pyautogui.write(environ.get(r'FILEPDF'))
    pyautogui.press('enter')
  except NoSuchElementException:
    driver.close()
    driver.quit()

  try:
    Log.info('deskripsi spermintaan pendampingan')
    driver.find_element(By.ID, "noSurat1").send_keys(nosurat1)
    tgl2 = driver.find_element(By.ID, "tglSurat1")
    tgl2.send_keys(tglsurat1)
    tgl2.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'keterangann1').send_keys(perihalsurat2)
  except NoSuchElementException:
    driver.close()
    driver.quit()
