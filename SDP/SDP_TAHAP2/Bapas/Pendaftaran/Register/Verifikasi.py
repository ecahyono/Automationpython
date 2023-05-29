from src import *
from regisdanverif import*
# init driver by os
@mark.fixture_penerimaan
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Memasukan User name dan Password di halaman Login')
	kasiebpsbdg(driver)

@mark.fixture_verifikasi
def testverifikasi():
  Pilih = input('Pilih Data Yang akan di verifikasi \n'
                '1. Register Pendampingan \n'
                '2. Register Litmas \n'
                '3. Register Pembimbingan \n'
                '4. Register Pengawasan \n'
                'Masukan Nomor : '
  )
  if Pilih == '1':
    Log.info('Akses Menu Register Pendampingan')
    driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/register-pendampingan')
  elif Pilih == '2':
    Log.info('Akses Menu Register Litmas')
    driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/register-litmas')
  elif Pilih == '3':
    Log.info('Akses Menu Register Pembimbingan')
    driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/register-pembimbingan')
  elif Pilih == '4':
    Log.info('Akses Menu Register Pengawasan')
    driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/register-pengawasan')

@mark.fixture_verifikasi
def testfilterindx():
  WebDriverWait(driver,85).until(EC.element_to_be_clickable((By.ID, "buttonCari")))
  Log.info('Pencarian data wbp dengan memfilter data table')
  driver.find_element(By.ID, 'kode_status').click()
  pilihan = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'permohonan')))
  pilihan.click()
  driver.find_element(By.ID, 'buttonCari').click()
  time.sleep(2)
  indx1 = time.time()
  WebDriverWait(driver,85).until(EC.element_to_be_clickable((By.ID, "buttonCari")))
  indx2 = time.time()
  waktu = indx1 - indx2
  Log.info("Waktu yang dibutuhkan: {:.2f} detik".format(abs(waktu)))

@mark.fixture_verifikasi
def testVerifikasinya():
  Log.info('Menekan tombol Detail')
  driver.find_element(By.CSS_SELECTOR, ".h-5.w-5").click()
  awal = time.time()
  WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
  WebDriverWait(driver, 25).until(EC.invisibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
  akhir = time.time()
  lamatunggu = awal - akhir
  Log.info("Waktu yang dibutuhkan: {:.2f} detik".format(abs(lamatunggu)))
  time.sleep(2)
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  Log.info('memilih opsi verifikasi')
  driver.find_element(By. ID, 'dropdownJenisRegistrasi').click()
  verif = input('Pilih Status Verifikasi \n'
                '1. Permohonan \n'
                '2. Revisi \n'
                '3. Disetujui \n'
                '4. Ditolak \n'
                'Pilih Nomer Yang  Diinginkan -->>'
          )
  if verif == '3':
    se7 = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.ID, "DisetujuiDrop")))
    se7.click()
  elif verif == '2':
    Nose7 = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.ID, "RevisiDrop")))
    Nose7.click()
    Log.info('memberikan deskripsi Hasil verifikasi')
    driver.find_element(By. XPATH, "//textarea[@placeholder='Masukkan Keterangan']").send_keys(deskripsi)
  elif verif == '1':
    print('Permohonan')

  Log.info('menyimpan Hasil Verifikasi')
  driver.find_element(By.ID,'submitButton').click()
  lama1 = time.time()
  WebDriverWait(driver,85).until(EC.element_to_be_clickable((By.ID, "buttonCari")))
  lama2 = time.time()
  lamakali = lama1 - lama2
  Log.info("Waktu yang dibutuhkan: {:.2f} detik".format(abs(lamakali)))
  driver.close()
  driver.quit()





