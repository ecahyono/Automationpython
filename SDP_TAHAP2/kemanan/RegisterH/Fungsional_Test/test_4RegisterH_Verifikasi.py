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
sys.path.append("/Users/will/Documents/work/Automationpython")
from Settings.setup import initDriver, loadDataPath
from Settings.login import login
from Settings.setup import quit
from dotenv import load_dotenv
load_dotenv()
import json


@mark.fixture_test()
def test_1_setupOS_Search():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_test()
def test_2_login_Search():
    login(driver)

@mark.fixture_test()
def test_3_aksesmenu_Search():
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.2)
    driver.find_element(By.LINK_TEXT, 'Register H').click()
    print('.')
    print('==========akses menu Register H==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_4_keyword_nama():  # Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.ID, 'filterColumn').send_keys('nama')
    driver.find_element(By.ID, 'filterColumn').click()
    print('.')
    print('========== Memilih kategori Nama ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_nama():
    driver.implicitly_wait(30)
    driver.find_element(By.XPATH, '//*[@id="namaLengkap"]').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('')
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    print('.')
    print('========== Search nama ==========')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_6_status_dalamproses():
    driver.implicitly_wait(30)
    driver.find_element(By.ID, 'filterStatus').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dalamProses"]')))
    driver.find_element(By.ID, 'dalamProses').click()
    print('.')
    print('========== Filter status Dalam Proses ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_7_Click_StatusDalamProses():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modalButton0"]')))
    driver.find_element(By.XPATH, '//*[@id="modalButton0"]').click()
    print('.')
    print('========== Click Button Status Dalam Proses ==========')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_8_Ubah_Status_Diizinkan():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="statusVerifikasiModal"]')))
    driver.find_element(By.XPATH, '//*[@id="statusVerifikasiModal"]').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "(//li[@id=\'diizinkan\'])[2]")))
    driver.find_element(By.XPATH, "(//li[@id=\'diizinkan\'])[2]").click()
    print('.')
    print('========== Ubah Status Menjadi Di Izinkan ==========')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_9_InputKeterangan():
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "keterangan").click()
    driver.find_element(By.ID, "keterangan").send_keys("KETERAGNAN")
    print('.')
    print('========== Input Keterangan ==========')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_10_SimpanButton():
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "simpanVerifikasi").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Diperbaharui\')]')))
    print('.')
    print('========== Button Simpan Verifikasi ==========')
    attach(data=driver.get_screenshot_as_png())

# DONE

def teardown():
    quit(driver)