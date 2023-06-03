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
	PKbapas(driver) #Operator BPS

@mark.fixture_pendampingan
def testpendampingan():
  Log.info('Menambah Data Register Pendampingan')
  driver.get('http://kumbang.torche.id:32400/bapas/pendampingan/daftar-pendampingan')
  time.sleep(1)
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
  global peka
  Log.info('memilih Pendampingan apa yang akan di eksekusi')
  peka = input('Pilih Salah satu dari Opsi Berikut: \n'
              '1. Pendampingan \n'
              '2. Diversi \n'
              '3. Sidang \n'
              'Pilih No ----->>>>>>'
              )
@mark.fixture_pendampingan
def testuserPKpendampinganpendampingn():
  if peka == '1':
    Log.info('Memilih Pendampingan')
    try:
      baris = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'filterPendampingan1')))
      baris.click()
      driver.find_element(By.ID, 'ButtonCari').click()
      time.sleep(2)
      WebDriverWait(driver, 55).until(EC.element_to_be_clickable((By.ID, 'ButtonCari')))
      for i in range(5):
        target_id = f"diProses{i}"
        try:
            yangadadiklick = driver.find_element(By.ID, target_id)
            if yangadadiklick.is_displayed():
              yangadadiklick.click()
            else :
              print('Tombol tidak terbaca bang')
        except NoSuchElementException:
            print(target_id)
      
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

      print('Memilih Pk lyanan Berikutnya? jawabannya adalah =' +  Switchfield)
      if Switchfield == 'Iya':
        driver.find_element(By.XPATH, "//div[2]/div[2]/div[2]/div[2]/div/div/span").click()
        orangpk = driver.find_element(By.ID, 'searchPetugasPenerima')
        orangpk.click()
        orangpk.send_keys('Jarwa')
        nextpk = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchPetugasPenerima0')))
        nextpk.click()
      elif Switchfield == 'tidak':
        print('Tidak Mmeilih PK Layanan Berikutnya')
      time.sleep(1)
      driver.find_element(By.ID, 'catatan').send_keys('Catatan Form Data Pendamping Klien')
      driver.find_element(By.ID, 'pilihFoto0').click()
      time.sleep(3)
      pyautogui.write(environ.get(r'Gambar'))
      pyautogui.press('enter')
      driver.find_element(By.ID, 'keterangann0').send_keys('keterangan pada dokumen')
      Log.info('Menekan tombol Selanjutnya')
      driver.find_element(By.ID, 'selanjutnya1').click()
      lanjut2 = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'selanjutnya2')))
      driver.find_element(By.ID, 'lihatLaporan').click()
      time.sleep(2)
      WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]/div/form[2]/div/iframe')))
      time.sleep(2)
      lanjut2.click()

      driver.find_element(By.ID, 'uploadLaporan').click()
      time.sleep(3)
      pyautogui.write(environ.get(r'FILEPDF'))
      pyautogui.press('enter')
    except NoSuchElementException:
      print('Pendampingan Sukses')
  elif peka == '2':
    Log.info('Memilih Diversi')
    try:
      baris = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'filterDiversi1')))
      baris.click()
      driver.find_element(By.ID, 'ButtonCari').click()
      time.sleep(2)
      WebDriverWait(driver, 55).until(EC.element_to_be_clickable((By.ID, 'ButtonCari')))
      proses1 = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//div[2]/button')))
      proses1.click()
      
      WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
      WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

      tgldiver = driver.find_element(By.ID, 'tglDiversi')
      tgldiver.send_keys(TanggalPendampingan)
      tgldiver.send_keys(Keys.ENTER)

      print('jawabannya adalah =' +  Switchfield)
      if Switchfield == 'Iya':
        driver.find_element(By.XPATH, '//span/div').click()
      elif Switchfield == 'tidak':
        print('Tidak Mmeilih PK Layanan Berikutnya')

      driver.find_element(By.ID, 'namaPenyidik').send_keys(NamaPenyidik)
      driver.find_element(By.ID, 'pekerjaSosial').send_keys(NamaPenyidik)
      driver.find_element(By.ID, 'penasehatHukum').send_keys(NamaPenyidik)
      driver.find_element(By.ID, 'korban').send_keys('Korban dalam Keadaan sehat walafiat')
      driver.find_element(By.ID, 'keluargaKorban').send_keys('Keluarga korban ada dirumah')
      driver.find_element(By.ID, 'hasilKesepakatan').send_keys('Hasil Keputusan yang tepat')
      driver.find_element(By.ID, 'hasilPendampingan').send_keys('Hasil hasilPendampingan')
      driver.find_element(By.ID, 'catatan').send_keys('catatan ini opsional')
      
      if Switchfield == 'Iya':
        driver.find_element(By. XPATH, '//input[@id="dropdownJenisLayanan"]').click()
        pilihan = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "jenisLayanan0")))
        pilihan.click()
      elif Switchfield == 'Tidak':
        print('Tidak di isi')
      
      if TipeLampiran == 'Pendampingan Divers':
        driver.find_element(By.ID, 'diversiRad0').click()
      elif TipeLampiran == 'Pendampingan Pelaksanaan Kesepakatan Diversi':
        driver.find_element(By.ID, 'kesepakatanRad0').click()
      driver.find_element(By.ID, 'keterangann0').send_keys('keterangan pada dokumen')
      driver.find_element(By.ID, 'pilihFoto0').click()
      time.sleep(3)
      pyautogui.write(environ.get(r'Gambar'))
      pyautogui.press('enter')
    
      Log.info('Menekan tombol Selanjutnya')
      driver.find_element(By.ID, 'selanjutnya1').click()
      lanjut2 = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'selanjutnya2')))
      driver.find_element(By.ID, 'lihatLaporan').click()
    except NoSuchElementException:
      print('Pendampingan Sukses')
  elif peka == '3':
    try:
      baris = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'filterSidang1')))
      baris.click()
      driver.find_element(By.ID, 'ButtonCari').click()
      time.sleep(2)
      WebDriverWait(driver, 55).until(EC.element_to_be_clickable((By.ID, 'ButtonCari')))
      proses12 = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//div/div[3]/button')))
      proses12.click()
      WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
      WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

      tingpenga = driver.find_element(By.ID, 'TingkatPengadilan')
      tingpenga.click()
      tingpenga.send_keys(TingkatPengadilan)
      tingpenga.send_keys(Keys.DOWN)
      tingpenga.send_keys(Keys.ENTER)

      tglsidang = driver.find_element(By.ID, 'tglSidang')
      tglsidang.send_keys(TanggalPendampingan)
      tglsidang.send_keys(Keys.ENTER)

      print('jawabnya adalah =' +  Switchfield)
      if Switchfield == 'Iya':
        driver.find_element(By.XPATH, "//div[4]/div/div/span").click()
        driver.find_element(By.ID, 'tuntuanJaksa').send_keys(NamaPenyidik)
        driver.find_element(By.ID, 'putusanHakim').send_keys(NamaPenyidik)
        driver.find_element(By.ID, 'namaHakim').send_keys(NamaPenyidik)
      elif Switchfield == 'tidak':
        print('Tidak Mmeilih PK Layanan Berikutnya')

      driver.find_element(By.ID, 'tuntuanJPU').send_keys(NamaPenyidik)
      driver.find_element(By.ID, 'PekerjaSosial').send_keys(NamaPenyidik)
      driver.find_element(By.ID, 'PenasihatHukum').send_keys(NamaPenyidik)
      driver.find_element(By.ID, 'Panitera').send_keys(NamaPenyidik)
      driver.find_element(By.ID, 'hasilSidang').send_keys(NamaPenyidik)

      tglsidang2 = driver.find_element(By.ID, 'tglSidangSelan')
      tglsidang2.send_keys(TanggalPendampingan)
      tglsidang2.send_keys(Keys.ENTER)
      
      driver.find_element(By.ID, 'pilihFoto0').click()
      time.sleep(3)
      pyautogui.write(environ.get(r'Gambar'))
      pyautogui.press('enter')

      driver.find_element(By.ID, 'catatan').send_keys(NamaPenyidik)
    
      Log.info('Menekan tombol Selanjutnya')
      driver.find_element(By.ID, 'selanjutnya1').click()
      lanjut2 = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'selanjutnya2')))
      driver.find_element(By.ID, 'lihatLaporan').click()
    except NoSuchElementException:
      print('Pendampingan Sukses')