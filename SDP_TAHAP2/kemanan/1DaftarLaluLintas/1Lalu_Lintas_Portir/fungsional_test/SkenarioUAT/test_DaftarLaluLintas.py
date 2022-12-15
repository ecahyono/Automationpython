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
    wb = load_workbook(filename=r"/Users/will/Documents/work/Automationpython/Filexel/KeamananUAT.xlsx")
    sys.path.append(environ.get("MACEXCELDIR"))

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))
    sys.path.append(environ.get("WINEXCELDIR"))


from Settings.setup import initDriver, loadDataPath, quit, sleep
from Settings.login import login

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('1Fungsi_Daftar_Lalu_Lintas_Index.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrange = wb['DaftarlaluLintasUAT']
print('.')
print('Mau Baris Ke Berapa ?')
index  = input('')

filterColumnindex                          = sheetrange['B'+str(index)].value
namaLengkapindex                           = sheetrange['C'+str(index)].value
nomorIndukindex                            = sheetrange['D'+str(index)].value





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
def test_DLP_001():
    print('.')
    print('Akses halaman Daftar Lalu Lintas (DLP-001)')

    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Daftar Lalu Lintas').click()
    sleep(driver)
    Log.info('(DLP-001) Akses halaman Daftar Lalu Lintas - Mengakses halaman Daftar Lalu Lintas dengan memilih modul Keamanan kemudian pilih menu Lalu Lintas lalu pilih submenu Daftar Lalu Lintas')
    attach(data=driver.get_screenshot_as_png())



@mark.fixture_test()
def test_DLP002():
    # Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(20)
    sleep(driver)
    print('Pengecekan data yang telah di filter')
    print('DLP-002')
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'filterColumn')))

    time.sleep(1)

    driver.find_element(By.ID, 'filterColumn').click()
    if filterColumnindex == 'namaLengkap':
        driver.find_element(By.XPATH, '//*[@id="namaLengkap"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(namaLengkapindex)
        print('.')
        Log.info('Search Data Form Kategori Nama ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == 'nomorInduk':
        driver.find_element(By.XPATH, '//*[@id="nomorInduk"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(nomorIndukindex)
        print('.')
        Log.info('Search Data Form Kategori No Induk ')
        attach(data=driver.get_screenshot_as_png())

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.text-green-500 path')))
    Log.info('(DLP-002) Pengecekan data yang telah di filter - Melakukan pengecekan filtering data berdasarkan kategori dan status')


                                ########## HALAMAN CARI IDENTITAS WBP ##########

sheetrangeCariIdentitas = wb['DaftarLaluLintas_CariIdentitas']
print('.')
print('Masuk Ke halaman Cari,Mau Baris Ke Berapa ?')
cari  = input('')

filterColumncari                          = sheetrangeCariIdentitas['B'+str(cari)].value
nomorRegcari                              = sheetrangeCariIdentitas['C'+str(cari)].value
Namacari                                  = sheetrangeCariIdentitas['D'+str(cari)].value
jenisKejahatancari                        = sheetrangeCariIdentitas['E'+str(cari)].value

@mark.fixture_test()
def test_DLP_003():
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, 'createButton').click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5 > path")))

    print('.')
    Log.info('Membuka Halaman Tambah')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)

    driver.implicitly_wait(60)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()

    if filterColumncari == 'nomorReg':
        driver.find_element(By.XPATH, '//*[@id="nomorReg"]').click()
        print('.')
        Log.info(' Memilih Dropdown Noregis  ')
        attach(data=driver.get_screenshot_as_png())

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(nomorRegcari)
        print('.')
        Log.info('Input Noregis  ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumncari == 'nama':
        driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
        print('.')
        Log.info('Memilih Dropdown Nama')
        attach(data=driver.get_screenshot_as_png())

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(Namacari)
        print('.')
        Log.info('Input Nama')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumncari == 'jenisKejahatan':
        driver.find_element(By.XPATH, '//*[@id="jenisKejahatan"]').click()
        print('.')
        Log.info('Memilih Dropdown Jenis Kejahatan  ')
        attach(data=driver.get_screenshot_as_png())

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(jenisKejahatancari)
        print('.')
        Log.info('Input Jenis kejahatan')
        attach(data=driver.get_screenshot_as_png())

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    print('.')
    Log.info('Click Button Cari ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_DLP_004():
    #belum
    print('kumaha ieu')

@mark.fixture_test()
def test_DLP_005():
    sleep(driver)
    # 5 HALAMAN
    driver.implicitly_wait(60)
    driver.execute_script("window.scrollTo(0,326)")
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '(//input[@type=\'text\'])[3]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'5/halaman\')]").click()
    driver.find_element(By.XPATH, '//input[@type=\'number\']').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, "//input[@type=\'number\']").send_keys(
        "2")  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 5 halaman cari  ')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    # 10 HALAMAN
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '(//input[@type=\'text\'])[3]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'10/halaman\')]").click()
    driver.find_element(By.XPATH, '//input[@type=\'number\']').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//input[@type=\'number\']').send_keys(
        '3')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 10 halaman cari ')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    # 20 HALAMAN
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '(//input[@type=\'text\'])[3]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'20/halaman\')]").click()
    driver.find_element(By.XPATH, '//input[@type=\'number\']').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//input[@type=\'number\']').send_keys(
        '3')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 20 halaman cari ')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    # 50 HALAMAN
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '(//input[@type=\'text\'])[3]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'50/halaman\')]").click()
    driver.find_element(By.XPATH, '//input[@type=\'number\']').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//input[@type=\'number\']').send_keys('3')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info(' Menampilkan 50 halaman cari ')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    # 100 HALAMAN
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '(//input[@type=\'text\'])[3]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'100/halaman\')]").click()
    driver.find_element(By.XPATH, '//input[@type=\'number\']').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//input[@type=\'number\']').send_keys(
        '3')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info('Menampilkan 100 halaman cari ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_DLP_006():
    #belum
    print('test button selanjutnya dan sebelum')

                                        ########## MASUK KE HALAMAN TAMBAH ##########

sheetrangeInput = wb['DaftarLaluLintas_Input']
Halinput = input('')

NamaInput                                  = sheetrangeInput['B'+str(Halinput)].value
JenisKeluarInput                           = sheetrangeInput['C'+str(Halinput)].value
TanggalKeluarInput                         = sheetrangeInput['D'+str(Halinput)].value
TanggalHarusKembaliInput                   = sheetrangeInput['E'+str(Halinput)].value
deskripsiInput                             = sheetrangeInput['F'+str(Halinput)].value
PengwalInternalInput                       = sheetrangeInput['G'+str(Halinput)].value
PengwalExternalInput                       = sheetrangeInput['H'+str(Halinput)].value

@mark.fixture_test()
def test_DLP_007():
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    time.sleep(0.4)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
    print('=')
    Log.info(' Memilih Dropdown Nama  ')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NamaInput)
    # driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('Wildan Cahyono')
    print('=')
    Log.info(' Input Nama  ')

    driver.implicitly_wait(60)
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    print('=')
    Log.info(' Click Button Cari  ')
    attach(data=driver.get_screenshot_as_png())

    driver.implicitly_wait(60)
    sleep(driver)
    time.sleep(2)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.CSS_SELECTOR, ".h-5 > path").click()
    print('=')
    Log.info(' Click Button Update  ')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, 'createButton').click()
    print('=')
    Log.info(' Click Button Tambah WBP  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_DLP_008():
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jenisKeluar"]')))
    driver.find_element(By.XPATH, '//*[@id="jenisKeluar"]').click()

    if JenisKeluarInput == 'Asimilasi':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Asimilasi')
        driver.find_element(By.XPATH, "//li[contains(.,\'Asimilasi\')]").click()
        print('.')
        Log.info(' Input Jenis Keluar Asimilasi  ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluarInput == 'Pembebasan Bersyarat':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Pembebasan Bersyarat')
        driver.find_element(By.XPATH, "//li[contains(.,\'Pembebasan Bersyarat\')]").click()
        print('.')
        Log.info(' Input Jenis Pembebasan bersyarat ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluarInput == 'Anak Kembali ke Orang Tua':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Anak Kembali ke Orang Tua')
        driver.find_element(By.XPATH, "//li[contains(.,\'Anak Kembali ke Orang Tua\')]").click()
        print('.')
        Log.info(' Input Jenis Anak Kembali ke Orang Tua ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluarInput == 'Cuti Bersyarat':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Cuti Bersyarat')
        driver.find_element(By.XPATH, "//li[contains(.,\'Cuti Bersyarat\')]").click()
        print('.')
        Log.info(' Input Jenis Cuti Bersyarat ')
        attach(data=driver.get_screenshot_as_png())


    elif JenisKeluarInput == 'Asimilasi di Rumah':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Asimilasi di Rumah')
        driver.find_element(By.XPATH, "//li[contains(.,\'Asimilasi di Rumah\')]").click()
        print('.')
        Log.info(' Input Jenis Asimilasi di Rumah ')
        attach(data=driver.get_screenshot_as_png())


    elif JenisKeluarInput == 'Bebas Biasa':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Bebas Biasa')
        driver.find_element(By.XPATH, "//li[contains(.,\'Bebas Biasa\')]").click()
        print('.')
        Log.info(' Input Jenis Bebas Biasa ')
        attach(data=driver.get_screenshot_as_png())


    elif JenisKeluarInput == 'Bebas dari Dakwaan':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Bebas dari Dakwaan')
        driver.find_element(By.XPATH, "//li[contains(.,\'Bebas dari Dakwaan\')]").click()
        print('.')
        Log.info(' Input Jenis Bebas dari Dakwaan ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluarInput == 'Bebas Dari Tuntutan':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Bebas Dari Tuntutan')
        driver.find_element(By.XPATH, "//li[contains(.,\'Bebas Dari Tuntutan\')]").click()
        print('.')
        Log.info(' Input Jenis Bebas Dari Tuntutan ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluarInput == 'Cuti Menjelang Bebas':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Cuti Menjelang Bebas')
        driver.find_element(By.XPATH, "//li[contains(.,\'Cuti Menjelang Bebas\')]").click()
        print('.')
        Log.info(' Input Jenis Cuti Menjelang Bebas ')
        attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="keluarKeamanan"]')))
    driver.find_element(By.XPATH, '//*[@id="keluarKeamanan"]').send_keys(TanggalKeluarInput)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="keluarKeamanan"]').send_keys(Keys.ENTER)

    print('=')
    Log.info(' Input Tanggal Keluar  ')
    attach(data=driver.get_screenshot_as_png())


    sleep(driver)
    driver.implicitly_wait(60)
    driver.execute_script("window.scrollTo(0,1462.5)")
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#deskripsi')))
    driver.find_element(By.CSS_SELECTOR, "#deskripsi").click()
    driver.find_element(By.CSS_SELECTOR, "#deskripsi").send_keys(deskripsi)
    print('=')
    Log.info(' Input Deskripsi Behasil ')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tanggalKembali"]')))
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').send_keys(TanggalHarusKembaliInput)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').send_keys(Keys.ENTER)
    print('=')
    Log.info(' Input Tanggal Harus Kembali  ')
    attach(data=driver.get_screenshot_as_png())


    sleep(driver)
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="addPengawal"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="addPengawal"]').click()
    print('=')
    Log.info(' Input tambah pengawal  ')
    attach(data=driver.get_screenshot_as_png())


    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jenis0"]')))
    driver.find_element(By.XPATH, '//*[@id="jenis0"]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Internal\')]").click()
    print('=')
    Log.info(' Input tambah Jenis pengawal  ')
    attach(data=driver.get_screenshot_as_png())


    sleep(driver)
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="pengawalInternal0"]').click
    driver.find_element(By.XPATH, '//*[@id="pengawalInternal0"]').send_keys(PengwalInternalInput)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="optionPengawal00"]')))
    driver.find_element(By.XPATH, '//*[@id="optionPengawal00"]').click()
    print('=')
    Log.info(' Input nama pengawal Internal  ')
    attach(data=driver.get_screenshot_as_png())


    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jenis1"]')))
    driver.find_element(By.XPATH, '//*[@id="jenis1"]').click()
    driver.find_element(By.CSS_SELECTOR, "#Eksternal1").click()
    print('=')
    Log.info(' Input tambah Jenis pengawal  ')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="pengawal1"]').click
    driver.find_element(By.XPATH, '//*[@id="pengawal1"]').send_keys(PengwalExternalInput)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//td[contains(.,'operator')]")))
    time.sleep(0.4)
    driver.find_element(By.XPATH, "//td[contains(.,'operator')]").click()
    print('=')
    Log.info(' Input nama pengawal Enternal  ')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    driver.implicitly_wait(60)
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSubmit"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSubmit"]').click()
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    print('=')
    Log.info(' Menekan Button Submit  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_DLP_009():
    #belum
    sleep(driver)
    print('Mencetak surat')
    Log.info('Mencetak surat data yang berstatus “Dalam Proses” dengan ceklis data yang akan dicetak suratnya pada checkbox lalu klik button Cetak Surat')

@mark.fixture_test()
def test_DLP_010():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-blue-500 .h-5")))
    driver.find_element(By.CSS_SELECTOR, ".text-blue-500 .h-5").click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[1]/div/button')))
    driver.find_element(By.ID, 'backButton').click()
    Log.info('Membuka Halaman Detail  ')
    attach(data=driver.get_screenshot_as_png())

    ########## masuk ke halaman ubah ##########

sheetrangeUbah = wb['DaftarLaluLintas_Edit']

HalUbah = input('')

NamaEditUbah                                    = sheetrangeUbah['B'+str(HalUbah)].value
noSKUbah                                        = sheetrangeUbah['C'+str(HalUbah)].value
JenisKeluarEditUbah                             = sheetrangeUbah['D'+str(HalUbah)].value
TanggalKeluarEditUbah                           = sheetrangeUbah['E'+str(HalUbah)].value
TanggalHarusKembaliEditUbah                     = sheetrangeUbah['F'+str(HalUbah)].value
deskripsiEditUbah                               = sheetrangeUbah['G'+str(HalUbah)].value
PengwalInternalEditUbah                         = sheetrangeUbah['H'+str(HalUbah)].value
PengwalExternalEditUbah                         = sheetrangeUbah['I'+str(HalUbah)].value


@mark.fixture_test()
def test_DLP_011():

    sleep(driver)
    driver.implicitly_wait(10)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="noSK"]')))
    driver.find_element(By.XPATH, '//*[@id="noSK"]').clear()
    driver.find_element(By.XPATH, '//*[@id="noSK"]').send_keys(noSK)
    print('.')
    Log.info('Ubah Deskripsi Berhasil')
    attach(data=driver.get_screenshot_as_png())


    sleep(driver)
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@id=\'fileSK\']/div/button/span").click()
    time.sleep(3)
    pyautogui.write("///////users/will/Downloads/pdf/rere.pdf")
    time.sleep(2)
    pyautogui.press('enter')
    pyautogui.write("///////users/will/Downloads/pdf/rere.pdf")
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.hotkey("backspace")
    pyautogui.write("///////users/will/Downloads/pdf/rere.pdf")
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')

    Log.info('Upload PDF')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="statusPendaftaran"]')))
    driver.find_element(By.XPATH, '//*[@id="statusPendaftaran"]').send_keys("Diizinkan")
    driver.find_element(By.XPATH, "//li[contains(.,\'Diizinkan\')]").click()
    print('=')
    Log.info('ubah status pendaftaran')
    attach(data=driver.get_screenshot_as_png())

