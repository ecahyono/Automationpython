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
import pyautogui

import sys
from os import environ, path
from dotenv import load_dotenv
load_dotenv()
from openpyxl import load_workbook

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR"))
    wb = load_workbook(environ.get("KeamananUAT"))

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))


from Settings.setup import initDriver, loadDataPath, quit, buttonTambah, buttonSubmit, selectKategoriPegawai, selectKategoriTamuDinas, sleep
from Settings.login import login, loginSPV

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('ManajemenBlokDanKamar_UAT.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


sheetrange = wb['tambahBlokdanKamar']
print('.')
print('Mau Baris Ke Berapa ?')
index  = input("")

#HalamanIndex
filterColumnIndex                             = sheetrange['A'+str(index)].value
statusKapasitasFormIndex                      = sheetrange['B'+str(index)].value

#tambahBlok
namablokTambah                                = sheetrange['C'+str(index)].value
tipeblokTambah                                = sheetrange['D'+str(index)].value
jeniskelaminTambah                            = sheetrange['E'+str(index)].value
jenisKejahatanTambah                          = sheetrange['F'+str(index)].value
jumlahLantaiTambah                            = sheetrange['G'+str(index)].value
formatPenomoranKamarTambah                    = sheetrange['H'+str(index)].value
kelUsiaTambah                                 = sheetrange['I'+str(index)].value
jumlahKamarPerlantaiTambah                    = sheetrange['J'+str(index)].value
noKamarAwalTambah                             = sheetrange['K'+str(index)].value
noKamarAkhirTambah                            = sheetrange['L'+str(index)].value

#tambahKamar
nomorKamarTambah                              = sheetrange['M'+str(index)].value
kelompokJenisKejahatanTambah                  = sheetrange['N'+str(index)].value
kapasitasInputTambah                          = sheetrange['O'+str(index)].value
kondisiRuanganTambah                          = sheetrange['P'+str(index)].value
lamaHuniTambah                                = sheetrange['Q'+str(index)].value


@mark.fixture_test()
def test_MBK_001():
    print(' == NEXT == Login Sebagai OPERATOR UPT')
    global driver, pathData
    sleep(driver)
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Login')

    login(driver)
    Log.info('Login')
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['ManajemenPenempatan']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Manajemen Blok dan Kamar').click()
    Log.info('akses menu Manajemen Blok Dan Kamar')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_MBK_002():
    print('== NEXT == MBK-002 / melakukan filtering data')
    sleep(driver)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.ID, 'kataKunci').click
    driver.find_element(By.ID, 'kataKunci').send_keys(filterColumnIndex)
    driver.find_element(By.ID, 'searchButton').click
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    Log.info('Berhasil menampilkan data blok berdasarkan kata kunci yang diinputkan di halaman Pemetaan Blok & Kamar')
    attach(data=driver.get_screenshot_as_png())
    
    #Melakukan pengecekan filtering data


@mark.fixture_test()
def test_MBK_003():
    print('== NEXT == MBK-003 / melakukan filtering data')
    
    driver.find_element(By.ID, 'statusKapasitasForm').click()
    sleep(driver)
    if statusKapasitasFormIndex == 'semua':
        sleep(driver)
        driver.find_element(By.XPATH, "//li[contains(.,\'Semua\')]").click()

    elif statusKapasitasFormIndex == 'kosong':
        sleep(driver)
        driver.find_element(By.XPATH, "//li[contains(.,\'Kosong\')]").click()

    elif statusKapasitasFormIndex == 'terisi':
        sleep(driver)
        driver.find_element(By.XPATH, "//li[contains(.,\'Terisi\')]").click()

    elif statusKapasitasFormIndex == 'penuh':
        sleep(driver)
        driver.find_element(By.XPATH, "//li[contains(.,\'Penuh\')]").click()
    
    elif statusKapasitasFormIndex == 'overcapacity':
        sleep(driver)
        driver.find_element(By.XPATH, "//li[contains(.,\'Overcapacity\')]").click()
    Log.info('Berhasil menampilkan data berdasarkan kategori kapasitas yang dipilih pada dropdown di halaman Pemetaan Blok & Kamar')
    attach(data=driver.get_screenshot_as_png())

    #Melakukan pengecekan filtering data

