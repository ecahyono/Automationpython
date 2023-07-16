from jenis_Litmas.src import *
from jenis_Litmas.fakeoption import *
from sesilitmas import *
from jenis_Litmas.litmasdiversi import *

def Hasildiversi(driver):
  Log.info('Instrumen Litmas Proses Peradilan Anak')
  driver.find_element(By. ID, 'tab-hasil_diversi').click()
  tutuppopup(driver)
  Log.info('Hasil Pelaksanaan Diversi Ditingkat Pengadilan')
  nav1 = driver.find_element(By.ID, "hasilPelaksanaanDiversiDitingkatPengadilan_ifr")
  ActionChains(driver).move_to_element(nav1).perform()
  nav1.click()
  nav1.send_keys(Keys.ALT + Keys.SHIFT + '1') #heading 123456
  nav1.send_keys('Contoh Heading')
  nav1.send_keys(Keys.RETURN)# Enter
  nav1.send_keys(Keys.CONTROL + 'b')  # Bold
  nav1.send_keys('Ini Adalah CONTOH Text Bold dalam paragrap')
  nav1.send_keys(Keys.CONTROL + 'b')  # Bold
  nav1.send_keys(Keys.RETURN)# Enter
  nav1.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  nav1.send_keys('Ini Adalah CONTOH Text Miring dalam paragrap')
  nav1.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  nav1.send_keys(Keys.RETURN)# Enter
  nav1.send_keys(Keys.CONTROL + 'u')  # Underline (garis)
  nav1.send_keys('Ini Adalah CONTOH Text Garis Bawah dalam paragrap')

def AkibatygdibuatKlien(driver):
  driver.find_element(By. ID, 'tab-akibat_perbuatan_klien').click()
  tutuppopup(driver)
  Log.info('Riwayat Hidup Klien')
  tab2 = driver.find_element(By.ID, "akibatYangDitimbukanOlehPerbuatanKlien_ifr")
  ActionChains(driver).move_to_element(tab2).perform()
  tab2.click()
  tab2.send_keys(Keys.ALT + Keys.SHIFT + '1') #heading 123456
  tab2.send_keys('Contoh Heading')
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'b')  # Bold
  tab2.send_keys('Ini Adalah CONTOH Text Bold dalam paragrap')
  tab2.send_keys(Keys.CONTROL + 'b')  # Bold
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab2.send_keys('Ini Adalah CONTOH Text Miring dalam paragrap')
  tab2.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'u')  # Underline (garis)
  tab2.send_keys('Ini Adalah CONTOH Text Garis Bawah dalam paragrap')

def KeadankeluargadiLapasRutanTujuan(driver):
  driver.find_element(By. ID, 'tab-keadaan_keluarga').click()
  tutuppopup(driver)
  Log.info('Keadan Keluarga dan Lingkungan di Lapas/Rutan Tujuan')
  tab2 = driver.find_element(By.ID, "keadaaKeluargaDanLingkuanDiLapasAtauRutanTujuan_ifr")
  ActionChains(driver).move_to_element(tab2).perform()
  tab2.click()
  tab2.send_keys(Keys.ALT + Keys.SHIFT + '1') #heading 123456
  tab2.send_keys('Contoh Heading')
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'b')  # Bold
  tab2.send_keys('Ini Adalah CONTOH Text Bold dalam paragrap')
  tab2.send_keys(Keys.CONTROL + 'b')  # Bold
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab2.send_keys('Ini Adalah CONTOH Text Miring dalam paragrap')
  tab2.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'u')  # Underline (garis)
  tab2.send_keys('Ini Adalah CONTOH Text Garis Bawah dalam paragrap')

def KeadaanLingkunganMasyarakat(driver):
  driver.find_element(By. ID, 'tab-keadaan_lingkungan').click()
  tutuppopup(driver)
  Log.info('Keadaan Lingkungan Masyarakat')
  tab2 = driver.find_element(By.ID, "keadaanLingkuanMasyarakat_ifr")
  ActionChains(driver).move_to_element(tab2).perform()
  tab2.click()
  tab2.send_keys(Keys.ALT + Keys.SHIFT + '1') #heading 123456
  tab2.send_keys('Contoh Heading')
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'b')  # Bold
  tab2.send_keys('Ini Adalah CONTOH Text Bold dalam paragrap')
  tab2.send_keys(Keys.CONTROL + 'b')  # Bold
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab2.send_keys('Ini Adalah CONTOH Text Miring dalam paragrap')
  tab2.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'u')  # Underline (garis)
  tab2.send_keys('Ini Adalah CONTOH Text Garis Bawah dalam paragrap')

