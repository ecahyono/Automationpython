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
fh = logging.FileHandler('test_1Fungsi_Daftar_Lalu_Lintas_Index.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrange = wb['DaftarLaluLintas_Index']
xr = sheetrange['A'+str(2)].value
i  = xr

filterColumn                          = sheetrange['B'+str(i)].value
namaLengkap                           = sheetrange['C'+str(i)].value
nomorInduk                            = sheetrange['D'+str(i)].value


@mark.fixture_test()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')

@mark.fixture_test()
def test_2_login():
    login(driver)
    Log.info('Login')


@mark.fixture_test()
def test_3_akses_menu_index():
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Daftar Lalu Lintas').click()
    print('.')
    Log.info('Akses Menu Daftar Lalu Lintas')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_4_Searchkategori():  # Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(20)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'filterColumn')))

    time.sleep(1)

    driver.find_element(By.ID, 'filterColumn').click()
    if filterColumn == 'namaLengkap':
        driver.find_element(By.XPATH, '//*[@id="namaLengkap"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(namaLengkap)
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
        driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.text-green-500 path')))

        print('.')
        Log.info('Search Data Form Kategori Nama ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumn == 'nomorInduk':
        driver.find_element(By.XPATH, '//*[@id="nomorInduk"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(nomorInduk)
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
        driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.text-green-500 path')))

        print('.')
        Log.info('Search Data Form Kategori No Induk ')
        attach(data=driver.get_screenshot_as_png())

# Mengosongkan kata kunci dan kategori dengan klik button clear value

# SORTIR TABLE HALAMAN INDEX
@mark.fixture_test()
def test_7_DLP001_SortirDatatable_NoInduk_Index():
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, "//span/i[2]").click()
    print('.')
    Log.info('Sortir No induk')
    attach(data=driver.get_screenshot_as_png())
    #NAMA
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, "//th[3]/div/span").click()
    print('.')
    Log.info('Sortir nama')
    attach(data=driver.get_screenshot_as_png())
    #JENIS
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, "//th[4]/div").click()
    print('.')
    Log.info(' Sortir jenis ')
    attach(data=driver.get_screenshot_as_png())
    #TANGGAL KELUAR
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, "//th[5]/div/span/i").click()
    print('.')
    Log.info('Sortir Tanggal Keluar ')
    attach(data=driver.get_screenshot_as_png())
    #TANGGAL KEMBALI
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, "//th[6]/div/span/i").click()
    print('.')
    Log.info('Sortir tanggal kembali ')
    attach(data=driver.get_screenshot_as_png())

# Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_8_DLP001_Pagination_Index():
    # 5 HALAMAN
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'5/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys('100')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info('halaman 5')
    attach(data=driver.get_screenshot_as_png())

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'10/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys('100')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info('halaman 10')
    attach(data=driver.get_screenshot_as_png())

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'20/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys('100')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info('halaman 20')
    attach(data=driver.get_screenshot_as_png())

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'50/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(
        '100')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info('halaman 50')
    attach(data=driver.get_screenshot_as_png())

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'100/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys('100')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info('halaman 100')
    attach(data=driver.get_screenshot_as_png())


# Membuka halaman Tambah Data / Cari Identitas melalui klik tombol tambah
@mark.fixture_test()
def test_9_membuka_halaman_tambah_Index():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5 > path")))
    print('.')
    Log.info('Membuka Halaman Tambah')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_10_back_index():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="backButton"]')))
    driver.find_element(By.XPATH, '//*[@id="backButton"]').click()
    print('.')
    Log.info('Back Ke Halaman Index  ')


# Membuka halaman detail melalui klik tombol aksi icon detail
@mark.fixture_test()
def test_11_membuka_halaman_ubah_Index():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 path")))
    driver.find_element(By.CSS_SELECTOR, ".text-green-500 path").click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[1]/div/button')))
    driver.find_element(By.ID, 'backButton').click()
    Log.info('Membuka Halaman Ubah  ')
    attach(data=driver.get_screenshot_as_png())


# Membuka form ubah melalui klik tombol aksi icon ubah
@mark.fixture_test()
def test_12_membuka_halaman_detail_Index():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-blue-500 .h-5")))
    driver.find_element(By.CSS_SELECTOR, ".text-blue-500 .h-5").click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[1]/div/button')))
    driver.find_element(By.ID, 'backButton').click()
    Log.info('Membuka Halaman Detail  ')
    attach(data=driver.get_screenshot_as_png())


# Melakukan export data tabel ke excel
@mark.fixture_test()
def test_13_export_exel_Index():
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div[1]/button').click()
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div[1]/div/div/div/div[2]/div/button[2]').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil mengunduh file\')]')))
    print('.')
    Log.info('Export Excel')
    attach(data=driver.get_screenshot_as_png())


# Melakukan export data tabel ke pdf
@mark.fixture_test()
def test_14_export_pdf_Index():
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[5]/div[2]/button').click()
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[5]/div[2]/div/div/div/div[2]/div/button[2]').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil mengunduh file\')]')))
    print('.')
    Log.info('Export PDF')
    attach(data=driver.get_screenshot_as_png())


# Melakukan cetak
@mark.fixture_test()
def test_15_cetak_Index():
    time.sleep(1)
    driver.implicitly_wait(30)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="printButton"]').click()
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[5]/div[3]/div/div/div/div[2]/div/button[2]').click()
    print('.')
    Log.info('Cetak')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_quit():
    quit(driver)