# MENEGEDIT DESKRIPSI
@mark.fixture_test()
def test_DLP_012():
    sleep(driver)
    driver.implicitly_wait(10)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="deskripsi"]')))
    driver.find_element(By.XPATH, '//*[@id="deskripsi"]').clear()
    driver.find_element(By.XPATH, '//*[@id="deskripsi"]').send_keys(deskripsiEdit)
    print('.')
    Log.info('Ubah Deskripsi Berhasil')
    attach(data=driver.get_screenshot_as_png())


    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jenisKeluar"]')))
    driver.find_element(By.XPATH, '//*[@id="jenisKeluar"]').click()
    sleep(driver)
    if JenisKeluarEdit == 'Asimilasi':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Asimilasi')
        driver.find_element(By.XPATH, "//li[contains(.,\'Asimilasi\')]").click()
        print('.')
        Log.info(' Input Jenis Keluar Asimilasi  ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluarEdit == 'Pembebasan Bersyarat':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Pembebasan Bersyarat')
        driver.find_element(By.XPATH, "//li[contains(.,\'Pembebasan Bersyarat\')]").click()
        print('.')
        Log.info(' Input Jenis Pembebasan bersyarat ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluarEdit == 'Anak Kembali ke Orang Tua':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Anak Kembali ke Orang Tua')
        driver.find_element(By.XPATH, "//li[contains(.,\'Anak Kembali ke Orang Tua\')]").click()
        print('.')
        Log.info(' Input Jenis Anak Kembali ke Orang Tua ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluarEdit == 'Cuti Bersyarat':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Cuti Bersyarat')
        driver.find_element(By.XPATH, "//li[contains(.,\'Cuti Bersyarat\')]").click()
        print('.')
        Log.info(' Input Jenis Cuti Bersyarat ')
        attach(data=driver.get_screenshot_as_png())


    elif JenisKeluarEdit == 'Asimilasi di Rumah':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Asimilasi di Rumah')
        driver.find_element(By.XPATH, "//li[contains(.,\'Asimilasi di Rumah\')]").click()
        print('.')
        Log.info(' Input Jenis Asimilasi di Rumah ')
        attach(data=driver.get_screenshot_as_png())


    elif JenisKeluarEdit == 'Bebas Biasa':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Bebas Biasa')
        driver.find_element(By.XPATH, "//li[contains(.,\'Bebas Biasa\')]").click()
        print('.')
        Log.info(' Input Jenis Bebas Biasa ')
        attach(data=driver.get_screenshot_as_png())


    elif JenisKeluarEdit == 'Bebas dari Dakwaan':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Bebas dari Dakwaan')
        driver.find_element(By.XPATH, "//li[contains(.,\'Bebas dari Dakwaan\')]").click()
        print('.')
        Log.info(' Input Jenis Bebas dari Dakwaan ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluarEdit == 'Bebas Dari Tuntutan':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Bebas Dari Tuntutan')
        driver.find_element(By.XPATH, "//li[contains(.,\'Bebas Dari Tuntutan\')]").click()
        print('.')
        Log.info(' Input Jenis Bebas Dari Tuntutan ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluarEdit == 'Cuti Menjelang Bebas':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Cuti Menjelang Bebas')
        driver.find_element(By.XPATH, "//li[contains(.,\'Cuti Menjelang Bebas\')]").click()
        print('.')
        Log.info(' Input Jenis Cuti Menjelang Bebas ')
        attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    driver.implicitly_wait(10)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "keluarKeamanan")))
    driver.find_element(By.ID, "keluarKeamanan").clear()
    driver.find_element(By.XPATH, '//*[@id="keluarKeamanan"]').send_keys(TanggalKeluarEdit)
    driver.find_element(By.ID, "keluarKeamanan").send_keys(Keys.ENTER)
    print('.')
    Log.info('Ubah Tanggal Keluar Berhasil')
    attach(data=driver.get_screenshot_as_png())

    # MENGEDIT TANGGAL KEMBALI

    sleep(driver)
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').clear()
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').send_keys(TanggalHarusKembaliEdit)
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').send_keys(Keys.ENTER)
    print('.')
    Log.info('Ubah Tanggal Kembali Berhasil')
    attach(data=driver.get_screenshot_as_png())
    time.sleep(5)

    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSubmit"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSubmit"]').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    Log.info('Button Submit')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_DLP_013():
    #belum
    print('cek halaman paling belakang, sesuaikan dengan jumlah data')

@mark.fixture_test()
def test_DLP014_DLP015():
    sleep(driver)
    # 5 HALAMAN
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'5/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(
        '100')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info('halaman 5')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'10/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(
        '100')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info('halaman 10')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'20/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(
        '100')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info('halaman 20')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
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

    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'100/halaman\')]").click()
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(
        '100')  # Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    Log.info('halaman 100')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_DLP016():

    sleep(driver)
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div[1]/button').click()
    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div[1]/div/div/div/div[2]/div/button[2]').click()
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil mengunduh file\')]')))
    print('.')
    Log.info('Export Excel')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_DLP017():
# Melakukan export data tabel ke pdf
    sleep(driver)
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[5]/div[2]/button').click()
    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[5]/div[2]/div/div/div/div[2]/div/button[2]').click()
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil mengunduh file\')]')))
    print('.')
    Log.info('Export PDF')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_DLP018():
# Melakukan cetak
    sleep(driver)
    time.sleep(1)
    driver.implicitly_wait(30)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="printButton"]').click()
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[5]/div[3]/div/div/div/div[2]/div/button[2]').click()
    print('.')
    Log.info('Cetak')
    attach(data=driver.get_screenshot_as_png())