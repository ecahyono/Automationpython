from src import *

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
g = 2  # barisexel
UPTO            = A['A'+str(g)].value
Namanoinduk     = A['B'+str(g)].value
JenisPNP        = A['C'+str(g)].value
# Kelusia         = A['D'+str(g)].value
Petpk           = A['E'+str(g)].value
suratperintah   = A['F'+str(g)].value
asalsurat1      = A['G'+str(g)].value
nosurat1        = A['H'+str(g)].value
tglsurat1       = A['I'+str(g)].value
perihalsurat1   = A['J'+str(g)].value
permintaanpenp  = A['K'+str(g)].value
nosurat2        = A['L'+str(g)].value
tglsurat2       = A['M'+str(g)].value
perihalsurat2   = A['N'+str(g)].value


@mark.fixture_pendampingan
def testpendampingan():
  driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/register-litmas/create')
  Log.info('Menambah Data Register Pendampingan')

@mark.fixture_pendampingan
def testcaridatawbp():
  try:
    elem = driver.find_element(By. XPATH, "//input[@placeholder='Pilih upt']")
    elem.click()
    time.sleep(2)
    elem.send_keys(UPTO)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,'"+UPTO+"')]")))
    driver.find_element(By.XPATH, "//li[contains(.,'"+UPTO+"')]").click()
    Log.info('Memilih UPT')
  except NoSuchElementException:
    Log.warning('Tidak ada elemen tersedia')
    Log.getloger
    driver.close()
    driver.quit()

  try:
    elem1 = driver.find_element(By. XPATH, "//input[@placeholder='Cari berdasarkan Nama / No Induk']")
    elem1.click()
    elem1.send_keys(Namanoinduk)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*/text()[normalize-space(.)='"+Namanoinduk+"']/parent::*")))
    driver.find_element(By.XPATH, "//*/text()[normalize-space(.)='"+Namanoinduk+"']/parent::*").click()
    Log.info('Memilih WBP')
  except NoSuchElementException:
    Log.warning('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

  try:  
    driver.find_element(By.ID, 'findButton').click()
    WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='el-descriptions__cell el-descriptions__content is-bordered-content' and text()='"+Namanoinduk+"']")))
    Log.info('Melakukan pencarian data WBP')
  except NoSuchElementException:
    Log.warning('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

@mark.fixture_pendampingan
def testformtambahpendampingan():
  try:
    driver.find_element(By.ID, 'dropdownJenisRegistrasi').click()
    driver.find_element(By.XPATH, "//li[contains(.,'"+ JenisPNP+"')]").click()
    Log.info('memelihi Jenis Litmas')
  except NoSuchElementException:
    Log.warning('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

  try:
    pk = driver.find_element(By.ID, 'searchPetugasPenerima')
    pk.click()
    pk.send_keys(Petpk)
    petg = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "searchPetugasPenerima0")))
    petg .click()
    Log.info('memelihi Petugas Pendamping')
  except NoSuchElementException:
    Log.warning('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

  try:
    driver.find_element(By.ID, 'pilihFoto0').click()
    time.sleep(3)
    pyautogui.write(environ.get(r'FILEPDF'))
    pyautogui.press('enter')
    Log.info('UPload surat Perintah')
  except NoSuchElementException:
    Log.warning('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

  try:
    driver.find_element(By.ID, 'dropdownSurat').click()
    driver.find_element(By.XPATH, "//*/text()[normalize-space(.)='"+asalsurat1+"']/parent::*").click()
    Log.info('deskripsi surat Perintah')
    driver.find_element(By.ID, "noSurat0").send_keys(nosurat1)
    Log.info('input Nomer surat')
    tglsuratpernth = driver.find_element(By.ID, "tglSurat0")
    tglsuratpernth.send_keys(tglsurat1)
    tglsuratpernth.send_keys(Keys.ENTER)
    Log.info('pilih tanggal surat')
    driver.find_element(By.ID, 'keterangann0').send_keys(perihalsurat1)
    Log.info('input Perihal surat')
  except NoSuchElementException:
    Log.warning('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

  try:
    driver.find_element(By.ID, 'pilihFoto1').click()
    time.sleep(3)
    pyautogui.write(environ.get(r'FILEPDF'))
    pyautogui.press('enter')
    Log.info('Upload surat permintaan pendampingan')
  except NoSuchElementException:
    Log.warning('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

  try:
    driver.find_element(By.ID, "noSurat1").send_keys(nosurat1)
    tgl2 = driver.find_element(By.ID, "tglSurat1")
    tgl2.send_keys(tglsurat1)
    tgl2.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'keterangann1').send_keys(perihalsurat2)
    Log.info('deskripsi spermintaan pendampingan')
  
  except NoSuchElementException:
    Log.warning('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

