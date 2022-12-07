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
fh = logging.FileHandler('Fungsi_P2U_Index.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


sheetrange = wb['Fungsi_P2U_Index']
xr = input("")
i  = xr

filterColumn                                = sheetrange['B'+str(i)].value
NamaWBP                                     = sheetrange['C'+str(i)].value
NomorInduk                                  = sheetrange['D'+str(i)].value
Keperluan                                   = sheetrange['E'+str(i)].value
inputKategori                               = sheetrange['F'+str(i)].value

filterTanggalMasuk                          = sheetrange['G'+str(i)].value
filterTanggalKeluar                         = sheetrange['H'+str(i)].value

@mark.fixture_test()
def test_1_SetupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')

@mark.fixture_test()
def test_2_Login():
    login(driver)
    Log.info('login')

@mark.fixture_test()
def test_3_akses_menu_index():
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Akses Pintu P2U').click()
    print('.')
    Log.info('akses menu daftar lalu lintas')
    attach(data=driver.get_screenshot_as_png())



@mark.fixture_test()
def test_4_SearchDATA():
    # Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(30)
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    if filterColumn == 'nama lengkap':
        driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys('nama')
        #KETIK NAMA
        driver.find_element(By.XPATH, "//li[contains(.,\'Nama Lengkap\')]").click()
        #PILIH DROPDOWN NAMA LENGKAP
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NamaWBP)
        #KETIK GALIH DI FORM MASUKAN KATA KUNCI
        Log.info('Search Bedasarkan Nama Lengkap')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumn == 'nomor induk':
        driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys('Nomor')
        # KETIK NOMOR
        driver.find_element(By.XPATH, "//li[contains(.,\'Nomor Identitas\')]").click()
        # PILIH DROPDOWN NOMOR IDENTITAS
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NomorInduk)
        Log.info('Search Bedasarkan Nomor Induk')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumn == 'keperluan':
        driver.find_element(By.XPATH, '//*[@id="filterColumn"]').send_keys('Keperluan')
        # KETIK NOMOR
        driver.find_element(By.XPATH, "//li[contains(.,\'Keperluan\')]").click()
        # PILIH DROPDOWN NOMOR IDENTITAS
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(Keperluan)
        Log.info('Search Bedasarkan Keperluan')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumn == 'kategori':
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="filterColumn"]').send_keys('Kategori')
        driver.find_element(By.XPATH, "//li[contains(.,\'Kategori\')]").click()
        driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
        Log.info('Search Bedasarkan kategori')
        attach(data=driver.get_screenshot_as_png())
        sleep(driver)

        if inputKategori == 'Pegawai':
            driver.find_element(By.XPATH, "//li[@id='pegawai']").click()
            Log.info('select kategori pegawai')
            attach(data=driver.get_screenshot_as_png())
        elif inputKategori == 'Tamu Dinas':
            driver.find_element(By.ID,'tamuDinas').click()
            Log.info('select kategori tamu dinas')
            attach(data=driver.get_screenshot_as_png())
        elif inputKategori == 'Kunjungan Onsite':
            driver.find_element(By.XPATH, "//li[@id='Kunjungan']").click()
            Log.info('select kategori Kunjungan onsite')
            attach(data=driver.get_screenshot_as_png())
        elif inputKategori == 'Kunjungan Online':
            driver.find_element(By.XPATH, "//li[@id='Kunjungan Online']").click()
            Log.info('select kategori Kunjungan Online')
            attach(data=driver.get_screenshot_as_png())
        sleep(driver)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()
    Log.info('Search Data berhasil')
    attach(data=driver.get_screenshot_as_png())

#Mengosongkan kata kunci dan kategori dengan klik button clear value
@mark.fixture_test()
def test_5_Clik_clear_value_Index():
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, '//*[@id="filterColumn"]')
    actions = ActionChains(driver)
    actions.move_to_element(nav1).perform()
    element2 = driver.find_element(By.CSS_SELECTOR, ".el-select__caret:nth-child(2) > svg")
    time.sleep(1)
    actions2 = ActionChains(driver)
    actions2.move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-select__caret:nth-child(2) > svg").click()
    print('.')
    Log.info('Clear Value Button')
    attach(data=driver.get_screenshot_as_png())

    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('tessssst') #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci yang tidak sesuai lalu data table yang ditampilkan kosong
    time.sleep(0.5)
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, '//*[@id="kataKunci"]')
    actions = ActionChains(driver)
    actions.move_to_element(nav1).perform()
    element2 = driver.find_element(By.CSS_SELECTOR, ".el-input__clear > svg")
    time.sleep(1)
    actions2 = ActionChains(driver)
    actions2.move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-input__clear > svg").click()
    print('.')
    Log.info('Clear Value Button')
    attach(data=driver.get_screenshot_as_png())



