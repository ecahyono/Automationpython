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
	PKbapas(driver) #Kasie BPS

@mark.fixture_pendampingan
def testpendampingan():
  Log.info('Menambah Data Register Pendampingan')
  driver.get('http://kumbang.torche.id:32400/bapas/pendampingan/daftar-pendampingan')
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'ButtonCari')))

@mark.fixture_Edit
def testfilterindx():
  global sr
  driver.find_element(By.ID, 'column').click()
  pilihan = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'jenisPendampinganFil')))
  pilihan.click()
  driver.find_element(By.ID, 'kode_status').click()
  pilihan2 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'LRK')))
  pilihan2.click()
  driver.find_element(By.ID, 'filterTgl').click()

  sr = input('Pilih Status Yang akan diberikan \n'
            '1. Update  Pendampingan Klien \n'
            '2. Update  diversi Klien \n'
            '3. Update  Sidang Klien \n'
            'Pilih Data yang akan di update->>>>:'
            )
  if sr == '1':
    Log.info('Memilih Jenis Pendampingan-> Pendampingan')
    driver.find_element(By.ID, 'filterPendampingan1').click()
    time.sleep(1)
  elif sr == '2':
    Log.info('Memilih Jenis Pendampingan-> Diversi')
    driver.find_element(By.ID, 'filterDiversi1').click()
    time.sleep(1)
  elif sr == '3':
    Log.info('Memilih Jenis Pendampingan-> Sidang')
    driver.find_element(By.ID, 'filterSidang1').click()
    time.sleep(1)
  elif sr == '4':
    print('Tidak Ada Pilihan Tersedia')

  Log.info('Pencarian data dengan memfilter data table')
  driver.find_element(By.ID, 'ButtonCari').click()
  time.sleep(2)
  indx1 = time.time()
  WebDriverWait(driver,85).until(EC.element_to_be_clickable((By.ID, "ButtonCari")))
  indx2 = time.time()
  waktu = indx1 - indx2
  Log.info("Waktu yang dibutuhkan: {:.2f} detik".format(abs(waktu)))
  
