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


from Settings.setup import initDriver, loadDataPath, quit, sleep
from Settings.login import login

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('1SearchData_IndexPortir.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrange = wb['Portir_SearchDataIndex']
xr = sheetrange['A'+str(2)].value
i  = xr

filterColumn                            = sheetrange['B'+str(i)].value
nama_lengkap                            = sheetrange['C'+str(i)].value
nomor_induk                             = sheetrange['D'+str(i)].value
NomorSurat                              = sheetrange['E'+str(i)].value
Pendaftar                               = sheetrange['F'+str(i)].value
semua                                   = sheetrange['G'+str(i)].value
statusColumn                            = sheetrange['H'+str(i)].value
@mark.fixture_test()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()


@mark.fixture_test()
def test_2_login():
    login(driver)


@mark.fixture_test()
def test_3_akses_menu_index():
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Portir').click()
    print('.')
    print('==========akses menu daftar lalu lintas==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_4_sortir_table_cari_Semua_Portir():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    sleep(driver)

    if filterColumn == 'semua':
        driver.find_element(By.XPATH, "//li[contains(.,\'Semua\')]").click()
        print('=')
        Log.info(' Memilih Dropdown Semua  ')
        attach(data=driver.get_screenshot_as_png())

        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(semua)

        Log.info(' Input kata kunci semua  ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumn == 'nomor induk':
        driver.find_element(By.ID, 'filterColumn').send_keys('induk')
        driver.find_element(By.XPATH, '//li[contains(.,\'Nomor Induk\')]').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(nomor_induk)

        Log.info(' Input kata kunci No induk  ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumn == 'Nomor Surat Penetapan':
        driver.find_element(By.ID, 'filterColumn').send_keys('Surat')
        driver.find_element(By.XPATH, '//li[contains(.,\'Nomor Surat Penetapan\')]').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NomorSurat)

        Log.info(' Input kata kunci Nomor Surat Penetapan  ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumn == 'Pendaftar':
        driver.find_element(By.ID, 'filterColumn').send_keys('Pendaftar')
        driver.find_element(By.XPATH, '//li[contains(.,\'created_by\')]').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(Pendaftar)
        Log.info(' Input kata kunci Pendaftar  ')
        attach(data=driver.get_screenshot_as_png())

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    time.sleep(1)
    driver.find_element(By.ID, 'searchButton').click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5")))
    print('=')
    Log.info(' Input Semua  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_sortir_5_Halaman_Index():
    # 5 HALAMAN
    driver.implicitly_wait(20)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'5/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys('100')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 5  ')
    attach(data=driver.get_screenshot_as_png())

    # Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)


@mark.fixture_test()
def test_6_sortir_10_Halaman_Index():
    # 10 HALAMAN
    driver.implicitly_wait(20)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'10/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys('2')
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 10  ')
    attach(data=driver.get_screenshot_as_png())


# Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_7_sortir_20_Halaman_Index():
    # 20 HALAMAN
    driver.implicitly_wait(20)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'20/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys('2')
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 20  ')
    attach(data=driver.get_screenshot_as_png())


# Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_8_sortir_50_Halaman_Index():
    # 50 HALAMAN
    driver.implicitly_wait(20)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'50/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys('100')
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 50  ')
    attach(data=driver.get_screenshot_as_png())


# Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_9_sortir_100_Halaman_Index():
    # 100 HALAMAN
    driver.implicitly_wait(20)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'100/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys('2')
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 100  ')
    attach(data=driver.get_screenshot_as_png())



@mark.fixture_test()
def test_10_SearchDataStatus_MasukPortir_Index():  # Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(20)
    time.sleep(1)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.ID, 'filterColumn').click()
    driver.find_element(By.XPATH, '//li[contains(.,\'Semua\')]').click()

    if statusColumn == 'Masuk Portir':
        driver.find_element(By.XPATH, '//*[@id="statusColumn"]').send_keys('Masuk Portir')
        driver.find_element(By.XPATH, "//li[contains(.,\'Masuk Portir\')]").click()

    elif statusColumn == 'Keluar Keamanan':
        driver.find_element(By.XPATH, '//*[@id="statusColumn"]').send_keys('keluar keamanan')
        driver.find_element(By.XPATH, "//li[contains(.,\'Keluar Keamanan\')]").click()

    elif statusColumn == 'Keluar Portir':
        driver.find_element(By.XPATH, '//li[contains(.,\'Semua\')]').click()
        driver.find_element(By.XPATH, '//*[@id="statusColumn"]').send_keys('keluar')
        driver.find_element(By.CSS_SELECTOR, "#statusKeluarPortir").click()

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5")))

    print('.')
    Log.info(' Search Data Form Kategori No Induk  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_11_exit():
    quit(driver)
