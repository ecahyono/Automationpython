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
from module.template import buttonTambah, buttonSubmit, selectKategoriPegawai, selectKategoriTamuDinas, quit
import sys
from pathlib import Path
sys.path.append("/Users/will/Documents/work/Automationpython")
from Settings.setup import initDriver, loadDataPath
from Settings.login import login
from dotenv import load_dotenv
load_dotenv()
import json

# file modul

# from module.login import login


@mark.fixture_test()
def test_1_SetupOS_Search_Tambah():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()


@mark.fixture_test()
def test_2_Login_SearchTambah():
    login(driver)


@mark.fixture_test()
def test_3_Akses_menu_index():
    driver.implicitly_wait(60)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Akses Pintu P2U').click()
    print('.')
    print('= akses menu daftar lalu lintas =')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_4_Search_Nama():
    driver.implicitly_wait(60)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, "//th[7]/div/span/i").click()

@mark.fixture_test()
def test_5_ClickDetail_KonfirmKeluar():
    WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="searchButton"]')))
    time.sleep(2)
    driver.find_element(By.ID, "detailButton0").click()

@mark.fixture_test()
def test_6_KonfirmKeluar():
    driver.implicitly_wait(60)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    time.sleep(5)
    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Diperbaharui\')]')))

def teardown():
    quit(driver)