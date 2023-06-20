from src import *
from fakeoption import *
from index import *

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
  driver.get('http://kumbang.torche.id:32400/bapas/litmas/penerimaan')
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div/div/div/button')))

@mark.fixture_pendampingan
def testfiltertable():
  filtertable(driver)
  driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[6]/div/button').click()
  
  WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
  WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
	



# def contoh():
  
#   driver.find_element(By. ID, "tab-2").click()
#   driver.find_element(By. ID, "tab-3").click()
#   driver.find_element(By. ID, "tab-4").click()
#   driver.find_element(By. ID, "tab-5").click()
#   driver.find_element(By. ID, "tab-6").click()
#   driver.find_element(By. ID, "tempat").click()
#   driver.find_element(By. ID, "tempat").send_keys("tempat sesi litmas")
#   driver.find_element(By. ID, "waktuPelaksanaan").click()
#   driver.find_element(By. XPATH, "//div[@id='el-popper-container-7325']/div[4]/div/div/div/div[2]/table/tbody/tr[4]/td[3]/div/span").click()
#   driver.find_element(By. ID, "waktuPelaksanaan").click()
#   driver.find_element(By. ID, "metode").click()
#   driver.find_element(By. XPATH, "//div[@id='el-popper-container-7325']/div[5]/div/div/div/ul/li").click()
#   driver.find_element(By. XPATH, "//div[@id='sesiLitmasButton']/form/div/div[2]/div[2]/div/div/div/span/div").click()
#   driver.find_element(By. XPATH, "//div[@id='prosesLitmas']/label/span[2]").click()
#   driver.find_element(By. XPATH, "//div[@id='prosesLitmas']/label[2]/span[2]").click()
#   driver.find_element(By. ID, "jenisPenolakan").click()
#   driver.find_element(By. ID, "jenisPenolakan").clear()
#   driver.find_element(By. ID, "jenisPenolakan").send_keys("jenispenolakan litmas sesi")
#   driver.find_element(By. ID, "alasanPenolakan").click()
#   driver.find_element(By. ID, "alasanPenolakan").clear()
#   driver.find_element(By. ID, "alasanPenolakan").send_keys("alasan penolakan")
#   driver.find_element(By. ID, "informan").click()
#   driver.find_element(By. ID, "informan").clear()
#   driver.find_element(By. ID, "informan").send_keys("informasn sesi litmas")
#   driver.find_element(By. ID, "nmaa").click()
#   driver.find_element(By. ID, "nmaa").clear()
#   driver.find_element(By. ID, "nmaa").send_keys("cahyotescahyo")
#   driver.find_element(By. ID, "jenisKelamin").click()
#   driver.find_element(By. XPATH, "//div[@id='el-popper-container-7325']/div[6]/div/div/div/ul/li").click()
#   driver.find_element(By. ID, "tempatLahir").click()
#   driver.find_element(By. ID, "tempatLahir").clear()
#   driver.find_element(By. ID, "tempatLahir").send_keys("tempatlahir")
#   driver.find_element(By. ID, "tanggalLahir").click()
#   driver.find_element(By. XPATH, "//div[@id='el-popper-container-7325']/div[7]/div/div/div/div[2]/table/tbody/tr[4]/td[3]/div/span").click()
#   driver.find_element(By. ID, "statusPerkawinan").click()
#   driver.find_element(By. XPATH, "//div[@id='el-popper-container-7325']/div[8]/div/div/div/ul/li").click()
#   driver.find_element(By. ID, "hubunganDenganNarapidana").click()
#   driver.find_element(By. XPATH, "//div[@id='el-popper-container-7325']/div[9]/div/div/div/ul/li[4]").click()
#   driver.find_element(By. ID, "pekerjaan").click()
#   driver.find_element(By. XPATH, "//div[@id='el-popper-container-7325']/div[10]/div/div/div/ul/li[3]").click()
#   driver.find_element(By. ID, "agama").click()
#   driver.find_element(By. XPATH, "//div[@id='el-popper-container-7325']/div[11]/div/div/div/ul/li[2]").click()
#   driver.find_element(By. ID, "suku").click()
#   driver.find_element(By. XPATH, "//div[@id='el-popper-container-7325']/div[12]/div/div/div/ul/li").click()
#   driver.find_element(By. ID, "pendidikan").click()
#   driver.find_element(By. XPATH, "//div[@id='el-popper-container-7325']/div[13]/div/div/div/ul/li").click()
#   driver.find_element(By. ID, "alamatPenjamin").click()
#   driver.find_element(By. ID, "alamatPenjamin").clear()
#   driver.find_element(By. ID, "alamatPenjamin").send_keys("alamat penjamin")
#   driver.find_element(By. ID, "provinsi").click()
#   driver.find_element(By. XPATH, "//div[@id='el-popper-container-7325']/div[14]/div/div/div/ul/li[7]").click()
#   driver.find_element(By. ID, "kotaAtauKabupaten").click()
#   driver.find_element(By. XPATH, "//div[@id='el-popper-container-7325']/div[15]/div/div/div/ul/li[8]").click()
#   driver.find_element(By. ID, "tab-hasil_diversi").click()
#   driver.find_element(By. XPATH, "//html").click()
#   driver.find_element(By. ID, "tab-riwayat_tindak_pidana").click()
#   driver.find_element(By. XPATH, "//html").click()
#   driver.find_element(By. XPATH, "//html").click()
#   driver.find_element(By. XPATH, "//body[@id='tinymce']/p").click()
#   driver.find_element(By. XPATH, "//html").click()
#   driver.find_element(By. XPATH, "//body[@id='tinymce']/p").click()
#   driver.find_element(By. ID, "tab-akibat_perbuatan_klien").click()
#   driver.find_element_by_css_selector("div.tox-icon > svg > path").click()
#   driver.find_element(By. XPATH, "//div[@id='akibatPerbuatanKlienButton']/form/div/div").click()