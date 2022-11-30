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
import platform
import logging
import sys

from dotenv import load_dotenv
load_dotenv()

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR")) 
elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))

from Settings.setup import initDriver, loadDataPath
from Settings.login import login


Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Test_Penerimaan_2_tambah.log', mode="w")
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
def test_Masukhalamatambah_4():
    driver.find_element(By.ID, 'createButton').click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Membuka halaman tambah penerimaan dengan klik button tambah')
    

@mark.fixture_penerimaan
def test_Input_dropdown_5():
    driver.find_element(By.ID, 'dropdownJenisRegistrasi').click()
    time.sleep(1)
    driver.find_element(By.ID, 'jenisRegistrasi0').click()
    time.sleep(2)
    driver.find_element(By.ID, 'dropdownInstansi').click()
    time.sleep(1)
    driver.find_element(By.ID, 'instansi3').click()
    time.sleep(2)
    driver.find_element(By.ID, 'dropdownPengadilanPenyita').click()
    time.sleep(1)
    driver.find_element(By.ID, 'pengadilanNegeri4').click()
    time.sleep(2)
    Petugas_Penerima = driver.find_element(By.ID, 'searchPetugasPenerima')
    Petugas_Penerima.click()
    Petugas_Penerima.send_keys('PEGWAI')
    driver.find_element(By. ID, 'searchPetugasPenerima0').click()
    
    time.sleep(2)
    PetugasygMenyerahkan = driver.find_element(By.ID, 'searchPetugasYangMenyerahkan')
    PetugasygMenyerahkan.click()
    PetugasygMenyerahkan.send_keys("Galih")
    driver.find_element(By. ID, 'searchPetugasYangMenyerahkan0').click()
    time.sleep(2)
    # Tabidentitas 
    ident = driver.find_element(By. ID, 'searchIdentitas-0')
    ident.click()
    ident.send_keys('EKO')
    driver.find_element(By. ID,'searchIdentitas-00').click()

    Log.info('Memilih value, kemudian mengosongkan pilihan dengan clear button value, lalu ditampilkan validation message jika mandatory')
@mark.fixture_penerimaan
def test_inputtext_6():
    driver.find_element(By.ID, 'inputNoRegistrasi').send_keys('NRB05') #Nomor Registrasi Rupbasan
    driver.find_element(By.ID, 'inputNoRegInstansi').send_keys('NRI005') #Nomor Registrasi Instansi
    driver.find_element(By.ID,'inputNoSuratIzinPenyitaan').send_keys('NSIP005') #Nomor Surat Izin Penyitaan
    driver.find_element(By.ID, 'inputNoSuratPenyitaan').send_keys('NSP005') #Nomor Surat Penyitaan
    driver.find_element(By.ID,'inputPasal').send_keys('PASAL') #Pasal
    driver.find_element(By.ID, 'inputNoBaSerahTerima').send_keys('NBAST005') #No. BA Serah Terima
    Log.info('Input field menggunakan varchar')
    time.sleep(2)
@mark.fixture_penerimaan
def test_Inputtextarea_7():
    driver.find_element(By.ID, 'inputKeterangan').send_keys('AUTOMAS1')
    Log.info('Input field lalu value indicatornya sesuai dan tidak bisa input lebih dari max length Bisa scroll isi field')
    time.sleep(2)
@mark.fixture_penerimaan
def test_Inputdate():
    Tanggal_Penerimaan = driver.find_element(By.ID,'inputTglPenerimaan')
    Tanggal_Penerimaan.send_keys('01/11/2022')
    Tanggal_Penerimaan.send_keys(Keys.ENTER)
    time.sleep(2)
    Tanggal_Surat_Izin_Penyitaan = driver.find_element(By.ID,'inputTglSuratIzinPenyitaan')
    Tanggal_Surat_Izin_Penyitaan.send_keys('01/11/2022')
    Tanggal_Surat_Izin_Penyitaan.send_keys(Keys.ENTER)
    time.sleep(2)
    Tanggal_Surat_Penyitaan = driver.find_element(By.ID, 'inputTglSuratPenyitaan')
    Tanggal_Surat_Penyitaan.send_keys('01/11/2022')
    Tanggal_Surat_Penyitaan.send_keys(Keys.ENTER)

    Log.info('Input field dengan tanggal lampau, yang akan datang, dan tanggal hari ini dan tanggal yang ditampilkannya sesuai')
    time.sleep(2)
@mark.fixture_penerimaan
def test_Pindahtabptgsinstansi():
    driver.find_element(By.ID, "tab-petugas_instansi").click()
    driver.find_element(By.ID, "tambahPenyerahPenerima").click()
    Log.info('klik tab Petugas Instansi yang Menyerahkan, kemudian menambah 1 baris status petugas')
    time.sleep(2)
@mark.fixture_penerimaan
def test_radiobuttonptgsinstansi():
    driver.find_element(By.ID, 'radioButtonStatusPetugasInternal-0').click() #memilih Internal
    time.sleep(2)    
    penyerah = driver.find_element(By.ID, 'searchPetugasPenyerah-0')
    penyerah.click() #mencari Identitas internal
    penyerah.send_keys('PEGWAI')
    driver.find_element(By. ID, 'searchPetugasPenyerah-09').click()

    time.sleep(2)

    driver.find_element(By.ID, 'radioButtonStatusPetugasEksternal-1').click() #memilih External
    time.sleep(2)  
    penyerah2 = driver.find_element(By.ID, 'searchPetugasPenyerahEksternal-1')
    penyerah2.click() #mencari Identitas external
    penyerah2.send_keys('g')
    driver.find_element(By. ID, 'searchPetugasPenyerahEksternal-11').click()

    Log.info('memilih radiobutton status petugas kemudian mencari petugas internal dan external')
    time.sleep(2)
@mark.fixture_penerimaan
def test_Pindahtabsaksii():
    driver.find_element(By.ID, "tab-saksi_penerimaan").click()
    driver.find_element(By.ID, "tambahSaksi").click()
    time.sleep(2)
    Log.info('Klik tab Saksi Penerima, kemudian menambah 1 baris status Saksi')

@mark.fixture_penerimaan
def test_radiobuttonsaksi():
    driver.find_element(By.ID, 'radioButtonStatusSaksiEksternal-0').click() #memilih External
    time.sleep(2)   
    saksi = driver.find_element(By.ID, 'searchSaksiPenerimaanEksternal-0')
    saksi.click() #mencari Identitas External
    saksi.send_keys('g')
    driver.find_element(By. ID, 'searchSaksiPenerimaanEksternal-00').click()
    time.sleep(2)
    driver.find_element(By.ID, 'radioButtonStatusSaksiInternal-1').click() #memilih Internal
    time.sleep(2)    
    saksi2 = driver.find_element(By.ID, 'searchSaksiPenerimaan-1')
    saksi2.click() #mencari Identitas internal
    saksi2.send_keys('PEGWAI')
    driver.find_element(By. ID, 'searchSaksiPenerimaan-13').click()
    time.sleep(2)
    Log.info('memilih radiobutton status petugas kemudian mencari petugas internal dan external')
    
@mark.fixture_penerimaan
def test_SubmitDatapenerimaan():
    driver.find_element(By.ID, "submitButton").click()

    Log.info('menekan button submit')