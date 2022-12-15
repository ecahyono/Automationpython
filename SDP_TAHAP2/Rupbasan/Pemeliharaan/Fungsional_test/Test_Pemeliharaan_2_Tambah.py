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
from openpyxl import load_workbook
import sys
import pyautogui

from dotenv import load_dotenv
load_dotenv()

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR")) 
elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))

from Settings.setup import initDriver, loadDataPath, sleep, quit
from Settings.login import login, loginOperator


Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Penerimaan_2_TambahPemeliharaan.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("RUPEXEL"))
sheetrange = wb['Pemeliharan']
i = 2

tglPemeliharaan  = sheetrange['A'+str(i)].value #Tanggal Pemeliharaan
jnspemeliharaan  = sheetrange['B'+str(i)].value #Jenis Pemeliharaan
KgiPemeliharaan  = sheetrange['C'+str(i)].value #Kegiatan Pemeliharaan
Keterangan       = sheetrange['D'+str(i)].value #Keterangan

ketpelaksana	 = sheetrange['E'+str(i)].value #Ketua Pelaksana
ptgsinternal     = sheetrange['F'+str(i)].value #Petugas Pemeliharaan (Internal)
ptgsexternal     = sheetrange['G'+str(i)].value #Petugas Pemeliharaan (Eksternal)

#tab Detail Pemeliharan
jumlhdetail      = sheetrange['H'+str(i)].value #jumlah
namabahan        = sheetrange['I'+str(i)].value #Nama Barang
kndbrng          = sheetrange['J'+str(i)].value #Kondisi Barang
subkonbrg        = sheetrange['K'+str(i)].value #Sub Kondisi Barang
jmlhbaik         = sheetrange['L'+str(i)].value #Jumlah Baik
jmlhRpar      	 = sheetrange['M'+str(i)].value #Jumlah Rusak Parah
jmlhRring        = sheetrange['N'+str(i)].value #Jumlah Rusak Ringan
ketdetail        = sheetrange['O'+str(i)].value #Keterangan

#tab identitas
jmlhbahan          = sheetrange['P'+str(i)].value #jumlah
identitas1         = sheetrange['Q'+str(i)].value #Nama Bahan
identitas2         = sheetrange['R'+str(i)].value #Jumlah Pakai
jumlahpenyerah     = sheetrange['S'+str(i)].value #Satuan
status1            = sheetrange['T'+str(i)].value #Satuan Lain
Penyerah1          = sheetrange['U'+str(i)].value #Keterangan

# init driver by os
@mark.fixture_penerimaan
def test_Ossetup_1():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')

@mark.fixture_penerimaan
def test_loggin_2():
    # login(driver)
    loginOperator(driver)
    Log.info('Memasukan User name dan Password di halaman Login)')

@mark.fixture_penerimaan
def test_aksesmenuPenerimaan_3():
	nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['Rupbasan'])
	ActionChains(driver).move_to_element(nav1).perform()
	driver.find_element(By.LINK_TEXT, 'Pemeliharaan').click()
	driver.find_element(By.ID, 'kataKunci').click()
	attach(data=driver.get_screenshot_as_png())
	Log.info('Menuju Menu Penerimaan dengan mengarahkan kursor ke navigasi ''Rubasan'' kemudian sub menu ''Penerimaan''')

@mark.fixture_penerimaan
def test_Masukhalamatambah_4():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
    driver.find_element(By.ID, 'createButton').click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Membuka halaman tambah penerimaan dengan klik button tambah')

@mark.fixture_penerimaan
def test_Iputdate_1():
	driver.find_element(By.ID, 'tglPemeliharaan').send_keys(tglPemeliharaan)

@mark.fixture_penerimaan
def test_dropdown_1():
    driver.find_element(By.ID, 'inputJenisPemeliharaan').click()
    if jnspemeliharaan =='Pemeliharaan Basan dan Baran Umum':
        driver.find_element(By.ID, 'JPB1').click()
    elif jnspemeliharaan == 'Pemeliharaan Basan dan Baran Khusus':
        driver.find_element(By.ID, 'JPB2').click()

@mark.fixture_penerimaan
def test_dropdown_2():
	driver.find_element(By.ID, 'inputKegiatanPemeliharaan').click()	
	if KgiPemeliharaan == 'Pemeliharaan Berkala (Preventive Maintenance)':
		driver.find_element(By.ID, 'KPB1')
	elif KgiPemeliharaan == 'Pemeliharaan Darurat (Emergency)':
		driver.find_element(By.ID, 'KPB2')

@mark.fixture_penerimaan
def test_area_1():
	driver.find_element(By.ID, 'keterangan').send_keys(KgiPemeliharaan)

@mark.fixture_penerimaan
def test_dropdown_3():
	driver.find_element(By.ID, 'cariKetua').send_keys(ketpelaksana) #ketua Pelaksana
@mark.fixture_penerimaan
def test_dropdown_4():
	driver.find_element(By.ID, 'cariPetugasInternal').send_keys(ptgsinternal) #Petugas Pemeliharaan (Internal)
@mark.fixture_penerimaan
def test_dropdown_5():
	driver.find_element(By.ID, 'cariPetugasEksternal').send_keys(ptgsexternal) #Petugas Pemeliharaan (Eksternal)