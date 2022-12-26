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