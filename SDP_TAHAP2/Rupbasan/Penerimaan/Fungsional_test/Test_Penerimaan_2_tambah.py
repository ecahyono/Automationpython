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
    driver.find_element(By.ID, 'dropdownJenisRegistrasiBasanBaran').click()
    time.sleep(1)
    driver.find_element(By.ID, 'Register Khusus Tingkat Mahkamah Agung').click()

    driver.find_element(By.ID, 'dropdownInstansi').click()
    time.sleep(1)
    driver.find_element(By.ID, 'POLRES TEBING TINGGI').click()

    driver.find_element(By.ID, 'dropdownPengadilanPenyita').click()
    time.sleep(1)
    driver.find_element(By.ID, 'Pengadilan Negeri Tarutung').click()

    
# @mark.fixture_penerimaan
# def test_5_input_text():
#     driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Nomor Registrasi Rupbasan']).send_keys('CNRB01')
#     driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Nomor Registrasi Instansi']).send_keys('AUTTCNRI001')
#     driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Nomor Surat Izin Penyitaan']).send_keys('AUTTCNSP001')
#     driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Nomor Surat Penyitaan']).send_keys('AUTTCNSP001')
#     driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Pasal']).send_keys('AUTTCPASAL')
#     driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['No. BA Serah Terima']).send_keys('AUTTCNBAST001')
#     driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['noregidentitas']).send_keys('AUTTCNRI001')
#     driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['NMlngkpidentitas']).send_keys('TESAUTO')
#     driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['NOKTP']).send_keys('1234123412341234')
#     driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['NOtlp']).send_keys('086767857665')

# @mark.fixture_penerimaan
# def test_6_Input_text_area():
#     driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Keterangan']).send_keys('*&+_-Keterangan @ Penerimaan Rupb454N')
#     driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['idnalamat']).send_keys('*&+_-ALAMATKeterangan @ Penerimaan Rupb454N')
#     driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['idenKeterangan']).send_keys('*&+_-Keterangan @ Penerimaan Rupb454N')

@mark.fixture_penerimaan
def test_7_Input_date():
    Tanggal_Penerimaan = driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Tanggal Penerimaan'])
    Tanggal_Penerimaan.click()
    Tanggal_Penerimaan.send_keys('01/11/2022')
    Tanggal_Penerimaan.send_keys(Keys.ENTER)

    Tanggal_Surat_Izin_Penyitaan = driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Tanggal Surat Izin Penyitaan'])
    Tanggal_Surat_Izin_Penyitaan.click()
    Tanggal_Surat_Izin_Penyitaan.send_keys('01/11/2022')
    Tanggal_Surat_Izin_Penyitaan.send_keys(Keys.ENTER)

    Tanggal_Surat_Penyitaan = driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Tanggal Surat Penyitaan'])
    Tanggal_Surat_Penyitaan.click()
    Tanggal_Surat_Penyitaan.send_keys('01/11/2022')
    Tanggal_Surat_Penyitaan.send_keys(Keys.ENTER)

    TglIdnlhr = driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['tgllhiridnt'])
    TglIdnlhr.click()
    TglIdnlhr.send_keys('01/09/1998')
    TglIdnlhr.send_keys(Keys.ENTER)
    Jenis_Registrasi.click()
    time.sleep(2)
    Jenis_Registrasi.send_keys('Register Barang Rampasan Negara')
    Jenis_Registrasi.send_keys(Keys.DOWN)
    Jenis_Registrasi.send_keys(Keys.ENTER)
    
    Instansi = driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Instansi'])
    Instansi.click()
    time.sleep(2)
    Instansi.send_keys('POLDA METRO JAYA')
    Instansi.send_keys(Keys.DOWN)
    Instansi.send_keys(Keys.ENTER)

    Pengadilan_Penyita = driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Pengadilan Penyita'])
    Pengadilan_Penyita.click()
    time.sleep(2)
    Pengadilan_Penyita.send_keys('Pengadilan Negeri Jakarta Pusat barat')
    Pengadilan_Penyita.send_keys(Keys.DOWN)
    Pengadilan_Penyita.send_keys(Keys.ENTER)

    Petugas_Penerima = driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Petugas Penerima'])
    Petugas_Penerima.click()
    Petugas_Penerima.send_keys('Ananda Septiana Lestari')
    driver.find_element(By. ID, 'cariPetugasInternal').click()
    driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1)> .el-descriptions__label ').click()
    time.sleep(2)
    PetugasygMenyerahkan = driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Petugas yang Menyerahkan'])
    PetugasygMenyerahkan.click()
    PetugasygMenyerahkan.send_keys("Rehan")
    driver.find_element(By. ID, 'cariPetugasEksternal').click()
    driver.find_element(By.XPATH, "//div[19]/div/div/div/ul/li").click()

    # Tabidentitas 
    TersangkaPemilik = driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['TersangkaPemilik'])
    TersangkaPemilik.click()
    driver.find_element(By.ID, "Tersangka").click()
    driver.find_element(By.XPATH, "//div[20]/div/div/div[1]/ul/li[1]").click()

    JenisKelamin = driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['JenisKelamin'])
    JenisKelamin.click()
    driver.find_element(By.ID, "L").click()

# @mark.fixture_penerimaan
# def test_9_Pindah_tab():
#     driver.find_element(By.ID, "tab-petugas_instansi").click()
#     driver.find_element(By.ID, "tab-saksi_penerimaan").click()

# @mark.fixture_penerimaan
# def test_10_pilih_radiobutton():
#     driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['internalradiosaksi']).click()
#     driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['externalradiosaksi']).click()

# @mark.fixture_penerimaan
# def test_11_Submit_Data_penerimaan():
#     driver.find_element(By.ID, "submitButton").click()