from jenis_Litmas.src import *
from jenis_Litmas.fakeoption import *
from sesilitmas import *

def RiwayatTindakPidana(driver):
  Log.info('Instrumen Litmas Diversi Riwayat Tindak Pidana')
  driver.find_element(By. ID, 'tab-riwayat_tindak_pidana_diversi').click()
  tutuppopup(driver)
  Log.info('a. Kronologis Kejadian')
  nav1 = driver.find_element(By.ID, "kronologiKejadian_ifr")
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

def RiwayatTindakPidana1(driver):
  tutuppopup(driver)
  Log.info('b. Motif Permasalahan Klien')
  nav2 = driver.find_element(By.ID, "motifPermasalahanKlien_ifr")
  ActionChains(driver).move_to_element(nav2).perform()
  nav2.click()
  nav2.send_keys(Keys.CONTROL + 'b')  # Bold
  nav2.send_keys('Ini Adalah CONTOH Text Bold dalam paragrap')
  nav2.send_keys(Keys.CONTROL + 'b')  # Bold
  nav2.send_keys(Keys.RETURN)# Enter
  nav2.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  nav2.send_keys('Ini Adalah CONTOH Text Miring dalam paragrap')
  nav2.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  nav2.send_keys(Keys.RETURN)# Enter
  nav2.send_keys(Keys.CONTROL + 'u')  # Underline (garis)
  nav2.send_keys('Ini Adalah CONTOH Text Garis Bawah dalam paragrap')

def RiwayatTindakPidana2(driver):
  tutuppopup(driver)
  Log.info('c. Catatan Pengulangan Tindak Pidana (Jika Ada)')
  nav3 = driver.find_element(By.ID, "catatanPengulanganTindakPidana_ifr")
  ActionChains(driver).move_to_element(nav3).perform()
  nav3.click()
  nav3.send_keys(Keys.CONTROL + 'b')  # Bold
  nav3.send_keys('Ini Adalah CONTOH Text Bold dalam paragrap')
  nav3.send_keys(Keys.CONTROL + 'b')  # Bold
  nav3.send_keys(Keys.RETURN)# Enter
  nav3.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  nav3.send_keys('Ini Adalah CONTOH Text Miring dalam paragrap')
  nav3.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  nav3.send_keys(Keys.RETURN)# Enter
  nav3.send_keys(Keys.CONTROL + 'u')  # Underline (garis)
  nav3.send_keys('Ini Adalah CONTOH Text Garis Bawah dalam paragrap')

def RiwayatHidupKlien(driver):
  Log.info('Instrumen Litmas Diversi Riwayat Hidup Klien')
  driver.find_element(By. ID, 'tab-riwayat_hidup').click()
  tutuppopup(driver)
  Log.info('Riwayat Hidup Klien')
  tab2 = driver.find_element(By.ID, "riwayatHidupKlien_ifr")
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
  
def RiwayatPendidikan(driver):
  Log.info('Instrumen Litmas Diversi Riwayat Pendidikan')
  driver.find_element(By. ID, 'tab-riwayat_pendidikan').click()
  tutuppopup(driver)
  Log.info('Riwayat Pendidikan')
  tab3 = driver.find_element(By.ID, "pendidikanDasar_ifr")
  ActionChains(driver).move_to_element(tab3).perform()
  tab3.click()
  tab3.send_keys(Keys.ALT + Keys.SHIFT + '1') #heading 123456
  tab3.send_keys('Contoh Heading')
  tab3.send_keys(Keys.RETURN)# Enter
  tab3.send_keys(Keys.CONTROL + 'b')  # Bold
  tab3.send_keys('Ini Adalah CONTOH Text Bold dalam paragrap')
  tab3.send_keys(Keys.CONTROL + 'b')  # Bold
  tab3.send_keys(Keys.RETURN)# Enter
  tab3.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab3.send_keys('Ini Adalah CONTOH Text Miring dalam paragrap')
  tab3.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab3.send_keys(Keys.RETURN)# Enter
  tab3.send_keys(Keys.CONTROL + 'u')  # Underline (garis)
  tab3.send_keys('Ini Adalah CONTOH Text Garis Bawah dalam paragrap')

