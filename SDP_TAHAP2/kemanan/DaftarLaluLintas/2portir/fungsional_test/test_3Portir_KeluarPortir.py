from distutils.archive_util import make_archive
from os import PRIO_PGRP, environ
from re import S, T
from threading import TIMEOUT_MAX
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
from pathlib import Path

# file modul
# from module.setup import initDriver, loadDataPath
# from module.login import login

sys.path.append("/Users/will/Documents/work/Automationpython")
from Settings.setup import initDriver, loadDataPath
from Settings.login import login
from dotenv import load_dotenv

load_dotenv()
import json


@mark.fixture_test()
def test_1_setupOS_KeluarPortir():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()


@mark.fixture_test()
def test_2_login_KeluarPortir():
    login(driver)


# AKSES MENU
@mark.fixture_test()
def test_3_akses_menu_KeluarPortir():
    driver.implicitly_wait(10)
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
def test_4_sortir_table_cari_nama_KeluarPortir():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
    print('=')
    print(' = Memilih Dropdown Nama  ')
    attach(data=driver.get_screenshot_as_png())
    #WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    #driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('')
    print('=')
    print(' = Input Nama  ')

    driver.find_element(By.XPATH, '//*[@id="statusColumn"]').send_keys('keluar portir')
    driver.find_element(By.CSS_SELECTOR, "#statusKeluarPortir").click()

    print('=')
    print(' = Keluar Keamanan  ')

    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()
    print('=')
    print(' = Click Button Cari  ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_5_Click_Button_Detile_KeluarPortir():
    driver.implicitly_wait(30)
    time.sleep(2)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    time.sleep(1)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5")))
    time.sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, ".h-5").click()

    print('=')
    print(' = Click Button Update  ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_6_KonfirmasiKeluar_KeluarPortir():
    driver.implicitly_wait(30)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,53)")
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#confirmButton > span")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#confirmButton > span")))
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, "#confirmButton > span").click()
    # driver.find_element(By.CSS_SELECTOR, "#lihatSurat > span").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))

    # driver.find_element(By.XPATH, '//*[@id="confirmButton"]').click()


def teardown():
    time.sleep(10)
    print('.')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▓▒▒▒▒▒▒▒▒▓▒')
    print('▒▒▓▓▓▓▓▓▓▓▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')

    driver.close()
    driver.quit()