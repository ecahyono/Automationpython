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
from Settings.login import login

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('P2UUAT.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


sheetrangeIndex = wb['Fungsi_P2U_Index']
print('.')
print('P2U Index, Mau Baris Ke Berapa ?')
index  = input('')

filterColumnIndex                                = sheetrangeIndex['B'+str(index)].value
NamaWBPIndex                                     = sheetrangeIndex['C'+str(index)].value
NomorIndukIndex                                  = sheetrangeIndex['D'+str(index)].value
KeperluanIndex                                   = sheetrangeIndex['E'+str(index)].value
inputKategoriIndex                               = sheetrangeIndex['F'+str(index)].value

filterTanggalMasuk                               = sheetrangeIndex['G'+str(index)].value
filterTanggalKeluar                              = sheetrangeIndex['H'+str(index)].value


@mark.fixture_test()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()


@mark.fixture_test()
def test_2_login():
    login(driver)


@mark.fixture_test()
def test_APO_001():
    print('.')
    print('Menjalankan APO-001 - Mengakses halaman Akses Pintu Otomatis dengan memilih modul Keamanan kemudian pilih menu Lalu Lintas lalu pilih submenu Akses Pintu Otomatis')

    driver.implicitly_wait(60)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Akses Pintu P2U').click()

    print('.')
    Log.info('(Berhasil APO-001) Berhasil menampilkan halaman Akses Pintu Otomatis')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_APO_002():
    print('.')
    print('(APO-002) / Melakukan pengecekan filtering data')

    driver.implicitly_wait(30)
    Log.info('Memilih Filter data')
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    if filterColumnIndex == 'nama lengkap':
        print('akan memilih Pencarian berdasarkan nama lepngkap')
        sleep(driver)
        driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys('nama')
        # KETIK NAMA
        driver.find_element(By.XPATH, "//li[contains(.,\'Nama Lengkap\')]").click()
        # PILIH DROPDOWN NAMA LENGKAP
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NamaWBPIndex)
        # KETIK GALIH DI FORM MASUKAN KATA KUNCI
        Log.info('Search Bedasarkan Nama Lengkap')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnIndex == 'nomor induk':
        print('akan memilih Pencarian berdasarkan Nomor induk')
        sleep(driver)
        driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys('Nomor')
        # KETIK NOMOR
        driver.find_element(By.XPATH, "//li[contains(.,\'Nomor Identitas\')]").click()
        # PILIH DROPDOWN NOMOR IDENTITAS
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NomorIndukIndex)
        Log.info('Search Bedasarkan Nomor Induk')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnIndex == 'keperluan':
        print('akan memilih Pencarian berdasarkan keperluan')
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="filterColumn"]').send_keys('Keperluan')
        # KETIK NOMOR
        driver.find_element(By.XPATH, "//li[contains(.,\'Keperluan\')]").click()
        # PILIH DROPDOWN NOMOR IDENTITAS
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(KeperluanIndex)
        Log.info('Search Bedasarkan Keperluan')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnIndex == 'kategori':
        time.sleep(1)
        print('akan memilih Pencarian berdasarkan Kategori')
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="filterColumn"]').send_keys('Kategori')
        driver.find_element(By.XPATH, "//li[contains(.,\'Kategori\')]").click()
        driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
        Log.info('Search Bedasarkan kategori')
        attach(data=driver.get_screenshot_as_png())
        sleep(driver)

        if inputKategoriIndex == 'Pegawai':
            print(' akan memilih Pencarian Pegawai')
            sleep(driver)
            driver.find_element(By.XPATH, "//li[@id='pegawai']").click()
            Log.info('select kategori pegawai')
            attach(data=driver.get_screenshot_as_png())

        elif inputKategoriIndex == 'Tamu Dinas':
            print(' akan memilih Pencarian Tamu Dinas')
            sleep(driver)
            driver.find_element(By.ID, 'tamuDinas').click()
            Log.info('select kategori tamu dinas')

            attach(data=driver.get_screenshot_as_png())
        elif inputKategoriIndex == 'Kunjungan Onsite':
            Log.info('select kategori Kunjungan onsite')
            sleep(driver)
            driver.find_element(By.XPATH, "//li[@id='Kunjungan']").click()
            attach(data=driver.get_screenshot_as_png())
        elif inputKategoriIndex == 'Kunjungan Online':
            Log.info('select kategori Kunjungan Online')
            sleep(driver)
            driver.find_element(By.XPATH, "//li[@id='Kunjungan Online']").click()
            attach(data=driver.get_screenshot_as_png())
    Log.info('Klik button search')
    sleep(driver)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()
    Log.info('(BERHASIL APO-002) / Berhasil menampilkan data sesuai dengan kategori yang dipilih pada dropdown di halaman Daftar Akses Pintu ')
    attach(data=driver.get_screenshot_as_png())