def HarapanRencanaKlien(driver):
  Log.info('Instrumen Litmas Diversi Harapan dan Rencana Klien')
  driver.find_element(By. ID, 'tab-harapan_dan_rencana').click()
  tutuppopup(driver)
  Log.info('Harapan dan Rencana Klien')
  tab4 = driver.find_element(By.ID, "harapanDanRencanaKlien_ifr")
  ActionChains(driver).move_to_element(tab4).perform()
  tab4.click()
  tab4.send_keys(Keys.ALT + Keys.SHIFT + '1') #heading 123456
  tab4.send_keys('Contoh Heading')
  tab4.send_keys(Keys.RETURN)# Enter
  tab4.send_keys(Keys.CONTROL + 'b')  # Bold
  tab4.send_keys('Ini Adalah CONTOH Text Bold dalam paragrap')
  tab4.send_keys(Keys.CONTROL + 'b')  # Bold
  tab4.send_keys(Keys.RETURN)# Enter
  tab4.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab4.send_keys('Ini Adalah CONTOH Text Miring dalam paragrap')
  tab4.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab4.send_keys(Keys.RETURN)# Enter
  tab4.send_keys(Keys.CONTROL + 'u')  # Underline (garis)
  tab4.send_keys('Ini Adalah CONTOH Text Garis Bawah dalam paragrap')

def AnalisaHasilPengamatan(driver):
  Log.info('Instrumen Litmas Diversi Analisa Hasil Pengamatan')
  driver.find_element(By. ID, 'tab-analisa_data').click()
  tutuppopup(driver)
  Log.info('a. Analisa')
  tab5 = driver.find_element(By.ID, "analisa_ifr")
  ActionChains(driver).move_to_element(tab5).perform()
  tab5.click()
  tab5.send_keys(Keys.ALT + Keys.SHIFT + '1') #heading 123456
  tab5.send_keys('Contoh Heading')
  tab5.send_keys(Keys.RETURN)# Enter
  tab5.send_keys(Keys.CONTROL + 'b')  # Bold
  tab5.send_keys('Ini Adalah CONTOH Text Bold dalam paragrap')
  tab5.send_keys(Keys.CONTROL + 'b')  # Bold
  tab5.send_keys(Keys.RETURN)# Enter
  tab5.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab5.send_keys('Ini Adalah CONTOH Text Miring dalam paragrap')
  tab5.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab5.send_keys(Keys.RETURN)# Enter
  tab5.send_keys(Keys.CONTROL + 'u')  # Underline (garis)
  tab5.send_keys('Ini Adalah CONTOH Text Garis Bawah dalam paragrap')

def AnalisaHasilPengamatan1(driver):
  tutuppopup(driver)
  Log.info('b. Kesimpulan')
  tab51 = driver.find_element(By.ID, "kesimpulan_ifr")
  ActionChains(driver).move_to_element(tab51).perform()
  tab51.click()
  tab51.send_keys(Keys.ALT + Keys.SHIFT + '1') #heading 123456
  tab51.send_keys('Contoh Heading')
  tab51.send_keys(Keys.RETURN)# Enter
  tab51.send_keys(Keys.CONTROL + 'b')  # Bold
  tab51.send_keys('Ini Adalah CONTOH Text Bold dalam paragrap')
  tab51.send_keys(Keys.CONTROL + 'b')  # Bold
  tab51.send_keys(Keys.RETURN)# Enter
  tab51.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab51.send_keys('Ini Adalah CONTOH Text Miring dalam paragrap')
  tab51.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab51.send_keys(Keys.RETURN)# Enter
  tab51.send_keys(Keys.CONTROL + 'u')  # Underline (garis)
  tab51.send_keys('Ini Adalah CONTOH Text Garis Bawah dalam paragrap')

def Rekomendasi(driver):
  Log.info('Instrumen Litmas Diversi Rekomendasi')
  driver.find_element(By. ID, 'tab-rekomendasi').click()
  tutuppopup(driver)
  Log.info('Rekomendasi')
  tab6 = driver.find_element(By.ID, "rekomendasi_ifr")
  ActionChains(driver).move_to_element(tab6).perform()
  tab6.click()
  tab6.send_keys(Keys.ALT + Keys.SHIFT + '1') #heading 123456
  tab6.send_keys('Contoh Heading')
  tab6.send_keys(Keys.RETURN)# Enter
  tab6.send_keys(Keys.CONTROL + 'b')  # Bold
  tab6.send_keys('Ini Adalah CONTOH Text Bold dalam paragrap')
  tab6.send_keys(Keys.CONTROL + 'b')  # Bold
  tab6.send_keys(Keys.RETURN)# Enter
  tab6.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab6.send_keys('Ini Adalah CONTOH Text Miring dalam paragrap')
  tab6.send_keys(Keys.CONTROL + 'i')  # Italic (miring)
  tab6.send_keys(Keys.RETURN)# Enter
  tab6.send_keys(Keys.CONTROL + 'u')  # Underline (garis)
  tab6.send_keys('Ini Adalah CONTOH Text Garis Bawah dalam paragrap')

