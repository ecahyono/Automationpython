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
import json
import os

from dotenv import load_dotenv
load_dotenv()


from module.setup import initDriver, loadDataPath
from module.login import login


# init driver by os
@mark.fixture_Penerimaan
def test_init():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_Penerimaan
def test_login():
    login(driver)
    return driver
@mark.fixture_Penerimaan
def akses_menu():

    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()

    driver.find_element(By.LINK_TEXT, 'Penerimaan').click()

@mark.fixture_Penerimaan
def test_tambah():   
    driver.find_element(By.XPATH, ).click()                                 
    time.sleep(3)
    attach(data=driver.get_screenshot_as_png())
    print('Tambah satu')
        

@mark.fixture_Penerimaan
def test_drop_jenis_registrasi():
    driver.find_element(By.ID, 'input_jenis_registrasi_baran_basan').click()
    if jenis_registrasi == 'Register Barang Rampasan Negara':
        driver.find_element(By.ID,'RBR').click()
    elif jenis_registrasi == 'Tingkat Penyidikan':
        driver.find_element(By.ID, 'RBS1').click()
    elif jenis_registrasi == 'Tingkat Penuntutan':
        driver.find_element(By.ID, 'RBS2').click()
    elif jenis_registrasi == 'Tingkat Pengadilan Negeri':
        driver.find_element(By.ID, 'RBS3').click
    elif jenis_registrasi == 'Tingkat Pengadilan Tinggi':
        driver.find_element(By.ID, 'RBS4').click
    attach(data=driver.get_screenshot_as_png())
    print('terpilih satu')

@mark.fixture_Penerimaan
def test_date():
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[1]/div[2]/div/div[1]/input').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[1]/div[2]/div/div[1]/input').send_keys(tgl_penerimaan)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
    attach(data=driver.get_screenshot_as_png())
    print('inputdate')
        

@mark.fixture_Penerimaan
def test_input():
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[1]/div[3]/div/div[1]/input').send_keys(No_Reg_Rupbasan)
    attach(data=driver.get_screenshot_as_png())
    print('akses_menu')
        

@mark.fixture_Penerimaan
def test_back():
    driver.find_element(By.ID, 'backButton').click()
    attach(data=driver.get_screenshot_as_png())
    print('sudah kembali')

