from src import *
from fakeoption import *

# init driver by os
@mark.fixture_verif
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Memasukan User name dan Password di halaman Login')
	kasiebpsbdg(driver) #Operator BPS

@mark.fixture_verif
def testpendampingan():
  Log.info('Menambah Data Register Pendampingan')
  driver.get('http://kumbang.torche.id:32400/bapas/pendampingan/daftar-pendampingan')
  time.sleep(1)
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'ButtonCari')))

@mark.fixture_verif
def testfilterindx():
  global peka
  driver.find_element(By.ID, 'column').click()
  pilihan = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'jenisPendampinganFil')))
  pilihan.click()
  driver.find_element(By.ID, 'kode_status').click()
  pilihan2 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'Pelak')))
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
  
@mark.fixture_verif
def testFormtambh():
  if peka == '1':
    Log.info('Membuka Halaman  Pendampingan')
    driver.find_element(By.ID, 'detailPendampingan0').click()  
  elif peka == '2':
    Log.info('Membuka Halaman  Diversi')
    driver.find_element(By.ID, 'detailDivesi0').click()  
  elif peka == '3':
    Log.info('Membuka Halaman  Sidang')
    driver.find_element(By.ID, 'detailSidang0').click()  

  WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
  WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  driver.find_element(By.ID, 'dropdownJenisRegistrasi').click()  
  
  verifkuy = input('Pilih Aksi yang akan di lakukan \n'
    '1. Laporan Disetujui Kasie \n'          
    '2. Laporan Revisi Kasie \n'
    'Masukan Pilihan Nomer Untul laporan :>>>'          
  )
  if verifkuy =='1':
    driver.find_element(By.ID, 'setujui').click()
  elif verifkuy =='2':
    driver.find_element(By.ID, 'resivi').click()
  elif verifkuy =='3':
    print('Tidak ada Pilihan tersedia')

@mark.fixture_veriv
def testsimpanverif():
  driver.find_element(By.ID, 'submitButton').click()
  Log.info('menyimpan verifikasi oleh kasie')
  time.sleep(2)
  indx12 = time.time()
  WebDriverWait(driver,85).until(EC.element_to_be_clickable((By.ID, "ButtonCari")))
  indx22 = time.time()
  waktu2 = indx12 - indx22
  Log.info("Waktu yang dibutuhkan: {:.2f} detik".format(abs(waktu2)))
