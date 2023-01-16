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
from openpyxl import load_workbook
import sys
import pyautogui

from dotenv import load_dotenv
load_dotenv()

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR")) 
elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))

from Settings.setup import initDriver, loadDataPath, sleep, quit
from Settings.login import login, oprupbasanbdg

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('aksesmenu.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

# init driver by os
@mark.fixture_aksesmenu
def test_00():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')

@mark.fixture_aksesmenu
def test_00_loggin():
    login(driver)
    Log.info('Memasukan User name dan Password di halaman Login)')

@mark.fixture_aksesmenu
def test_Registrasi():
	nav1 = driver.find_element(By.ID, '01')
	ActionChains(driver).move_to_element(nav1).perform()

@mark.fixture_aksesmenu
def test_Registrasi():
	driver.find_element(By.LINK_TEXT, 'Penerimaan').click()

	attach(data=driver.get_screenshot_as_png())
	Log.info('Mengakses menu Penerimaan dengan memilih modul Rupbasan kemudian pilih menu Penerimaan')
	
@mark.fixture_aksesmenu
def test_RGS_001():
	nav1 = driver.find_element(By.ID, '01')
	ActionChains(driver).move_to_element(nav1).perform()
	time.sleep(2)
	nav2 = driver.find_element(By.ID, 'PP0')
	ActionChains(driver).move_to_element(nav2).perform()

	driver.find_element(By.LINK_TEXT, 'Penerimaan').click()

	attach(data=driver.get_screenshot_as_png())
	Log.info('Mengakses menu Penerimaan dengan memilih modul Rupbasan kemudian pilih menu Penerimaan')


