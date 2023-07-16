from src import *
from fakeoption import *
from indikator import *

def sesiakhir(driver):
  driver.find_element(By. ID, 'dropdownAlasanPengakhiran').click()
  if opsisesiterakhir == 'Telah Berakhir Masa Bimbingan':
    driver.find_element(By.ID, 'Pencabutan Pembimbingan').click()
  elif opsisesiterakhir == 'Pencabutan Pembimbingan':
    driver.find_element(By.ID, 'Telah Berakhir Masa Bimbingan').click()
  elif opsisesiterakhir == 'Meninggal Dunia':
    driver.find_element(By.ID, 'Meninggal Dunia').click()
  driver.find_element(By. ID, 'inputDetailAlasanPengakhiran').send_keys('Detail Alasan Pengakhiran')
  driver.find_element(By. ID, 'inputSuratPutusanPenetapan').send_keys('Surat Putusan/Penetapan')
  driver.find_element(By. ID, 'inputSaranPK').send_keys('Saran PK (Perkembangan Klien)')
  driver.find_element(By. ID, 'inputTanggapanSidangTPP').send_keys('Tanggapan Sidang TPP')

def perkembanganklienn(driver):
  Log.info('Sesi Terakhir Pembimbingan')
  Log.info('Keadaan Klien, Keluarga dan Lingkungan Bimbingan')
  driver.find_element(By. ID, 'tab-perkembangan_klien').click()
  
  Log.info('Penelusuran Minat & Bakat')
  nav1 = driver.find_element(By.ID, "keadaanKlienKeluargaLingkunganBimbingan_ifr")
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

  Log.info('Evaluasi Pembimbing Kemasyarakatan')
  nav2 = driver.find_element(By.ID, "evaluasiPembimbingKemasyarakatan_ifr")
  ActionChains(driver).move_to_element(nav2).perform()
  nav2.click()
  nav2.send_keys(Keys.ALT + Keys.SHIFT + '1') #heading 123456
  nav2.send_keys('Contoh Heading')
  nav2.send_keys(Keys.RETURN)# Enter
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