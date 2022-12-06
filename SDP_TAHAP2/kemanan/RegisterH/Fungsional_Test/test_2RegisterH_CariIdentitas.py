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
fh = logging.FileHandler('RegisterH_CariIdentitas.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


sheetrange = wb['RegisterH_CariIdentitas']
print(".")
print("masukan baris yang akan dibaca")
xr = input("")
i  = xr

filterColumn                                    = sheetrange['B'+str(i)].value
nama                                            = sheetrange['C'+str(i)].value
jenisKejahatan                                  = sheetrange['D'+str(i)].value
nomorReg                                        = sheetrange['E'+str(i)].value
semua                                           = sheetrange['F'+str(i)].value

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
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Register H').click()
    print('.')
    Log.info('akses menu daftar lalu lintas')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_4_membuka_halaman_tambah_index_Search():
    driver.implicitly_wait(60)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, 'createButton').click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="backButton"]')))
    print('.')
    Log.info(' Membuka Halaman Tambah ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_5_sortir_Halaman_Index():
    # 5 HALAMAN
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, "(//input[@type=\'text\'])[3]").click()
    driver.find_element(By.XPATH, "//li[contains(.,\'5/halaman\')]").click()
    driver.find_element(By.XPATH, "//input[@type=\'number\']").send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, "//input[@type=\'number\']").send_keys('10')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 5 halaman  ')
    attach(data=driver.get_screenshot_as_png())
    sleep(driver)

    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, "(//input[@type=\'text\'])[3]").click()
    driver.find_element(By.XPATH, "//li[contains(.,\'10/halaman\')]").click()
    driver.find_element(By.XPATH, "//input[@type=\'number\']").send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, "//input[@type=\'number\']").send_keys('10')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 10 Halaman  ')
    attach(data=driver.get_screenshot_as_png())
    sleep(driver)

    # 5 HALAMAN
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, "(//input[@type=\'text\'])[3]").click()
    driver.find_element(By.XPATH, "//li[contains(.,\'20/halaman\')]").click()
    driver.find_element(By.XPATH, "//input[@type=\'number\']").send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, "//input[@type=\'number\']").send_keys('10')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 20 halaman  ')
    attach(data=driver.get_screenshot_as_png())
    sleep(driver)

    # 5 HALAMAN
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, "(//input[@type=\'text\'])[3]").click()
    driver.find_element(By.XPATH, "//li[contains(.,\'50/halaman\')]").click()
    driver.find_element(By.XPATH, "//input[@type=\'number\']").send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, "//input[@type=\'number\']").send_keys('10')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 50 halaman  ')
    attach(data=driver.get_screenshot_as_png())
    sleep(driver)

    # 5 HALAMAN
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, "(//input[@type=\'text\'])[3]").click()
    driver.find_element(By.XPATH, "//li[contains(.,\'100/halaman\')]").click()
    driver.find_element(By.XPATH, "//input[@type=\'number\']").send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, "//input[@type=\'number\']").send_keys('10')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 100 Halaman  ')
    attach(data=driver.get_screenshot_as_png())
    sleep(driver)

@mark.fixture_test()
def test_6_search_data_kategori_nama_Search():  # Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(60)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'filterColumn')))

    time.sleep(1)
    driver.find_element(By.ID, 'filterColumn').send_keys('nama')
    driver.find_element(By.ID, 'filterColumn').click()
    sleep(driver)

    driver.find_element(By.XPATH, '//*[@id="nama"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(nama)
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    sleep(driver)

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="view0"]')))



    print('.')
    Log.info('Search Data Form Kategori Nama ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_7_search_data_kategori_JenisKejahatan_Search():  # Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(60)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'filterColumn')))

    time.sleep(1)
    driver.find_element(By.ID, 'filterColumn').send_keys('Jenis')
    driver.find_element(By.ID, 'filterColumn').click()
    sleep(driver)

    driver.find_element(By.XPATH, '//*[@id="jenisKejahatan"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(jenisKejahatan)
    sleep(driver)

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="view0"]')))

    print('.')
    Log.info('Search Data Form Kategori Nama ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_8_search_data_kategori_NoregSearch():  # Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(60)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'filterColumn')))

    time.sleep(1)
    driver.find_element(By.ID, 'filterColumn').send_keys('no')
    driver.find_element(By.ID, 'filterColumn').click()
    sleep(driver)

    driver.find_element(By.XPATH, '//*[@id="nomorReg"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(nomorReg)
    sleep(driver)

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="view0"]')))

    print('.')
    Log.info('Search Data Form Kategori Nama ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_9_search_data_kategori_Semua_Search():  # Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(60)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'filterColumn')))

    time.sleep(1)
    driver.find_element(By.ID, 'filterColumn').send_keys('semua')
    driver.find_element(By.ID, 'filterColumn').click()
    sleep(driver)

    driver.find_element(By.XPATH, '//*[@id="semua"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(semua)
    sleep(driver)

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="view0"]')))

    print('.')
    Log.info('Search Data Form Kategori Nama ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_exit():
    quit(driver)