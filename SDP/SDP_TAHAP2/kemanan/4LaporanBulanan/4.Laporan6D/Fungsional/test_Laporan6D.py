from distutils.archive_util import make_archive
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
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
import pyautogui

import sys
from os import environ, path
from dotenv import load_dotenv
load_dotenv()
from openpyxl import load_workbook

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR"))
    wb = load_workbook(environ.get("KeamananUAT"))

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))
    wb = load_workbook(environ.get("KeamananUATWin"))


from Settings.setupkeamanan import initDriver, loadDataPath, quit, sleep
from Settings.loginkeamanan import oplapkamtibwaru,kanwiljabar,pusat, SpvRutanBdg
from Settings.Page.keamanan import menulaporan6d

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Loglaporan6D.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


i = 2
laporan6D = wb['Laporan6D']


jenisSarana                              = laporan6D['A'+str(i)].value
kondisiBaik                              = laporan6D['B'+str(i)].value
kondisiRusak                             = laporan6D['C'+str(i)].value
keterangan                               = laporan6D['D'+str(i)].value

usulan                                   = laporan6D['F'+str(i)].value
jumlah                                   = laporan6D['G'+str(i)].value

nama                                     = laporan6D['I'+str(i)].value
deskripsi                                = laporan6D['J'+str(i)].value
status                                   = laporan6D['K'+str(i)].value




@mark.fixture_test()
def test_1_SetupOs():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_test()
def test_2_Login():
    Log.info('Setup Os')
    oplapkamtibwaru(driver)
    Log.info('Login Op Laporan Kamtib 6 D')


@mark.fixture_test()
def test_2_AksesMenu():
    sleep(driver)
    menulaporan6d(driver)
    Log.info('Akses halaman Laporan 6 D')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_3_CreateButton():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, "createButton").click()
    Log.info('Klik tombol tambah data')

@mark.fixture_test()
def test_4_InputJenisSarana():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, "jenisSarana").click()
    driver.execute_script("window.scrollTo(0,0)")
    driver.find_element(By.ID, "jenisSarana").send_keys(jenisSarana)
    driver.find_element(By.XPATH, "//li[contains(.,\'"+ jenisSarana +"')]").click()
    Log.info('Input Jenis Sarana')

@mark.fixture_test()
def test_5_InputKondisi():
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, "#kondisiBaik .el-input__inner").send_keys(kondisiBaik)
    driver.find_element(By.CSS_SELECTOR, "#kondisiRusak .el-input__inner").send_keys(kondisiRusak)
    Log.info('Input Kondisi')

@mark.fixture_test()
def test_6_InputKeterangan():
    sleep(driver)
    driver.find_element(By.ID, "keterangan").click()
    driver.find_element(By.ID, "keterangan").send_keys(keterangan)
    Log.info('Input Keterangan')

@mark.fixture_test()
def test_7_ButtonSubmit():
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, "#submitButton > span").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    Log.info('Klik tombol submit')


@mark.fixture_test()
def test_8_TambahUsulan():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.invisibility_of_element((By.CSS_SELECTOR, '.el-loading-mask')))
    driver.find_element(By.CSS_SELECTOR, "#tambahUsulan > span").click()
    driver.find_element(By.ID, "usulan").send_keys(usulan)
    driver.find_element(By.ID, "usulan5").click()

@mark.fixture_test()
def test_9_InputJumlah():
    driver.find_element(By.ID, "jumlah").send_keys(jumlah)

@mark.fixture_test()
def test_10_ClickButtonSUbmit():
    driver.find_element(By.CSS_SELECTOR, "#submitButton > span").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))


@mark.fixture_test()
def test_11_SetupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')


@mark.fixture_test()
def test_12_LoginSpv():
    Log.info('Setup Os')
    SpvRutanBdg(driver)
    Log.info('Login Spv Laporan Kamtib 6D')

@mark.fixture_test()
def test_13_AksesMenuSpv():
    sleep(driver)
    menulaporan6d(driver)
    Log.info('Akses halaman Laporan 6D')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_14_KirimLaporanSpv():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'buttonVerifikasiLaporan')))
    time.sleep(2)
    driver.find_element(By.ID, "buttonVerifikasiLaporan").click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'kirimLaporan')))
    time.sleep(3)
    
    driver.find_element(By.CSS_SELECTOR, "#kirimLaporan > span").click()

@mark.fixture_test()
def test_15_loginKanwil():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')
    kanwiljabar(driver)
    Log.info('Login Spv Laporan Kamtib 6D')

