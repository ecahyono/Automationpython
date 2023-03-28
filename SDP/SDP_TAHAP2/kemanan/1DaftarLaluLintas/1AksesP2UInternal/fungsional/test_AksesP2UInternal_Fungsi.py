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

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))


from Settings.setupkeamanan import initDriver, loadDataPath, quit, sleep
from Settings.loginkeamanan import Op_Keamanan_p2u, SpvRutanBdg
from Settings.Page.keamanan import p2uinternal

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Log1_P2Uinternal.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("KeamananUAT"))
sheetrangeIndex = wb['P2U_Internal']

i = 6

NamaInput                                 = sheetrangeIndex['A'+str(i)].value
Nosk                                      = sheetrangeIndex['B'+str(i)].value
jenisKeluar                               = sheetrangeIndex['C'+str(i)].value
TanggalKeluar                             = sheetrangeIndex['D'+str(i)].value
tanggalKembali                            = sheetrangeIndex['E'+str(i)].value
deskripsi                                 = sheetrangeIndex['F'+str(i)].value
JenisPengawal                             = sheetrangeIndex['G'+str(i)].value
namaPengawalExternal                      = sheetrangeIndex['H'+str(i)].value
namaPengawalInternal                      = sheetrangeIndex['I'+str(i)].value

@mark.fixture_test()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')
    sleep(driver)

@mark.fixture_test()
def test_2_loginOperator():
    sleep(driver)
    Op_Keamanan_p2u(driver)
    Log.info('Login Operator Keamanan P2U')


@mark.fixture_test()
def test_3_AksesMenu():
    sleep(driver)
    p2uinternal(driver)
    print('.')
    Log.info('Akses halaman Daftar Lalu Lintas P2U Internal')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_4_ClickButtonCreate():
    sleep(driver)
    print('Click Button Create')
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, 'createButton').click()
    Log.info('Click Button Create')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_SearchNamaWBP():
    sleep(driver)
    print('Pilih Dropdown Nama')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))

    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))

    print('== NEXT == Input kata kunci nama')
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').clear()
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NamaInput)
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_6_SearchNamaWBP():
    sleep(driver)
    Log.info('Search Nama WBP')
    driver.find_element(By.ID, 'buttonSearch' ).click()
    Log.info('Click Button Search')
    attach(data=driver.get_screenshot_as_png())
    sleep(driver)