@mark.fixture_Edit
def testFormedit():
  if sr == '1':
    Log.info('Membuka Halaman Edit Pendampingan')
    driver.find_element(By.ID, 'updatePendampingan0').click()  
  elif sr == '2':
    Log.info('Membuka Halaman Edit Diversi')
    driver.find_element(By.ID, 'updateDiversi0').click()  
  elif sr == '3':
    Log.info('Membuka Halaman Edit Siang')
    driver.find_element(By.ID, 'updateSidang0').click()  
    print('Tidak Ada Pilihan Tersedia')
  #
  loli = time.time()
  WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
  WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
  popi = time.time()
  waktulit = loli-popi
  Log.info("Waktu yang dibutuhkan: {:.2f} detik".format(abs(waktulit)))
  time.sleep(1)
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  if sr == '1':
    Log.info('Edit Pendampingan')
    tgl = driver.find_element(By.ID, 'tglPendampingan')
    tgl.clear()
    tgl.send_keys(TanggalPendampingan)
    tgl.send_keys(Keys.ENTER)
    filed1 = driver.find_element(By.ID, 'namaPenyidik')
    filed1.clear()
    filed1.send_keys(NamaPenyidik)
    filed2 = driver.find_element(By.ID, 'resumeBAP')
    filed2.clear()
    filed2.send_keys(ResumeBeritaAcaraPendampingan)
    tglnext = driver.find_element(By.ID, 'tglBerikutnya')
    tglnext.clear()
    tglnext.send_keys(TanggalPendampinganBerikutnya)
    tglnext.send_keys(Keys.ENTER)
    layanannext = driver.find_element(By.ID, 'dropdownJenisLayanan')
    layanannext.click()
    layanannext.send_keys(JenisLayananBerikutnya)
    layanannext.send_keys(Keys.DOWN)
    layanannext.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'catatan').send_keys('Catatan Form Data Pendamping Klien')
  elif sr == '2':
    Log.info('Edit Diversi')
    tgldiver = driver.find_element(By.ID, 'tglPendampingan')
    tgldiver.clear()
    tgldiver.send_keys(TanggalPendampingan)
    tgldiver.send_keys(Keys.ENTER)

    Log.info('Untuk Pendampingan Terakhir jawabannya adalah =' +  Switchfield)
    if Switchfield == 'Iya':
      driver.find_element(By.XPATH, '//span/div').click()
    elif Switchfield == 'tidak':
      print('Tidak Mmeilih PK Layanan Berikutnya')

    filed3 = driver.find_element(By.ID, 'namaPenyidik')
    filed3.clear()
    filed3.send_keys(NamaPenyidik)
    filed4 = driver.find_element(By.ID, 'namaSosial')
    filed4.clear()
    filed4.send_keys(NamaPenyidik)
    filed5 = driver.find_element(By.ID, 'namaHukum')
    filed5.clear()
    filed5.send_keys(NamaPenyidik)
    filed6 = driver.find_element(By.ID, 'namaABH')
    filed6.clear()
    filed6.send_keys(NamaPenyidik)
    driver.find_element(By.ID, 'korban').send_keys('Korban dalam Keadaan sehat walafiat')
    # driver.find_element(By.ID, 'keluargaKorban').send_keys('Keluarga korban ada dirumah')
    # driver.find_element(By.ID, 'hasilKesepakatan').send_keys('Hasil Keputusan yang tepat')
    # driver.find_element(By.ID, 'hasilPendampingan').send_keys('Hasil hasilPendampingan')
    driver.find_element(By.ID, 'catatanTambahan').send_keys('catatan ini opsional')
    if Switchfield == 'Iya':
      driver.find_element(By. ID, 'dropdownJenisLayanan').click()
      pilihan = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "jenisLayanan0")))
      pilihan.click()
    elif Switchfield == 'Tidak':
      print('Tidak di isi')
  elif sr == '3':
    Log.info('Edit Siddang')
    tglsidang = driver.find_element(By.ID, 'tglSidang')
    tglsidang.clear()
    tglsidang.send_keys(TanggalPendampingan)
    tglsidang.send_keys(Keys.ENTER)

    tingpenga = driver.find_element(By.ID, 'TingkatPengadilan')
    tingpenga.click()
    tingpenga.send_keys(TingkatPengadilan)
    tingpenga.send_keys(Keys.DOWN)
    tingpenga.send_keys(Keys.ENTER)

    gild1 = driver.find_element(By.ID, 'namaHakim')
    gild1.clear()
    gild1.send_keys(NamaPenyidik)
    gild2 = driver.find_element(By.ID, 'tuntuanJPU')
    gild2.clear()
    gild2.send_keys(NamaPenyidik)
    gild3 = driver.find_element(By.ID, 'namaSosial')
    gild3.clear()
    gild3.send_keys(NamaPenyidik)
    gild4 = driver.find_element(By.ID, 'namaHukum')
    gild4.clear()
    gild4.send_keys(NamaPenyidik)
    gild5 = driver.find_element(By.ID, 'Panitera')
    gild5.clear()
    gild5.send_keys(NamaPenyidik)
    gild6 = driver.find_element(By.ID, 'hasilSidang')
    gild6.clear()
    gild6.send_keys(NamaPenyidik)

    tglsidang2 = driver.find_element(By.ID, 'tglSidangSelan')
    tglsidang2.clear()
    tglsidang2.send_keys(TanggalPendampingan)
    tglsidang2.send_keys(Keys.ENTER)

    driver.find_element(By.ID, 'catatan').send_keys('Catatan Form Data Pendamping Klien')
  elif sr == '4':
    print('Tidak Diinputkan')
  #
  driver.find_element(By.ID, 'tambah_foto').click()
  driver.find_element(By.ID, 'pilihFoto0').click()
  time.sleep(3)
  pyautogui.write(environ.get(r'Gambar'))
  pyautogui.press('enter')
  driver.find_element(By.ID, 'keterangann0').send_keys('keterangan pada Update dokumen')
  driver.find_element(By.ID, 'pilihFoto1').click()
  time.sleep(3)
  pyautogui.write(environ.get(r'Gambar'))
  pyautogui.press('enter')
  driver.find_element(By.ID, 'keterangann1').send_keys('keterangan pada Update dokumen')
  driver.find_element(By.ID, 'tab-2').click()

# @mark.fixture_verifikasi
# def testpilihopsiverif():
#   pass
#   # driver.find_element(By.ID, 'submitButton').click()