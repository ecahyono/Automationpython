from jenis_Litmas.src import *
from jenis_Litmas.fakeoption import *

def sesilitmas(driver):
  time.sleep(2)
  driver.find_element(By.ID, 'tempat').send_keys(AlamatRumah)
  tglpelak = driver.find_element(By.ID, 'waktuPelaksanaan')
  tglpelak.send_keys(tanggal_hasil)
  tglpelak.send_keys(Keys.ENTER)
  metod = driver.find_element(By.ID, 'metode')
  metod.click()
  metod.send_keys(metode)
  metod.send_keys(Keys.DOWN)
  metod.send_keys(Keys.ENTER)
  
  print('Apakah Klien ini Melakukan Litmas Terakhir? =' +Switchfield)
  if Switchfield == 'Iya':
    driver.find_element(By.XPATH, '//span/div').click()
  else:
    pass

  if Switchfield == 'Iya':
    print('ApaProses Litmas Klien tersebut???' +Radio)
    if Radio == 'Penyelesaian': #nanti dibalik
      WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'Selesaian')))
      driver.find_element(By.ID, 'Selesaian').click()
      tglend = driver.find_element(By.ID, 'tanggalPenyelesaian')
      tglend.send_keys(tanggal_hasil)
      tglend.send_keys(Keys.ENTER)
    elif Radio == 'Penolakan':
      WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'Tolakan')))
      driver.find_element(By.ID, 'Tolakan').click()
      driver.find_element(By.ID, 'jenisPenolakan').send_keys('Contoh jenis penolakan')
      driver.find_element(By.ID, 'Tolakan').click()
  elif Switchfield == 'Tidak':
    pass
  driver.find_element(By.ID, 'informan').send_keys('Orang yang memberikan informasi lebih lanjut')

def Penjamin(driver):
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

def tutuppopup(driver):
  WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.tox-icon > svg')))
  popuptutup1 = driver.find_element(By.CSS_SELECTOR, 'div.tox-icon > svg')
  popuptutup1.click()

def simpansesi(driver):
  driver.find_element(By.ID, 'buttonSimpan').click()