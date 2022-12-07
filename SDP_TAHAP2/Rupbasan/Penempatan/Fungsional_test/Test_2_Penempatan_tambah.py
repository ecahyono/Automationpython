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

from Settings.setup import initDriver, loadDataPath, quit, sleep
from Settings.login import login

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('TF2_Penempatan_tambah.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrange1 = wb['Penempatan']
j = 2

caribarang   	= sheetrange1['A'+str(j)].value #Cari Barang
tglpenempatan 	= sheetrange1['B'+str(j)].value #Tanggal Penempatan
tglpenyimpanan  = sheetrange1['C'+str(j)].value #Tanggal Penyimpanan
pilihtersangka 	= sheetrange1['D'+str(j)].value #Pilih Tersangka
gudang 		  	= sheetrange1['E'+str(j)].value #Gudang
sektorgudang   	= sheetrange1['F'+str(j)].value #Sektor Gudang
barisraklemari 	= sheetrange1['G'+str(j)].value #Baris/Rak/Lemari
nourut  		= sheetrange1['H'+str(j)].value #No Urut
keterangan      = sheetrange1['I'+str(j)].value #Keterangan

@mark.fixture_penempatan
def test_Ossetup_1():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')

@mark.fixture_penempatan
def test_loggin_2():
    login(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Memasukan User name dan Password di halaman Login)')

@mark.fixture_penempatan
def test_akses_menu_penempatan_3():
    nav = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['MainText'])
    ActionChains(driver).move_to_element(nav).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Penempatan').click()
    driver.find_element(By.XPATH, pathData['Rupelemen']['indexpenempatan']['klik']).click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('mengakses menu penempatan')

@mark.fixture_penempatan
def test_aksesmenu_tambah_4():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By. ID, 'searchButton')))
    driver.find_element(By. ID, 'createButton').click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('membuka halaman tambah dengan menekan button tambah')

@mark.fixture_penempatan
def test_tambah_1():
	barang = driver.find_element(By.ID, 'identity_keyword')
	barang.click()
	barang.send_keys(caribarang)
	sleep(driver)
	driver.find_element(By.ID, 'identity_keyword-0').click()

	attach(data=driver.get_screenshot_as_png())
	Log.info('Memilih value, kemudian mengosongkan pilihan dengan clear button value, lalu ditampilkan validation message jika mandatory')

@mark.fixture_penempatan
def test_tambah_2():
	tgl = driver.find_element(By.ID, 'tgl_penempatan')
	tgl.click()
	tgl.send_keys(tglpenempatan)
	tgl.send_keys(Keys.ENTER)

	attach(data=driver.get_screenshot_as_png())
	Log.info('memilih tanggal dengan format DD/MM/YYYY ')

@mark.fixture_penempatan
def test_tambah_3():
    tgl2 = driver.find_element(By.ID, 'tgl_penyimpanan')
    tgl2.click()
    tgl2.send_keys(tglpenyimpanan)
    tgl2.send_keys(Keys.ENTER)

    attach(data=driver.get_screenshot_as_png())
    Log.info('memilih tanggal dengan format DD/MM/YYYY ')

@mark.fixture_penempatan
def test_tambah_4():
    Tersangka = driver.find_element(By. ID, 'dropdownPilihTersangka')
    Tersangka.click()
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="el-popper-container-7411"]/div[16]/div/p')))


@mark.fixture_penempatan
def test_tambah_4():
    driver.find_element(By. ID, 'dropdownGudang').click()
    driver.find_element(By. ID, 'Gudang Berharga').click()
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['+penempatan']['descgudang'])))
    
    driver.find_element(By. ID, 'dropdownSektorGudang').click()
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//div[17]/div/div/div[1]/ul')))
    driver.find_element(By. ID, 'Test Sektor Pribadi').click()
    
    driver.find_element(By. ID, 'dropdownBaris').click()
    driver.find_element(By. ID, 'baris satuya').click()
    
    driver.find_element(By. ID, 'dropdownNoUrut').click()
    driver.find_element(By. ID, '764').click()  

    attach(data=driver.get_screenshot_as_png())
    Log.info('Memilih value, kemudian mengosongkan pilihan dengan clear button value, lalu ditampilkan validation message jika mandatory')

@mark.fixture_penempatan
def test_inputtestarea_7():
    area = driver.find_element(By. ID, 'keterangan')
    area.send_keys(keterangan)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Input field menggunakan varchar, value indicatornya sesuai ')

# @mark.fixture_penempatan
# def test_muatulang_8():
#     driver.find_element(By.ID, 'resetButton').click()
#     driver.find_element(By.XPATH, pathData['Id Even Button']['Button Muat Ulang Ya']).click()
#     # driver.find_element(By.ID, 'resetButton').click()
#     # driver.find_element(By.XPATH, pathData['Id Even Button']['Button Muat Ulang Tidak']).click()
#     attach(data=driver.get_screenshot_as_png())
#     Log.info('Hapus semua inputan di form dengan klik button muat ulang')

# @mark.fixture_penempatan
# def test_submitdata_9():

#     filter = driver.find_element(By. XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/form/div/div[1]/div/div/div/div/div/input')
#     ActionChains(driver).move_to_element(filter).perform()

#     elemnthps = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['+penempatan']['hpscaribrng'])
#     ActionChains(driver).move_to_element(elemnthps).perform()
#     elemnthps.click()

#     test_SelectDropdwn_5()
#     test_inputdate_6()
#     test_inputtestarea_7()
#     driver.find_element(By.ID, 'submitButton').click()
#     WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By. ID, 'searchButton')))

#     attach(data=driver.get_screenshot_as_png())
#     Log.info('Simpan data dengan klik button simpan dan data akan tampil di halaman index dengan data sesuai inputan')
    