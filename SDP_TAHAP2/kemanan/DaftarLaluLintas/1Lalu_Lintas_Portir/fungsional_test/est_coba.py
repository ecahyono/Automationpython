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

from dotenv import load_dotenv
load_dotenv()
#file modul
from module.setup import initDriver, loadDataPath
from module.login import login

import json

# init driver by os
@mark.fixture_test()
def test_1_init():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_test()
def test_2_login():
    login(driver)

@mark.fixture_test()
def test_3_akses_menu():
    vars = {}
    vars["x"] = driver.execute_script("return 1")
    # 4 | do |  | 
    condition = True
    while condition:
        driver.implicitly_wait(10)
        
        nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
        ActionChains(driver).move_to_element(nav1).perform()

        element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
        time.sleep(1)
        ActionChains(driver).move_to_element(element2).perform()
        time.sleep(1)

        driver.find_element(By.LINK_TEXT, 'Daftar Lalu Lintas').click()
        
        print('.')
        print('==========akses menu daftar lalu lintas==========')
        vars["x"] = driver.execute_script("return arguments[0]+1", vars["x"])
        condition = driver.execute_script("return (arguments[0]<1)", vars["x"])
        attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_4_membuka_halaman_tambah():
    driver.implicitly_wait(10)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, pathData['id']['createButton'])))
    driver.find_element(By.XPATH, pathData['id']['createButton']).click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5 > path")))
    #WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, 'pathData['id']['createButton'])))
    #driver.find_element(By.XPATH, pathData['id']['createButton']).click()
    print('.')
    print('================================================================================= Membuka Halaman Tambah  ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_5_sortir_table_cari_nama_Tambah():
    driver.implicitly_wait(20)
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/label/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
    print('.')
    print('================================================================================= Memilih Dropdown Nama  ')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div/input')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div/input').send_keys('WILLLD BINTI eko cah cah ge')
    print('.')
    print('================================================================================= Input Nama  ')

    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button').click()
    print('.')
    print('==========Click Button Cari  ==========')
    attach(data=driver.get_screenshot_as_png())




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

    print('░░▄███▄███▄')
    print('░░█████████')
    print('░░▒▀█████▀░')
    print('░░▒░░▀█▀')
    print('░░▒░░█░')
    print('░░▒░█')
    print('░░░█')
    print('░░█░░░░███████')
    print('░██░░░██▓▓███▓██▒')
    print('██░░░█▓▓▓▓▓▓▓█▓████')
    print('██░░██▓▓▓(◐)▓█▓█▓█')
    print('███▓▓▓█▓▓▓▓▓█▓█▓▓▓▓█')
    print('▀██▓▓█░██▓▓▓▓██▓▓▓▓▓█')
    print('░▀██▀░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█')
    print('░░░░▒░░░█▓▓▓▓▓█▓▓▓▓▓▓█')
    print('░░░░▒░░░█▓▓▓▓█▓█▓▓▓▓▓█')
    print('░▒░░▒░░░█▓▓▓█▓▓▓█▓▓▓▓█')
    print('░▒░░▒░░░█▓▓▓█░░░█▓▓▓█')
    print('░▒░░▒░░██▓██░░░██▓▓██')
    driver.close()
    driver.quit()
