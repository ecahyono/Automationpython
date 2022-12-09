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
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('tambahBlokdanKamar.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrange = wb['tambahBlokdanKamar']
print('.')
print('Mau Baris Ke Berapa ?')
xr = input('')
i  = xr

filterColumn                            = sheetrange['B'+str(i)].value
namablok                                = sheetrange['C'+str(i)].value
tipeblok                                = sheetrange['D'+str(i)].value
jeniskelamin                            = sheetrange['E'+str(i)].value
jenisKejahatan                          = sheetrange['F'+str(i)].value
jumlahLantai                            = sheetrange['G'+str(i)].value
formatPenomoranKamar                    = sheetrange['H'+str(i)].value
kelUsia                                 = sheetrange['I'+str(i)].value
jumlahKamarPerlantai                    = sheetrange['J'+str(i)].value
noKamarAwal                             = sheetrange['K'+str(i)].value
noKamarAkhir                            = sheetrange['L'+str(i)].value

nomorKamar                              = sheetrange['M'+str(i)].value
kelompokJenisKejahatan                  = sheetrange['N'+str(i)].value
kapasitasInput                          = sheetrange['O'+str(i)].value
kondisiRuangan                          = sheetrange['P'+str(i)].value
lamaHuni                                = sheetrange['Q'+str(i)].value





@mark.fixture_test()
def test_1_SetupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Login')


@mark.fixture_test()
def test_2_Login():
    login(driver)
    Log.info('Login')

@mark.fixture_test()
def test_3_AksesMenu_ManajemenBlokDanKamar():
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['ManajemenPenempatan']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Manajemen Blok dan Kamar').click()
    print('.')
    Log.info('Manajemen Blok Dan Kamar')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_4_ClickButtonTambah_PemetaanBlock():
    driver.implicitly_wait(30)
    #sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.border:nth-child(1)')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    print('.')
    Log.info('Click Button Tambah halaman Pemetaan Block')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_ClickButtonTambah_MasterBlokDanKamar():
    driver.implicitly_wait(30)
    #sleep(driver)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, 'createButton').click()
    print('.')
    Log.info('Click Button Tambah Master Blok Dan Kamar')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_6_InputNamaBlok():
    driver.implicitly_wait(30)
    #sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'blok')))
    driver.find_element(By.ID, 'blok').send_keys(namablok)
    Log.info('Input Nama Blok')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_7_InputTipeBlok():
    driver.implicitly_wait(30)
    #sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'tipe_id')))
    driver.find_element(By.ID, 'tipe_id').click()

    if tipeblok == 'Umum':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Umum\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Umum\')]").click()
        Log.info('Input Tipe Blok Umum')
        attach(data=driver.get_screenshot_as_png())

    elif tipeblok == 'Tutup Sunyi':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Tutup Sunyi\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Tutup Sunyi\')]").click()
        Log.info('Input Tipe Blok Tutup Sunyi')
        attach(data=driver.get_screenshot_as_png())

    elif tipeblok == 'Mapenaling':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Mapenaling\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Mapenaling\')]").click()
        Log.info('Input Tipe Blok Umum')
        attach(data=driver.get_screenshot_as_png())

    elif tipeblok == 'Isolasi':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Isolasi\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Isolasi\')]").click()
        Log.info('Input Tipe Blok Umum')
        attach(data=driver.get_screenshot_as_png())



@mark.fixture_test()
def test_8_JenisKelaminBlok():
    driver.implicitly_wait(30)
    #sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'kel_jenis_kelamin_id')))
    driver.find_element(By.ID, "kel_jenis_kelamin_id").click()
    if jeniskelamin == 'Laki-laki':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Laki-laki\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Laki-laki\')]").click()

        Log.info('Input Blok Untuk Jenis Kelamin Laki Laki')
        attach(data=driver.get_screenshot_as_png())

    elif jeniskelamin == 'Perempuan':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Perempuan\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Perempuan\')]").click()

        Log.info('Input Blok Untuk Jenis Kelamin Perempuan')
        attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_9_JenisKejahatan():
    driver.implicitly_wait(30)
    #sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'jenis_kejahatan_values')))
    driver.find_element(By.ID, "jenis_kejahatan_values").click()
    if jenisKejahatan == 'Korupsi Teroris Kriminal':
        driver.find_element(By.XPATH, "//li[contains(.,\'Korupsi\')]").click()
        driver.find_element(By.XPATH, "//li[contains(.,\'Teroris\')]").click()
        driver.find_element(By.XPATH, "//li[contains(.,\'Kriminal Umum\')]").click()
        time.sleep(1)
        driver.find_element(By.ID, "jenis_kejahatan_values").send_keys(Keys.TAB)
        Log.info('Input unutk Jenis kejahatan Teroris, Kriminal, Korupsi')
        attach(data=driver.get_screenshot_as_png())

    elif jenisKejahatan == 'Korupsi':
        driver.find_element(By.XPATH, "//li[contains(.,\'Korupsi\')]").click()
        time.sleep(1)
        driver.find_element(By.ID, "jenis_kejahatan_values").send_keys(Keys.TAB)
        Log.info('Input unutk Jenis kejahatan Korupsi')
        attach(data=driver.get_screenshot_as_png())

    elif jenisKejahatan == 'Teroris':
        driver.find_element(By.XPATH, "//li[contains(.,\'Teroris\')]").click()
        time.sleep(1)
        driver.find_element(By.ID, "jenis_kejahatan_values").send_keys(Keys.TAB)
        Log.info('Input unutk Jenis kejahatan Teroris')
        attach(data=driver.get_screenshot_as_png())

    elif jenisKejahatan == 'Kriminal':
        driver.find_element(By.XPATH, "//li[contains(.,\'Kriminal\')]").click()
        time.sleep(1)
        driver.find_element(By.ID, "jenis_kejahatan_values").send_keys(Keys.TAB)
        Log.info('Input unutk Jenis kejahatan Kriminal')
        attach(data=driver.get_screenshot_as_png())

    elif jenisKejahatan == 'Korupsi Teroris':
        driver.find_element(By.XPATH, "//li[contains(.,\'Korupsi\')]").click()
        driver.find_element(By.XPATH, "//li[contains(.,\'Teroris\')]").click()
        time.sleep(1)
        driver.find_element(By.ID, "jenis_kejahatan_values").send_keys(Keys.TAB)
        Log.info('Input unutk Jenis kejahatan Korupsi,Teroris')
        attach(data=driver.get_screenshot_as_png())

    elif jenisKejahatan == 'Teroris Kriminal':
        driver.find_element(By.XPATH, "//li[contains(.,\'Teroris\')]").click()
        driver.find_element(By.XPATH, "//li[contains(.,\'Kriminal Umum\')]").click()
        time.sleep(1)
        driver.find_element(By.ID, "jenis_kejahatan_values").send_keys(Keys.TAB)
        Log.info('Input unutk Jenis kejahatan Teroris, Kriminal')
        attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_10_JumlahLantai():
    driver.implicitly_wait(30)
    #sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "Masukkan Jumlah Lantai"]')))
    driver.find_element(By.XPATH, '// *[ @ id = "Masukkan Jumlah Lantai"]').send_keys(jumlahLantai)
    Log.info('Input Jumlah Lantai')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_11_FormatPenomoranKamar():
    driver.implicitly_wait(30)
    #sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'penomoran_kamar')))
    driver.find_element(By.ID, "penomoran_kamar").click()
    if formatPenomoranKamar == 'Angka 8 mulai kiri atas':
        driver.find_element(By.XPATH, "//li[contains(.,\'Angka 8 (mulai kiri atas)\')]").click()
        Log.info('Input Format Penomoran Kamar')
        attach(data=driver.get_screenshot_as_png())

    elif formatPenomoranKamar == '8 mulai kiri bawah':
        driver.find_element(By.XPATH, "//li[contains(.,\'Angka 8 (mulai kiri bawah)\')]").click()
        Log.info('Input Format Penomoran Kamar 8 mulai kiri bawah')
        attach(data=driver.get_screenshot_as_png())

    elif formatPenomoranKamar == '8 mulai kanan bawah':
        driver.find_element(By.XPATH, "//li[contains(.,\'Angka 8 (mulai kanan bawah)\')]").click()
        Log.info('Input Format Penomoran Kamar Angka 8 mulai kanan bawah')
        attach(data=driver.get_screenshot_as_png())

    elif formatPenomoranKamar == 'Ke Depan 1 arah':
        driver.find_element(By.XPATH, "//li[contains(.,\'Belakang Ke Depan (1 arah)\')]").click()
        Log.info('Input Format Penomoran Kamar Belakang Ke Depan 1 arah')
        attach(data=driver.get_screenshot_as_png())

    elif formatPenomoranKamar ==  'Ke Depan 2 arah':
        driver.find_element(By.XPATH, "//li[contains(.,\'Belakang Ke Depan (2 arah)\')]").click()
        Log.info('Input Format Penomoran Kamar Belakang Ke Depan 2 arah')
        attach(data=driver.get_screenshot_as_png())

    elif formatPenomoranKamar == 'Depan Ke Belakang 1 arah':
        driver.find_element(By.XPATH, "//li[contains(.,\'Depan Ke Belakang (1 arah)\')]").click()
        Log.info('Input Format Penomoran Kamar Depan Ke Belakang 1 arah')
        attach(data=driver.get_screenshot_as_png())

    elif formatPenomoranKamar == 'Depan Ke Belakang 2 arah':
        driver.find_element(By.XPATH, "//li[contains(.,\'Depan Ke Belakang (2 arah)\')]").click()
        Log.info('Input Format Penomoran Kamar Depan Ke Belakang 2 arah')
        attach(data=driver.get_screenshot_as_png())

    elif formatPenomoranKamar == 'Kanan Kiri 1 arah':
        driver.find_element(By.XPATH, "//li[contains(.,\'Kanan Kiri (1 arah)\')]").click()
        Log.info('Input Format Penomoran Kamar Kanan Kiri 1 arah')
        attach(data=driver.get_screenshot_as_png())






@mark.fixture_test()
def test_12_Umur():
    driver.implicitly_wait(30)
    #sleep(driver)
    driver.find_element(By.ID, "kel_usia_id").click()
    if kelUsia == 'Dewasa':
        driver.find_element(By.XPATH, "//li[contains(.,\'Dewasa')]").click()
        Log.info('memilih kelompok usia Dewasa')
        attach(data=driver.get_screenshot_as_png())

    elif kelUsia == 'Lansia':
        driver.find_element(By.XPATH, "//li[contains(.,\'Lansia')]").click()
        Log.info('memilih kelompok usia Dewasa')
        attach(data=driver.get_screenshot_as_png())

    elif kelUsia == 'Anak-anak':
        driver.find_element(By.XPATH, "//li[contains(.,\'Anak-anak')]").click()
        Log.info('memilih kelompok usia Anak Anak')
        attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_13_InputJumlahKamar():
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "jumlah_kamar_per_lantai-0").click()

    if jumlahLantai == 1:
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-0").send_keys(jumlahKamarPerlantai)
        attach(data=driver.get_screenshot_as_png())

    elif jumlahLantai == 2:
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-0").click()
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-0").send_keys(jumlahKamarPerlantai)
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-1").click()
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-1").send_keys(jumlahKamarPerlantai)
        attach(data=driver.get_screenshot_as_png())

    elif jumlahLantai == 3:
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-0").click()
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-0").send_keys(jumlahKamarPerlantai)
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-1").click()
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-1").send_keys(jumlahKamarPerlantai)
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-2").click()
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-2").send_keys(jumlahKamarPerlantai)
        attach(data=driver.get_screenshot_as_png())

    elif jumlahLantai == 4:
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-0").click()
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-0").send_keys(jumlahKamarPerlantai)
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-1").click()
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-1").send_keys(jumlahKamarPerlantai)
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-2").click()
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-2").send_keys(jumlahKamarPerlantai)
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-3").click()
        driver.find_element(By.ID, "jumlah_kamar_per_lantai-3").send_keys(jumlahKamarPerlantai)
        attach(data=driver.get_screenshot_as_png())

    Log.info('Input Jumlah Kamar perlantai')
    attach(data=driver.get_screenshot_as_png())




