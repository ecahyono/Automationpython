from jenis_Litmas.src import *
from jenis_Litmas.fakeoption import *
from sesilitmas import sesilitmas, Penjamin
from jenis_Litmas.litmasdiversi import *
from jenis_Litmas.litmasprosesperadilananak import *
from jenis_Litmas.litmasprogrampelayanananakLPAS import *
from jenis_Litmas.litmasprogrampembinaanawalanak import *
from jenis_Litmas.litmasprogramasimilasianak import *
from jenis_Litmas.indikator import *

# init driver by os
@mark.fixture_Litmas
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Memasukan User name dan Password di halaman Login')
	PKbapas(driver) #Operator BPS

@mark.fixture_Litmas
def testlitmas():
  Log.info('Menambah Data Register Pendampingan')
  driver.get('http://kumbang.torche.id:32400/bapas/litmas/penerimaan')
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'CariFilter')))

# I    Litmas Anak
# I.A    Litmas Diversi ----done
# I.B    Litmas Proses Peradilan Anak ----done
# I.C    Litmas Program Pelayanan Anak(LPAS) ----done
# I.D    Litmas Program Pembinaan Awal Anak ----done
# I.E    Litmas Program Asimilasi Anak ----done
# I.F    Litmas Program Re-Integrasi (CB) Anak ----done
# I.G    Litmas Program Re-Integrasi (CMB) Anak ----done
# I.H    Litmas Program Re-Integrasi (PB) Anak ----done
# I.I    Litmas Pembimbingan
# VIII    Litmas Dewasa
# VIII.A    Litmas Proses Peradilan Dewasa  ----done
# VIII.B    Litmas untuk Program Pelayanan di RUTAN ----done
# VIII.C    Litmas Pembinaan Awal ----done
# VIII.D    Litmas Program Asimilasi ----done
# VIII.E    Litmas Program Re-Integrasi (CB) ----done
# VIII.F    Litmas Program Re-Integrasi (CMB) ----done
# VIII.G    Litmas Program Re-Integrasi (PB) ----done

@mark.fixture_Litmas
def testfiltertable():
  global forkatkun
  kolom = driver.find_element(By.ID, "column")
  kolom.click()
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'JenLit')))
  driver.find_element(By.ID, "JenLit").click()
  jenlitmasnya = driver.find_element(By.ID, "dropdownJenisRegistrasi")
  jenlitmasnya.click()

  forkatkun = input('Pilih Jenis Litmas yang akan DItambah instrumen \n'
        '1. Litmas Diversi \n'
        '2. Litmas Proses Peradilan Anak \n'
        '3. Litmas Program Pelayanan Anak(LPAS) \n'
        '4. Litmas Program Pembinaan Awal Anak \n'
        '5. Litmas Program Asimilasi Anak \n'
        '6. Litmas Program Re-Integrasi (CB) Anak \n'
        '7. Litmas Program Re-Integrasi (CMB) Anak \n'
        '8. Litmas Program Re-Integrasi (PB) Anak \n'
        '9. Litmas Pembimbingan \n'
        '10. Litmas Proses Peradilan Dewasa \n'
        '11. Litmas untuk Program Pelayanan di RUTAN \n'
        '12. Litmas Pembinaan Awal \n'
        '13. Litmas Program Asimilasi \n'
        '14. Litmas Program Re-Integrasi (CB) \n'
        '15. Litmas Program Re-Integrasi (CMB) \n'
        '16. Litmas Program Re-Integrasi (PB) \n'
        'Masukan Nomer yang tersedia =>: '
  )
  if forkatkun == '1':
    Log.info('Memilih Jenis Litmas=' +Lit1)
    jenlitmasnya.send_keys(Lit1)
    turu(driver)
    driver.find_element(By.ID, "jenisLItmas0").click()
  elif forkatkun == '2':
    Log.info('Memilih Jenis Litmas=' +Lit2)
    jenlitmasnya.send_keys(Lit2)
    turu(driver)
    driver.find_element(By.ID, "jenisLItmas1").click()
  elif forkatkun == '3':
    Log.info('Memilih Jenis Litmas=' +Lit3)
    jenlitmasnya.send_keys(Lit3)
    turu(driver)
    driver.find_element(By.ID, "jenisLItmas2").click()
  elif forkatkun == '4':
    Log.info('Memilih Jenis Litmas=' +Lit4)
    jenlitmasnya.send_keys(Lit4)
    turu(driver)
    driver.find_element(By.ID, "jenisLItmas3").click()
  elif forkatkun == '5':
    Log.info('Memilih Jenis Litmas=' +Lit5)
    jenlitmasnya.send_keys(Lit5)
    turu(driver)
    driver.find_element(By.ID, "jenisLItmas4").click()
  elif forkatkun == '6':
    Log.info('Memilih Jenis Litmas=' +Lit6)
    jenlitmasnya.send_keys(Lit6)
    turu(driver)
    driver.find_element(By.ID, "jenisLItmas5").click()
  elif forkatkun == '7':
    Log.info('Memilih Jenis Litmas=' +Lit7)
    jenlitmasnya.send_keys(Lit7)
    turu(driver)
    driver.find_element(By.ID, "jenisLItmas6").click()
  elif forkatkun == '8':
    Log.info('Memilih Jenis Litmas=' +Lit8)
    jenlitmasnya.send_keys(Lit8)
    turu(driver)
    driver.find_element(By.ID, "jenisLItmas7").click()
  elif forkatkun == '9':
    Log.info('Memilih Jenis Litmas=' +Lit9)
    jenlitmasnya.send_keys(Lit9)
    turu(driver)
    driver.find_element(By.ID, "jenisLItmas8").click()
  elif forkatkun == '10':
    Log.info('Memilih Jenis Litmas=' +Lit10)
    jenlitmasnya.send_keys(Lit10)
    turu(driver)
    driver.find_element(By.ID, "jenisLItmas9").click()
  elif forkatkun == '11':
    Log.info('Memilih Jenis Litmas=' +Lit11)
    jenlitmasnya.send_keys(Lit11)
    turu(driver)
    driver.find_element(By.ID, "jenisLItmas10").click()
  elif forkatkun == '12':
    Log.info('Memilih Jenis Litmas=' +Lit12)
    jenlitmasnya.send_keys(Lit12)
    turu(driver)
    driver.find_element(By.ID, "jenisLItmas11").click()
  elif forkatkun == '13':
    Log.info('Memilih Jenis Litmas=' +Lit13)
    jenlitmasnya.send_keys(Lit13)
    turu(driver)
    driver.find_element(By.ID, "jenisLItmas12").click()
  elif forkatkun == '14':
    Log.info('Memilih Jenis Litmas=' +Lit14)
    jenlitmasnya.send_keys(Lit14)
    turu(driver)
    driver.find_element(By.ID, "jenisLItmas13").click()
  elif forkatkun == '15':
    Log.info('Memilih Jenis Litmas=' +Lit15)
    jenlitmasnya.send_keys(Lit15)
    turu(driver)
    driver.find_element(By.ID, "jenisLItmas14").click()
  elif forkatkun == '16':
    Log.info('Memilih Jenis Litmas=' +Lit16)
    jenlitmasnya.send_keys(Lit16)
    turu(driver)
    driver.find_element(By.ID, "jenisLItmas15").click()
  
  driver.find_element(By.ID, 'CariFilter').click()
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'CariFilter')))
  time.sleep(5)

