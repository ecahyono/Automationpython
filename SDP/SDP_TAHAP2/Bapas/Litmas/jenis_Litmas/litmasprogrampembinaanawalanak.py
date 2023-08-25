from jenis_Litmas.src import *
from jenis_Litmas.fakeoption import *
from sesilitmas import *
from jenis_Litmas.indikator import *

def RiwayatTindkPidana(driver):
  Log.info('Instrumen Litmas Diversi Riwayat Tindak Pidana')
  driver.find_element(By. ID, 'tab-riwayat_tindak_pidana').click()
  tutuppopup(driver)
  Log.info('a. Kronologis Kejadian')
  nav1 = driver.find_element(By.ID, "kronoliKejadian_ifr")
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

def RiwayatTindkPidana1(driver):
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

def rencanaKlien(driver):
  Log.info('Instrumen Litmas Litmas Program Pembinaan Awal Anak')
  driver.find_element(By. ID, 'tab-rencana_klien').click()
  tutuppopup(driver)
  Log.info('Rencana Klien')
  nav1 = driver.find_element(By.ID, "rencanaKlien_ifr")
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

def potensiKeluargaDanLingkunganTempatTinggalKlien(driver):
  Log.info('Instrumen Litmas Litmas Program Pembinaan Awal Anak')
  driver.find_element(By. ID, 'tab-potensi_keluarga_dan_klien').click()
  tutuppopup(driver)
  Log.info('Potensi Keluarga dan Lingkungan Tempat Tinggal Klien')
  nav1 = driver.find_element(By.ID, "potensiKeluargaDanLingkunganTempatTinggalKlien_ifr")
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

def programPerawatanYangDiterimaKlienDiLpas(driver):
  Log.info('Instrumen Litmas Litmas Program Pembinaan Awal Anak')
  driver.find_element(By. ID, 'tab-program_perawatan').click()
  tutuppopup(driver)
  Log.info('Program Perawatan yang Diterima Klien di LPAS')
  nav1 = driver.find_element(By.ID, "programPerawatanYangDiterimaKlienDiLpas_ifr")
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