@mark.fixture_test()
def test_16_AksesMenuSpv():
    sleep(driver)
    menulaporan6d(driver)
    Log.info('Akses halaman Laporan 6D')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_17_VerifikasiLaporanKanwil():
    sleep(driver)
    time.sleep(2)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'formfilterUpt2')))
    driver.find_element(By.ID, "formfilterUpt2").click()
    time.sleep(1)
    driver.find_element(By.ID, "formfilterUpt2").send_keys("Rutan Kelas")
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,\'Rutan Kelas I Bandung\')]")))
    
    driver.find_element(By.XPATH, "//span[contains(.,\'Rutan Kelas I Bandung\')]").click()
    Log.info('Input UPT')

@mark.fixture_test()
def test_18_ClickButtonSearch():
    sleep(driver)
    driver.find_element(By.ID, "searchButton").click()
    Log.info('Click Button Search')

@mark.fixture_test()
def test_19_ClickButtonVerifikasi():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'buttonVerifikasi')))
    driver.find_element(By.ID, "buttonVerifikasi").click()
    Log.info('Click Button Verifikasi')


@mark.fixture_test()
def test_20_StatusVerifikasiModal():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'simpanVerifikasi')))
    time.sleep(3)
    driver.find_element(By.ID, "statusVerifikasiModal").click()
    Log.info('Click Verifikasi Modal')

@mark.fixture_test()
def test_21_UbahStatus():
    sleep(driver)
    driver.find_element(By.ID, "diizinkan").click()
    Log.info('Ubah Status Verifikasi')

@mark.fixture_test()
def test_22_Inputketerangan():
    sleep(driver)
    driver.find_element(By.ID, "keterangan").send_keys("keterangan")
    Log.info('Input Keterangan')

@mark.fixture_test()
def test_23_SimpanVerifikasi():
    sleep(driver)
    driver.find_element(By.ID, "simpanVerifikasi").click()
    Log.info('Click Button Simpan Verifikasi')


@mark.fixture_test()
def test_24_loginPusat():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')
    pusat(driver)
    Log.info('Login Spv Laporan Kamtib 6D')

@mark.fixture_test()
def test_25_AksesMenuPusat():
    sleep(driver)
    menulaporan6d(driver)
    Log.info('Akses halaman Laporan 6D')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_26_PilihKanwil():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'formfilterKanwil')))
    driver.find_element(By.ID, "formfilterKanwil").send_keys("jawa barat")
    driver.find_element(By.XPATH, "//li[contains(.,\'Jawa Barat\')]").click()
    Log.info('Pilih Kanwil')

@mark.fixture_test()
def test_27_PilihUPT():
    sleep(driver)
    driver.find_element(By.ID, "formfilterUpt").click()
    time.sleep(1)
    driver.find_element(By.ID, "formfilterUpt").send_keys("rutan kelas")
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,\'Rutan Kelas I Bandung\')]")))
    driver.find_element(By.XPATH, "//li[contains(.,\'Rutan Kelas I Bandung\')]").click()
    Log.info('PilihUPT')

@mark.fixture_test()
def test_28_ClickButtonSearch():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.CSS_SELECTOR, "#searchButton > span").click()
    Log.info('Click Button Search')

@mark.fixture_test()
def test_29_ClickButtonMaster():
    sleep(driver)
    driver.find_element(By.ID, "buttonMaster").click()
    Log.info('Click Button Master')

@mark.fixture_test()
def test_30_CreateButton():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'backButton')))
    driver.find_element(By.ID, "createButton").click()
    Log.info('Click Button Create')

@mark.fixture_test()
def test_31_InputNama():
    sleep(driver)
    driver.find_element(By.ID, "nama").send_keys(nama)
    Log.info('Input Nama barang')
@mark.fixture_test()
def test_32_InputDeskripsi():
    sleep(driver)
    driver.find_element(By.ID, "deskripsi").send_keys(deskripsi)
    Log.info('Input Deskripsi')

@mark.fixture_test()
def test_33_Switch():
    sleep(driver)
    driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/div[2]/form/div[3]/div/div/div/span/span").click()
    Log.info('Click Switch')

@mark.fixture_test()
def test_34_Tambah():
    driver.find_element(By.ID, "submitButton").click()
    Log.info('Click Button Tambah')

@mark.fixture_test()
def test_35_exit():
    time.sleep(5)
    quit(driver)
    Log.info('Exit')






    
    