sheetrangeTambah = wb['Fungsi_P2U_Input']
print("2.pegawai 3.Tamu Dinas")
tambah = input("")

inputKategoritambah                       = sheetrangeTambah['B' + str(tambah)].value
NamaAtauNiptambah                         = sheetrangeTambah['C' + str(tambah)].value
inputNiptambah                            = sheetrangeTambah['D' + str(tambah)].value
inputNamatambah                           = sheetrangeTambah['E' + str(tambah)].value
inputJabatantambah                        = sheetrangeTambah['F' + str(tambah)].value
InputInstansitambah                       = sheetrangeTambah['G' + str(tambah)].value
inputKeperluantambah                      = sheetrangeTambah['H' + str(tambah)].value
KunjunganOnsitetambah                     = sheetrangeTambah['I' + str(tambah)].value
KunjunganOnlinetambah                     = sheetrangeTambah['J' + str(tambah)].value


@mark.fixture_test()
def test_APO_003():
    print('.')
    print('(BERHASIL APO-003) / Menambahkan data akses pintu otomatis dengan menekan button tambah dan melakukan pencarian identitas Non-WBP, kemudian input keperluan / keterangan lalu klik button konfirmasi masuk')


@mark.fixture_test()
# pergi ke halaman tambah
def test_4_ButtonTambah_PegawaiTambah():
    print(".")
    print('Click Button TAMBAH')
    sleep(driver)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButton"]')))
    Log.info(' Membuka Halaman Tambah ')
    attach(data=driver.get_screenshot_as_png())

    print(".")
    print('Input data ')
    driver.implicitly_wait(30)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    if inputKategoritambah == 'Pegawai':
        Log.info('Input data Pegawai')
        sleep(driver)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'pegawai')))
        driver.find_element(By.XPATH, "//li[@id=\'pegawai\']").click()
        driver.find_element(By.ID, 'inputSearch').send_keys(NamaAtauNiptambah)
        if driver.find_elements(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label'):
            driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label').click()
            driver.find_element(By.ID, 'inputKeperluan').send_keys(inputKeperluantambah)
        elif driver.find_elements(By.CSS_SELECTOR, ".el-select-dropdown__empty"):
            driver.find_element(By.ID, 'inputNip').click()
            driver.find_element(By.ID, 'inputNip').send_keys(inputNiptambah)
            Log.info(' Input NIP ')
            sleep(driver)
            attach(data=driver.get_screenshot_as_png())
            driver.find_element(By.ID, 'inputNama').send_keys(inputNamatambah)
            Log.info(' Input Nama ')
            sleep(driver)
            attach(data=driver.get_screenshot_as_png())
            driver.find_element(By.ID, 'inputJabatan').send_keys(inputJabatantambah)
            Log.info(' Input Jabatan ')
            sleep(driver)
            attach(data=driver.get_screenshot_as_png())
            driver.find_element(By.ID, 'inputKeperluan').send_keys(inputKeperluantambah)
            Log.info(' Input Keperluan ')
            sleep(driver)
            attach(data=driver.get_screenshot_as_png())

    elif inputKategoriIndex == 'Tamu Dinas':

        driver.find_element(By.ID, "tamuDinas").click()
        Log.info(' Memilih Kategori Tamu Dinas ')
        driver.find_element(By.ID, 'inputSearch').send_keys(NamaAtauNiptambah)
        Log.info(' Cari Nama atau Nip Kategori Tamu Dinas ')
        attach(data=driver.get_screenshot_as_png())

        if driver.find_elements(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label'):
            driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label').click()
            driver.find_element(By.ID, 'inputKeperluan').send_keys(inputKeperluantambah)

        elif driver.find_elements(By.CSS_SELECTOR, ".el-select-dropdown__empty"):
            driver.find_element(By.ID, 'inputNip').send_keys(inputNiptambah)
            sleep(driver)
            driver.find_element(By.ID, 'inputNama').send_keys(inputNamatambah)
            sleep(driver)
            driver.find_element(By.ID, 'inputInstansiId').send_keys(InputInstansitambah)
            if InputInstansitambah == "POLRES BANDUNG":
                driver.find_element(By.CSS_SELECTOR, '#optionInstansi0').click()
            elif InputInstansitambah == "POLDA JABAR":
                driver.find_element(By.ID, '//div[contains(.,\'POLDA JABAR\')]').click()
            elif InputInstansitambah == "POLRES MAGELANG":
                driver.find_element(By.ID, '//div[contains(.,\'POLRES MAGELANG\')]').click()
            sleep(driver)
            driver.find_element(By.ID, 'inputJabatan').send_keys(inputJabatantambah)
            sleep(driver)
            driver.find_element(By.ID, 'inputKeperluan').send_keys(inputKeperluantambah)
            print('.')
            Log.info(' Input NIP ')
            attach(data=driver.get_screenshot_as_png())

    elif inputKategoriIndex == 'Kunjungan Onsite':

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
        driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
        driver.find_element(By.ID, "kunjungan").click()
        attach(data=driver.get_screenshot_as_png())
        driver.find_element(By.ID, 'pickKunjungan0').click()

    Log.info('(BERHASIL APO_003) / Menampilkan alert berhasil kemudian data yang sesuai ditampilkan di pada main grid ')
    sleep(driver)
    buttonSubmit(driver)
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_APO_004():
    print(".")
    print(' (APO-004) / Melakukan konfirmasi keluar pada Non-WBP yang akan keluar melalui akses pintu otomatis dan menampilkan waktu keluar pada main grid')
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys('nama')
    sleep(driver)
    # KETIK NAMA
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama Lengkap\')]").click()
    sleep(driver)
    # PILIH DROPDOWN NAMA LENGKAP
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NamaWBPIndex)
    sleep(driver)
    # KETIK GALIH DI FORM MASUKAN KATA KUNCI
    Log.info('Search Bedasarkan Nama Lengkap')
    attach(data=driver.get_screenshot_as_png())

    Log.info('Klik check Box Belum Konfirmasi Keluar')
    sleep(driver)
    driver.find_element(By.XPATH, "//label[@id=\'konfirmasiKeluar\']/span/span").click()

    Log.info('Klik Button Search')
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()

    Log.info('Clik Button Detail')
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.ID, "detailButton0").click()

    Log.info('Klik Konfirmasi Keluar')
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    time.sleep(5)
    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Diperbaharui\')]')))
    Log.info('( BERHASIL APO-004 / Menampilkan alert berhasil kemudian berhasil konfirmasi keluar dan menampilkan waktu keluar ')

