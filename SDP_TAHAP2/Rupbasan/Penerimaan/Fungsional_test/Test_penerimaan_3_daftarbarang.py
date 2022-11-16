from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from pytest_html_reporter import attach
from pytest import mark
import platform
import time
import os
import pytest
import json
import sys

from dotenv import load_dotenv
load_dotenv()

#file modul
if platform.system() == 'Darwin':
    sys.path.append('/Users/will/Documents/work/Automationpython')
elif platform.system() == 'Windows':
    sys.path.append(r'C:\Users\user\Documents\TRCH\Automationpython\Settings')

from module.setup import initDriver, loadDataPath
from module.login import login

# init driver by os
@mark.fixture_Barang_penerimaan
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_Barang_penerimaan
def test_login():
    login(driver)

@mark.fixture_Barang_penerimaan
def test_akses_menu():
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.LINK_TEXT, 'Penerimaan').click()
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Barang_penerimaan
def test_Buka_halaman_Daftarbarang():
    driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['daftarbarang']).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, pathData ['Id Navigate Button']['Back Button'])))
    attach(data=driver.get_screenshot_as_png())

# @mark.fixture_Barang_penerimaan
# def test_tambah_Daftarbarang():

