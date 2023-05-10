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

A = wb['Register Pembimbingan']
g = 2  # barisexel
UPTO                        = A['A'+str(g)].value
NoregNama                   = A['B'+str(g)].value
jenisKlien                  = A['C'+str(g)].value
JenisPembimbingan           = A['D'+str(g)].value
DasarPembimbingan           = A['E'+str(g)].value
TglAwalBimbingan            = A['F'+str(g)].value
TglAkhirBimbignan           = A['G'+str(g)].value
CariPetugas                 = A['H'+str(g)].value
SuratDasarPembimbingan      = A['I'+str(g)].value
Asalsurat                   = A['J'+str(g)].value
Nosurat1                    = A['K'+str(g)].value
Nosurat1                    = A['L'+str(g)].value   
Perihalsurat1               = A['M'+str(g)].value   
SuratPengantarPenyerahan    = A['N'+str(g)].value   
BeritaAcaraSerahTerimaKlien = A['R'+str(g)].value
SuratPerintah               = A['V'+str(g)].value

@mark.fixture_pendampingan
def testpendampingan():
  Log.info('Menambah Data Register Pendampingan')
  driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/register-pembimbingan/create')

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
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('Memilih WBP')
    elem1 = driver.find_element(By. XPATH, "//input[@placeholder='Cari berdasarkan Nama / No Induk']")
    elem1.click()
    elem1.send_keys(NoregNama)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*/text()[normalize-space(.)='"+NoregNama+"']/parent::*")))
    driver.find_element(By.XPATH, "//*/text()[normalize-space(.)='"+NoregNama+"']/parent::*").click()
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

@mark.fixture_pendampingan
def testformtambahpendampingan():
  try:
    Log.info('memelihi Jenis Klien')
    jereg = driver.find_element(By.ID, 'dropdownJenisRegistrasi')
    jereg.click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "jenisRegistrasi0")))
    jereg.send_keys(jenisKlien)
    driver.find_element(By.XPATH, "//li[contains(.,'"+jenisKlien+"')]").click()
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('memelihi Jenis Pembimbingan')
    jenpembi = driver.find_element(By.ID, 'dropdownJenisPembimbingan')
    jenpembi.send_keys(JenisPembimbingan)
    jenpembi.send_keys(Keys.DOWN)
    jenpembi.send_keys(Keys.ENTER)
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
    tglaawal = driver.find_element(By. XPATH, "//input[@placeholder='Pilih Tgl Awal Bimbingan']")
    tglaawal.click()
    tglaawal.send_keys(TglAwalBimbingan)
    tglaawal.send_keys(Keys.ENTER)
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('Tgl Akir nimbingan')
    tglakhir = driver.find_element(By. XPATH, "//input[@placeholder='Pilih Tgl Akhir Bimbingan']")
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
    pk.send_keys(CariPetugas)
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
    pyautogui.write(SuratDasarPembimbingan)
    pyautogui.press('enter')
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('deskripsi SuratDasarPembimbingan')
    driver.find_element(By.ID, 'dropdownSurat').click()
    driver.find_element(By.XPATH, "//*/text()[normalize-space(.)='"+Asalsurat+"']/parent::*").click()
    Log.info('input Nomer surat')
    driver.find_element(By.XPATH, "//input[@placeholder='Masukkan No Surat Permintaann Pendampingan']").send_keys(Nosurat1)
    Log.info('pilih tanggal surat')
    tglsuratpernth = driver.find_element(By.XPATH, "//input[@placeholder='Tgl Surat ']")
    tglsuratpernth.click()
    time.sleep(1)
    tglsuratpernth.send_keys(Nosurat1)
    tglsuratpernth.send_keys(Keys.ENTER)
    Log.info('input Perihal surat')
    driver.find_element(By.ID, 'keterangann0').send_keys(Perihalsurat1)
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('Upload SuratPengantarPenyerahan')
    driver.find_element(By.ID, 'pilihFoto1').click()
    time.sleep(3)
    pyautogui.write(SuratPengantarPenyerahan)
    pyautogui.press('enter')
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('Upload SuratPengantarPenyerahan')
    driver.find_element(By.ID, 'pilihFoto2').click()
    time.sleep(3)
    pyautogui.write(BeritaAcaraSerahTerimaKlien)
    pyautogui.press('enter')
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('Upload SuratPengantarPenyerahan')
    driver.find_element(By.ID, 'pilihFoto3').click()
    time.sleep(3)
    pyautogui.write(SuratPerintah)
    pyautogui.press('enter')
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

  try:
    Log.info('deskripsi SuratPengantarPenyerahan')
  #   driver.find_element(By.XPATH, "//input[@placeholder='Masukkan No Surat Permintaann Pendampingan']").send_keys(nosurat1)
  #   driver.find_element(By.XPATH, "//input[@placeholder='Masukkan No Surat Permintaann Pendampingan']").send_keys(tglsurat1)
    driver.find_element(By.ID, 'keterangann1').send_keys(Perihalsurat1)
    driver.find_element(By.ID, 'keterangann2').send_keys(Perihalsurat1)
    driver.find_element(By.ID, 'keterangann3').send_keys(Perihalsurat1)
  except NoSuchElementException:
    driver.close()
    driver.quit()
    Log.info('Tidak ada elemen tersedia')