@mark.fixture_test()
def test_APO_005():
    print('.')
    print('(APO - 005) / Menampilkan detail Detail Portir Akses Pintu P2U dengan menggunakan button (Detail) pada kolom aksi di tabel Daftar Portir Akses Pintu')
    print(".")
    print('(APO-004) / Melakukan konfirmasi keluar pada Non-WBP yang akan keluar melalui akses pintu otomatis dan menampilkan waktu keluar pada main grid')
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys('nama')
    sleep(driver)
    # KETIK NAMA
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama Lengkap\')]").click()
    sleep(driver)
    # PILIH DROPDOWN NAMA LENGKAP
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NamaWBPIndex)
    sleep(driver)
    # KETIK GALIH DI FORM MASUKAN KATA KUNCI
    Log.info('Search Bedasarkan Nama Lengkap')
    attach(data=driver.get_screenshot_as_png())
    Log.info('Klik Button Search')
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()

    Log.info('Clik Button Detail')
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    time.sleep(5)
    driver.find_element(By.ID, "detailButton0").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'backButton')))
    driver.find_element(By.ID, 'backButton').click()


@mark.fixture_test()
def test_APO_006():
    print('')
    print('(APO-006 / Menampilkan dropdown jumlah data HALAMAN yang dipilih oleh pengguna dan ditampilkan pada main grid, DATA TABEL SESUAI HALAMAN')

    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke1']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'5/halaman\')]").click()

    Log.info('Berhasil menampilkan jumlah halaman data yang ditampilkan pada main grid')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_APO_007():
    print('.')
    print('( APO - 007 ) / Menampilkan jumlah data yang sesuai dengan total halaman yang dipilih')
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    Log.info('pergi ke halaman paling belakang')
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, ".el-input--small > .el-input__inner").send_keys(Keys.BACKSPACE)
    driver.find_element(By.CSS_SELECTOR, ".el-input--small > .el-input__inner").send_keys('100')

    Log.info('Berhasil menampilkan jumlah data yang sesuai pada main grid')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_APO_008():
    print('.')
    print('(APO - 008) / Menampilkan halaman sebelumnya dan selanjutnya menggunakan navigasi button ')
    sleep(driver)
    driver.implicitly_wait(30)

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    Log.info('Klik button selanjutnya')
    driver.find_element(By.CSS_SELECTOR, ".btn-next svg").click()

    Log.info('Klik button Sebelumnya')
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, ".btn-prev svg").click()
    Log.info('(APO -008) / Berhasil menampilkan halaman sebelumnya dan selanjutnya')

