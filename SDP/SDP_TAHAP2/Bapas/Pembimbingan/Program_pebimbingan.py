from src import *
from fakeoption import *
from indikator import *

def programpembimbingan(driver):
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
  driver.find_element(By. ID, "filterColumn").click()
  driver.find_element(By. ID, "semua").click()
  driver.find_element(By. ID, "kataKunci").send_keys('Pelaksanaan')
  driver.find_element(By. ID, "searchButton").click()
  turu(driver)
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

  driver.find_element(By. ID, "programPembimbinganButton").click()
  Log.info('Buka Halaman Program Pembimbingan')
  lagiloading(driver)
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  driver.find_element(By. ID, "sesiPembimbinganButton").click()
  Log.info('Buka Halaman sesi Program Pembimbingan')
  lagiloading(driver)

  # tutuppopup(driver)

  driver.find_element(By. ID, "inputSubJenisProgram").send_keys('Sub Jenis Program')
  driver.find_element(By. ID, "inputNamaProgram").send_keys('Nama Program')
  driver.find_element(By. ID, "inputUraianKegiatan").send_keys('Uraian Kegiatan')
  #checkbox
  driver.find_element(By. XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]/div/form[1]/div[1]/div[1]/div[2]/div[1]/div[5]/div/label').click()
  #checkbox
  tangglsesi = driver.find_element(By. ID, "tanggalSesi").send_keys(TglAwalBimbingan)
  tangglsesi.send_keys(Keys.ENTER)
  #Waktu Kegiatan
  wakawal = driver.find_element(By. ID, "waktuAwal").send_keys('08:00:00')
  wakawal.send_keys(Keys.ENTER)
  waktakhir = driver.find_element(By. ID, "waktuAkhir").send_keys('11:00:00')
  waktakhir.send_keys(Keys.ENTER)

  driver.find_element(By. ID, "inputPenanggungJawabMitra").send_keys('Penanggung jawab mitra')
  mitra = driver.find_element(By. ID, "dropdownMitra")
  mitra.click()
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'mitra0')))
  driver.find_element(By. ID, "mitra0").click()

  driver.find_element(By. ID, "inputMateriBimbingan").send_keys('Materi Uraian Kegiatan')
  driver.find_element(By. ID, "inputSaran").send_keys('Saran Dari Materi Uraian Kegiatan yang di adakan')
  
  JumlahInstrukturPetugas = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]/div/form/div[1]/div[1]/div[2]/div[1]/div[10]/div/div/div/input')
  JumlahInstrukturKlien   = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]/div/form/div[1]/div[1]/div[2]/div[1]/div[11]/div/div/div/input')
  JumlahInstrukturInstansiLain  = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]/div/form/div[1]/div[1]/div[2]/div[1]/div[12]/div/div/div/input')  
  JumlahInstrukturPetugas.click()
  pyautogui.hotkey('backspace')
  JumlahInstrukturPetugas.send_keys('1')
  JumlahInstrukturKlien.click()
  pyautogui.hotkey('backspace')
  JumlahInstrukturKlien.send_keys('1')
  JumlahInstrukturInstansiLain.click()
  pyautogui.hotkey('backspace')
  JumlahInstrukturInstansiLain.send_keys('1') 

  mitra = driver.find_element(By. ID, "dropdownMitraInstansi")
  mitra.click()
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'mitraInstansi0')))
  driver.find_element(By. ID, "mitraInstansi0").click() 
  peralatan = driver.find_element(By. ID, 'dropdownSarPras').click()
  sarana = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'Sarana')))
  sarana.click()
  peralatan1 = driver.find_element(By. ID, 'dropdownPeralatan').click()
  sarana1 = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'peralatan0')))
  sarana1.click() 
  
  driver.find_element(By.ID, 'pilihFoto0').click()
  lamaturu(driver)
  pyautogui.write(environ.get(r'FOTBRG1'))
  pyautogui.press('enter')  
  driver.find_element(By.ID, 'keterangann0').send_keys('Keterangan Foto Sesi Pembimbingan')


  