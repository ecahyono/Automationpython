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
fh = logging.FileHandler('test_3Fungsi_Daftar_Lalu_Lintas_Tambah.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrange = wb['DaftarLaluLintas_Input']
xr = sheetrange['A'+str(2)].value
i = xr

Nama                                  = sheetrange['B'+str(i)].value
JenisKeluar                           = sheetrange['C'+str(i)].value
TanggalKeluar                         = sheetrange['D'+str(i)].value
TanggalHarusKembali                   = sheetrange['E'+str(i)].value
deskripsi                             = sheetrange['F'+str(i)].value
PengwalInternal                       = sheetrange['G'+str(i)].value
PengwalExternal                       = sheetrange['H'+str(i)].value

@mark.fixture_test()
def test_1_setupOS_HalamanTambah():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_test()
def test_2_login_HalamanTambah():
    login(driver)

@mark.fixture_test()
def test_3_akses_menu_HalamanTambah():
    sleep(driver)
    driver.implicitly_wait(60)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Daftar Lalu Lintas').click()
    print('=')
    Log.info(' akses menu daftar lalu lintas')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_4_membuka_halaman_HalamanTambah():
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5 > path")))

    print('=')
    Log.info(' Membuka Halaman Tambah  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_sortir_table_cari_nama_HalamanTambah():
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    time.sleep(0.4)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
    print('=')
    Log.info(' Memilih Dropdown Nama  ')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(Nama)
    #driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('Wildan Cahyono')
    print('=')
    Log.info(' Input Nama  ')

    driver.implicitly_wait(60)
    sleep(driver)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    print('=')
    Log.info(' Click Button Cari  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_6_Click_Button_Detile_HalamanTambah():
    driver.implicitly_wait(60)
    sleep(driver)
    time.sleep(2)
    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.CSS_SELECTOR, ".h-5 > path").click()
    print('=')
    Log.info(' Click Button Update  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_7_Click_Button_Tambah_WBP_HalamanTambah():
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, 'createButton').click()
    print('=')
    Log.info(' Click Button Tambah WBP  ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()    
def test_8_sortir_detil_wbp_HalamanTambah():
    sleep(driver)
    WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tab-0"]')))
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-0"]')))
    driver.execute_script("window.scrollTo(0,1462.5)")
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[3]/div').click()
    driver.find_element(By.XPATH, '//*[@id="tab-1"]').click()
    time.sleep(0.3)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="tab-2"]').click()
    time.sleep(0.3)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="tab-3"]').click()
    time.sleep(0.3)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="tab-4"]').click()
    time.sleep(0.3)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="tab-5"]').click()
    time.sleep(0.3)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="tab-6"]').click()
    time.sleep(0.3)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="tab-7"]').click()

    print('=')
    Log.info(' Detile WBP')

@mark.fixture_test()
def test_9_detile_perkara_HalamanTambah():

    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tab-registrasi"]')))
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-registrasi"]')))
    driver.execute_script("window.scrollTo(0,1462.5)")
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[3]/div').click()
    driver.find_element(By.XPATH, '//*[@id="tab-registrasi"]').click()
    time.sleep(0.3)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="tab-sidang"]').click()
    time.sleep(0.3)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="tab-tahanan_rumah"]').click()
    time.sleep(0.3)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="tab-meninggal_dunia"]').click()
    time.sleep(0.3)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="tab-mutasi_upt"]').click()
    time.sleep(0.3)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="tab-pm"]').click()
    time.sleep(0.3)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="tab-pembebasan"]').click()
    print('=')
    Log.info('Detile Perkara')

