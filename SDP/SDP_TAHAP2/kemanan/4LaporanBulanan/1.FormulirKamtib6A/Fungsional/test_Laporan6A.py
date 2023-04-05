
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
from Settings.Page.keamanan import menulaporan6a

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
    menulaporan6a(driver)
    Log.info('Akses halaman Laporan 6A')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_3_CreateButton():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, "createButton").click()
    Log.info('Klik tombol tambah data')

@mark.fixture_test()
def test_4_FilterColumn():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.ID, "semua").click()
    Log.info('Filter Column Semua')

@mark.fixture_test()
def test_5_Katakunci():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    driver.find_element(By.ID, "kataKunci").click()
    driver.find_element(By.ID, "kataKunci").send_keys(nama)
    Log.info('Search Nama WBP')

@mark.fixture_test()
def test_6_ButtonSearch():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    driver.find_element(By.ID, "buttonSearch").click()
    Log.info('Klik tombol search')

@mark.fixture_test()
def test_7_ClickButtonDaftarkan():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    driver.find_element(By.ID, "daftarkan0").click()
    Log.info('Klik tombol daftarkan')

@mark.fixture_test()
def test_8_InputnoSK():
    sleep(driver)
    driver.find_element(By.ID, "noSkAsimilasi").click()
    driver.find_element(By.ID, "noSkAsimilasi").send_keys(nosk)
    Log.info('Input No SK Asimilasi')

@mark.fixture_test()
def test_9_InputTanggalSk():
    sleep(driver)
    driver.find_element(By.ID, "tanggalSkAsimilasi").click()
    driver.find_element(By.ID, "tanggalSkAsimilasi").send_keys(tanggalSkAsimilasi)
    Log.info('Input Tanggal SK Asimilasi')

@mark.fixture_test()
def test_10_InputTanggalAsimilasi():
    sleep(driver)
    driver.find_element(By.ID, "tanggalAsimilasi").click()
    driver.find_element(By.ID, "tanggalAsimilasi").send_keys(tanggalAsimilasi)
    Log.info('Input Tanggal Asimilasi')

@mark.fixture_test()
def test_11_Inputlokasi():
    sleep(driver)
    driver.find_element(By.ID, "lokasiAsimilasi").click()
    driver.find_element(By.ID, "lokasiAsimilasi").send_keys(lokasiAsimilasi)
    Log.info('Input Lokasi Asimilasi')

@mark.fixture_test()
def test_12_InputNamaPetugas():
    sleep(driver)
    driver.find_element(By.ID, "namaPetugas").click()
    driver.find_element(By.ID, "namaPetugas").send_keys(namaPetugas)
    Log.info('Input Nama Petugas')

@mark.fixture_test()
def test_13_InputNamaPenjamin():
    sleep(driver)
    driver.find_element(By.ID, "namaPenjamin").click()
    driver.find_element(By.ID, "namaPenjamin").send_keys(namaPenjamin)
    Log.info('Input Nama Pengjamin')

@mark.fixture_test()
def test_14_InputPihakLain():
    sleep(driver)
    driver.find_element(By.ID, "keterlibatanLain").click()
    driver.find_element(By.ID, "keterlibatanLain").send_keys(keterlibatanLain)
    Log.info('Input Keterlibatan Pihak Lain')

@mark.fixture_test()
def test_15_InputKeterangan():
    sleep(driver)
    driver.find_element(By.ID, "keterangan").click()
    driver.find_element(By.ID, "keterangan").send_keys(keterangan)
    Log.info('Input Keterangan')

@mark.fixture_test()
def test_16_ClickButtonSubmit():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    Log.info('Klik tombol submit')

@mark.fixture_test()
def test_17_loginSPV():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')
    SpvRutanBdg(driver)
    Log.info('Login Spv Laporan Kamtib 6A')

@mark.fixture_test()
def test_18_AksesMenuSpv():
    sleep(driver)
    menulaporan6a(driver)
    Log.info('Akses halaman Laporan 6A')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_19_KirimLaporanSpv():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    time.sleep(2)
    driver.find_element(By.ID, "buttonVerifikasiLaporan").click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'kirimLaporan')))
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#kirimLaporan > span").click()


@mark.fixture_test()
def test_20_loginKanwil():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')
    kanwiljabar(driver)
    Log.info('Login Spv Laporan Kamtib 6A')

@mark.fixture_test()
def test_21_AksesMenuSpv():
    sleep(driver)
    menulaporan6a(driver)
    Log.info('Akses halaman Laporan 6A')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_22_VerifikasiLaporanKanwil():
    sleep(driver)
    time.sleep(2)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'formfilterUpt2')))
    driver.find_element(By.ID, "formfilterUpt2").click()
    driver.find_element(By.ID, "formfilterUpt2").send_keys("Rutan Kelas I Bandung")
    driver.find_element(By.XPATH, "//span[contains(.,\'Rutan Kelas I Bandung\')]").click()
    Log.info('Input UPT')

@mark.fixture_test()
def test_23_ClickButtonSearch():
    sleep(driver)
    driver.find_element(By.ID, "searchButton").click()
    Log.info('Click Button Search')

@mark.fixture_test()
def test_24_ClickButtonVerifikasi():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'buttonVerifikasi')))
    driver.find_element(By.ID, "buttonVerifikasi").click()
    Log.info('Click Button Verifikasi')


@mark.fixture_test()
def test_25_StatusVerifikasiModal():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'simpanVerifikasi')))
    time.sleep(3)
    driver.find_element(By.ID, "statusVerifikasiModal").click()
    Log.info('Click Verifikasi Modal')

@mark.fixture_test()
def test_26_UbahStatus():
    sleep(driver)
    driver.find_element(By.ID, "diizinkan").click()
    Log.info('Ubah Status Verifikasi')

@mark.fixture_test()
def test_27_Inputketerangan():
    sleep(driver)
    driver.find_element(By.ID, "keterangan").send_keys("keterangan")
    Log.info('Input Keterangan')

@mark.fixture_test()
def test_28_SimpanVerifikasi():
    sleep(driver)
    driver.find_element(By.ID, "simpanVerifikasi").click()
    Log.info('Click Button Simpan Verifikasi')

@mark.fixture_test()
def test_29_loginPusat():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')
    pusat(driver)
    Log.info('Login Spv Laporan Kamtib 6A')

@mark.fixture_test()
def test_30_AksesMenuPusat():
    sleep(driver)
    menulaporan6a(driver)
    Log.info('Akses halaman Laporan 6A')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_31_PilihKanwil():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'formfilterKanwil')))
    driver.find_element(By.ID, "formfilterKanwil").click()
    driver.find_element(By.ID, "formfilterKanwil").send_keys("jawa barat")
    driver.find_element(By.XPATH, "//li[contains(.,\'Jawa Barat\')]").click()
    Log.info('Pilih Kanwil')

@mark.fixture_test()
def test_32_PilihUPT():
    driver.find_element(By.ID, "formfilterUpt").click()
    driver.find_element(By.ID, "formfilterUpt").send_keys("rutan kelas I Bandung")
    driver.find_element(By.XPATH, "//li[contains(.,\'Rutan Kelas I Bandung\')]").click()
    Log.info('Pilih UPT')

@mark.fixture_test()
def test_33_ClickButtonSearch():
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.CSS_SELECTOR, "#searchButton > span").click()
    Log.info('Click Button Search')

@mark.fixture_test()
def test_34_exit():
    time.sleep(5)
    quit(driver)