@mark.fixture_test()
def test_7_ClickButtonDetile():
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.CSS_SELECTOR, ".h-5 > path").click()
    Log.info('Click Button Detile')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_8_ButtonTambah():
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, 'createButton').click()
    Log.info('Click Button Tambah WBP')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_9_InputNoSK():
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'buttonSubmit')))
    driver.find_element(By.ID, 'noSK').send_keys(Nosk)
    Log.info('Input No SK')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_10_UploadSK():
    sleep(driver)
    driver.find_element(By.XPATH, "//div[@id=\'fileSK\']/div/button").click()
    
    sleep(driver)
    pyautogui.write("///////users/will/test.pdf")
    pyautogui.press('return')
    pyautogui.write("///////users/will/test.pdf")

    pyautogui.press('return')
    time.sleep(0.5)
    pyautogui.press('escape')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    
    

    Log.info('Upload SK')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_11_InputJenisKeluar():
    sleep(driver)
    driver.find_element(By.ID, 'jenisKeluar').click()
    
    if jenisKeluar == 'Pembebasan Bersyarat':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Pembebasan Bersyarat')
        driver.find_element(By.XPATH, "//li[contains(.,\'Pembebasan Bersyarat\')]").click()
        attach(data=driver.get_screenshot_as_png())

    elif jenisKeluar == 'Anak Kembali ke Orang Tua':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Anak Kembali ke Orang Tua')
        driver.find_element(By.XPATH, "//li[contains(.,\'Anak Kembali ke Orang Tua\')]").click()
        attach(data=driver.get_screenshot_as_png())

    elif jenisKeluar == 'Asimilasi':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Asimilasi')
        driver.find_element(By.XPATH, "//li[contains(.,\'Asimilasi\')]").click()
        attach(data=driver.get_screenshot_as_png())

    elif jenisKeluar == 'Asimilasi di Rumah':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Asimilasi di Rumah')
        driver.find_element(By.XPATH, "//li[contains(.,\'Asimilasi di Rumah\')]").click()
        attach(data=driver.get_screenshot_as_png())

    elif jenisKeluar == 'Bebas Biasa':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Bebas Biasa')
        driver.find_element(By.XPATH, "//li[contains(.,\'Bebas Biasa\')]").click()
        attach(data=driver.get_screenshot_as_png())

    elif jenisKeluar == 'Bebas dari Dakwaan':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Bebas dari Dakwaan')
        driver.find_element(By.XPATH, "//li[contains(.,\'Bebas dari Dakwaan\')]").click()
        attach(data=driver.get_screenshot_as_png())

    elif jenisKeluar == 'Bebas Dari Tuntutan':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Bebas Dari Tuntutan')
        driver.find_element(By.XPATH, "//li[contains(.,\'Bebas Dari Tuntutan\')]").click()
        attach(data=driver.get_screenshot_as_png())

    elif jenisKeluar == 'Cuti Menjelang Bebas':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Cuti Menjelang Bebas')
        driver.find_element(By.XPATH, "//li[contains(.,\'Cuti Menjelang Bebas\')]").click()
        attach(data=driver.get_screenshot_as_png())

    elif jenisKeluar == 'Cuti Bersyarat':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Cuti Bersyarat')
        driver.find_element(By.XPATH, "//li[contains(.,\'Cuti Bersyarat\')]").click()
        attach(data=driver.get_screenshot_as_png())

    elif jenisKeluar == 'Dikeluarkan Demi Hukum':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Dikeluarkan Demi Hukum')
        driver.find_element(By.XPATH, "//li[contains(.,\'Dikeluarkan Demi Hukum\')]").click()
        attach(data=driver.get_screenshot_as_png())

    elif jenisKeluar == 'Dikembalikan ke Pihak Penahan':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Dikembalikan ke Pihak Penahan')
        driver.find_element(By.XPATH, "//li[contains(.,\'Dikembalikan ke Pihak Penahan\')]").click()
        attach(data=driver.get_screenshot_as_png())

    elif jenisKeluar == 'Dirawat Dirumah Sakit':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Dirawat Dirumah Sakit')
        driver.find_element(By.XPATH, "//li[contains(.,\'Dirawat Dirumah Sakit\')]").click()
        attach(data=driver.get_screenshot_as_png())

    elif jenisKeluar == 'Diversi':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Diversi')
        driver.find_element(By.XPATH, "//li[contains(.,\'Diversi\')]").click()
        attach(data=driver.get_screenshot_as_png())
    Log.info('Input Jenis Keluar')


@mark.fixture_test()
def test_12_InputTanggalKeluarKeamanan():
    sleep(driver)
    driver.find_element(By.ID, "keluarKeamanan").click()
    sleep(driver)
    driver.find_element(By.ID, "keluarKeamanan").send_keys(TanggalKeluar)
    Log.info('Input Tanggal Keluar')
    attach(data=driver.get_screenshot_as_png())
    sleep(driver)

@mark.fixture_test()
def test_13_InputTanggalKembali():
    sleep(driver)
    driver.find_element(By.ID, "tanggalKembali").click()
    sleep(driver)
    driver.find_element(By.ID, "tanggalKembali").send_keys(tanggalKembali)
    Log.info('Input Tanggal Kembali')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_14_InputDeskripsi():
    sleep(driver)
    driver.find_element(By.ID, "deskripsi").click()
    driver.find_element(By.ID, "deskripsi").send_keys(deskripsi)
    Log.info('Input Deskripsi')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_15_InputJenisPengawal():
    sleep(driver)
    driver.find_element(By.ID, "jenis0").click()
    sleep(driver)
    if JenisPengawal == 'Eksternal':
        driver.find_element(By.ID, "Eksternal0").click()
        driver.find_element(By.ID, 'pengawal0').click()
        driver.find_element(By.XPATH, "//td[contains(.,'"+ namaPengawalExternal +"')]").click()
        Log.info('input pengawal external')
        attach(data=driver.get_screenshot_as_png())

    elif JenisPengawal == 'Internal':
        driver.find_element(By.ID, "Internal0").click()
        driver.find_element(By.ID, 'pengawalInternal0').click()
        driver.find_element(By.XPATH, "//td[contains(.,'"+ namaPengawalInternal +"')]").click()
        Log.info('input pengawal internal')
        attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_16_ClickButtonSubmit():
    sleep(driver)
    driver.find_element(By.ID, 'buttonSubmit').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    Log.info('click button submit')
    attach(data=driver.get_screenshot_as_png())




