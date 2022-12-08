from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
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
from openpyxl import load_workbook

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
fh = logging.FileHandler('Mutasi_3_Ubah.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("RUPEXEL"))
sheetrange = wb['Mutasi']
i = 4

CariData       		 = sheetrange['A'+str(i)].value
NomorSuratMutasi     = sheetrange['B'+str(i)].value
TglSuratMutasi       = sheetrange['C'+str(i)].value
NoSuratBA        	 = sheetrange['D'+str(i)].value
JenisRegistrasiAkhir = sheetrange['E'+str(i)].value
Alamat        		 = sheetrange['F'+str(i)].value
Keterangan      	 = sheetrange['G'+str(i)].value

sheetrange1 = wb['IndexMutasi']
j = 2
pilihkategori    = sheetrange1['A'+str(j)].value
Katkun			 = sheetrange1['B'+str(j)].value
# init driver by os
@mark.fixture_Mutasi
def test_Ossetup_1():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')

@mark.fixture_Mutasi
def test_loggin_2():
    login(driver)
    Log.info('Memasukan User name dan Password di halaman Login)')

@mark.fixture_Mutasi
def test_aksesmenuPenerimaan_3():
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.LINK_TEXT, 'Mutasi').click()
    driver.find_element(By.XPATH, pathData['Rupelemen']['indexpenempatan']['klik']).click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Menuju Menu Mutasi dengan mengarahkan kursor ke navigasi ''Rubasan'' kemudian sub menu ''Mutasi''')

@mark.fixture_Mutasi
def test_pencariandatatabel_4():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    driver.find_element(By.ID, 'filterColumn').click()
    time.sleep(2)
    if pilihkategori == 'No Registrasi Rupbasan':
        driver.find_element(By.ID, 'noRegistrasiRupbasan').click()
    elif pilihkategori == 'Nama Identitas':
        driver.find_element(By.ID, 'namaIdentitas').click()
    elif pilihkategori == 'No Surat Mutasi':
        driver.find_element(By.ID, 'noSuratMutasi').click()
    elif pilihkategori == 'Jenis Registrasi Awal':
        driver.find_element(By.ID, 'noSuratMutasi').click()
    elif pilihkategori == 'Jenis Registrasi Akhir':
        driver.find_element(By.ID, 'noSuratMutasi').click()
    elif pilihkategori == 'Tgl Surat':
        driver.find_element(By.ID, 'tglSurat').click()
        # driver.implicitly_wait(10)
        driver.find_element(By.ID, 'tglSurat').send_keys(Katkun)
        
    if (pilihkategori == 'No Registrasi Rupbasan'or pilihkategori == 'Nama Identitas' or pilihkategori == 'No Surat Mutasi' or pilihkategori == 'Jenis Registrasi Awal' or pilihkategori == 'Jenis Registrasi Akhir'):
        driver.find_element(By.ID, 'kataKunci').send_keys(Katkun)
    else:
        pass

    driver.find_element(By.ID, 'buttonSearch').click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))    
    attach(data=driver.get_screenshot_as_png())
    Log.info('Melakukan pencarian data berdasarkan kategori')

@mark.fixture_Mutasi
def test_aksesmenu_ubah_12(): 
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    driver.find_element(By.XPATH, pathData['Rupelemen']['indexmutasi']['ubahmuta']).click()
    # driver.find_element(By.CSS_SELECTOR, ".h-5").click()
    
    attach(data=driver.get_screenshot_as_png())
    Log.info('Membuka halaman Ubah dan kembali ke halaman sebelumnya dengan klik button kembali')

@mark.fixture_Mutasi
def test_tambah_1():
    WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.XPATH, pathData['Rupelemen']['indexmutasi']['loadubah'])))
    Nosur = driver.find_element(By.ID, 'no_surat')
    Nosur.clear()
    Nosur.send_keys(NomorSuratMutasi)

    attach(data=driver.get_screenshot_as_png())
    Log.info('Mengisi Nomor Surat Mutasi')
	
@mark.fixture_Mutasi
def test_tambah_2():
    tgl = driver.find_element(By.ID, 'tgl_surat')
    tgl.clear()
    tgl.send_keys(TglSuratMutasi)
    tgl.send_keys(Keys.ENTER)

    attach(data=driver.get_screenshot_as_png())
    Log.info('Mengisi Tanggal Surat Mutasi')

@mark.fixture_Mutasi
def test_tambah_3():
    NoBA = driver.find_element(By.ID,  'no_ba')
    NoBA.clear()
    NoBA.send_keys(NoSuratBA)

    attach(data=driver.get_screenshot_as_png())
    Log.info('Mengisi Nomor Surat BA')

@mark.fixture_Mutasi
def test_tambah_4():
    driver.find_element(By.ID,'jenisRegistrasiAkhir').click()
    if JenisRegistrasiAkhir == 'Register Barang Rampasan Negara':
        driver.find_element(By.XPATH,'//*[@id="jenisRegistrasiAkhir-0"]').click()
    elif JenisRegistrasiAkhir == 'Tingkat Penyidikan':
        driver.find_element(By.XPATH,'//*[@id="jenisRegistrasiAkhir-1"]').click()
    elif JenisRegistrasiAkhir =='Tingkat Penuntutan':
        driver.find_element(By.XPATH,'//*[@id="jenisRegistrasiAkhir-2"]').click()
    elif JenisRegistrasiAkhir =='Tingkat Pengadilan Negeri':
        driver.find_element(By.XPATH,'//*[@id="jenisRegistrasiAkhir-3"]').click()
    elif JenisRegistrasiAkhir =='Tingkat Pengadilan Tinggi':
        driver.find_element(By.XPATH,'//*[@id="jenisRegistrasiAkhir-4"]').click()
    elif JenisRegistrasiAkhir =='Tingkat Mahkamah Agung':	
        driver.find_element(By.XPATH,'//*[@id="jenisRegistrasiAkhir-5"]').click()
    elif JenisRegistrasiAkhir =='Register Khusus Tingkat Penyidikan':
        driver.find_element(By.XPATH,'//*[@id="jenisRegistrasiAkhir-6"]').click()
    elif JenisRegistrasiAkhir =='Register Khusus Tingkat Penuntutan':
        driver.find_element(By.XPATH,'//*[@id="jenisRegistrasiAkhir-7"]').click()
    elif JenisRegistrasiAkhir =='Register Khusus Tingkat Pengadilan Negeri':
        driver.find_element(By.XPATH,'//*[@id="jenisRegistrasiAkhir-8"]').click()
    elif JenisRegistrasiAkhir =='Register Khusus Tingkat Pengadilan Tinggi':
        driver.find_element(By.XPATH,'//*[@id="jenisRegistrasiAkhir-9"]').click()
    elif JenisRegistrasiAkhir =='Register Khusus Tingkat Mahkamah Agung':
        driver.find_element(By.XPATH,'//*[@id="jenisRegistrasiAkhir-10"]').click()
        

    attach(data=driver.get_screenshot_as_png())
    Log.info('Mengisi Jenis Registrasi Akhir')

@mark.fixture_Mutasi
def test_tambah_5():
    Almt = driver.find_element(By.ID, 'alamat')
    Almt.clear()
    Almt.send_keys(Alamat)

    attach(data=driver.get_screenshot_as_png())
    Log.info('Mengisi Alamat')

@mark.fixture_Mutasi
def test_tambah_6():
    Ket = driver.find_element(By.ID,'keterangan')
    Ket.clear()
    Ket.send_keys(Keterangan)

    attach(data=driver.get_screenshot_as_png())
    Log.info('Mengisi Keterangan')

# @mark.fixture_Mutasi
# def test_Meresetform_8():
#     reset = driver.find_element(By.ID, 'resetButton')
#     reset.click()
#     time.sleep(1)
#     driver.find_element(By. XPATH, pathData['AksesMenu']['Rupbasan']['menu']['resetformYa']).click()
#     Log.info('Mereset Form tambah Mutasi dengan Option Ya')

# @mark.fixture_Mutasi
# def test_Submit():
#     driver.find_element(By.ID,'submitButton').click()
