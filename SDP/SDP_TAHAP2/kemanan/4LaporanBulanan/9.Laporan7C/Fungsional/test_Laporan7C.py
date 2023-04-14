from openpyxl import Workbook
from faker import Faker
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
from datetime import datetime

import sys
from os import environ, path
from dotenv import load_dotenv
load_dotenv()
from openpyxl import load_workbook

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR"))
    wb = load_workbook(environ.get("KeamananUAT"))
    file_path = environ.get("fakermac")

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))
    wb = load_workbook(environ.get("KeamananUATWin"))


from Settings.setupkeamanan import initDriver, loadDataPath, quit, sleep
from Settings.loginkeamanan import oplapkamtibwaru,kanwiljabar,pusat, SpvRutanBdg
from Settings.Page.keamanan import menulaporan7c
import random
import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Loglaporan7B.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

workbook = Workbook()
worksheet = workbook.active
worksheet.title = 'LaporanFaker'

fake = Faker('id_ID')
JenisGangguan = ['Kerusuhan Kunjungan','Kerusuhan Petugas dengan WBP ','Kerusuhan WBP dengan WBP ','Kerusuhan Kunjungan']
identitaspelaku = ['Drs. Tina Uyainah','Paris Mandasari, S.Ked','Okto Irawan','dr. Nilam Siregar, M.Pd','Kayla Prastuti']
tingkatgangguan = ['1','2','3','4', '5', '6' ]
korban = ['1','2','3','4', '5', '6' ]
TindakLanjutBarang = ['Evaluasi','Agenda Ulang']
for i in range(50):
    JenisGangguanFaker          = random.choice(JenisGangguan)
    identitaspelakuFaker        = random.choice(identitaspelaku)
    waktukejadianFaker          = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    tingkatgangguanFaker        = random.choice(tingkatgangguan)
    korbanptgsFaker             = random.choice(korban)
    korbanwbpFaker              = random.choice(korban)
    korbanMasyarakatFaker       = random.choice(korban)
    keteranganFaker             = fake.paragraph(nb_sentences=2)
    

    worksheet.append([
         JenisGangguanFaker, 
         identitaspelakuFaker, 
         waktukejadianFaker, 
         tingkatgangguanFaker, 
         korbanptgsFaker,
         korbanwbpFaker, 
         korbanMasyarakatFaker, 
         keteranganFaker
        ])
workbook.save(file_path)

workbook = load_workbook(filename=file_path)
worksheet = workbook.active
for row in worksheet.iter_rows(min_row=2, values_only=True):
    jenisgangguanfkr                        = row[0]
    identitaspelakufkr                      = row[1]
    waktukejadianfkr                        = row[2]
    tingkatgangguanfkr                      = row[3]
    korbanptgsfkr                           = row[4]
    korbanwbpfkr                            = row[5]
    korbanmasyarakanfkr                     = row[6]
    keteranganFkr                           = row[7]
   


@mark.fixture_test()
def test_1_SetupOs():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()      

@mark.fixture_test()
def test_2_Login():
    Log.info('Setup Os')
    oplapkamtibwaru(driver)
    Log.info('Login Op Laporan Kamtib 7 B')

@mark.fixture_test()
def test_2_AksesMenu():
    sleep(driver)
    try:
        menulaporan7c(driver)
        Log.info('Akses halaman Laporan 7 B')
        attach(data=driver.get_screenshot_as_png())
        assert True
    except:
        Log.info('Gagal Akses halaman Laporan 7 B')
        attach(data=driver.get_screenshot_as_png())
        quit(driver)
        assert False

@mark.fixture_test()
def test_3_CreateButton():
    sleep(driver)
    try:
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
        driver.find_element(By.ID, "createButton").click()
        Log.info('Klik tombol tambah data')
        attach(data=driver.get_screenshot_as_png())
        assert True
    except:
        Log.info('Gagal Klik tombol tambah data')
        attach(data=driver.get_screenshot_as_png())
        quit(driver)
        assert False
    

    driver.find_element(By.ID, "jenisGangguan").click()
    driver.find_element(By.ID, "jenisGangguan").send_keys(jenisgangguanfkr)
    driver.find_element(By.XPATH, "(//li[@id=\'identitasPelaku\'])[2]").click()
    driver.find_element(By.ID, "waktuKejadian").click()
    driver.find_element(By.ID, "waktuKejadian").send_keys(waktukejadianfkr)
    driver.find_element(By.CSS_SELECTOR, ".el-form:nth-child(3)").click()
    driver.find_element(By.ID, "waktuKejadian").click()
    driver.find_element(By.ID, "tingkatGangguan").click()
    driver.find_element(By.ID, "tingkatGangguan").send_keys(tingkatgangguanfkr)
    driver.find_element(By.ID, "jumlahPetugas").send_keys(korbanptgsfkr)
    driver.find_element(By.ID, "jumlahWbp").send_keys(korbanwbpfkr)
    driver.find_element(By.ID, "jumlahMasyarakat").send_keys(korbanmasyarakanfkr)
    driver.find_element(By.ID, "kerugianMateril").click()
    driver.find_element(By.ID, "kerugianMateril").send_keys(kerugianfkr)
    driver.find_element(By.ID, "tindakLanjut").send_keys(tindalwanjut)
    driver.find_element(By.ID, "keterangan").send_keys(keteranganFkr)



@mark.fixture_test()
def test_29_exit():
    quit(driver)
    Log.info('Exit')








    
    