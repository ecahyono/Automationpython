from src import *
# init driver by os
@mark.fixture_penerimaan
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = webfirefox()
	pathData = loadDataPath()
	Log.info('Memasukan User name dan Password di halaman Login')
	kasiebpsbdg(driver)

A = wb['Verifikasi']
g = 2  # barisexel
opsi            = A['A'+str(g)].value
opsi            = A['B'+str(g)].value
status          = A['C'+str(g)].value
statusverif     = A['D'+str(g)].value
deskripsi       = A['E'+str(g)].value

D = wb['Register Pendampingan']
j = 3  # barisexel
JenisPNP        = D['C'+str(j)].value

@mark.fixture_verifikasi
def testverifikasipendampingn():
  Log.info('Menambah Data Register Penolakan')
  driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/register-pendampingan')
  WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='el-button' and span='Cari']")))

  Log.info('Pencarian data wbp dengan memfilter data table')

  Log.info('Menekan tombol Detail')
  driver.find_element(By.CSS_SELECTOR, ".h-5.w-5").click()
  WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='el-descriptions__cell el-descriptions__content is-bordered-content' and text()='"+JenisPNP+"']")))
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  driver.find_element(By. ID, 'dropdownJenisRegistrasi').click()
  WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.ID, "jenisRegistrasi0")))
  driver.find_element(By.XPATH, "//li[contains(.,'"+ statusverif+"')]").click()

  driver.find_element(By. XPATH, "//textarea[@placeholder='Masukkan Keterangan']").send_keys(deskripsi)
  




