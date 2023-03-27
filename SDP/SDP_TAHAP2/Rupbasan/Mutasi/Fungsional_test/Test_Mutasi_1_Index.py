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
fh = logging.FileHandler('Mutasi_1_Index.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("RUPEXEL"))
sheetrange = wb['IndexMutasi']
i = 5

pilihkategori    = sheetrange['A'+str(i)].value
Katkun			 = sheetrange['B'+str(i)].value

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

# @mark.fixture_Mutasi
# def test_sortirtabel_3():
#     WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
#     driver.find_element(By.XPATH, pathData['Rupelemen']['indexmutasi']['ascend']).click()
#     WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
#     driver.find_element(By.XPATH, pathData['Rupelemen']['indexmutasi']['descend']).click()
#     WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))

    # attach(data=driver.get_screenshot_as_png())
    # Log.info('Melakukan sortir data tabel')

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
def test_hapuspencarian_5():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    filter = driver.find_element(By. ID, "filterColumn")
    ActionChains(driver).move_to_element(filter).perform()

    elemnthps = driver.find_element(By.XPATH, pathData['Rupelemen']['indexmutasi']['hapuscari'])
    ActionChains(driver).move_to_element(elemnthps).perform()
    elemnthps.click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))

    attach(data=driver.get_screenshot_as_png())
    Log.info('menghapus field inputan dengan klik clear value button')

# @mark.fixture_Mutasi
# def test_pilih3halaman_6():
#     Halaman2 = driver.find_element(By.XPATH, pathData['Rupelemen']['indexpenempatan']['pilihhalmn'])
#     Halaman2.click()
#     halaman3 = driver.find_element(By.XPATH, pathData['Rupelemen']['indexpenempatan']['3halaman'])
#     halaman3.click()
#     WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))

# @mark.fixture_Mutasi
# def test_pilih5halaman_6():
#     WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
#     Halaman = driver.find_element(By.XPATH, pathData['Rupelemen']['indexpenempatan']['pilihhalmn'])
#     Halaman.click()
#     halaman5 = driver.find_element(By.XPATH, pathData['Rupelemen']['indexpenempatan']['5halaman'])
#     halaman5.click()
#     WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))

# @mark.fixture_Mutasi
# def test_pilihpagetabel_7():
#     WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
#     pergipage = driver.find_element(By.XPATH, pathData['Rupelemen']['indexpenempatan']['pergipage'])
#     pergipage.clear()
#     pergipage.send_keys('5')
#     pergipage.send_keys(Keys.ENTER)
#     WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))

#     attach(data=driver.get_screenshot_as_png())
#     Log.info('Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir')

@mark.fixture_Mutasi
def test_aksesmenu_detail_11():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    test_pencariandatatabel_4()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    driver.find_element(By.XPATH, pathData['Rupelemen']['indexmutasi']['detailmutasi']).click()

    attach(data=driver.get_screenshot_as_png())
    Log.info('Membuka halaman Detail')

@mark.fixture_Mutasi
def test_kembalihalaman():
	driver.find_element(By.ID, 'backButton').click()
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
	attach(data=driver.get_screenshot_as_png())
	Log.info('kembali ke halaman sebelumnya dengan klik button kembali')

@mark.fixture_Mutasi
def test_aksesmenu_ubah_12(): 
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    test_pencariandatatabel_4()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))

    driver.find_element(By.XPATH, pathData['Rupelemen']['indexmutasi']['ubahmuta']).click()
    
    test_kembalihalaman()
    
    attach(data=driver.get_screenshot_as_png())
    Log.info('Membuka halaman Ubah dan kembali ke halaman sebelumnya dengan klik button kembali')


@mark.fixture_Mutasi
def test_cetakBA_13(): 
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    test_pencariandatatabel_4()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))

    driver.find_element(By. ID, 'cetakBarcode-0').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'cetakBarcode')))
    attach(data=driver.get_screenshot_as_png())
    Log.info('mencetak barkode perbaris tabel kemudian muncul alert jika berhasil di download')

# @mark.fixture_Mutasi
# def test_exportPDF_8():
#     WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
#     driver.find_element(By.ID, 'pdfButton').click()
#     driver.find_element(By.ID, 'wholeButton').click()
#     time.sleep(2)
#     driver.find_element(By.ID, 'thisButton').click()
#     WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'pdfButton')))

#     attach(data=driver.get_screenshot_as_png())
#     Log.info('Melakukan cetak PDF')

# @mark.fixture_Mutasi
# def test_exportexcel_9():
#     WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
#     driver.find_element(By.ID, 'excelButton').click()
#     driver.find_element(By.ID, 'wholeButton').click()
#     time.sleep(2)
#     driver.find_element(By.ID, 'thisButton').click()
#     WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'excelButton')))

#     attach(data=driver.get_screenshot_as_png())
#     Log.info('Melakukan cetak EXCEL')

# @mark.fixture_Mutasi
# def test_printdatatable_10():
#     WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
#     driver.find_element(By.ID, 'printButton').click()
#     driver.find_element(By.XPATH, pathData['Rupelemen']['indexpenempatan']['printsemua']).click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, pathData['Rupelemen']['indexpenempatan']['printinisaja']).click()
#     WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'printButton')))

#     attach(data=driver.get_screenshot_as_png())
#     Log.info('Melakukan cetak Print data Table')

# @mark.fixture_Mutasi
# def test_aksesmenu_tambah_14():
#     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
#     driver.find_element(By.ID, 'createButton').click()

#     attach(data=driver.get_screenshot_as_png())
#     Log.info('Mengakses menu tambah')