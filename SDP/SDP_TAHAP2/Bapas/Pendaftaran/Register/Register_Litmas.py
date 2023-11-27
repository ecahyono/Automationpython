from src import *
from fakeoption import *
from Register_Pendampingan import SimpanRegister

# init driver by os
@mark.fixture_Litmas
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Memasukan User name dan Password di halaman Login')
	bapasbdg(driver) #Operator BPS

@mark.fixture_Litmas
def testlitmas():
  Log.info('Menambah Data Register litmas')
  # register_litmas(driver)
  driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/register-litmas')
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonCari')))

@mark.fixture_Litmas
def testdatawbplitmas():
  B = wb['Register Litmas']
  litmas = 16
  while litmas <= len(B['A']):
    UPTOlitmas         = B['A'+str(litmas)].value
    Namanoinduklitmas  = B['B'+str(litmas)].value
    Jenislitmas        = B['C'+str(litmas)].value
    Petpklitmas        = B['E'+str(litmas)].value
    driver.find_element(By.ID, 'createButton').click()
    try:
      Log.info('Memilih UPT')
      time.sleep(3)
      elem = driver.find_element(By. ID, "upt")
      elem.click()
      WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.ID, 'upt0')))
      elem.send_keys(UPTOlitmas)
      klikupt = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,'"+UPTOlitmas+"')]")))
      klikupt.click()
      # driver.find_element(By.XPATH, "//li[contains(.,'"+UPTO+"')]").click()

      Log.info('Memilih WBP')
      elem1 = driver.find_element(By. ID, "nama")
      elem1.click()
      elem1.send_keys(Namanoinduklitmas)
      awal = time.time()
      wbpnya = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "nama0")))
      akhir = time.time()
      lamatunggu = awal - akhir
      Log.info("Waktu yang dibutuhkan: {:.2f} detik".format(abs(lamatunggu)))
      wbpnya.click()
      driver.find_element(By.XPATH, "//*/text()[normalize-space(.)='"+Namanoinduklitmas+"']/parent::*").click()

      Log.info('Melakukan pencarian data WBP')
      time.sleep(3)
      driver.find_element(By.ID, 'findButton').click()
      kop = time.time()
      WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='el-descriptions__cell el-descriptions__content is-bordered-content' and text()='"+Namanoinduklitmas+"']")))
      kip = time.time()
      tungguload = kop - kip
      Log.info("Waktu yang dibutuhkan: {:.2f} detik".format(abs(tungguload)))


      Log.info('memelihi Jenis Litmas')
      jenis = driver.find_element(By.ID, 'dropdownJenisRegistrasi')
      jenis.click()
      time.sleep(2)
      jenis.send_keys(Jenislitmas)
      driver.find_element(By.XPATH, "//li[contains(.,'"+ Jenislitmas+"')]").click()



      Log.info('memelihi Petugas Pendamping')
      time.sleep(2)
      pk = driver.find_element(By.ID, 'searchPetugasPenerima')
      pk.click()
      pk.send_keys(Petpklitmas)
      time.sleep(2)
      petg = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "searchPetugasPenerima0")))
      petg .click()
  

      # driver.find_element(By.ID, 'tambah_foto').click()
      # namafotonya = driver.find_element(By.ID, 'namaFoto2')
      # namafotonya.click()
      # namafotonya.send_keys(Keys.DOWN)
      # namafotonya.send_keys(Keys.ENTER)


      Log.info('UPload surat Perintah')
      driver.find_element(By.ID, 'pilihFoto0').click()
      time.sleep(3)
      pyautogui.write(environ.get(r'FILEPDF'))
      pyautogui.press('enter')

      Log.info('deskripsi surat Perintah')
      asalsuratnya = driver.find_element(By.ID, 'dropdownSurat')
      asalsuratnya.click()
      klikasalsurat = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By. ID, 'surat0')))
      klikasalsurat.click()
      Log.info('input Nomer surat')
      driver.find_element(By.ID, "noSurat0").send_keys(nosurat1)
      Log.info('pilih tanggal surat')
      tglsuratpernth = driver.find_element(By.ID, "TglSurat0")
      tglsuratpernth.send_keys(tglsuratPembimbingan)
      tglsuratpernth.send_keys(Keys.ENTER)
      Log.info('input Perihal surat')
      driver.find_element(By.ID, 'keterangann0').send_keys("perihal surat")

      Log.info('Upload surat permintaan litmas')
      driver.find_element(By.ID, 'pilihFoto1').click()
      time.sleep(3)
      pyautogui.write(environ.get(r'FILEPDF'))
      pyautogui.press('enter')

      Log.info('deskripsi spermintaan litmas')
      driver.find_element(By.ID, "noSurat1").send_keys(nosurat1)
      tgl2 = driver.find_element(By.ID, "TglSurat1")
      tgl2.send_keys(tglsuratPembimbingan)
      tgl2.send_keys(Keys.ENTER)
      driver.find_element(By.ID, 'keterangann1').send_keys("perihal surat")


      # Log.info('Upload surat permintaan litmas')
      # driver.find_element(By.ID, 'pilihFoto2').click()
      # time.sleep(3)
      # pyautogui.write(environ.get(r'FILEPDF'))
      # pyautogui.press('enter')

      # Log.info('deskripsi spermintaan litmas')
      # driver.find_element(By.ID, "noSurat2").send_keys(nosurat1)
      # tgl2 = driver.find_element(By.ID, "TglSurat1")
      # tgl2.send_keys(tglsuratPembimbingan)
      # tgl2.send_keys(Keys.ENTER)
      # driver.find_element(By.ID, 'keterangann2').send_keys("perihal surat")
      SimpanRegister(driver)
      WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonCari')))

    except TimeoutException:
      print('UPSS')
    litmas = litmas + 1
  print ('Beres registerlitmas')