@mark.fixture_test()
def test_MBK_004():
    print('== NEXT == MBK-004 / Melakukan pengecekan filtering daftar kamar berdasarkan lantai')
    
    #Melakukan pengecekan filtering daftar kamar berdasarkan lantai
    
@mark.fixture_test()
def test_MBK_005():
    print('== NEXT == MBK-005 / Melakukan pengecekan data kapasitas dan jumlah yang telah terisi dari kamar yang dipilih dengan klik salah satu nomor kamar')

    #Pengecekan kapasitas kamar dan jumlah yang telah terisi

@mark.fixture_test()
def test_MBK_006():
    print('== NEXT == MBK-006 / Mengakses halaman Manajemen Blok dan Kamar dengan menekan button Tambah Blok dan Kamar')
    sleep(driver)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.border:nth-child(1)')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    Log.info('Click Button Tambah halaman Pemetaan Block')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_MBK_007():
    print('== NEXT == MBK_008 / Menambahkan data kamar dengan menginputkan data kamar pada form tambah kamar kemudian klik button Simpan ke Daftar Kamar')
    
    print('== NEXT == / clik create button')
    sleep(driver)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, 'createButton').click()
    Log.info('Click Button Tambah Master Blok Dan Kamar')
    attach(data=driver.get_screenshot_as_png())

    print('== NEXT == / input nama blok')
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'blok')))
    driver.find_element(By.ID, 'blok').send_keys(namablokTambah)
    Log.info('Input Nama Blok')
    attach(data=driver.get_screenshot_as_png())

    print('== NEXT == / input tipe blok')
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'tipe_id')))
    driver.find_element(By.ID, 'tipe_id').click()

    if tipeblokTambah == 'Umum':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Umum\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Umum\')]").click()
        Log.info('Input Tipe Blok Umum')
        attach(data=driver.get_screenshot_as_png())

    elif tipeblokTambah == 'Tutup Sunyi':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Tutup Sunyi\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Tutup Sunyi\')]").click()
        Log.info('Input Tipe Blok Tutup Sunyi')
        attach(data=driver.get_screenshot_as_png())

    elif tipeblokTambah == 'Mapenaling':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Mapenaling\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Mapenaling\')]").click()
        Log.info('Input Tipe Blok Umum')
        attach(data=driver.get_screenshot_as_png())

    elif tipeblokTambah == 'Isolasi':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Isolasi\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Isolasi\')]").click()
        Log.info('Input Tipe Blok Umum')
        attach(data=driver.get_screenshot_as_png())

    print('== NEXT == / input jenis kelamin')
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'kel_jenis_kelamin_id')))
    driver.find_element(By.ID, "kel_jenis_kelamin_id").click()
    if jeniskelaminTambah == 'Laki-laki':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Laki-laki\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Laki-laki\')]").click()

        Log.info('Input Blok Untuk Jenis Kelamin Laki Laki')
        attach(data=driver.get_screenshot_as_png())

    elif jeniskelaminTambah == 'Perempuan':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Perempuan\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Perempuan\')]").click()

        Log.info('Input Blok Untuk Jenis Kelamin Perempuan')
        attach(data=driver.get_screenshot_as_png())


    print('== NEXT == / input jenis kejahatan')
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'jenis_kejahatan_values')))
    driver.find_element(By.ID, "jenis_kejahatan_values").click()
    if jenisKejahatanTambah == 'Korupsi Teroris Kriminal':
        driver.find_element(By.XPATH, "//li[contains(.,\'Korupsi\')]").click()
        driver.find_element(By.XPATH, "//li[contains(.,\'Teroris\')]").click()
        driver.find_element(By.XPATH, "//li[contains(.,\'Kriminal Umum\')]").click()
        time.sleep(1)
        driver.find_element(By.ID, "jenis_kejahatan_values").send_keys(Keys.TAB)
        Log.info('Input untuk Jenis kejahatan Teroris, Kriminal, Korupsi')
        attach(data=driver.get_screenshot_as_png())

    elif jenisKejahatanTambah == 'Korupsi':
        driver.find_element(By.XPATH, "//li[contains(.,\'Korupsi\')]").click()
        time.sleep(1)
        driver.find_element(By.ID, "jenis_kejahatan_values").send_keys(Keys.TAB)
        Log.info('Input untuk Jenis kejahatan Korupsi')
        attach(data=driver.get_screenshot_as_png())

    elif jenisKejahatanTambah == 'Teroris':
        driver.find_element(By.XPATH, "//li[contains(.,\'Teroris\')]").click()
        time.sleep(1)
        driver.find_element(By.ID, "jenis_kejahatan_values").send_keys(Keys.TAB)
        Log.info('Input untuk Jenis kejahatan Teroris')
        attach(data=driver.get_screenshot_as_png())

    elif jenisKejahatanTambah == 'Kriminal':
        driver.find_element(By.XPATH, "//li[contains(.,\'Kriminal\')]").click()
        time.sleep(1)
        driver.find_element(By.ID, "jenis_kejahatan_values").send_keys(Keys.TAB)
        Log.info('Input untuk Jenis kejahatan Kriminal')
        attach(data=driver.get_screenshot_as_png())

    elif jenisKejahatanTambah == 'Korupsi Teroris':
        driver.find_element(By.XPATH, "//li[contains(.,\'Korupsi\')]").click()
        driver.find_element(By.XPATH, "//li[contains(.,\'Teroris\')]").click()
        time.sleep(1)
        driver.find_element(By.ID, "jenis_kejahatan_values").send_keys(Keys.TAB)
        Log.info('Input untuk Jenis kejahatan Korupsi,Teroris')
        attach(data=driver.get_screenshot_as_png())

    elif jenisKejahatanTambah == 'Teroris Kriminal':
        driver.find_element(By.XPATH, "//li[contains(.,\'Teroris\')]").click()
        driver.find_element(By.XPATH, "//li[contains(.,\'Kriminal Umum\')]").click()
        time.sleep(1)
        driver.find_element(By.ID, "jenis_kejahatan_values").send_keys(Keys.TAB)
        Log.info('Input untuk Jenis kejahatan Teroris, Kriminal')
        attach(data=driver.get_screenshot_as_png())

    print('== NEXT == / masukan jumlah lantai')
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "Masukkan Jumlah Lantai"]')))
    driver.find_element(By.XPATH, '// *[ @ id = "Masukkan Jumlah Lantai"]').send_keys(jumlahLantaiTambah)
    Log.info('input jumlah lantai')
    attach(data=driver.get_screenshot_as_png())

    print('== NEXT == / penomoran kamar')
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'penomoran_kamar')))
    driver.find_element(By.ID, "penomoran_kamar").click()
    if formatPenomoranKamarTambah == 'Angka 8 mulai kiri atas':
        driver.find_element(By.XPATH, "//li[contains(.,\'Angka 8 (mulai kiri atas)\')]").click()
        Log.info('Input Format Penomoran Kamar')
        attach(data=driver.get_screenshot_as_png())

    elif formatPenomoranKamarTambah == '8 mulai kiri bawah':
        driver.find_element(By.XPATH, "//li[contains(.,\'Angka 8 (mulai kiri bawah)\')]").click()
        Log.info('Input Format Penomoran Kamar 8 mulai kiri bawah')
        attach(data=driver.get_screenshot_as_png())

    elif formatPenomoranKamarTambah == '8 mulai kanan bawah':
        driver.find_element(By.XPATH, "//li[contains(.,\'Angka 8 (mulai kanan bawah)\')]").click()
        Log.info('Input Format Penomoran Kamar Angka 8 mulai kanan bawah')
        attach(data=driver.get_screenshot_as_png())

    elif formatPenomoranKamarTambah == 'Ke Depan 1 arah':
        driver.find_element(By.XPATH, "//li[contains(.,\'Belakang Ke Depan (1 arah)\')]").click()
        Log.info('Input Format Penomoran Kamar Belakang Ke Depan 1 arah')
        attach(data=driver.get_screenshot_as_png())

    elif formatPenomoranKamarTambah ==  'Ke Depan 2 arah':
        driver.find_element(By.XPATH, "//li[contains(.,\'Belakang Ke Depan (2 arah)\')]").click()
        Log.info('Input Format Penomoran Kamar Belakang Ke Depan 2 arah')
        attach(data=driver.get_screenshot_as_png())

    elif formatPenomoranKamarTambah == 'Depan Ke Belakang 1 arah':
        driver.find_element(By.XPATH, "//li[contains(.,\'Depan Ke Belakang (1 arah)\')]").click()
        Log.info('Input Format Penomoran Kamar Depan Ke Belakang 1 arah')
        attach(data=driver.get_screenshot_as_png())

    elif formatPenomoranKamarTambah == 'Depan Ke Belakang 2 arah':
        driver.find_element(By.XPATH, "//li[contains(.,\'Depan Ke Belakang (2 arah)\')]").click()
        Log.info('Input Format Penomoran Kamar Depan Ke Belakang 2 arah')
        attach(data=driver.get_screenshot_as_png())

    elif formatPenomoranKamarTambah == 'Kanan Kiri 1 arah':
        driver.find_element(By.XPATH, "//li[contains(.,\'Kanan Kiri (1 arah)\')]").click()
        Log.info('Input Format Penomoran Kamar Kanan Kiri 1 arah')
        attach(data=driver.get_screenshot_as_png())
    Log.info('input penomoran kamar')



    print('== NEXT == / kelompok usia')
    sleep(driver)
    driver.find_element(By.ID, "kel_usia_id").click()
    if kelUsiaTambah == 'Dewasa':
        driver.find_element(By.XPATH, "//li[contains(.,\'Dewasa')]").click()
        Log.info('memilih kelompok usia Dewasa')
        attach(data=driver.get_screenshot_as_png())

    elif kelUsiaTambah == 'Lansia':
        driver.find_element(By.XPATH, "//li[contains(.,\'Lansia')]").click()
        Log.info('memilih kelompok usia Dewasa')
        attach(data=driver.get_screenshot_as_png())

    elif kelUsiaTambah == 'Anak-anak':
        driver.find_element(By.XPATH, "//li[contains(.,\'Anak-anak')]").click()
        Log.info('memilih kelompok usia Anak Anak')
        attach(data=driver.get_screenshot_as_png())


    print('== NEXT == / input jumlah kamar per lantai')
    sleep(driver)
    driver.find_element(By.ID, "jumlah_kamar_per_lantai-0").click()

    if jumlahLantaiTambah == 1:
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-0").send_keys(jumlahKamarPerlantaiTambah)
        attach(data=driver.get_screenshot_as_png())

    elif jumlahLantaiTambah == 2:
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-0").click()
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-0").send_keys(jumlahKamarPerlantaiTambah)
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-1").click()
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-1").send_keys(jumlahKamarPerlantaiTambah)
        attach(data=driver.get_screenshot_as_png())

    elif jumlahLantaiTambah == 3:
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-0").click()
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-0").send_keys(jumlahKamarPerlantaiTambah)
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-1").click()
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-1").send_keys(jumlahKamarPerlantaiTambah)
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-2").click()
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-2").send_keys(jumlahKamarPerlantaiTambah)
        attach(data=driver.get_screenshot_as_png())

    elif jumlahLantaiTambah == 4:
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-0").click()
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-0").send_keys(jumlahKamarPerlantaiTambah)
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-1").click()
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-1").send_keys(jumlahKamarPerlantaiTambah)
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-2").click()
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-2").send_keys(jumlahKamarPerlantaiTambah)
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-3").click()
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-3").send_keys(jumlahKamarPerlantaiTambah)
        attach(data=driver.get_screenshot_as_png())

    Log.info('Input Jumlah Kamar perlantai')
    attach(data=driver.get_screenshot_as_png())



    print('== NEXT == /  nokamar awal dan akhir')
    sleep(driver)
    if jumlahLantaiTambah == 1:
        driver.find_element(By.ID, "noKamarAwal-0").click()
        driver.find_element(By.ID, "noKamarAwal-0").send_keys(noKamarAwalTambah)
        driver.find_element(By.ID, "noKamarAkhir-0").click()
        driver.find_element(By.ID, "noKamarAkhir-0").send_keys(noKamarAkhirTambah)

    elif jumlahLantaiTambah ==2:
        driver.find_element(By.ID, "noKamarAwal-0").click()
        driver.find_element(By.ID, "noKamarAwal-0").send_keys(noKamarAwalTambah)
        driver.find_element(By.ID, "noKamarAkhir-0").click()
        driver.find_element(By.ID, "noKamarAkhir-0").send_keys(noKamarAkhirTambah)

        driver.find_element(By.ID, "noKamarAwal-1").click()
        driver.find_element(By.ID, "noKamarAwal-1").send_keys(noKamarAwalTambah)
        driver.find_element(By.ID, "noKamarAkhir-1").click()
        driver.find_element(By.ID, "noKamarAkhir-1").send_keys(noKamarAkhirTambah)

    elif jumlahLantaiTambah == 3:
        driver.find_element(By.ID, "noKamarAwal-0").click()
        driver.find_element(By.ID, "noKamarAwal-0").send_keys(noKamarAwalTambah)
        driver.find_element(By.ID, "noKamarAkhir-0").click()
        driver.find_element(By.ID, "noKamarAkhir-0").send_keys(noKamarAkhirTambah)

        driver.find_element(By.ID, "noKamarAwal-1").click()
        driver.find_element(By.ID, "noKamarAwal-1").send_keys(noKamarAwalTambah)
        driver.find_element(By.ID, "noKamarAkhir-1").click()
        driver.find_element(By.ID, "noKamarAkhir-1").send_keys(noKamarAkhirTambah)

        driver.find_element(By.ID, "noKamarAwal-2").click()
        driver.find_element(By.ID, "noKamarAwal-2").send_keys(noKamarAwalTambah)
        driver.find_element(By.ID, "noKamarAkhir-2").click()
        driver.find_element(By.ID, "noKamarAkhir-2").send_keys(noKamarAkhirTambah)

    elif jumlahLantaiTambah == 4:
        driver.find_element(By.ID, "noKamarAwal-0").click()
        driver.find_element(By.ID, "noKamarAwal-0").send_keys(noKamarAwalTambah)
        driver.find_element(By.ID, "noKamarAkhir-0").click()
        driver.find_element(By.ID, "noKamarAkhir-0").send_keys(noKamarAkhirTambah)

        driver.find_element(By.ID, "noKamarAwal-1").click()
        driver.find_element(By.ID, "noKamarAwal-1").send_keys(noKamarAwalTambah)
        driver.find_element(By.ID, "noKamarAkhir-1").click()
        driver.find_element(By.ID, "noKamarAkhir-1").send_keys(noKamarAkhirTambah)

        driver.find_element(By.ID, "noKamarAwal-2").click()
        driver.find_element(By.ID, "noKamarAwal-2").send_keys(noKamarAwalTambah)
        driver.find_element(By.ID, "noKamarAkhir-2").click()
        driver.find_element(By.ID, "noKamarAkhir-2").send_keys(noKamarAkhirTambah)

        driver.find_element(By.ID, "noKamarAwal-3").click()
        driver.find_element(By.ID, "noKamarAwal-3").send_keys(noKamarAwalTambah)
        driver.find_element(By.ID, "noKamarAkhir-3").click()
        driver.find_element(By.ID, "noKamarAkhir-3").send_keys(noKamarAkhirTambah)



    Log.info('Input koridor')
    attach(data=driver.get_screenshot_as_png())


    driver.implicitly_wait(30)
    print('== NEXT == / click submit button')
    sleep(driver)
    driver.find_element(By.ID, "submitButton").click()
    #WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    Log.info('Submit data blok ')
    attach(data=driver.get_screenshot_as_png())

    ################################### kamar ###################################