@mark.fixture_test()
def test_10_Input_JenisKeluar_HalamanTambah():
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jenisKeluar"]')))
    driver.find_element(By.XPATH, '//*[@id="jenisKeluar"]').click()

    if JenisKeluar == 'Asimilasi':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Asimilasi')
        driver.find_element(By.XPATH, "//li[contains(.,\'Asimilasi\')]").click()
        print('.')
        Log.info(' Input Jenis Keluar Asimilasi  ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluar == 'Pembebasan Bersyarat':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Pembebasan Bersyarat')
        driver.find_element(By.XPATH, "//li[contains(.,\'Pembebasan Bersyarat\')]").click()
        print('.')
        Log.info(' Input Jenis Pembebasan bersyarat ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluar == 'Anak Kembali ke Orang Tua':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Anak Kembali ke Orang Tua')
        driver.find_element(By.XPATH, "//li[contains(.,\'Anak Kembali ke Orang Tua\')]").click()
        print('.')
        Log.info(' Input Jenis Anak Kembali ke Orang Tua ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluar == 'Cuti Bersyarat':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Cuti Bersyarat')
        driver.find_element(By.XPATH, "//li[contains(.,\'Cuti Bersyarat\')]").click()
        print('.')
        Log.info(' Input Jenis Cuti Bersyarat ')
        attach(data=driver.get_screenshot_as_png())


    elif JenisKeluar == 'Asimilasi di Rumah':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Asimilasi di Rumah')
        driver.find_element(By.XPATH, "//li[contains(.,\'Asimilasi di Rumah\')]").click()
        print('.')
        Log.info(' Input Jenis Asimilasi di Rumah ')
        attach(data=driver.get_screenshot_as_png())


    elif JenisKeluar == 'Bebas Biasa':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Bebas Biasa')
        driver.find_element(By.XPATH, "//li[contains(.,\'Bebas Biasa\')]").click()
        print('.')
        Log.info(' Input Jenis Bebas Biasa ')
        attach(data=driver.get_screenshot_as_png())


    elif JenisKeluar == 'Bebas dari Dakwaan':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Bebas dari Dakwaan')
        driver.find_element(By.XPATH, "//li[contains(.,\'Bebas dari Dakwaan\')]").click()
        print('.')
        Log.info(' Input Jenis Bebas dari Dakwaan ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluar == 'Bebas Dari Tuntutan':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Bebas Dari Tuntutan')
        driver.find_element(By.XPATH, "//li[contains(.,\'Bebas Dari Tuntutan\')]").click()
        print('.')
        Log.info(' Input Jenis Bebas Dari Tuntutan ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluar == 'Cuti Menjelang Bebas':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Cuti Menjelang Bebas')
        driver.find_element(By.XPATH, "//li[contains(.,\'Cuti Menjelang Bebas\')]").click()
        print('.')
        Log.info(' Input Jenis Cuti Menjelang Bebas ')
        attach(data=driver.get_screenshot_as_png())






@mark.fixture_test()
def test_11_Input_Tanggal_Keluar_HalamanTambah():

    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="keluarKeamanan"]')))
    driver.find_element(By.XPATH, '//*[@id="keluarKeamanan"]').send_keys(TanggalKeluar)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="keluarKeamanan"]').send_keys(Keys.ENTER)

    print('=')
    Log.info(' Input Tanggal Keluar  ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_12_Input_Deskripsi_HalamanTambah():
    sleep(driver)
    driver.implicitly_wait(60)
    driver.execute_script("window.scrollTo(0,1462.5)")
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#deskripsi')))
    driver.find_element(By.CSS_SELECTOR, "#deskripsi").click()
    driver.find_element(By.CSS_SELECTOR, "#deskripsi").send_keys(deskripsi)
    print('=')
    Log.info(' Input Deskripsi Behasil ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_13_Input_Tanggal_Harus_Kembali_HalamanTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tanggalKembali"]')))
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').send_keys(TanggalHarusKembali)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').send_keys(Keys.ENTER)
    print('=')
    Log.info(' Input Tanggal Harus Kembali  ')
    attach(data=driver.get_screenshot_as_png())
    
@mark.fixture_test()
def test_14_tambah_Pengwal_HalamanTambah():
    sleep(driver)
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="addPengawal"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="addPengawal"]').click()
    print('=')
    Log.info(' Input tambah pengawal  ')
    attach(data=driver.get_screenshot_as_png())



@mark.fixture_test()
def test_15_JenisPengawal_HalamanTambah():
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jenis0"]')))
    driver.find_element(By.XPATH, '//*[@id="jenis0"]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Internal\')]").click()
    print('=')
    Log.info(' Input tambah Jenis pengawal  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_16_NamaPengawalInternal_HalamanTambah():
    sleep(driver)
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="pengawalInternal0"]').click
    driver.find_element(By.XPATH, '//*[@id="pengawalInternal0"]').send_keys(PengwalInternal)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="optionPengawal00"]')))
    driver.find_element(By.XPATH, '//*[@id="optionPengawal00"]').click()
    print('=')
    Log.info(' Input nama pengawal Internal  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_17_JenisPengawalEksternal_HalamanTambah():
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jenis1"]')))
    driver.find_element(By.XPATH, '//*[@id="jenis1"]').click()
    driver.find_element(By.CSS_SELECTOR, "#Eksternal1").click()
    print('=')
    Log.info(' Input tambah Jenis pengawal  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_18_NamaPengawalEksternal_HalamanTambah():
    sleep(driver)
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="pengawal1"]').click
    driver.find_element(By.XPATH, '//*[@id="pengawal1"]').send_keys(PengwalExternal)
    time.sleep(1)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, "//td[contains(.,'operator')]")))
    time.sleep(0.4)
    driver.find_element(By.XPATH, "//td[contains(.,'operator')]").click()
    print('=')
    Log.info(' Input nama pengawal Enternal  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_19_ButtonSubmitInternal_HalamanTambah():
    sleep(driver)
    driver.implicitly_wait(60)
    time.sleep(3)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSubmit"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSubmit"]').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    print('=')
    Log.info(' Menekan Button Submit  ')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_exit():
    quit(driver)