def Tanggapan(driver):
  Log.info('Tanggapan Pihak Ketiga (Keluarga, Panti Asuhan, Sekolah)')
  driver.find_element(By. ID, 'tab-tanggapan_spa').click()
  tutuppopup(driver)
  Log.info('a. Tanggapan Klien')
  tab2 = driver.find_element(By.ID, "tanggapanKlien_ifr")
  ActionChains(driver).move_to_element(tab2).perform()
  tab2.click()
  tab2.send_keys(Keys.ALT + Keys.SHIFT + '1') #heading 123456
  tab2.send_keys('Contoh Heading')
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'b')  # Bold
  tab2.send_keys('Ini Adalah CONTOH Text Bold dalam paragrap')
  tab2.send_keys(Keys.CONTROL + 'b')  # Bold
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab2.send_keys('Ini Adalah CONTOH Text Miring dalam paragrap')
  tab2.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'u')  # Underline (garis)
  tab2.send_keys('Ini Adalah CONTOH Text Garis Bawah dalam paragrap')

def Tanggapan1(driver):
  Log.info('Tanggapan Pihak Ketiga (Keluarga, Panti Asuhan, Sekolah)')
  tutuppopup(driver)
  Log.info('b. Tanggapan Korban')
  tab2 = driver.find_element(By.ID, "tanggapanKorban_ifr")
  ActionChains(driver).move_to_element(tab2).perform()
  tab2.click()
  tab2.send_keys(Keys.ALT + Keys.SHIFT + '1') #heading 123456
  tab2.send_keys('Contoh Heading')
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'b')  # Bold
  tab2.send_keys('Ini Adalah CONTOH Text Bold dalam paragrap')
  tab2.send_keys(Keys.CONTROL + 'b')  # Bold
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab2.send_keys('Ini Adalah CONTOH Text Miring dalam paragrap')
  tab2.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'u')  # Underline (garis)
  tab2.send_keys('Ini Adalah CONTOH Text Garis Bawah dalam paragrap')

def Tanggapan2(driver):
  Log.info('Tanggapan Pihak Ketiga (Keluarga, Panti Asuhan, Sekolah)')
  tutuppopup(driver)
  Log.info('c. Tanggapan Keluarga Korban')
  tab2 = driver.find_element(By.ID, "tanggapanKeluargaKorban_ifr")
  ActionChains(driver).move_to_element(tab2).perform()
  tab2.click()
  tab2.send_keys(Keys.ALT + Keys.SHIFT + '1') #heading 123456
  tab2.send_keys('Contoh Heading')
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'b')  # Bold
  tab2.send_keys('Ini Adalah CONTOH Text Bold dalam paragrap')
  tab2.send_keys(Keys.CONTROL + 'b')  # Bold
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab2.send_keys('Ini Adalah CONTOH Text Miring dalam paragrap')
  tab2.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'u')  # Underline (garis)
  tab2.send_keys('Ini Adalah CONTOH Text Garis Bawah dalam paragrap')

def Tanggapan3(driver):
  Log.info('Tanggapan Pihak Ketiga (Keluarga, Panti Asuhan, Sekolah)')
  tutuppopup(driver)
  Log.info('d. Tanggapan Masyarakat')
  tab2 = driver.find_element(By.ID, "tanggapanMasyarakat_ifr")
  ActionChains(driver).move_to_element(tab2).perform()
  tab2.click()
  tab2.send_keys(Keys.ALT + Keys.SHIFT + '1') #heading 123456
  tab2.send_keys('Contoh Heading')
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'b')  # Bold
  tab2.send_keys('Ini Adalah CONTOH Text Bold dalam paragrap')
  tab2.send_keys(Keys.CONTROL + 'b')  # Bold
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab2.send_keys('Ini Adalah CONTOH Text Miring dalam paragrap')
  tab2.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'u')  # Underline (garis)
  tab2.send_keys('Ini Adalah CONTOH Text Garis Bawah dalam paragrap')

def Tanggapan4(driver):
  Log.info('Tanggapan Pihak Ketiga (Keluarga, Panti Asuhan, Sekolah)')
  tutuppopup(driver)
  Log.info('e. Tanggapan Pemerintah')
  tab2 = driver.find_element(By.ID, "tanggapanPemerinatah_ifr")
  ActionChains(driver).move_to_element(tab2).perform()
  tab2.click()
  tab2.send_keys(Keys.ALT + Keys.SHIFT + '1') #heading 123456
  tab2.send_keys('Contoh Heading')
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'b')  # Bold
  tab2.send_keys('Ini Adalah CONTOH Text Bold dalam paragrap')
  tab2.send_keys(Keys.CONTROL + 'b')  # Bold
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab2.send_keys('Ini Adalah CONTOH Text Miring dalam paragrap')
  tab2.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab2.send_keys(Keys.RETURN)# Enter
  tab2.send_keys(Keys.CONTROL + 'u')  # Underline (garis)
  tab2.send_keys('Ini Adalah CONTOH Text Garis Bawah dalam paragrap')