@mark.fixture_test()
def test_14_InputNoKamar():
    driver.implicitly_wait(30)
    #sleep(driver)
    if jumlahLantai == 1:
        driver.find_element(By.ID, "noKamarAwal-0").click()
        driver.find_element(By.ID, "noKamarAwal-0").send_keys(noKamarAwal)
        driver.find_element(By.ID, "noKamarAkhir-0").click()
        driver.find_element(By.ID, "noKamarAkhir-0").send_keys(noKamarAkhir)

    elif jumlahLantai ==2:
        driver.find_element(By.ID, "noKamarAwal-0").click()
        driver.find_element(By.ID, "noKamarAwal-0").send_keys(noKamarAwal)
        driver.find_element(By.ID, "noKamarAkhir-0").click()
        driver.find_element(By.ID, "noKamarAkhir-0").send_keys(noKamarAkhir)

        driver.find_element(By.ID, "noKamarAwal-1").click()
        driver.find_element(By.ID, "noKamarAwal-1").send_keys(noKamarAwal)
        driver.find_element(By.ID, "noKamarAkhir-1").click()
        driver.find_element(By.ID, "noKamarAkhir-1").send_keys(noKamarAkhir)

    elif jumlahLantai == 3:
        driver.find_element(By.ID, "noKamarAwal-0").click()
        driver.find_element(By.ID, "noKamarAwal-0").send_keys(noKamarAwal)
        driver.find_element(By.ID, "noKamarAkhir-0").click()
        driver.find_element(By.ID, "noKamarAkhir-0").send_keys(noKamarAkhir)

        driver.find_element(By.ID, "noKamarAwal-1").click()
        driver.find_element(By.ID, "noKamarAwal-1").send_keys(noKamarAwal)
        driver.find_element(By.ID, "noKamarAkhir-1").click()
        driver.find_element(By.ID, "noKamarAkhir-1").send_keys(noKamarAkhir)

        driver.find_element(By.ID, "noKamarAwal-2").click()
        driver.find_element(By.ID, "noKamarAwal-2").send_keys(noKamarAwal)
        driver.find_element(By.ID, "noKamarAkhir-2").click()
        driver.find_element(By.ID, "noKamarAkhir-2").send_keys(noKamarAkhir)

    elif jumlahLantai == 4:
        driver.find_element(By.ID, "noKamarAwal-0").click()
        driver.find_element(By.ID, "noKamarAwal-0").send_keys(noKamarAwal)
        driver.find_element(By.ID, "noKamarAkhir-0").click()
        driver.find_element(By.ID, "noKamarAkhir-0").send_keys(noKamarAkhir)

        driver.find_element(By.ID, "noKamarAwal-1").click()
        driver.find_element(By.ID, "noKamarAwal-1").send_keys(noKamarAwal)
        driver.find_element(By.ID, "noKamarAkhir-1").click()
        driver.find_element(By.ID, "noKamarAkhir-1").send_keys(noKamarAkhir)

        driver.find_element(By.ID, "noKamarAwal-2").click()
        driver.find_element(By.ID, "noKamarAwal-2").send_keys(noKamarAwal)
        driver.find_element(By.ID, "noKamarAkhir-2").click()
        driver.find_element(By.ID, "noKamarAkhir-2").send_keys(noKamarAkhir)

        driver.find_element(By.ID, "noKamarAwal-3").click()
        driver.find_element(By.ID, "noKamarAwal-3").send_keys(noKamarAwal)
        driver.find_element(By.ID, "noKamarAkhir-3").click()
        driver.find_element(By.ID, "noKamarAkhir-3").send_keys(noKamarAkhir)



    Log.info('Input koridor')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_16_Submit():
    driver.implicitly_wait(30)
    #sleep(driver)
    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    Log.info('Submit')
    attach(data=driver.get_screenshot_as_png())

    ################################### kamar###################################

