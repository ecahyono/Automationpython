from jenis_Litmas.src import *
from jenis_Litmas.fakeoption import *
from sesilitmas import *
from jenis_Litmas.litmasdiversi import *

def perkembanganPembinaanKlienDiLapasAtauRutan(driver):
  Log.info('Instrumen Litmas Litmas Program Asimilasi Anak')
  driver.find_element(By. ID, 'tab-perkembangan_pembinaan').click()
  tutuppopup(driver)
  Log.info('Perkembangan Pembinaan Klien di Lapas/Rutan')
  nav1 = driver.find_element(By.ID, "perkembanganPembinaanKlienDiLapasAtauRutan_ifr")
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

def keadaanPenangungJawabAtauPenjamin(driver):
  Log.info('Instrumen Litmas Litmas Program Asimilasi Anak')
  driver.find_element(By. ID, 'tab-keadaan_penjamin').click()
  tutuppopup(driver)
  Log.info('Keadaan Penanggung Jawab/Penjamin')
  nav1 = driver.find_element(By.ID, "keadaanPenangungJawabAtauPenjamin_ifr")
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

def tanggapankorban(driver):
  Log.info('Tanggapan Korban dan Keluarga Korban, Pemerintah dan Lembaga Sosial')
  driver.find_element(By. ID, 'tab-tanggapan').click()
  tutuppopup(driver)
  Log.info('a. Tanggapan Korban')
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

def tanggapanPemerintah(driver):
  Log.info('Tanggapan Korban dan Keluarga Korban, Pemerintah dan Lembaga Sosial')
  tutuppopup(driver)
  tab2 = driver.find_element(By.ID, "tanggapanPemerintah_ifr")
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

def tanggapanKeluargaKoraban(driver):
  tutuppopup(driver)
  tab2 = driver.find_element(By.ID, "tanggapanKeluargaKoraban_ifr")
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

def keadaanPihakKetiga(driver):
  Log.info('Keadaan Pihak Ketiga (Lembaga Sosial Pembina)')
  driver.find_element(By. ID, 'tab-keadaan_pihak_ketiga').click()
  tutuppopup(driver)
  tab2 = driver.find_element(By.ID, "keadaanPihakKetiga_ifr")
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
  
