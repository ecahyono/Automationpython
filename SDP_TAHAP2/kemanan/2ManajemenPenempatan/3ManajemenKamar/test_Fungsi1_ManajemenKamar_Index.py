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
from Settings.login import login, loginOperator

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('1ManajemenKamarIndex.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrangeIndex = wb['ManajemenKamarIndex']
print('.')
print('Mau Baris Ke Berapa ?')
index  = input('')

filterColumnindex                            = sheetrangeIndex['B'+str(index)].value
Namaindex                                    = sheetrangeIndex['C'+str(index)].value
NoRegisindex                                 = sheetrangeIndex['D'+str(index)].value
SemuaIndex                                   = sheetrangeIndex['E'+str(index)].value
StatusIndex                                  = sheetrangeIndex['F'+str(index)].value




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
def test_MKR_001():
    print('.')
    print('Akses halaman Manajemen Kamar (MKR-001)')

    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Daftar Lalu Lintas').click()
    sleep(driver)
    Log.info('(MKR-001) Mengakses halaman Manajemen Kamar dengan memilih modul Keamanan kemudian pilih menu Manajemen Penempatan lalu pilih submenu Manajemen Kamar')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_MKR_002():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button[2]')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button[2]').click()
    sleep(driver)
    Log.info('(MKR_002)Clik Button Keterangan - Menampilkan jumlah data WBP yang bebas berdasarkan waktunya dengan menekan button Keterangan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_MKR_003():
    sleep(driver)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'filterColumn')))
    driver.find_element(By.ID, 'filterColumn').click()
    if filterColumnindex == 'namaIndex':
        driver.find_element(By.ID, 'nama_lengkap').click()
        driver.find_element(By.ID, 'kataKunci').send_keys(Namaindex)
        Log.info('Mencari Berdasarkan Nama')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == 'noregisIndex':
        driver.find_element(By.ID, 'nmr_reg_gol').click()
        driver.find_element(By.ID, 'kataKunci').send_keys(NoRegisindex)
        Log.info('Mencari Berdasarkan No Regis')
        attach(data=driver.get_screenshot_as_png())

    driver.find_element(By.ID, 'statusVerifikasistatusVerifikasi').click()
    if StatusIndex == 'Dalam Proses':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'DalamProses')))
        driver.find_element(By.ID, 'DalamProses').click
        Log.info('Memilih status dalam proses')

    elif StatusIndex == 'Diizinkan':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'Diizinkan')))
        driver.find_element(By.ID, 'Diizinkan').click
        Log.info('Memilih Status Diizinkan')

    elif StatusIndex == 'Perbaikan':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'Perbaikan')))
        driver.find_element(By.ID, 'Perbaikan').click
        Log.info('Memilih Status Perbaikan')

    elif StatusIndex == 'Ditolak':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'Ditolak')))
        driver.find_element(By.ID, 'Ditolak').click
        Log.info('Memilih Status Ditolak')

    elif StatusIndex == 'Semua':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'semuaStatusVerifikasi')))
        driver.find_element(By.ID, 'semuaStatusVerifikasi').click
        Log.info('Memilih Status Semua')

    driver.find_element(By.ID, 'searchButton').click()

    Log.info('(MKR_003) Search data - Melakukan pengecekan filtering data dengan menginputkan kata kunci dan memilih kategori pada halaman Manajemen Kamar lalu klik button cari')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_MKR_004():
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.ID, 'createButton').click()
    Log.info('(MKR_004)Click button create - Mengakses halaman Cari Identitas WBP yang akan dimutasi dengan menekan button Tambah Mutasi Blok/Kamar pada halaman Manajemen Kamar')




                                            ########## HALAMAN CARI ##########

sheetrangeCari = wb['ManajemenKamarCari']
print('.')
print('Halaman cari, Mau Baris Ke Berapa ?')
cari  = input('')

filterColumnCari                            = sheetrangeCari['B'+str(cari)].value
NamaCari                                    = sheetrangeCari['C'+str(cari)].value
NoRegisCari                                 = sheetrangeCari['D'+str(cari)].value
JenisKejahatanCari                          = sheetrangeCari['E'+str(cari)].value

@mark.fixture_test()
def test_MKR_005():
    sleep(driver)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'filterColumn')))
    driver.find_element(By.ID, 'filterColumn').click()
    if filterColumnCari == 'namaCari':
        driver.find_element(By.ID, 'nama_lengkap').click()
        driver.find_element(By.ID, 'kataKunci').send_keys(NamaCari)
        Log.info('Mencari Berdasarkan Nama')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnCari == 'noregisIndex':
        driver.find_element(By.ID, 'nmr_reg_gol').click()
        driver.find_element(By.ID, 'kataKunci').send_keys(NoRegisCari)
        Log.info('Mencari Berdasarkan No Regis')
        attach(data=driver.get_screenshot_as_png())

    driver.find_element(By.ID, 'searchButton').click()
    Log.info('(MKR_004) Search Identitas - Melakukan pencarian identitas WBP yang akan dimutasi di halaman Cari Identitas dengan memilih kategori pencarian dan menginputkan kata kunci lalu klik button Cari. Jika ingin Kembali ke halaman sebelumnya, klik button Kembali')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_MKR_006():
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.ID,'mutasi-0').click()


@mark.fixture_test()
def test_MKR_007():
    attach(data=driver.get_screenshot_as_png())

    Log.info('Memilih Blok & Kamar untuk WBP yang bisa dilakukan dengan 2 cara, ')



    Log.info(' Cara 1 : menekan button Denah Blok & Kamar lalu memilih Blok pada pop up kemudian pilih Lantai dan pilih Kamar kemudian klik button Simpan ')


    Log.info('2: pilih Blok dan Kamar pada dropdown di form Catat Penempatan Kamar')

@mark.fixture_test()
def test_MKR_008():
    Log.info('Menginputkan data tanggal dan alasan mutasi pada form Catat Mutasi Kamar lalu klik button simpan untuk menyimpan data Mutasi Kamar ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_MKR_009():
    Log.info('Menampilkan detail data Penghuni dengan menggunakan button (Detail) pada kolom aksi di tabel data Penghuni pada halaman Manajemen Kamar. Jika ingin Kembali ke halaman sebelumnya, klik button Kembali')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_MKR_010():
    Log.info('Mengubah data Penghuni dengan menggunakan button (Update) pada kolom aksi di tabel halaman Manajemen Kamar kemudian ubah data di form dan klik button simpan. Jika ingin Kembali ke halaman sebelumnya, klik button Kembali')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_MKR_011():
    Log.info('Mencetak sterek dengan menekan Button Cetak Sterek')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_MKR_012():
    Log.info('Menampilkan dropdown jumlah data yang dipilih oleh pengguna dan ditampilkan pada main grid')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_MKR_013():
    Log.info('Menampilkan jumlah data yang sesuai dengan total halaman yang dipilih')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_MKR_014():
    Log.info('Menampilkan halaman sebelumnya dan selanjutnya menggunakan navigasi button ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_MKR_015():
    Log.info('Mencetak data penghuni (sesuai dengan jumlah halaman) dengan menekan Button Export Excel')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_MKR_016():
    Log.info('Mencetak data penghuni (sesuai dengan jumlah halaman) dengan menekan Button Export PDF')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_MKR_017():
    Log.info('Mencetak data penghuni (sesuai dengan jumlah halaman) yang terhubung langsung dengan perangkat tambahan (printer)')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_exit():
    quit(driver)
    attach(data=driver.get_screenshot_as_png())