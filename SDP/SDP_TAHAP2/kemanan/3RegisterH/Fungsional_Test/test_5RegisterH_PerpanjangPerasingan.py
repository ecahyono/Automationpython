from distutils.archive_util import make_archive
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import platform
from pytest import mark
import time
from pytest_html_reporter import attach

import sys
from os import environ, path
from dotenv import load_dotenv
load_dotenv()
from openpyxl import load_workbook

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR"))
    wb = load_workbook(filename=r"/Users/will/Documents/work/Automationpython/Filexel/Keamanan.xlsx")
    sys.path.append(environ.get("MACEXCELDIR"))

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))
    sys.path.append(environ.get("WINEXCELDIR"))


from Settings.setup import initDriver, loadDataPath, quit, buttonTambah, buttonSubmit, selectKategoriPegawai, selectKategoriTamuDinas, sleep
from Settings.login import login

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('RegisterH_PerpanjangPerasingan.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


sheetrange = wb['RegisterH_PerpanjangPerasingan']
print(".")
print("masukan baris yang akan dibaca")
xr = input("")
i  = xr

filterColumn                                    = sheetrange['B'+str(i)].value
nama                                            = sheetrange['C'+str(i)].value
noSurat                                         = sheetrange['D'+str(i)].value
tanggalSurat                                    = sheetrange['E'+str(i)].value
tanggalMulai                                    = sheetrange['F'+str(i)].value
lamaPengasingan                                 = sheetrange['G'+str(i)].value
alasan                                          = sheetrange['H'+str(i)].value



@mark.fixture_test()
def test_1_setupOS_Search():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_test()
def test_2_login_Search():
    login(driver)

@mark.fixture_test()
def test_3_aksesmenu_Search():
    driver.implicitly_wait(60)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.1)
    driver.find_element(By.LINK_TEXT, 'Register H').click()
    
    Log.info('========== akses menu Register H ==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_4_Kategori_nama_HalPer():  # Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(60)
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.ID, 'filterColumn').send_keys('nama')
    driver.find_element(By.ID, 'filterColumn').click()
    
    Log.info('Memilih kategori nama')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_Search_Nama():
    driver.implicitly_wait(60)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="namaLengkap"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(nama)
    
    Log.info(' Search Nama WBP')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_6_FilterStatus_Diizinkan():
    driver.implicitly_wait(60)
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.ID, 'filterStatus').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="diizinkan"]')))
    driver.find_element(By.ID, 'diizinkan').click()
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    
    Log.info('Filter status di izinkan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_7_Click_ButtonPerpanjangan_HalPer():
    driver.implicitly_wait(60)
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.CSS_SELECTOR, '#perpanjangan0').click()
    
    Log.info('Click Status Di izinkan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_8_InputNoSurat_HalamanTambah_HalPer():
    driver.implicitly_wait(60)
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#detailRegis')))

    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="noSurat"]').send_keys(noSurat)
    
    Log.info('Input Nomor Surat')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_9_InputTanggalSurat_HalamanTambah_HalPer():
    driver.implicitly_wait(60)
    sleep(driver)
    driver.find_element(By.ID, 'tanggalSurat').send_keys(tanggalSurat)
    driver.find_element(By.ID, 'tanggalSurat').send_keys(Keys.ENTER)
    
    Log.info('Input tanggal Surat')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_10_InputLamaPerasingan_HalamanTambah_HalPer():
    driver.implicitly_wait(60)
    sleep(driver)
    driver.find_element(By.XPATH,'//*[@id="lamaPengasingan"]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="lamaPengasingan"]/div/input').send_keys(lamaPengasingan)

    
    Log.info('Input lama perpanjangan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_11_InputAlasan_HalamanTambah_HalPer():
    driver.implicitly_wait(60)
    sleep(driver)
    driver.find_element(By.ID, 'alasan').send_keys(alasan)
    
    Log.info('Input alasan')
    attach(data=driver.get_screenshot_as_png())

    
    Log.info('Input alasan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_12_Submit_HalamanTambah():
    driver.implicitly_wait(60)
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    
    Log.info('Submit data perpanjangan')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_exit():
    quit(driver)