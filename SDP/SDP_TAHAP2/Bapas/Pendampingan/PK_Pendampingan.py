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

@mark.fixture_tamabh
def testfilterindx():
  global peka
  driver.find_element(By.ID, 'column').click()
  pilihan = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'jenisPendampinganFil')))
  pilihan.click()
  driver.find_element(By.ID, 'kode_status').click()
  pilihan2 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'DIS')))
  pilihan2.click()
  driver.find_element(By.ID, 'filterTgl').click()

  peka = input('Pilih Status Yang akan diberikan \n'
            '1. Tambah  Pendampingan Klien \n'
            '2. Tambah  diversi Klien \n'
            '3. Tambah  Sidang Klien \n'
            'Pilih Data yang akan di Tambah->>>>:'
            )
  if peka == '1':
    Log.info('Memilih Jenis Pendampingan-> Pendampingan')
    driver.find_element(By.ID, 'filterPendampingan1').click()
    time.sleep(1)
  elif peka == '2':
    Log.info('Memilih Jenis Pendampingan-> Diversi')
    driver.find_element(By.ID, 'filterDiversi1').click()
    time.sleep(1)
  elif peka == '3':
    Log.info('Memilih Jenis Pendampingan-> Sidang')
    driver.find_element(By.ID, 'filterSidang1').click()
    time.sleep(1)
  elif peka == '4':
    print('Tidak Ada Pilihan Tersedia')

  Log.info('Pencarian data dengan memfilter data table')
  driver.find_element(By.ID, 'ButtonCari').click()
  time.sleep(2)
  indx1 = time.time()
  WebDriverWait(driver,85).until(EC.element_to_be_clickable((By.ID, "ButtonCari")))
  indx2 = time.time()
  waktu = indx1 - indx2
  Log.info("Waktu yang dibutuhkan: {:.2f} detik".format(abs(waktu)))
  
@mark.fixture_tambh
def testFormtambh():
  if peka == '1':
    Log.info('Membuka Halaman  Pendampingan')
    driver.find_element(By.ID, 'PendampinganInput0').click()  
  elif peka == '2':
    Log.info('Membuka Halaman  Diversi')
    driver.find_element(By.ID, 'DiversiInput0').click()  
  elif peka == '3':
    Log.info('Membuka Halaman  Sidang')
    driver.find_element(By.ID, 'SidangInput0').click()  

  WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
  WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  if peka == '1':
    Log.info('Memilih Diversi')
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
  elif peka == '2':
    Log.info('Memilih Diversi')
    tgldiver = driver.find_element(By.ID, 'tglDiversi')
    tgldiver.send_keys(TanggalPendampingan)
    tgldiver.send_keys(Keys.ENTER)

    print('jawabannya adalah ='+Switchfield)
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
    if Switchfield == 'Iya':
      driver.find_element(By. XPATH, '//input[@id="dropdownJenisLayanan"]').click()
      pilihan = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "jenisLayanan0")))
      pilihan.click()
    elif Switchfield == 'Tidak':
      print('Tidak di isi') 
    if TipeLampiran == 'Pendampingan Diversi':
      driver.find_element(By.ID, 'diversiRad0').click()
    elif TipeLampiran == 'Pendampingan Pelaksanaan Kesepakatan Diversi':
      driver.find_element(By.ID, 'kesepakatanRad0').click()
  elif peka == '3':
    Log.info('Memilih sidang')
    tingpenga = driver.find_element(By.ID, 'TingkatPengadilan')
    tingpenga.click()
    tingpenga.send_keys(TingkatPengadilan)
    tingpenga.send_keys(Keys.DOWN)
    tingpenga.send_keys(Keys.ENTER)

    tglsidang = driver.find_element(By.ID, 'tglSidang')
    tglsidang.send_keys(TanggalPendampingan)
    tglsidang.send_keys(Keys.ENTER)

    print('Apakah Sidang Terakhir? jawabnya adalah ==' +Switchfield)
    if Switchfield == 'Iya':
      driver.find_element(By.XPATH, "//div[4]/div/div/span").click()
      driver.find_element(By.ID, 'tuntuanJaksa').send_keys(NamaPenyidik)
      driver.find_element(By.ID, 'putusanHakim').send_keys(NamaPenyidik)
    elif Switchfield == 'tidak':
      print('Tidak Mmeilih PK Layanan Berikutnya')

    driver.find_element(By.ID, 'namaHakim').send_keys(NamaPenyidik)
    driver.find_element(By.ID, 'tuntuanJPU').send_keys(NamaPenyidik)
    driver.find_element(By.ID, 'PekerjaSosial').send_keys(NamaPenyidik)
    driver.find_element(By.ID, 'PenasihatHukum').send_keys(NamaPenyidik)
    driver.find_element(By.ID, 'Panitera').send_keys(NamaPenyidik)
    driver.find_element(By.ID, 'hasilSidang').send_keys(NamaPenyidik)

    tglsidang2 = driver.find_element(By.ID, 'tglSidangSelan')
    tglsidang2.send_keys(TanggalPendampingan)
    tglsidang2.send_keys(Keys.ENTER)
  elif peka == '4':
    print('Tidak Diinputkan')
  driver.find_element(By.ID, 'catatan').send_keys('catatan ini opsional')
  driver.find_element(By.ID, 'pilihFoto0').click()
  time.sleep(3)
  pyautogui.write(environ.get(r'Gambar'))
  pyautogui.press('enter')
  driver.find_element(By.ID, 'keterangann0').send_keys('keterangan pada dokumen')
# @mark.fixture_tambh
# def testsimpan():
#   Log.info('Menekan tombol Selanjutnya')
#   driver.find_element(By.ID, 'selanjutnya1').click()
#   lanjut2 = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'selanjutnya2')))
#   driver.find_element(By.ID, 'lihatLaporan').click()
