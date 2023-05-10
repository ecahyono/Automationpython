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

A = wb['Register Pendampingan']
g = 3  # barisexel
UPTO            = A['A'+str(g)].value
Namanoinduk     = A['B'+str(g)].value

JenisPNP        = A['C'+str(g)].value
Kelusia         = A['D'+str(g)].value
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
  Log.info('Menambah Data Register Pendampingan')
  driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/register-pendampingan/create')

@mark.fixture_pendampingan
def testcaridatawbp():
  try:
    Log.info('Memilih UPT')
    elem = driver.find_element(By. XPATH, "//input[@placeholder='Pilih upt']")
    elem.click()
    time.sleep(2)
    elem.send_keys(UPTO)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,'"+UPTO+"')]")))
    driver.find_element(By.XPATH, "//li[contains(.,'"+UPTO+"')]").click()
  except NoSuchElementException:
    Log.info('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

  try:
    Log.info('Memilih WBP')
    elem1 = driver.find_element(By. XPATH, "//input[@placeholder='Cari berdasarkan Nama / No Induk']")
    elem1.click()
    elem1.send_keys(Namanoinduk)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*/text()[normalize-space(.)='"+Namanoinduk+"']/parent::*")))
    driver.find_element(By.XPATH, "//*/text()[normalize-space(.)='"+Namanoinduk+"']/parent::*").click()
  except NoSuchElementException:
    Log.info('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

  try:  
    Log.info('Melakukan pencarian data WBP')
    driver.find_element(By.ID, 'findButton').click()
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '')))
    time.sleep(4)
  except NoSuchElementException:
    Log.info('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

@mark.fixture_pendampingan
def testformtambahpendampingan():
  try:
    Log.info('memelihi Jenis Pendampingan')
    driver.find_element(By.ID, 'dropdownJenisRegistrasi').click()
    driver.find_element(By.XPATH, "//li[contains(.,'"+ JenisPNP+"')]").click()
  except NoSuchElementException:
    Log.info('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

  try:
    Log.info('memelihi Kelompok usia')
  except NoSuchElementException:
    Log.info('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

  try:
    Log.info('memelihi Petugas Pendamping')
    pk = driver.find_element(By.ID, 'searchPetugasPenerima')
    pk.click()
    pk.send_keys(Petpk)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*/text()[normalize-space(.)='"+Petpk+"']/parent::*")))
    driver.find_element(By.XPATH, "//*/text()[normalize-space(.)='"+Petpk+"']/parent::*").click()
  except NoSuchElementException:
    Log.info('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

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

  try:
    Log.info('deskripsi surat Perintah')
    driver.find_element(By.ID, 'dropdownSurat').click()
    driver.find_element(By.XPATH, "//*/text()[normalize-space(.)='"+asalsurat1+"']/parent::*").click()
    Log.info('input Nomer surat')
    driver.find_element(By.XPATH, "//input[@placeholder='Masukkan No Surat Permintaann Pendampingan']").send_keys(nosurat1)
    Log.info('pilih tanggal surat')
    tglsuratpernth = driver.find_element(By.XPATH, "//input[@placeholder='Tgl Surat ']")
    tglsuratpernth.click()
    tglsuratpernth.send_keys(tglsurat1)
    tglsuratpernth.send_keys(Keys.ENTER)
    Log.info('input Perihal surat')
    driver.find_element(By.ID, 'keterangann0').send_keys(perihalsurat1)
  except NoSuchElementException:
    Log.info('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()

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
  #   driver.find_element(By.XPATH, "//input[@placeholder='Masukkan No Surat Permintaann Pendampingan']").send_keys(nosurat1)
  #   driver.find_element(By.XPATH, "//input[@placeholder='Masukkan No Surat Permintaann Pendampingan']").send_keys(tglsurat1)
    driver.find_element(By.ID, 'keterangann1').send_keys(perihalsurat2)
  
  except NoSuchElementException:
    Log.info('Tidak ada elemen tersedia')
    driver.close()
    driver.quit()
    