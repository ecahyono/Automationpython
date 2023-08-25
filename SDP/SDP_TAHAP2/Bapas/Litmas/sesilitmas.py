from jenis_Litmas.src import *
from jenis_Litmas.fakeoption import *
from jenis_Litmas.indikator import *

def sesilitmas(driver):
  WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, "tempat")))
  driver.find_element(By.ID, 'tempat').send_keys(AlamatRumah)
  tglwaktu = driver.find_element(By.ID, 'waktuPelaksanaan')
  tglwaktu.click()
  print(taggldanwaktu)
  sekarangwaktu = WebDriverWait(driver, 45).until(EC.visibility_of_element_located((By.XPATH, '//div[5]/div/div[2]/button/span')))
  sekarangwaktu.click()
  metod = driver.find_element(By.ID, 'metode')
  metod.click()
  metod.send_keys(metode)
  metod.send_keys(Keys.DOWN)
  metod.send_keys(Keys.ENTER)
  
  print('Apakah Klien ini Melakukan Litmas Terakhir? =' +Switchfield)
  if Switchfield == 'Iya':
    # driver.find_element(By.ID, 'litmasTerakhir').click()
    driver.find_element(By.XPATH, '//span/div').click()
  else:
    pass

  if Switchfield == 'Iya':
    print('ApaProses Litmas Klien tersebut???' +Radio)
    if Radio == 'Penyelesaian': #nanti dibalik
      WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'Selesaian')))
      driver.find_element(By.ID, 'Selesaian').click()
    elif Radio == 'Penolakan':
      WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'Tolakan')))
      driver.find_element(By.ID, 'Tolakan').click()
      driver.find_element(By.ID, 'jenisPenolakan').send_keys('Contoh jenis penolakan')
      driver.find_element(By.ID, 'alasanPenolakan').send_keys('Contoh alasanPenolakan penolakan')
  elif Switchfield == 'Tidak':
    pass
  driver.find_element(By.ID, 'informan').send_keys('Orang yang memberikan informasi lebih lanjut')
  simpansesi(driver)
  turu(driver)

def Penjamin(driver):
  WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, "nmaa")))
  driver.find_element(By.ID, 'nmaa').send_keys(Namapalsu)
  Jenk = driver.find_element(By.ID, 'jenisKelamin')
  Jenk.click()
  Jenk.send_keys(jeniskel)
  Jenk.send_keys(Keys.DOWN)
  Jenk.send_keys(Keys.ENTER)

  driver.find_element(By.ID, 'tempatLahir').send_keys('Indonesia')
  
  tgllhr = driver.find_element(By.ID, 'tanggalLahir')
  tgllhr.send_keys('17/08/1995')
  tgllhr.send_keys(Keys.ENTER)

  kawin = driver.find_element(By.ID, 'statusPerkawinan')
  kawin.click()
  kawin.send_keys('Belum Kawin')
  kawin.send_keys(Keys.DOWN)
  kawin.send_keys(Keys.ENTER)
  
  kemis = driver.find_element(By.ID, 'hubunganDenganNarapidana')
  kemis.click()
  kemis.send_keys('Kakak')
  kemis.send_keys(Keys.DOWN)
  kemis.send_keys(Keys.ENTER)

  sekola = driver.find_element(By.ID, 'pekerjaan')
  sekola.click()
  sekola.send_keys('pelajar')
  sekola.send_keys(Keys.DOWN)
  sekola.send_keys(Keys.ENTER)

  religi = driver.find_element(By.ID, 'agama')
  religi.click()
  religi.send_keys('Islam')
  religi.send_keys(Keys.DOWN)
  religi.send_keys(Keys.ENTER)

  rass = driver.find_element(By.ID, 'suku')
  rass.click()
  rass.send_keys('Sunda')
  rass.send_keys(Keys.DOWN)
  rass.send_keys(Keys.ENTER)

  masadep = driver.find_element(By.ID, 'pendidikan')
  masadep.click()
  masadep.send_keys('Tidak sekola')
  masadep.send_keys(Keys.DOWN)
  masadep.send_keys(Keys.ENTER)

  driver.find_element(By.ID, 'alamatPenjamin').send_keys(AlamatRumah)

  pulau = driver.find_element(By.ID, 'provinsi')
  pulau.click()
  pulau.send_keys('Jawa barat')
  pulau.send_keys(Keys.DOWN)
  pulau.send_keys(Keys.ENTER)

  city = driver.find_element(By.ID, 'kotaAtauKabupaten')
  city.click()
  city.send_keys('Bandung')
  city.send_keys(Keys.DOWN)
  city.send_keys(Keys.ENTER)