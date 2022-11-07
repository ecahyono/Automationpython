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

from dotenv import load_dotenv
load_dotenv()



#file modul
from module.setup import initDriver, loadDataPath
from module.login import login

import json

# init driver by os
@mark.fixture_Penerimaan
def test_init():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_Penerimaan
def test_login():
    login(driver)

@mark.fixture_Penerimaan
def test_akses_menu():
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.LINK_TEXT, 'Penerimaan').click()
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Penerimaan
def test_halaman_Ubah():
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['ubah']).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['Id Navigate Button']['Back Button'])))
    driver.find_element(By.XPATH, pathData ['Id Navigate Button']['Back Button']).click()
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Penerimaan
def test_sortirtabel():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['AksesMenu']['Rupbasan']['button']['daftarbarang'])))
    driver.find_element(By.XPATH, pathData ['AksesMenu']['Rupbasan']['button']['ascendingtable']).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['AksesMenu']['Rupbasan']['button']['daftarbarang'])))

    time.sleep(3)
    driver.find_element(By.XPATH, pathData ['AksesMenu']['Rupbasan']['button']['descendingtable']).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['AksesMenu']['Rupbasan']['button']['daftarbarang'])))


@mark.fixture_Penerimaan
def test_halaman_tambah():
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['tambah']).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['Id Navigate Button']['Back Button'])))
    driver.find_element(By.XPATH, pathData ['Id Navigate Button']['Back Button']).click()
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Penerimaan
def test_halaman_Daftarbarang():
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['daftarbarang']).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['Id Navigate Button']['Back Button'])))
    driver.find_element(By.XPATH, pathData ['Id Navigate Button']['Back Button']).click()
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Penerimaan
def test_halaman_cetakBA():
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['CetakBA']).click() 
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Penerimaan
def test_halaman_exportexel():
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['exportexel']).click() 
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Penerimaan
def test_halaman_exportexelsemuahal():
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['excelsemuhalaman']).click() 
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Penerimaan
def test_halaman_exportexelhalinisaj():
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['excelHalamaninisaja']).click() 
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Penerimaan
def test_halaman_exportpdf():
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['exportPDF']).click() 
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Penerimaan
def test_halaman_pdfsemuahal():
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['pdfsemuaH']).click() 
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Penerimaan
def test_halaman_pdfhalinisaj():
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['pdfhinisaj']).click() 
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Penerimaan
def test_halaman_print():
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['cetak']).click() 
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Penerimaan
def test_halaman_printsemuahal():
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['cetaksemua']).click() 
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Penerimaan
def test_halaman_printhalinisaj():
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['cetakhalinisaj']).click() 
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_Penerimaan
def test_pageindex20hal():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['AksesMenu']['Rupbasan']['button']['daftarbarang'])))
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['pilihpage']).click() 

    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['20halaman']).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['AksesMenu']['Rupbasan']['button']['daftarbarang'])))
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Penerimaan
def test_pageindex50hal():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['AksesMenu']['Rupbasan']['button']['daftarbarang'])))
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['pilihpage']).click() 

    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['50halaman']).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['AksesMenu']['Rupbasan']['button']['daftarbarang'])))
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Penerimaan
def test_pageindex100hal():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['AksesMenu']['Rupbasan']['button']['daftarbarang'])))
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['pilihpage']).click() 

    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['100halaman']).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['AksesMenu']['Rupbasan']['button']['daftarbarang'])))
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Penerimaan
def test_pageindex5hal():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['AksesMenu']['Rupbasan']['button']['daftarbarang'])))
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['pilihpage']).click() 

    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['button']['5halaman']).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pathData ['AksesMenu']['Rupbasan']['button']['daftarbarang'])))
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Penerimaan
def test_pergikepage():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, pathData ['AksesMenu']['Rupbasan']['button']['daftarbarang'])))
    driver.find_element(By.XPATH, pathData['Other Search']['Pergi Ke']).send_keys(Keys.BACK_SPACE)
    time.sleep(3)
    driver.find_element(By.XPATH, pathData['Other Search']['Pergi Ke']).send_keys('4')
    driver.find_element(By.XPATH, pathData['Other Search']['Pergi Ke']).send_keys(Keys.ENTER)

# search masih belum berfungsi
