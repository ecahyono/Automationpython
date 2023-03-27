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
from Settings.login import login, loginOperator

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('1Fungsi_Laporan6A_Tambah.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrange = wb['Laporan6A_Tambah']
xr = input('')
i  = xr

filterColumn                            = sheetrange['B'+str(i)].value
namaNoregis                             = sheetrange['C'+str(i)].value
inputtahun                              = sheetrange['D'+str(i)].value
noSkAsimilasi                           = sheetrange['E'+str(i)].value
tanggalSkAsimilasi                      = sheetrange['F'+str(i)].value
tanggalAsimilasi                        = sheetrange['G'+str(i)].value
lokasiAsimilasi                         = sheetrange['H'+str(i)].value
namaPetugas                             = sheetrange['I'+str(i)].value
namaPenjamin                            = sheetrange['J'+str(i)].value
keterlibatanLain                        = sheetrange['K'+str(i)].value
keterangan                              = sheetrange['L'+str(i)].value


@mark.fixture_test()
def test_1_SetupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Login')


@mark.fixture_test()
def test_2_Login():
    login(driver)
    Log.info('Login')


@mark.fixture_test()
def test_3_akses_menu_index():
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaporanBulanan']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Formulir Kamtib 6A').click()
    Log.info('Akses Menu Laporan Bulanan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_4_ClickButtonTambah():
    #sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#createButton > span')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#createButton > span')))
    #sleep(driver)
    driver.find_element(By.CSS_SELECTOR, '#createButton > span').click()
    Log.info('Akses Menu Laporan Bulanan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_search_Nama():
    #sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="backButton"]')))

    #sleep(driver)
    driver.find_element(By.ID, 'filterColumn').click()
    if filterColumn == "nama":
        driver.find_element(By.XPATH, '//*[@id="filterColumn"]').send_keys('nama')
        driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
    elif filterColumn == "noregis":
        driver.find_element(By.XPATH, '//*[@id="filterColumn"]').send_keys('no')
        driver.find_element(By.XPATH, "//li[contains(.,\'No Registrasi\')]").click()


@mark.fixture_test()
def test_6_input_Nama():
    #sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(namaNoregis)
    driver.find_element(By.ID, 'buttonSearch').click()

@mark.fixture_test()
def test_7_ClickButton_Daftarkan():
    #sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="daftarkan0"]')))
    driver.find_element(By.ID, 'daftarkan0').click()


"""
@mark.fixture_test()
def test_6_input_TahundanBulanLaporan():
    #sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="detailRegis"]')))
    driver.find_element(By.ID, 'setToday').click()
    Log.info('menunggu halaman tambah muncul')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_input_NomorSK_Asimilasi():
    #sleep(driver)
    driver.implicitly_wait(60)
    driver.find_element(By.ID, 'noSkAsimilasi').send_keys(noSkAsimilasi)
    Log.info('input nomor sk asimilasi')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_input_TanggalSk_Asimilasi():
    #sleep(driver)
    driver.find_element(By.ID, 'tanggalSkAsimilasi').send_keys(tanggalSkAsimilasi)
    driver.find_element(By.ID, 'tanggalAsimilasi').send_keys(Keys.ENTER)
    Log.info('input tanggal sk asimilasi')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_tanggal_Pelaksanaan_Asimilasi():
    #sleep(driver)
    driver.find_element(By.ID, 'tanggalAsimilasi').send_keys(tanggalAsimilasi)
    driver.find_element(By.ID, 'tanggalAsimilasi').send_keys(Keys.ENTER)
    Log.info('input tanggal pelaksanaan asimilasi')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_lokasiAsimilasi():
    #sleep(driver)
    driver.find_element(By.ID, 'lokasiAsimilasi').send_keys(lokasiAsimilasi)
    Log.info('input lokasi asimilasi')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_namaPetugas():
    #sleep(driver)
    driver.find_element(By.ID, 'namaPetugas').send_keys(namaPetugas)
    Log.info('input nama petugas')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_NamaPenjamin():
    #sleep(driver)
    driver.find_element(By.ID, 'namaPenjamin').send_keys(namaPenjamin)
    Log.info('input Nama Penjamin')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_KeterlibatanPihaklain():
    #sleep(driver)
    driver.find_element(By.ID, 'keterlibatanLain').send_keys(keterlibatanLain)
    Log.info('input Keterlibatan Pihak Lain')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_Keterangan():
    #sleep(driver)
    driver.find_element(By.ID, 'keterangan').send_keys(keterangan)
    Log.info('input Keterangan')
    attach(data=driver.get_screenshot_as_png())
"""




@mark.fixture_test()
def test_exit():
    quit(driver)
