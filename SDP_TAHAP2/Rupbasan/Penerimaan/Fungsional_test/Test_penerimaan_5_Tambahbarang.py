from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pytest_html_reporter import attach
import os, platform, time, pytest
from selenium import webdriver
from os import environ, path
from pathlib import Path
from pytest import mark
import pyautogui
import platform
import logging
import sys


from dotenv import load_dotenv
load_dotenv()

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR")) 
elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))

from Settings.setup import initDriver, loadDataPath, quit
from Settings.login import login


Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Test_penerimaan_5_Tambahbarang.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

# init driver by os
@mark.fixture_penempatan
def test_Ossetup_1():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')

@mark.fixture_penempatan
def test_loggin_2():
    login(driver)
    Log.info('Memasukan User name dan Password di halaman Login)')

@mark.fixture_penerimaan
def test_aksesmenuPenerimaan_3():
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.LINK_TEXT, 'Penerimaan').click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Menuju Menu Penerimaan dengan mengarahkan kursor ke navigasi ''Rubasan'' kemudian sub menu ''Penerimaan''')

@mark.fixture_penerimaan
def test_membukahalamanDetailBarang_4():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
    time.sleep(1)
    driver.find_element(By.ID, 'filterColumn').click()
    time.sleep(1)
    driver.find_element(By. ID, 'keterangan').click()
    driver.find_element(By. ID, 'kataKunci').send_keys('Test QA')
    driver.find_element(By.ID , 'searchButton').click()
    time.sleep(1)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
    driver.find_element(By.ID, 'daftarBarang1').click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'backButton')))

    attach(data=driver.get_screenshot_as_png())
    Log.info('Akses menu halama detail Penerimaan')

#Kelengkapan Basan Baran ==============================================================
@mark.fixture_penerimaan
def test_inputtexttabkelangkapan_5():
    driver.find_element(By.ID, 'nama_barang').send_keys('Kalung emas') #Nama Barang
    driver.find_element(By.ID, 'jumlah').send_keys('24')
    driver.find_element(By.ID, 'jumlah_baik').send_keys('12')
    driver.find_element(By.ID, 'jumlah_rusak_ringan').send_keys('6')
    driver.find_element(By.ID, 'jumlah_rusak_berat').send_keys('6')

    driver.find_element(By.ID, 'namaFoto0').send_keys('Foto barang')

@mark.fixture_penerimaan
def test_dropdownttabkelangkapan_6():
    driver.find_element(By.ID, 'input_jenis_baran_basan').click() 
    driver.find_element(By.ID, 'JSB3').click() #Berharga

    driver.find_element(By.ID, 'input_satuan_baran_basan').click()
    driver.find_element(By.ID, '01').click() #unit

# @mark.fixture_penerimaan
# def test_fotottabkelangkapan_7():
#     driver.find_element(By.ID, 'pilihFoto0').click()
#     time.sleep(5)
#     pyautogui.write(environ.get(r"FOTBRG1"))
#     pyautogui.press('enter')

@mark.fixture_penerimaan
def test_textareattabkelangkapan_8():
    driver.find_element(By.ID, 'keterangann0').send_keys('Keterangan foto 1 dan seterusnya')

@mark.fixture_penerimaan
def test_checkbox_9():
    driver.find_element(By.ID, 'barang_temuan').click()

# # Penelitian ==============================================================
def test_pindahtabpenelitian_10():
    driver.find_element(By.ID, 'tab-penelitian').click()

@mark.fixture_penerimaan
def test_dropdownttabPenelitian_11(): 
    # Golongan
    driver.find_element(By.ID, 'golongan').click()
    time.sleep(2)
    driver.find_element(By.ID, '038').click() # PERHIASAN
    #Kondisi Barang
    driver.find_element(By.ID, 'kondisiBarang').click()
    time.sleep(2)
    driver.find_element(By.ID, 'KBB1').click() #Baik
    #Kondisi Barang
    driver.find_element(By.ID, 'kondisiBarang').click()
    time.sleep(2)
    driver.find_element(By.ID, 'KBB1').click() #Baik

    # Tim Peneliti
    Penelitian = driver.find_element(By.ID, 'cariPeneliti0')
    Penelitian.click()
    Penelitian.send_keys("SARADINDA")
    driver.find_element(By.ID, 'petugas0').click()
    
    driver.find_element(By.ID, 'tambahPeneliti').click()
    # Tim Peneliti
    Penelitian = driver.find_element(By.ID, 'cariPeneliti1')
    Penelitian.click()
    Penelitian.send_keys("Robi Sugara")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#petugas0').click()

# @mark.fixture_penerimaan
# def test_inputtexttabPenelitian_12():
#     driver.find_element(By.ID, 'noPenelitian')    .send_keys('AUTTCNP01') #Nomor Penelitian
#     driver.find_element(By.ID, 'noSkPeneliti')    .send_keys('AUTTCSKP01') #Nomor SK Peneliti
#     driver.find_element(By.ID, 'keadaanSegel')    .send_keys('Baik') #Keadaan Segel Penyita
#     driver.find_element(By.ID, 'sifat')           .send_keys('Keras') #Sifat
#     driver.find_element(By.ID, 'merekKondisi')    .send_keys('sinarmas baik') #Merek Dan Kondisi
#     driver.find_element(By.ID, 'berat')           .send_keys('10') #Berat
#     driver.find_element(By.ID, 'volumeCc')        .send_keys('1') #Volume / CC
#     driver.find_element(By.ID, 'panjang')         .send_keys('25') #Panjang
#     driver.find_element(By.ID, 'lebar')           .send_keys('2') #Lebar
#     driver.find_element(By.ID, 'tinggi')          .send_keys('5') #Tinggi
#     driver.find_element(By.ID, 'tipeMerek')       .send_keys('sinarmas') #Tipe / Merek
#     driver.find_element(By.ID, 'pembuatPabrik')   .send_keys('rajamas') #Pembuat Pabrik
#     driver.find_element(By.ID, 'nomorPabrik')     .send_keys('NO983473') #Nomor Pabrik
#     driver.find_element(By.ID, 'nmr_dikeluarkan') .send_keys('NOKeluar28734') #Nomor Dikeluarkan
#     driver.find_element(By.ID, 'asalDari')        .send_keys('Jakarta') #Asal Basan Dari
#     driver.find_element(By.ID, 'perkiraanUsia')   .send_keys('30') #Perkiraan Usia
#     driver.find_element(By.ID, 'batasan')         .send_keys('Dewasa') #Batasan
#     driver.find_element(By.ID, 'NoImb')           .send_keys('AUTTCKSP01') #No. IMB
#     driver.find_element(By.ID, 'isiGedung')       .send_keys('AUTTCKSP01') #Isi Gedung
#     driver.find_element(By.ID, 'suratBukti')      .send_keys('AUTTCKSP01') #Surat Bukti
#     driver.find_element(By.ID, 'bendera')         .send_keys('Indonesia') #Bendera Negara
#     driver.find_element(By.ID, 'ciriKhusus')      .send_keys('Warna emas') #Ciri Khusus
#     driver.find_element(By.ID, 'halLainnya')      .send_keys('ini emas asli') #Hal Lainnya

# @mark.fixture_penerimaan
# def test_inputDatetabPenelitian_13():
#     tglPenelitian = driver.find_element(By.ID, 'tglPenelitian')
#     tglPenelitian.click()
#     tglPenelitian.send_keys('02/11/2022') #Tanggal Penelitian
#     tglPenelitian.send_keys(Keys.ENTER)

#     tglSkPeneliti = driver.find_element(By.ID, 'tglSkPeneliti')
#     tglSkPeneliti.click()
#     tglSkPeneliti.send_keys('02/11/2022') #TTanggal SK Peneliti
#     tglSkPeneliti.send_keys(Keys.ENTER)

#     tglKeluar = driver.find_element(By.ID, 'tglKeluar')
#     tglKeluar.click()
#     tglKeluar.send_keys('02/11/2022') #Tanggal Keluar
#     tglKeluar.send_keys(Keys.ENTER)

#     tglBerlakuPasSenpi = driver.find_element(By.ID, 'tglBerlakuPasSenpi')
#     tglBerlakuPasSenpi.click()
#     tglBerlakuPasSenpi.send_keys('02/11/2022') #Tanggal Berlaku
#     tglBerlakuPasSenpi.send_keys(Keys.ENTER)

# @mark.fixture_penerimaan
# def test_inputtextareatabPenelitian_14():
#     driver.find_element(By.ID, 'catatanPemeliharaanKhusus').send_keys('AUTTCNP01Keterangan Catatan Pemeliharaan Khusus') #Catatan Pemeliharaan Khusus
#     driver.find_element(By.ID, 'rekomendasiTimPeneliti').send_keys('AUTTCNP01Keterangan Rekomendasi Tim Peneliti') #Rekomendasi Tim Peneliti

# @mark.fixture_penerimaan
# def test_checkboxtabPenelitian_15():
#     driver.find_element(By.ID, 'PemeliharaanKhusus').click() #Pemeliharaan Khusus

# Penilaian ==============================================================
# def test_pindahtabpenilaian_16():
#     driver.find_element(By.ID, 'tab-penilaian').click()

# @mark.fixture_penerimaan
# def test_inputtextabPenelitian_17():
#     driver.find_element(By.ID, 'noBaPenelitian').send_keys('AUTTCBAP01') #Nomor BA Penelitian
#     driver.find_element(By.ID, 'nilaiSatuan').send_keys('5000000') #Nilai Satuan Barang

# @mark.fixture_penerimaan
# def test_inputtextareatabPenelitian_18():
#     driver.find_element(By.ID, 'keterangan').send_keys('AUTTCNP01Keterangan Penilaian') #Keterangan

# @mark.fixture_penerimaan
# def test_inputDatetabPenilaia_19():
#     tglPenilaian = driver.find_element(By.ID, 'tglPenilaian')
#     tglPenilaian.click()
#     tglPenilaian.send_keys('02/11/2022') #Tanggal Penelitian
#     tglPenilaian.send_keys(Keys.ENTER)

# @mark.fixture_penerimaan
# def test_dropdowntabpenilaian_20():
    
#     # Tim Penilaian
#     Penilai = driver.find_element(By.ID, 'cariPenilai0')
#     Penilai.click()
#     Penilai.send_keys("SARADINDA")
#     driver.find_element(By.ID, 'petugas0').click()

# @mark.fixture_penerimaan
# def test_submitdata_21():
#     driver.find_element(By.ID,'submitButton').click()
    
