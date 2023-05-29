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
	bapasbdg(driver)

A = wb['Verifikasi']
g = 2  # barisexel
statusverif     = A['D'+str(g)].value
deskripsi       = A['E'+str(g)].value

D = wb['Register Pendampingan']
j = 3  # barisexel
JenisPNP        = D['C'+str(j)].value

@mark.fixture_verifikasi
def testverifikasi():
  Pilih = input('Pilih Data Yang akan di Edit \n'
                '1. Register Pendampingan \n'
                '2. Register Litmas \n'
                '3. Register Pembimbingan \n'
                '4. Register Pengawasan \n'
                'Masukan Nomor : '
  )
  if Pilih == '1':
    Log.info('Edit Register Pendampingan')
    driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/register-pendampingan')
  elif Pilih == '2':
    Log.info('Edit Register Litmas')
    driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/register-litmas')
  elif Pilih == '3':
    Log.info('Edit Register Pembimbingan')
    driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/register-pembimbingan')
  elif Pilih == '4':
    Log.info('Edit Register Pengawasan')
    driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/register-pengawasan')

@mark.fixture_verifikasi
def testfilterindx():
  WebDriverWait(driver,85).until(EC.element_to_be_clickable((By.ID, "buttonCari")))
  Log.info('Pencarian data wbp dengan memfilter data table')
  driver.find_element(By.ID, 'kode_status').click()
  pilihan = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'revisi')))
  pilihan.click()
  driver.find_element(By.ID, 'buttonCari').click()
  time.sleep(2)
  WebDriverWait(driver,85).until(EC.element_to_be_clickable((By.ID, "buttonCari")))

@mark.fixture_verifikasi
def testVerifikasinya():
  Log.info('Menekan tombol Detail')
  driver.find_element(By.XPATH, '//div[2]/a/button').click()
  WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
  WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
  time.sleep(2)
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	
