
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
    wb = load_workbook(environ.get("KeamananUAT"))

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))


from Settings.setupkeamanan import initDriver, loadDataPath, quit, sleep
from Settings.loginkeamanan import SpvRutanBdg, oplapkamtibwaru,kanwiljabar,pusat
from Settings.Page.keamanan import menulaporan6b

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('LogLaporan6A.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


i = 2
laporan6a = wb['Laporan6A']


nama                                            = laporan6a['A'+str(i)].value
nosk                                            = laporan6a['B'+str(i)].value
tanggalSkAsimilasi                              = laporan6a['C'+str(i)].value
tanggalAsimilasi                                = laporan6a['D'+str(i)].value
lokasiAsimilasi                                 = laporan6a['E'+str(i)].value
namaPetugas                                     = laporan6a['F'+str(i)].value
namaPenjamin                                    = laporan6a['G'+str(i)].value
keterlibatanLain                                = laporan6a['H'+str(i)].value
keterangan                                      = laporan6a['I'+str(i)].value

@mark.fixture_test()
def test_1loginOperatir():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')
    oplapkamtibwaru(driver)
    Log.info('Login Op Laporan Kamtib 6A')


@mark.fixture_test()
def test_2_AksesMenu():
    sleep(driver)
    menulaporan6b(driver)
    Log.info('Akses halaman Laporan 6B')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_3_CreateButton():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, "createButton").click()
    Log.info('Klik tombol tambah data')

@mark.fixture_test()
def test_4_UraianSingkatKejadian():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'submitButton')))

@mark.fixture_test()
def test_5_WaktuKejadian():
    sleep(driver)

@mark.fixture_test()
def test_6_Kerusakan():
    sleep(driver)

@mark.fixture_test()
def test_7_TotalKerugian():
    sleep(driver)

@mark.fixture_test()
def test_8_KorbanJiwa():
    sleep(driver)

@mark.fixture_test()
def test_9_TindakanSementaraYangDilakukan():
    sleep(driver)

@mark.fixture_test()
def test_10_TindakLanjut():
    sleep(driver)

@mark.fixture_test()
def test_11_SumberDana():
    sleep(driver)

@mark.fixture_test()
def test_12_BantuanPihakLain():
    sleep(driver)

@mark.fixture_test()
def test_13_Keterangan():
    sleep(driver)

@mark.fixture_test()
def test_14_Submit():
    sleep(driver)