@mark.fixture_Litmas
def testmemilihjenislitmas():
  time.sleep(3)
  driver.find_element(By.XPATH,"//td[6]/div/button").click() #diganti
  
  # WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
  # WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))

  WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, "tempat")))

@mark.fixture_Litmas
def testmengisiinstrumenlitmas():
  sesilitmas(driver)
  Penjamin(driver)
  if forkatkun == '1':
    RiwayatTindakPidana(driver)
    RiwayatTindakPidana1(driver)
    RiwayatTindakPidana2(driver)
  else:
    RiwayatTindkPidana(driver)
    RiwayatTindkPidana1(driver)
  
  if forkatkun == '1':
    RiwayatHidupKlien(driver)
    RiwayatPendidikan(driver)
    HarapanRencanaKlien(driver)
  elif (forkatkun == '2'or forkatkun == '10'):
    Hasildiversi(driver)
    AkibatygdibuatKlien(driver)
    RiwayatHidupKlien(driver)
    KeadankeluargadiLapasRutanTujuan(driver)
    KeadaanLingkunganMasyarakat(driver)
    Tanggapan(driver)
    Tanggapan1(driver)
    Tanggapan2(driver)
    Tanggapan3(driver)
    Tanggapan4(driver)
    HarapanRencanaKlien(driver)
  elif (forkatkun == '3'or forkatkun == '11'):
    RiwayatPendidikan(driver)
    MinatdanBakat(driver)
    # RiwayatHidupKlien(driver)
    harapanklien(driver)
    TanggapanPihakKetiga(driver)
    TanggapanPihakKetiga1(driver)
    TanggapanPihakKetiga2(driver)
  elif (forkatkun == '4' or forkatkun == '12'):
    RiwayatHidupKlien(driver)
    RiwayatPendidikan(driver)
    MinatdanBakat(driver)
    rencanaKlien(driver)
    potensiKeluargaDanLingkunganTempatTinggalKlien(driver)
    programPerawatanYangDiterimaKlienDiLpas(driver)
  elif (forkatkun == '5' or forkatkun == '13'):
    RiwayatHidupKlien(driver)
    perkembanganPembinaanKlienDiLapasAtauRutan(driver)
    keadaanPenangungJawabAtauPenjamin(driver)
    KeadaanLingkunganMasyarakat(driver)
    tanggapankorban(driver)
    tanggapanKeluargaKoraban(driver)
    Tanggapan3(driver)
    tanggapanPemerintah(driver)
    HarapanRencanaKlien(driver)
    keadaanPihakKetiga(driver)
  elif (forkatkun == '6'or forkatkun == '7' or forkatkun == '8' or forkatkun == '14' or forkatkun == '15'or forkatkun == '16'):
    RiwayatHidupKlien(driver)
    perkembanganPembinaanKlienDiLapasAtauRutan(driver)
    keadaanPenangungJawabAtauPenjamin(driver)
    KeadaanLingkunganMasyarakat(driver)
    tanggapankorban(driver)
    tanggapanKeluargaKoraban(driver)
    Tanggapan3(driver)
    tanggapanPemerintah(driver)
    HarapanRencanaKlien(driver)
  AnalisaHasilPengamatan(driver)
  AnalisaHasilPengamatan1(driver)
  Rekomendasi(driver)