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

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR"))
    sys.path.append("/Users/will/Documents/work/Automationpython")
elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))

from Settings.setup import initDriver, loadDataPath, quit
from Settings.login import login

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('result.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)



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
def test_3_AksesMenu_ManajemenBlokDanKamar():
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['ManajemenPenempatan']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Manajemen Blok dan Kamar').click()
    print('.')
    Log.info('Manajemen Blok Dan Kamar')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_4_ClickButtonTambah_PemetaanBlock():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.border:nth-child(1)')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    print('.')
    Log.info('Click Button Tambah halaman Pemetaan Block')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_ClickButtonTambah_MasterBlokDanKamar():
    driver.implicitly_wait(30)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, 'createButton').click()
    print('.')
    Log.info('Click Button Tambah Master Blok Dan Kamar')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_6_InputNamaBlok():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'blok')))
    driver.find_element(By.ID, 'blok').send_keys('blok testing1')
    Log.info('Input Nama Blok')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_7_InputTipeBlok():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'tipe_id')))
    driver.find_element(By.ID, 'tipe_id').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Umum\')]')))
    driver.find_element(By.XPATH, "//li[contains(.,\'Umum\')]").click()
    Log.info('Input Tipe Blok')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_8_JenisKelaminBlok():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'kel_jenis_kelamin_id')))
    driver.find_element(By.ID, "kel_jenis_kelamin_id").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Laki-laki\')]')))
    driver.find_element(By.XPATH, "//li[contains(.,\'Laki-laki\')]").click()

    Log.info('Input Blok Untuk Jenis Kelamin Laki Laki')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_9_JenisKejahatan():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'jenis_kejahatan_values')))
    driver.find_element(By.ID, "jenis_kejahatan_values").click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Korupsi\')]").click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Teroris\')]").click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Kriminal Umum\')]").click()
    time.sleep(2)
    driver.find_element(By.ID, "jenis_kejahatan_values").send_keys(Keys.TAB)

    Log.info('Input Jenis kejahatan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_10_JumlahLantai():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "Masukkan Jumlah Lantai"]')))
    driver.find_element(By.XPATH, '// *[ @ id = "Masukkan Jumlah Lantai"]').send_keys('2')
    Log.info('Input Jumlah Lantai')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_11_FormatPenomoranKamar():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'penomoran_kamar')))
    driver.find_element(By.ID, "penomoran_kamar").click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Angka 8 (mulai kiri atas)\')]").click()
    Log.info('Input Format Penomoran Kamar')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_12_Umur():
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "kel_usia_id").click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Dewasa')]").click()
    Log.info('usia')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_13_InputJumlahKamar():
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "jumlah_kamar_per_lantai-0").click()
    driver.find_element(By.ID, "jumlah_kamar_per_lantai-0").send_keys("10")
    driver.find_element(By.ID, "jumlah_kamar_per_lantai-1").click()
    driver.find_element(By.ID, "jumlah_kamar_per_lantai-1").send_keys("10")
    Log.info('Input Jumlah Halaman')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_14_BAKALDIHAPUS():
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "posisi_koridor_utama_per_lantai-0").click()
    driver.find_element(By.ID, "posisi_koridor_utama_per_lantai-0").send_keys("2-6")
    driver.find_element(By.ID, "posisi_koridor_utama_per_lantai-1").click()
    driver.find_element(By.ID, "posisi_koridor_utama_per_lantai-1").send_keys("2-6")
    Log.info('Input koridor')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_15_BAKALDIHAPUS():
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "posisi_koridor_simpang_per_lantai-0").click()
    driver.find_element(By.ID, "posisi_koridor_simpang_per_lantai-0").send_keys("4-8")
    driver.find_element(By.ID, "posisi_koridor_simpang_per_lantai-1").click()
    driver.find_element(By.ID, "posisi_koridor_simpang_per_lantai-1").send_keys("4-8")
    Log.info('koridor simpang')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_16_Submit():
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    Log.info('Submit')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_17_JenisLantai():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'lantai_id')))
    driver.find_element(By.ID, 'lantai_id').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'lantai-0')))
    driver.find_element(By.ID, "lantai-0").click()
    Log.info('Input Nomor Kamar')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_18_InputNomorKamar():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'nomorKamar')))
    driver.find_element(By.ID, "nomorKamar").send_keys('01')
    Log.info('Input Nomor Kamar')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_19_PeruntukanKelompokUsia():
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "kel_usia_id").click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Dewasa\')]").click()
    Log.info('Usia Ruangan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_20_TipeKamar():
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "tipe_id").click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Umum\')]").click()
    Log.info('Tipe Ruangan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_21_JenisKelamin():
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "kel_jenis_kelamin_id").click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Perempuan\')]").click()
    Log.info('Jenis Kelamin')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_22_KapasitasInput():
    driver.implicitly_wait(30)
    driver.find_element(By.ID, 'kapasitasInput').send_keys(30)
    Log.info('Kapasitas Ruangan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_23_KondisiRuangan():
    driver.implicitly_wait(30)
    driver.find_element(By.ID, 'kondisiInput').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Baik\')]").click()
    Log.info('Kondisi Ruangan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_24_LamaHuni():
    driver.implicitly_wait(30)
    driver.find_element(By.ID, 'lamaHuni').send_keys(30)
    Log.info('Lama Huni')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_25_ButtonSubmit():
    driver.implicitly_wait(30)
    driver.find_element(By.ID, 'submitButton').click()
    Log.info('Submit')
    attach(data=driver.get_screenshot_as_png())
    #MASIH BELUM SELESAI

@mark.fixture_test()
def teardown():
    quit(driver)