@mark.fixture_test()
def test_MBK_008():

    print('== NEXT == /  Menambahkan data kamar dengan menginputkan data kamar pada form tambah kamar kemudian klik button Simpan ke Daftar Kamar')
    sleep(driver)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "app"] / div / div[2] / div[1] / div[2] / div[2] / div / div[5] / div / span[3] / div / input')))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'lantai_id')))
    driver.find_element(By.ID, 'lantai_id').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'lantai-0')))
    driver.find_element(By.ID, "lantai-0").click()
    Log.info('Pilih Lantai yang akan di inputkan')
    attach(data=driver.get_screenshot_as_png())

    print('== NEXT == /  input nomor kamar')
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'nomorKamar')))
    driver.find_element(By.ID, "nomorKamar").send_keys(nomorKamarTambah)
    Log.info('Input Nomor Kamar')
    attach(data=driver.get_screenshot_as_png())


    print('== NEXT == /  peruntukan kelompok usia')
    sleep(driver)
    driver.find_element(By.ID, "kel_usia_id").click()
    if kelUsiaTambah == 'Dewasa':
        driver.find_element(By.XPATH, "//li[contains(.,\'Dewasa')]").click()
        Log.info('memilih kelompok usia Dewasa')
        attach(data=driver.get_screenshot_as_png())

    elif kelUsiaTambah == 'Lansia':
        driver.find_element(By.XPATH, "//li[contains(.,\'Lansia')]").click()
        Log.info('memilih kelompok usia Dewasa')
        attach(data=driver.get_screenshot_as_png())

    elif kelUsiaTambah == 'Anak-anak':
        driver.find_element(By.XPATH, "//li[contains(.,\'Anak-anak')]").click()
        Log.info('memilih kelompok usia Anak Anak')
        attach(data=driver.get_screenshot_as_png())

    print('== NEXT == /  kelompok jenis kelamin')
    sleep(driver)
    driver.find_element(By.ID, "kel_jenis_kelamin_id").click()
    if jeniskelaminTambah == 'Laki-laki':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Laki-laki\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Laki-laki\')]").click()

        Log.info('Input Blok Untuk Jenis Kelamin Laki Laki')
        attach(data=driver.get_screenshot_as_png())

    elif jeniskelaminTambah == 'Perempuan':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Perempuan\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Perempuan\')]").click()

        Log.info('Input Blok Untuk Jenis Kelamin Perempuan')
        attach(data=driver.get_screenshot_as_png())


    print('== NEXT == / input tipe kamar')
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'tipe_id')))
    driver.find_element(By.ID, 'tipe_id').click()

    if tipeblokTambah == 'Umum':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Umum\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Umum\')]").click()
        Log.info('Input Tipe Blok Umum')
        attach(data=driver.get_screenshot_as_png())

    elif tipeblokTambah == 'Tutup Sunyi':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Tutup Sunyi\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Tutup Sunyi\')]").click()
        Log.info('Input Tipe Blok Tutup Sunyi')
        attach(data=driver.get_screenshot_as_png())

    elif tipeblokTambah == 'Mapenaling':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Mapenaling\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Mapenaling\')]").click()
        Log.info('Input Tipe Blok Umum')
        attach(data=driver.get_screenshot_as_png())

    elif tipeblokTambah == 'Isolasi':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Isolasi\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Isolasi\')]").click()
        Log.info('Input Tipe Blok Umum')
        attach(data=driver.get_screenshot_as_png())


    driver.find_element(By.ID, 'kel_jenis_kejahatan_id').click()
    if kelompokJenisKejahatanTambah == 'Teroris':
        driver.find_element(By.XPATH, "//li[contains(.,\'Teroris\')]").click()
        Log.info('Input untuk Jenis kejahatan Teroris')
        attach(data=driver.get_screenshot_as_png())

    elif kelompokJenisKejahatanTambah == 'Korupsi':
        driver.find_element(By.XPATH, "//li[contains(.,\'Korupsi\')]").click()
        Log.info('Input untuk Jenis kejahatan Korupsi')
        attach(data=driver.get_screenshot_as_png())

    elif kelompokJenisKejahatanTambah == 'Kriminal':
        driver.find_element(By.XPATH, "//li[contains(.,\'Kriminal\')]").click()
        driver.find_element(By.ID, "jenis_kejahatan_values").send_keys(Keys.TAB)
        Log.info('Input untuk Jenis kejahatan Kriminal')
        attach(data=driver.get_screenshot_as_png())


    print('== NEXT == / input kapasitas input')
    sleep(driver)

    driver.find_element(By.CSS_SELECTOR, ".el-input:nth-child(3) > .el-input__inner").send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, "//div[@id=\'kapasitasInput\']/div/input").send_keys(kapasitasInputTambah)
    Log.info('Input Kapasitas Ruangan')
    attach(data=driver.get_screenshot_as_png())

    print('== NEXT == / input kondisi input')
    sleep(driver)

    driver.find_element(By.ID, 'kondisiInput').click()
    if kondisiRuanganTambah == 'Baik':
        driver.find_element(By.XPATH, "//li[contains(.,\'Baik\')]").click()
        Log.info('Kondisi Ruangan Baik')
        attach(data=driver.get_screenshot_as_png())

    elif kondisiRuanganTambah == 'Rusak':
        driver.find_element(By.XPATH, "//li[contains(.,\'Baik\')]").click()
        Log.info('Kondisi Ruangan Rusak')
        attach(data=driver.get_screenshot_as_png())


    print('== NEXT == / input lama huni')
    sleep(driver)
    driver.find_element(By.ID, 'lamaHuni').send_keys(lamaHuniTambah)
    Log.info('Lama Huni')
    attach(data=driver.get_screenshot_as_png())


    print('== NEXT == / submit button')
    sleep(driver)
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    Log.info('Submit')
    attach(data=driver.get_screenshot_as_png())
    #MASIH BELUM SELESAI