@mark.fixture_test()
def test_17_loginSpv():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')
    SpvRutanBdg(driver)
    Log.info('Login Super Visor P2U')


@mark.fixture_test()
def test_18_AksesMenu():
    sleep(driver)

    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Akses P2U Internal').click()
    sleep(driver)
    print('.')
    Log.info('Akses halaman Daftar Lalu Lintas P2U Internal')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_19_PilihDropdownNama():
    sleep(driver)
    print('Pilih Dropdown Nama')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.ID, 'statusColumn').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Dalam Proses\')]").click()
    Log.info('Klik Status Dalam Proses')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_20_SearchNamaWBP_():
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').clear()
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NamaInput)
    Log.info('Search Nama WBP')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_21_ClickButtonSearch():
    sleep(driver)
    driver.find_element(By.ID, 'searchButton' ).click()
    Log.info('Click Button Search')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_22_ClickButtonVerifikasi():
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.CSS_SELECTOR, ".w-6 > path").click()
    Log.info('Click Button Verifikasi')
    attach(data=driver.get_screenshot_as_png())
    
@mark.fixture_test()
def test_23_InputKeterangan():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'keterangan')))
    driver.find_element(By.ID, 'keterangan').send_keys(deskripsi)
    Log.info('Input Keterangan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_24_ClickButtonDiziinkan():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'Izinkan')))
    driver.find_element(By.ID, 'Izinkan').click()
    Log.info('click button izinkan')
    driver.execute_script("window.scrollTo(0,527)") 
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_25_ClickButtonYa():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Ya')]")))
    driver.find_element(By.XPATH, "//span[contains(.,'Ya')]").click()
    Log.info ('Click button ya ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_26_loginOperator():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')
    Op_Keamanan_p2u(driver)
    Log.info('Login Operator Keamanan')


@mark.fixture_test()
def test_27_AksesMenu():
    sleep(driver)
    p2uinternal(driver)
    print('.')
    Log.info('Akses halaman Daftar Lalu Lintas P2U Internal')
    attach(data=driver.get_screenshot_as_png())
    Log.info('Akses halaman Daftar Lalu Lintas P2U Internal')
    attach(data=driver.get_screenshot_as_png())
    




@mark.fixture_test()
def test_28_StatusDalamProses():
    print('Pilih Dropdown Nama')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.ID, 'statusColumn').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Dalam Proses\')]").click()
    Log.info('Filter Status Dalam Proses')
    
@mark.fixture_test()
def test_28_SearchNamaWbp():
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').clear()
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NamaInput)
    Log.info('Search Nama WBP')
    driver.find_element(By.ID, 'searchButton' ).click()
    Log.info('Click Button Search')

@mark.fixture_test()
def test_29_ClickButtonDetile():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, "#detailButton-0 .h-5").click()
    Log.info('Click Button Detile')

@mark.fixture_test()
def test_30_ClickButtonKonfirmasiKeluar():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    Log.info('clik button keluar P2U')

@mark.fixture_test()
def test_31_SearchStatusKeluarP2U():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.ID, 'statusColumn').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Keluar P2U\')]").click()
    Log.info('filter status Keluar P2U')

@mark.fixture_test()
def test_32_SearchNamaWBP():
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').clear()
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NamaInput)
    Log.info('Search Nama WBP')

@mark.fixture_test()
def test_33_ClickButtonSearch():
    driver.find_element(By.ID, 'searchButton' ).click()
    Log.info('click button search')

@mark.fixture_test()
def test_34_ClickButtonDetail():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, "#detailButton-0 .h-5").click()
    Log.info('Click Button Detile')

@mark.fixture_test()
def test_35_ClickButtonMasukP2U():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    Log.info('click button masuk P2U')

    sleep(driver)

@mark.fixture_test()
def test_36_exit():
    quit(driver)

        

  
        






