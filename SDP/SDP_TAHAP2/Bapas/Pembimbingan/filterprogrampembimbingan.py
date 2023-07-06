from src import *
from fakeoption import *
from indikator import *

def filtertabel(driver):
  driver.find_element(By. ID, "filterColumn").click()
  jenisreg = WebDriverWait(driver, 50).until(EC.element_to_be_clickable(((By.ID, 'jenis_registrasi'))))
  jenisreg.click()
  Katkun = driver.find_element(By.ID, 'dropdownJenisRegistrasi')
  Katkun.click()
  Pilih = input('1. Pembimbingan Diversi \n'
    '2. Pembimbingan Penetapan Bagi Anak Berusia Kurang dari 12 Tahun \n'
    '3. Pembimbingan Penetapan Tindakan Anak \n'
    '4. Pembimbingan Pidana dengan Syarat Anak (pidana pembinaan di luar lembaga) \n'
    '5. Pembimbingan Pidana dengan Syarat Anak (pelayanan masyarakat) \n'
    '6. Pembimbingan Pidana dengan Syarat Anak (pidana pengawasan) \n'
    '7. Pembimbingan Pidana Peringatan Anak \n'
    '8. Pembimbingan Pidana Pelatihan Kerja Anak \n'
    '9. Pembimbingan Asimilasi Anak \n'
    '10. Pembimbingan CB Anak \n'
    '11. Pembimbingan CMB Anak \n'
    '12. Pembimbingan PB Anak \n'
    '13. Pembimbingan Tambahan (After Care) Anak \n'
    '14. Buku Ekspirasi Pembimbingan dan Pengawasan Anak \n'
    '15. Pidana dengan Syarat \n'
    '16. Pembimbingan Asimilasi \n'
    '17. Pembimbingan CB \n'
    '18. Pembimbingan CMB \n'
    '19. Pembimbingan PB \n'
    '20. Pembimbingan Tambahan After Care \n'
    '21. Pembimbingan dan Pengawasan (buku pembantu register) \n'
    'Masukan Nomer yang tersedia diatas--->> :')
  try:
    if Pilih =='1':
      Log.info('Pembimbingan Diversi')
      Katkun.send_keys(Pembimbng1)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi0').click()
    elif Pilih =='2':
      Log.info('Pembimbingan Penetapan Bagi Anak Berusia Kurang dari 12 Tahun')
      Katkun.send_keys(Pembimbng2)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi1').click()
    elif Pilih =='3':
      Log.info('Pembimbingan Penetapan Tindakan Anak')
      Katkun.send_keys(Pembimbng3)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi2').click()
    elif Pilih =='4':
      Log.info('Pembimbingan Pidana dengan Syarat Anak (pidana pembinaan di luar lembaga)')
      Katkun.send_keys(Pembimbng4)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi3').click()
    elif Pilih =='5':
      Log.info('Pembimbingan Pidana dengan Syarat Anak (pelayanan masyarakat)')
      Katkun.send_keys(Pembimbng5)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi4').click()
    elif Pilih =='6':
      Log.info('Pembimbingan Pidana dengan Syarat Anak (pidana pengawasan)')
      Katkun.send_keys(Pembimbng6)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi5').click()
    elif Pilih =='7':
      Log.info('Pembimbingan Pidana Peringatan Anak')
      Katkun.send_keys(Pembimbng7)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi6').click()
    elif Pilih =='8':
      Log.info('Pembimbingan Pidana Pelatihan Kerja Anak')
      Katkun.send_keys(Pembimbng8)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi7').click()
    elif Pilih =='9':
      Log.info('Pembimbingan Asimilasi Anak')
      Katkun.send_keys(Pembimbng9)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi8').click()
    elif Pilih =='10':
      Log.info('Pembimbingan CB Anak')
      Katkun.send_keys(Pembimbng10)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi9').click()
    elif Pilih =='11':
      Log.info('Pembimbingan CMB Anak')
      Katkun.send_keys(Pembimbng11)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi10').click()
    elif Pilih =='12':
      Log.info('Pembimbingan PB Anak')
      Katkun.send_keys(Pembimbng12)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi11').click()
    elif Pilih =='13':
      Log.info('Pembimbingan Tambahan (After Care) Anak')
      Katkun.send_keys(Pembimbng13)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi12').click()
    elif Pilih =='14':
      Log.info('Buku Ekspirasi Pembimbingan dan Pengawasan Anak')
      Katkun.send_keys(Pembimbng14)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi13').click()
    elif Pilih =='15':
      Log.info('Pidana dengan Syarat')
      Katkun.send_keys(Pembimbng15)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi14').click()
    elif Pilih =='16':
      Log.info('Pembimbingan Asimilasi')
      Katkun.send_keys(Pembimbng16)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi15').click()
    elif Pilih =='17':
      Log.info('Pembimbingan CB')
      Katkun.send_keys(Pembimbng17)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi16').click()
    elif Pilih =='18':
      Log.info('Pembimbingan CMB')
      Katkun.send_keys(Pembimbng18)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi17').click()
    elif Pilih =='19':
      Log.info('Pembimbingan PB')
      Katkun.send_keys(Pembimbng19)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi18').click()
    elif Pilih =='20':
      Log.info('Pembimbingan Tambahan After Care')
      Katkun.send_keys(Pembimbng20)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi19').click()
    elif Pilih =='21':
      Log.info('Pembimbingan dan Pengawasan (buku pembantu register)')
      Katkun.send_keys(Pembimbng21)
      turu(driver)
      driver.find_element(By.ID, 'jenisRegistrasi20').click()
  except NoSuchElementException:
    Log.info('ERORRRRRRRRR')
  driver.find_element(By.ID, "searchButton").click()	
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
  