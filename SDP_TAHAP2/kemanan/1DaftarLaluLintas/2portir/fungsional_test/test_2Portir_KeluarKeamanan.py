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
fh = logging.FileHandler('Portir_KeluarKeamanan.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrange = wb['Portir_SearchDataIndex']
xr = sheetrange['A'+str(14)].value
i  = xr

NamaWbp                               = sheetrange['B'+str(i)].value


@mark.fixture_test()
def test_1_setupOS_KeluarKeamanan():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_test()
def test_2_login_KeluarKeamanan():
    login(driver)


#AKSES MENU 
@mark.fixture_test()
def test_3_akses_menu_KeluarKeamanan():
    
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Portir').click()
    print('.')
    print('==========akses menu daftar lalu lintas==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_4_sortir_table_cari_nama_KeluarKeamanan():
    driver.implicitly_wait(30)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
    print('=')
    print(' = Memilih Dropdown Nama  ')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NamaWbp)
    print('=')
    print(' = Input Nama  ')

    driver.find_element(By.XPATH, '//*[@id="statusColumn"]').send_keys('keluar keamanan')
    driver.find_element(By.XPATH, "//li[contains(.,\'Keluar Keamanan\')]").click()

    print('=')
    print(' = Keluar Portir  ')

    driver.implicitly_wait(30)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()
    print('=')
    print(' = Click Button Cari  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_Click_Button_Detile_KeluarKeamanan():
    driver.implicitly_wait(30)
    time.sleep(2)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5")))
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5")))
    time.sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, ".h-5").click()

    
    print('=')
    print(' = Click Button Update  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_6_KonfirmasiKeluar_KeluarKeamanan():
    driver.implicitly_wait(30)  
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,53)")
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#lihatSurat > span")))
    time.sleep(5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#confirmButton > span")))
    driver.find_element(By. CSS_SELECTOR, "#confirmButton > span").click()
    #driver.find_element(By.CSS_SELECTOR, "#lihatSurat > span").click()
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Diperbaharui\')]')))
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))

    #driver.find_element(By.XPATH, '//*[@id="confirmButton"]').click()

@mark.fixture_test()
def test_exit():
    quit(driver)