@mark.fixture_test()
def test_APO_008():
    print('.')
    print('(APO - 009) / Mencetak data akses pintu otomatis (sesuai dengan jumlah halaman) dengan menekan Button Export Excel ')

    sleep(driver)
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.CSS_SELECTOR, '#excelButton span').click()
    driver.find_element(By.CSS_SELECTOR, '#thisButton > span').click()
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil mengunduh file\')]')))
    Log.info(
        '(PTR-010) / Mencetak data portir sesuai dengan total halaman yang dipilih dengan format Excel (.xlsx) kemudian tampil alert berhasil')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_APO_009():
    # Melakukan export data tabel ke pdf
    print('.')
    print('Menjalankan APO - 009 / Mencetak data P2U (sesuai dengan jumlah halaman) dengan menekan Button Export PDF')
    sleep(driver)
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.CSS_SELECTOR, '#pdfButton span').click()
    driver.find_element(By.CSS_SELECTOR, '#pdfButton #thisButton').click()
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil mengunduh file\')]')))
    Log.info('(BERHASIL APO - 009) / Berhasil mencetak data akses pintu otomatis sesuai dengan total halaman yang dipilih dengan format Excel (.xlsx) kemudian tampil alert berhasil')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_PTR_010():
    print('.')
    print('Menjalankan APO - 010 / Pengecekan cetak data akses pintu otomatis dengan format PDF')
    sleep(driver)
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.CSS_SELECTOR, '#printButton path').click()
    driver.find_element(By.CSS_SELECTOR, '#printButton .el-button:nth-child(2) > span').click()

    print('.')
    Log.info('(BERHASIL APO - 010) / Menampilkan halaman preview lalu setelah berhasil mencetak data, tampil alert berhasil')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_PTR_010():
    print('.')
    print('Menjalankan APO - 010 / Pengecekan cetak data akses pintu otomatis dengan format PDF')
    sleep(driver)
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.CSS_SELECTOR, "#printButton > #printButton").click()
    driver.find_element(By.CSS_SELECTOR, '#printButton .el-button:nth-child(2) > span').click()

    print('.')
    Log.info('(BERHASIL APO - 010) / Menampilkan halaman preview lalu setelah berhasil mencetak data, tampil alert berhasil')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_exit():
    print('Exit Program . . . . . . . . . . .')
    sleep(driver)
    quit(driver)