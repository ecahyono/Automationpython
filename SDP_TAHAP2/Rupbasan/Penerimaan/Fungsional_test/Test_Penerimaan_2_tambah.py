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
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['AksesMenu']['Rupbasan']['menu']['MainText'])
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

    driver.find_element(By.ID, 'cariPetugasundefined').click()
    time.sleep(1)
    driver.find_element(By.ID, 'Pengadilan Negeri Tarutung').click()

    Petugas_Penerima = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['+penerimaan']['PtgPenerima'])
    Petugas_Penerima.click()
    Petugas_Penerima.send_keys('Ananda Septiana Lestari')
    driver.find_element(By. ID, 'cariPetugasInternal').click()
    driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1)> .el-descriptions__label ').click()
    time.sleep(2)
    PetugasygMenyerahkan = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['+penerimaan']['PMenyerahkan'])
    PetugasygMenyerahkan.click()
    PetugasygMenyerahkan.send_keys("Rehan")
    driver.find_element(By. ID, 'cariPetugasEksternal').click()
    driver.find_element(By.XPATH, "//div[19]/div/div/div/ul/li").click()

    # Tabidentitas 
    driver.find_element(By. ID, 'cariIdentitasundefined').click()

@mark.fixture_penerimaan
def test_inputtext_6():
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[1]/div[3]/div/div[1]/input').send_keys('TCAUTTCNRB01') #Nomor Registrasi Rupbasan
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[1]/div[5]/div/div/input').send_keys('TCAUTTCNRI001') #Nomor Registrasi Instansi
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[1]/div[5]/div/div/input').send_keys('TCAUTTCNSP001') #Nomor Surat Izin Penyitaan
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[1]/div[6]/div/div[1]/input').send_keys('TCAUTTCNSP001') #Nomor Surat Penyitaan
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/input').send_keys('TCAUTTCPASAL') #Pasal
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/form/div[1]/div[2]/div[5]/div/div/input').send_keys('TCAUTTCNBAST001') #No. BA Serah Terima

    #No. Registrasi
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/form/div[5]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[1]/div/div/div[2]/div/div/input').send_keys('TCAUTTCNRI001') 
    #Nama Lengkap
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/form/div[5]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[1]/div/div/div[3]/div/div[1]/input').send_keys('TESAUTO')
    #No. KTP
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/form/div[5]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[1]/div/div/div[4]/div/div/input').send_keys('1234123412341234')
    #No. Telepon
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/form/div[5]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[1]/div/div/div[8]/div/div[1]/input').send_keys('086767857665')

@mark.fixture_penerimaan
def test_Inputtextarea_7():
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['+penerimaan']['Keterangan']).send_keys('*&+_-Keterangan @ Penerimaan Rupb454N')
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['+penerimaan']['idnalamat']).send_keys('*&+_-ALAMATKeterangan @ Penerimaan Rupb454N')
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['+penerimaan']['idenKeterangan']).send_keys('*&+_-Keterangan @ Penerimaan Rupb454N')

@mark.fixture_penerimaan
def test_7_Input_date():
    Tanggal_Penerimaan = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['+penerimaan']['Tanggal Penerimaan'])
    Tanggal_Penerimaan.click()
    Tanggal_Penerimaan.send_keys('01/11/2022')
    Tanggal_Penerimaan.send_keys(Keys.ENTER)

    Tanggal_Surat_Izin_Penyitaan = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['+penerimaan']['Tanggal Surat Izin Penyitaan'])
    Tanggal_Surat_Izin_Penyitaan.click()
    Tanggal_Surat_Izin_Penyitaan.send_keys('01/11/2022')
    Tanggal_Surat_Izin_Penyitaan.send_keys(Keys.ENTER)

    Tanggal_Surat_Penyitaan = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['+penerimaan']['Tanggal Surat Penyitaan'])
    Tanggal_Surat_Penyitaan.click()
    Tanggal_Surat_Penyitaan.send_keys('01/11/2022')
    Tanggal_Surat_Penyitaan.send_keys(Keys.ENTER)

    TglIdnlhr = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['+penerimaan']['tgllhiridnt'])
    TglIdnlhr.click()
    TglIdnlhr.send_keys('01/09/1998')
    TglIdnlhr.send_keys(Keys.ENTER)

@mark.fixture_penerimaan
def test_9_Pindah_tab():
    driver.find_element(By.ID, "tab-petugas_instansi").click()
    driver.find_element(By.ID, "tab-saksi_penerimaan").click()

@mark.fixture_penerimaan
def test_10_pilih_radiobutton():
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['+penerimaan']['internalradiosaksi']).click()
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['+penerimaan']['externalradiosaksi']).click()

@mark.fixture_penerimaan
def test_11_Submit_Data_penerimaan():
    driver.find_element(By.ID, "submitButton").click()