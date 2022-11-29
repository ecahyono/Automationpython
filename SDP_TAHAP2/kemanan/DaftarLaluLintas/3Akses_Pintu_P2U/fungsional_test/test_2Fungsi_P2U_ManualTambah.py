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

@mark.fixture_test()
def test_2_Login():
    login(driver)

@mark.fixture_test()
# Akses menu ke halaman akses pintu p2u
def test_3_Akses_menu():
    driver.implicitly_wait(15)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Akses Pintu P2U').click()
    print('.')
    print('==========akses menu daftar lalu lintas==========')
    attach(data=driver.get_screenshot_as_png())

# ==================================================== TAMBAH PEGAWAI ====================================================
@mark.fixture_test()
# pergi ke halaman tambah
def test_4_ButtonTambah_PegawaiTambah():
    driver.implicitly_wait(20)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButton"]')))
    print('.')
    print('========== Membuka Halaman Tambah ==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
# Memilih kategori pegawai
def test_5_Kategori_Pegawaitambah():
    driver.implicitly_wait(20)
    driver.implicitly_wait(15)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "pegawai").click()
    print('.')
    print('========== Input NIP ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
# Input nama
def test_6_InputNiP_Pegawaitambah():
    driver.implicitly_wait(20)
    driver.find_element(By.ID, 'inputNip').send_keys("0097736")
    print('.')
    print('========== Input NIP ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
# Input nama
def test_7_InputNama_Pegawaitambah():
    driver.implicitly_wait(20)
    driver.find_element(By.ID, 'inputNama').send_keys("STERIO")
    print('.')
    print('========== Input NIP ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_8_InputJabatan_Pegawaitambah():
    driver.implicitly_wait(20)
    driver.find_element(By.ID, 'inputJabatan').send_keys("SARJANA MUDA")
    print('.')
    print('========== Input NIP ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_9_InputKeperluan_Pegawaitambah():
    driver.implicitly_wait(20)
    driver.find_element(By.ID, 'inputKeperluan').send_keys("Jalan jalan")
    print('.')
    print('========== Input NIP ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
# menekan button submit input data manual
def test_10_Submit_PegawaiTambah():
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))

# ==================================================== TAMU DINAS ====================================================

@mark.fixture_test()
# membuka halaman tambah
def test_11_CreateButton_TamuDinasTambah():
    driver.implicitly_wait(20)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButton"]')))
    print('.')
    print('========== Membuka Halaman Tambah ==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_12_Kategori_TamuDinasTambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "tamuDinas").click()
    print('.')
    print('========== Input kategori tamu dinas ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_13_InputNip_TamuDinasTambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'inputNama')))
    driver.find_element(By.ID, 'inputNip').send_keys('98329')

    print('.')
    print('========== Input nip ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_14_InputNama_TamuDinasTambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'inputNama')))
    driver.find_element(By.ID, 'inputNama').send_keys('input nama tamu dinas')

    print('.')
    print('========== Input nip ==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_15_InputInstansi_TamuDinasTambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputInstansiId"]')))
    driver.find_element(By.XPATH, '//*[@id="inputInstansiId"]').click()
    driver.find_element(By.ID, "optionInstansi0").click()
    print('.')
    print('========== Input kategori tamu dinas ==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_16_InputJabatan_TamuDinasTambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'inputJabatan')))
    driver.find_element(By.ID, 'inputJabatan').send_keys('input jabatan ')

    print('.')
    print('========== Input nip ==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_17_InputKeperluan_TamuDinasTambah():
    driver.implicitly_wait(15)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'inputKeperluan')))
    driver.find_element(By.ID, 'inputKeperluan').send_keys('input keperluan test ')

@mark.fixture_test()
def test_18_SubmitButton_TamuDinasTambah():
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))

    print('.')
    print('========== Input nip ==========')
    attach(data=driver.get_screenshot_as_png())


def teardown():
    quit(driver)


#INPUT MANUAL KUNJUNGAN ONLINE BELUM ( TIDAK ADA DATA )
#INPUT MANUAL KUNJUNGAN ONSITE BELUM ( TIDAK ADA DATA )