@mark.fixture_test()
def test_17_JenisLantai():
    driver.implicitly_wait(30)
    #sleep(driver)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "app"] / div / div[2] / div[1] / div[2] / div[2] / div / div[5] / div / span[3] / div / input')))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'lantai_id')))
    driver.find_element(By.ID, 'lantai_id').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'lantai-0')))
    driver.find_element(By.ID, "lantai-0").click()
    Log.info('Pilih Lantai')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_18_InputNomorKamar():
    driver.implicitly_wait(30)
    #sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'nomorKamar')))
    driver.find_element(By.ID, "nomorKamar").send_keys(nomorKamar)
    Log.info('Input Nomor Kamar')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_19_PeruntukanKelompokUsia():
    driver.implicitly_wait(30)
    #sleep(driver)
    driver.find_element(By.ID, "kel_usia_id").click()
    if kelUsia == 'Dewasa':
        driver.find_element(By.XPATH, "//li[contains(.,\'Dewasa')]").click()
        Log.info('memilih kelompok usia Dewasa')
        attach(data=driver.get_screenshot_as_png())

    elif kelUsia == 'Lansia':
        driver.find_element(By.XPATH, "//li[contains(.,\'Lansia')]").click()
        Log.info('memilih kelompok usia Dewasa')
        attach(data=driver.get_screenshot_as_png())

    elif kelUsia == 'Anak-anak':
        driver.find_element(By.XPATH, "//li[contains(.,\'Anak-anak')]").click()
        Log.info('memilih kelompok usia Anak Anak')
        attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_20_JenisKelamin():
    driver.implicitly_wait(30)
    # sleep(driver)
    driver.find_element(By.ID, "kel_jenis_kelamin_id").click()
    if jeniskelamin == 'Laki-laki':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Laki-laki\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Laki-laki\')]").click()

        Log.info('Input Blok Untuk Jenis Kelamin Laki Laki')
        attach(data=driver.get_screenshot_as_png())

    elif jeniskelamin == 'Perempuan':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Perempuan\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Perempuan\')]").click()

        Log.info('Input Blok Untuk Jenis Kelamin Perempuan')
        attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_21_TipeKamar():
    driver.implicitly_wait(30)
    # sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'tipe_id')))
    driver.find_element(By.ID, 'tipe_id').click()

    if tipeblok == 'Umum':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Umum\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Umum\')]").click()
        Log.info('Input Tipe Blok Umum')
        attach(data=driver.get_screenshot_as_png())

    elif tipeblok == 'Tutup Sunyi':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Tutup Sunyi\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Tutup Sunyi\')]").click()
        Log.info('Input Tipe Blok Tutup Sunyi')
        attach(data=driver.get_screenshot_as_png())

    elif tipeblok == 'Mapenaling':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Mapenaling\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Mapenaling\')]").click()
        Log.info('Input Tipe Blok Umum')
        attach(data=driver.get_screenshot_as_png())

    elif tipeblok == 'Isolasi':
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Isolasi\')]')))
        driver.find_element(By.XPATH, "//li[contains(.,\'Isolasi\')]").click()
        Log.info('Input Tipe Blok Umum')
        attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_22_kelompokJenisKejahatan():
    driver.find_element(By.ID, 'kel_jenis_kejahatan_id').click()
    if kelompokJenisKejahatan == 'Teroris':
        driver.find_element(By.XPATH, "//li[contains(.,\'Teroris\')]").click()
        Log.info('Input unutk Jenis kejahatan Teroris')
        attach(data=driver.get_screenshot_as_png())

    elif kelompokJenisKejahatan == 'Korupsi':
        driver.find_element(By.XPATH, "//li[contains(.,\'Korupsi\')]").click()
        Log.info('Input unutk Jenis kejahatan Korupsi')
        attach(data=driver.get_screenshot_as_png())

    elif jenisKejahatan == 'Kriminal':
        driver.find_element(By.XPATH, "//li[contains(.,\'Kriminal\')]").click()
        driver.find_element(By.ID, "jenis_kejahatan_values").send_keys(Keys.TAB)
        Log.info('Input unutk Jenis kejahatan Kriminal')
        attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_23_KapasitasInput():
    driver.implicitly_wait(30)
    #sleep(driver)
    driver.find_element(By.ID, 'kapasitasInput').send_keys(kapasitasInput)
    Log.info('Kapasitas Ruangan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_24_KondisiRuangan():
    driver.implicitly_wait(30)
    #sleep(driver)
    driver.find_element(By.ID, 'kondisiInput').click()
    if kondisiRuangan == 'Baik':
        driver.find_element(By.XPATH, "//li[contains(.,\'Baik\')]").click()
        Log.info('Kondisi Ruangan Baik')
        attach(data=driver.get_screenshot_as_png())

    elif kondisiRuangan == 'Rusak':
        driver.find_element(By.XPATH, "//li[contains(.,\'Baik\')]").click()
        Log.info('Kondisi Ruangan Rusak')
        attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_25_LamaHuni():
    driver.implicitly_wait(30)
    #sleep(driver)
    driver.find_element(By.ID, 'lamaHuni').send_keys(lamaHuni)
    Log.info('Lama Huni')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_26_ButtonSubmit():
    driver.implicitly_wait(30)
    #sleep(driver)
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    Log.info('Submit')
    attach(data=driver.get_screenshot_as_png())
    #MASIH BELUM SELESAI

@mark.fixture_test()
def test_exit():
    sleep(driver)
    quit(driver)
