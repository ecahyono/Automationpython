from src import *
from regisdanverif import *
from fakeoption import *

# init driver by os
@mark.fixture_pendampingan
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Memasukan User name dan Password di halaman Login')
	PKbapas(driver) #Operator BPS

@mark.fixture_pendampingan
def testpendampingan():
  Log.info('Menambah Data Register Pendampingan')
  driver.get('http://kumbang.torche.id:32400/bapas/pendampingan/daftar-pendampingan')
  time.sleep(2)
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'ButtonCari')))

@mark.fixture_pendampingan
def testfiltertabelpk():
  Log.info('Memfilter tabel berdasarkan Jenis Pendampingan')
  driver.find_element(By. ID, "column").click()
  kolom = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.ID, 'jenisPendampinganFil')))
  kolom.click()
  driver.find_element(By.ID,'filterTgl').click()
  time.sleep(2)

@mark.fixture_pendampingan
def testuserPKpendampingan():
  Log.info('memilih Pendampingan apa yang akan di eksekusi')
  peka = input('Pilih Salah satu dari Opsi Berikut: \n'
              '1. Pendampingan \n'
              '2. Diversi \n'
              '3. Sidang \n'
              'Pilih No ----->>>>>>'
              )
  if peka == '1':
    try:
      baris = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'filterPendampingan1')))
      baris.click()
      driver.find_element(By.ID, 'ButtonCari').click()
      time.sleep(2)
      try :
        WebDriverWait(driver, 55).until(EC.element_to_be_clickable((By.ID, 'diProses0')))
        driver.find_element(By.ID, 'diProses0').click()
      except NoSuchElementException:
        print('Tidak ada ')
      WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
      WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

      tglpend = driver.find_element(By.ID, 'tglPendampingan')
      tglpend.send_keys(TanggalPendampingan)
      tglpend.send_keys(Keys.ENTER)
      driver.find_element(By.ID, 'namaPenyidik').send_keys(NamaPenyidik)
      driver.find_element(By.ID, 'resumeBAP').send_keys(ResumeBeritaAcaraPendampingan)
      tglnext = driver.find_element(By.ID, 'tglBerikutnya')
      tglnext.send_keys(TanggalPendampinganBerikutnya)
      tglnext.send_keys(Keys.ENTER)
      layanannext = driver.find_element(By.ID, 'dropdownJenisLayanan')
      layanannext.click()
      layanannext.send_keys(JenisLayananBerikutnya)
      layanannext.send_keys(Keys.DOWN)
      layanannext.send_keys(Keys.ENTER)

      print('Memilih Pk lyanan Berikutnya? jawabannya adalah =' +  PKLayananBerikutnya)
      if PKLayananBerikutnya == 'Iya':
        driver.find_element(By.XPATH, '(.//*[normalize-space(text()) and normalize-space(.)="Tidak"])[2]/preceding::div[1]').click()
        orangpk = driver.find_element(By.ID, 'searchPetugasPenerima')
        orangpk.click()
        orangpk.send_keys('Jarwa')
        nextpk = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchPetugasPenerima0')))
        nextpk.click()
      elif PKLayananBerikutnya == 'Tidak':
        print('Tidak Mmeilih PK Layanan Berikutnya')
      driver.find_element(By.ID, 'catatan').send_keys('Catatan Form Data Pendamping Klien')
      driver.find_element(By.ID, 'pilihFoto0').click()
      time.sleep(3)
      pyautogui.write(environ.get(r'Gambar'))
      pyautogui.press('enter')
      driver.find_element(By.ID, 'keterangann0').send_keys('keterangan pada dokumen')

      # driver.find_element(By.ID, 'selanjutnya1').click()
      # WebDriverWait(driver, 50).until(EC.invisibility_of_element_located((By.ID, 'selanjutnya1')))
      
    except NoSuchElementException:
      print('Pendampingan Sukses')
  elif peka == '2':
    try:
      baris = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'filterPendampingan1')))
      baris.click()
      driver.find_element(By.ID, 'ButtonCari').click()
      time.sleep(2)
      WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.ID, 'diProses0')))
      driver.find_element(By.ID, 'diProses0').click()
      WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
      WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

      tglpend = driver.find_element(By.ID, 'tglPendampingan')
      
      driver.find_element(By.ID, 'tglDiversi').send_keys('11/05/2023 22:25')
      driver.find_element(By.ID, 'PendampingTerakhir').click()
      driver.find_element(By.ID, 'namaPenyidik').send_keys('Andaraga')
      driver.find_element(By.ID, 'pekerjaSosial').send_keys('DONISALAMAN')
      driver.find_element(By.ID, 'penasehatHukum').send_keys('NOIRoh')
      driver.find_element(By.ID, 'korban').send_keys('Korban dalam Keadaan sehat walafiat')
      driver.find_element(By.ID, 'keluargaKorban').send_keys('Keluarga korban ada dirumah')
      driver.find_element(By.ID, 'hasilKesepakatan').send_keys('Hasil Keputusan yang tepat')
      driver.find_element(By.ID, 'hasilPendampingan').send_keys('Hasil hasilPendampingan')
      driver.find_element(By.ID, 'catatan').send_keys('catatan ini opsional')
      try:
        driver.find_element(By. ID, 'dropdownJenisLayanan').click()
        pilihan = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "jenisLayanan0")))
        pilihan.click()
      except NoSuchElementException:
        pass
      
      driver.find_element(By.ID, 'diversiRad0').click()
      driver.find_element(By.ID, 'keterangann0').send_keys('keterangan pada dokumen')
      driver.find_element(By.ID, 'kesepakatanRad0').click()

      driver.find_element(By.ID, 'pilihFoto0').click()
      time.sleep(3)
      pyautogui.write(environ.get(r'Gambar'))
      pyautogui.press('enter')
    
      driver.find_element(By.ID, '')
    except NoSuchElementException:
      print('Pendampingan Sukses')



# def diversi():
#   if peka
#   driver.find_element(By.ID, 'diProses0').click()
#   WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
#   WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
#   driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#   

# def pendampingan():
#   driver.find_element(By. ID, 'tglPendampingan').send_keys('11/05/2023 22:25')
#   driver.find_element(By.ID, 'namaPenyidik').send_keys('Andaraga')
#   driver.find_element(By.ID, 'resumeBAP').send_keys('Andaraga')
#   driver.find_element(By. ID, 'tglBerikutnya').send_keys('11/05/2023')
#   driver.find_element(By.ID, 'dropdownJenisLayanan').send_keys('Andaraga')
#   l8ist = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "jenisLayanan0")))
#   l8ist.click()
#   driver.find_element(By.ID, 'PKberikutnya').click()
#   driver.find_element(By.ID, 'searchPetugasPenerima').click()
#   l8istpk = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "searchPetugasPenerima0")))
#   l8istpk.click()
#   driver.find_element(By.ID, 'catatan').send_keys('Andaraga')

#   driver.find_element(By.ID, 'pilihFoto0').click()
#   time.sleep(3)
#   pyautogui.write(environ.get(r'Gambar'))
#   pyautogui.press('enter')
#   driver.find_element(By.ID, 'keterangann0').send_keys('keterangan pada dokumen')

#   driver.find_element(By.ID, 'selanjutnya1').click()