@mark.fixture_test()
def test_MBK_010():
    
    print('== NEXT == MBK-010 / Menambahkan data blok dan lantai dengan menggunakan button tambah lalu menginputkan data blok dan lantai kemudian klik button simpan')

@mark.fixture_test()
def test_MBK_011():
    print('== NEXT ==')
    #Mengubah data Blok dan Kamar dengan menggunakan button (Update) pada kolom aksi di tabel kemudian ubah data di form dan klik button ubah

@mark.fixture_test()
def test_MBK_012():
    print('== NEXT ==')
    #Pengecekan verifikasi data blok dan kamar oleh supervisor

@mark.fixture_test()
def test_MBK_013():
    print('== NEXT ==')
    #Pengecekan jumlah data per-halaman

@mark.fixture_test()
def test_MBK_014():
    print('== NEXT ==')
    #Pengecekan jumlah data per-halaman

@mark.fixture_test()
def test_MBK_015():
    print('== NEXT ==')
    #Pengecekan navigasi button halaman

@mark.fixture_test()
def test_MBK_016():
    print('== NEXT ==')
    #Pengecekan cetak blok dan kamar dengan format Excel

@mark.fixture_test()
def test_MBK_017():
    print('== NEXT ==')
    #Pengecekan cetak data blok dan kamar dengan format PDF

@mark.fixture_test()
def test_MBK_018():
    print('== NEXT ==')
    #Pengecekan print / cetak data blok dan kamar