#SORTIR TABLE HALAMAN INDEX
@mark.fixture_test()
def test_6_Sortir_data_table_NoInduk_Index():
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, "//span/i[2]").click()
    print('.')
    Log.info('Sortir No Induk=')
    attach(data=driver.get_screenshot_as_png())
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, "//th[3]/div/span").click()
    print('.')
    Log.info('Sortir Nama=')
    attach(data=driver.get_screenshot_as_png())
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, "//th[4]/div").click()
    print('.')
    Log.info('Sortir Jenis=')
    attach(data=driver.get_screenshot_as_png())
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, "//th[5]/div/span/i").click()
    print('.')
    Log.info('Sortir Tanggal Keluar=')
    attach(data=driver.get_screenshot_as_png())
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, "//th[6]/div/span/i").click()
    print('.')
    Log.info('Sortir No Tanggal Kembali=')
    attach(data=driver.get_screenshot_as_png())

#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_7_Sortir_5_Halaman_Index():
    #5 HALAMAN
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke1']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'5/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys('100')
    # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 5  ')
    attach(data=driver.get_screenshot_as_png())


#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_8_Sortir_10_Halaman_Index():
    #10 HALAMAN
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke1']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'10/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys('2')
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 10  ')
    attach(data=driver.get_screenshot_as_png())


#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_9_Sortir_20_Halaman_Index():
     #20 HALAMAN
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke1']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'20/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys('2')
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 20  ')
    attach(data=driver.get_screenshot_as_png())


#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_10_Sortir_50_Halaman_Index():
    #50 HALAMAN
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke1']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'50/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys('2')
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 50  ')
    attach(data=driver.get_screenshot_as_png())

#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_11_Sortir_100_Halaman_Index():
    #100 HALAMAN
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke1']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'100/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Click ke']).send_keys('2')
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 100  ')
    attach(data=driver.get_screenshot_as_png())



@mark.fixture_test()
def test_12_Export_pdf_Index():
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.XPATH, '//*[@id="pdfButton"]/button').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[5]/div[2]/div/div/div/div[2]/div/button[2]').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil mengunduh file\')]')))
    print('.')
    Log.info(' Export PDF    ')
    attach(data=driver.get_screenshot_as_png())



#Melakukan export data tabel ke excel
@mark.fixture_test()
def test_13_Export_exel_Index():
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.XPATH, '//*[@id="excelButton"]/button').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div[1]/div/div/div/div[2]/div/button[2]').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil mengunduh file\')]')))
    print('.')
    Log.info(' Export Excel   ')
    attach(data=driver.get_screenshot_as_png())

#Melakukan export data tabel ke pdf

#Melakukan cetak
@mark.fixture_test()
def test_14_Cetak_Index():
    time.sleep(1)
    driver.implicitly_wait(30)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.XPATH, '//*[@id="printButton"]').click()
    driver.find_element(By.XPATH, '//*[@id="printButton"]/div/div/div/div[2]/div/button[2]').click()


    print('.')
    Log.info(' Cetak ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_15_SearchTanggal():
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.ID, 'searchButton')))
    # BUTTON CARI
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filterTanggalMasuk"]')))
    # BUTTON CARI
    time.sleep(1)
    driver.find_element(By.ID, "filterTanggalMasuk").send_keys(filterTanggalMasuk)
    driver.find_element(By.ID, "filterTanggalMasuk").send_keys(Keys.ENTER)
    WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.ID, 'searchButton')))
    driver.find_element(By.ID, 'searchButton').click()
    print('.')
    Log.info('Search Tanggal Masuk=')
    attach(data=driver.get_screenshot_as_png())

    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="searchButton"]')))
    # BUTTON CARI
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filterTanggalMasuk"]')))
    # BUTTON CARI
    time.sleep(1)
    driver.find_element(By.ID, "filterTanggalKeluar").send_keys(filterTanggalKeluar)
    driver.find_element(By.ID, "filterTanggalKeluar").send_keys(Keys.ENTER)
    WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.ID, 'searchButton')))
    driver.find_element(By.ID, 'searchButton').click()

    print('.')
    Log.info('Search Tanggal Keluar=')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_16_exit():
    quit(driver)
    # TAMBAHAN FILTER TANGGAL
