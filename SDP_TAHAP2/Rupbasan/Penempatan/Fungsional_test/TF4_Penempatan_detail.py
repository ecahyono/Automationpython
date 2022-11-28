from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pytest_html_reporter import attach
import os, platform, time, pytest
from selenium import webdriver
from os import environ, path
from pathlib import Path
from pytest import mark
import platform
import logging
import sys

from dotenv import load_dotenv
load_dotenv()

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR")) 
elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))

from Settings.setup import initDriver, loadDataPath, quit
from Settings.login import login

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('TF4_Penempatan_detail.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

@mark.fixture_penempatan
def test_Ossetup_1():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')

@mark.fixture_penempatan
def test_loggin_2():
    login(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Memasukan User name dan Password di halaman Login)')

@mark.fixture_penempatan
def test_akses_menu_penempatan_3():
    nav = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['MainText'])
    ActionChains(driver).move_to_element(nav).perform()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, 'Penempatan').click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('mengakses menu penempatan')

@mark.fixture_penempatan
def test_akses_Ubah_4():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

    pilkat = driver.find_element(By. ID, "filterColumn")
    pilkat.click()
    pilkat.send_keys('Barang')
    pilkat.send_keys(Keys.DOWN)
    pilkat.send_keys(Keys.ENTER)

    driver.find_element(By. ID, 'kataKunci').send_keys('Mouse') #barang dengan No urut 109
    driver.find_element(By. ID, 'searchButton').click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    time.sleep(2)
    driver.find_element(By. XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[8]/td[12]/div/div/div[1]/a/button').click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('melakukan pencarian data dengan memilih salah satu dari kategori yang disediakan kemudian membuka halaman Detail mdengan klik icon Detail. Data yang di tampilkan sesuai')
