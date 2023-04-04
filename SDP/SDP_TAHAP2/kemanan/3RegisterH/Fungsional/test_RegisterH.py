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
from selenium.webdriver.firefox.options import Options
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


from Settings.setup import initDriver, loadDataPath, quit, sleep
from Settings.loginkeamanan import loginOperatorSumedang, Op_Keamanan_p2u, SpvRutanBdg, op_keamanan_mp
from Settings.Page.keamanan import RegisterH

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Register H.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

i = 2
Regh = wb['RegisterH_Tambah']

nama                                            = Regh['A'+str(i)].value
noSurat                                         = Regh['B'+str(i)].value
tanggalSurat                                    = Regh['C'+str(i)].value
tanggalMulai                                    = Regh['D'+str(i)].value
lamaPengasingan                                 = Regh['E'+str(i)].value
alasan                                          = Regh['F'+str(i)].value
filterStatus                                    = Regh['H'+str(i)].value
UbahStatus                                      = Regh['I'+str(i)].value
keterangan                                      = Regh['J'+str(i)].value


@mark.fixture_test()
def test_1loginOperator():

    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')
    op_keamanan_mp(driver)
    Log.info('Login Operator Manajemen Penempatan')


@mark.fixture_test()
def test_2_AksesMenu():
    sleep(driver)
    RegisterH(driver)
    Log.info('Akses Menu Register H')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_3_ClickButtonTambah():
    sleep(driver)
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, 'createButton').click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="backButton"]')))
    Log.info(' Membuka Halaman Tambah  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_4_SearchNama():
    sleep(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'filterColumn')))
    driver.find_element(By.ID, 'kataKunci').send_keys(nama)
    Log.info('Klik Search Kategori berdasarkan Nama')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_ClickButtonSearch():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    Log.info('Klik Button Search')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_6_ClickPerasingan():
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="view0"]')))
    driver.find_element(By.XPATH,'//*[@id="view0"]').click()
    Log.info('Klik Button Perasingan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_7_InputNosurat():
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'detailRegis')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'noSurat')))
    driver.find_element(By.XPATH, '//*[@id="noSurat"]').send_keys(noSurat)
    Log.info('Input Nomor Surat')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_8_UploadSurat():
    sleep(driver)
    driver.find_element(By.ID, "uploadButton").click()

    sleep(driver)
    pyautogui.write("///////users/will/test.pdf")
    pyautogui.press('enter')
    pyautogui.write("///////users/will/test.pdf")
    pyautogui.press('enter')
    pyautogui.press('escape')
    pyautogui.press('escape')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')    
    Log.info('Upload Surat')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_9_InputTanggalSurat():
    sleep(driver)
    driver.find_element(By.ID, 'tanggalSurat').clear()
    driver.find_element(By.ID, 'tanggalSurat').send_keys(tanggalSurat)
    Log.info('Input Tanggal Surat')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_10_InputTanggalMulai():
    sleep(driver)
    driver.find_element(By.ID, 'tanggalMulai').send_keys(tanggalMulai)
    Log.info('Input Tanggal Mulai')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_11_InputLamaPerasingan():
    sleep(driver)
    driver.find_element(By.XPATH,'//*[@id="lamaPengasingan"]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="lamaPengasingan"]/div/input').send_keys(lamaPengasingan)
    Log.info('Input Lama Perasingan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_12_InputAlasan():

    driver.find_element(By.ID, 'alasan').send_keys(alasan)
    Log.info('Input Alasan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_13_ClickButtonSubmit():
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    Log.info('Click Button Submit')
    attach(data=driver.get_screenshot_as_png())








































@mark.fixture_test()
def test_14_loginSpv():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')
    SpvRutanBdg(driver)
    Log.info('Login Spv Manajemen Penempatan')


@mark.fixture_test()
def test_15_AksesMenuSpv():
    sleep(driver)
    RegisterH(driver)
    Log.info('Akses Menu Register H')
    attach(data=driver.get_screenshot_as_png())



@mark.fixture_test()
def test_16_SearchKeywordNama():  # Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.ID, 'filterColumn').send_keys('nama')
    driver.find_element(By.XPATH, '//*[@id="namaLengkap"]').click()
    Log.info(' Memilih kategori Nama ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_17_SearchNamaWbp():
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(nama)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    Log.info('Search nama')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_18_statusStatus():
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'filterStatus')))
    driver.find_element(By.ID, 'filterStatus').click()
    if filterStatus == 'dalamproses':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dalamProses"]')))
        driver.find_element(By.ID, 'filterStatus').send_keys('dalam Proses')
        driver.find_element(By.ID, 'dalamProses').click()
        Log.info(' Filter status Dalam Proses ')
        attach(data=driver.get_screenshot_as_png())
    elif filterStatus == 'perbaikan':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dalamProses"]')))
        driver.find_element(By.XPATH, "//li[@id=\'perbaikan\']").click()
        Log.info('.')
        Log.info(' Filter status Dalam Proses ')
        attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_19_Click_StatusDalamProses():
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modalButton0"]')))
    driver.find_element(By.XPATH, '//*[@id="modalButton0"]').click()
    Log.info('.')
    Log.info('Click Button Status Dalam Proses')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_20_UbahStatusDiizinkan():
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="statusVerifikasiModal"]')))
    driver.find_element(By.XPATH, '//*[@id="statusVerifikasiModal"]').click()
    if UbahStatus == 'diizinkan':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//li[@id=\'diizinkan\'])[2]")))
        driver.find_element(By.XPATH, "(//li[@id=\'diizinkan\'])[2]").click()
        Log.info('.')
        Log.info('Ubah Status Menjadi Di Izinkan')
        attach(data=driver.get_screenshot_as_png())
    elif UbahStatus == 'perbaikan':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//li[@id=\'perbaikan\'])[2]")))
        driver.find_element(By.XPATH, "(//li[@id=\'perbaikan\'])[2]").click()
        Log.info('.')
        Log.info('Ubah Status Menjadi Di perbaikan')
        attach(data=driver.get_screenshot_as_png())
    elif UbahStatus == 'ditolak':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//li[@id=\'ditolak\'])[2]")))
        driver.find_element(By.XPATH, "(//li[@id=\'ditolak\'])[2]").click()
        Log.info('.')
        Log.info('Ubah Status Menjadi Di Tolak')
        attach(data=driver.get_screenshot_as_png())
    elif UbahStatus == 'dalamProses':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//li[@id=\'dalamProses\'])[2]")))
        driver.find_element(By.XPATH, "(//li[@id=\'dalamProses\']/span)[2]").click()
        Log.info('.')
        Log.info('Ubah Status Menjadi Dalam Proses')
        attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_21_InputKeterangan():
    sleep(driver)
    driver.find_element(By.ID, "keterangan").click()
    driver.find_element(By.ID, "keterangan").send_keys(keterangan)
    Log.info('.')
    Log.info('Input Keterangan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_22_SimpanButton():
    sleep(driver)
    driver.find_element(By.ID, "simpanVerifikasi").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Diperbaharui\')]')))
    Log.info('.')
    Log.info('Button Simpan Verifikasi')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_23_exit():
    quit(driver)

  