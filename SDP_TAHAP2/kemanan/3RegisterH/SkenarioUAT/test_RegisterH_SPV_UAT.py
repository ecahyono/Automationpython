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
import pyautogui

import sys
from os import environ, path
from dotenv import load_dotenv
load_dotenv()
from openpyxl import load_workbook

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR"))
    wb = load_workbook(environ.get("KeamananUAT"))

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))


from Settings.setup import initDriver, loadDataPath, quit, buttonTambah, buttonSubmit, selectKategoriPegawai, selectKategoriTamuDinas, sleep
from Settings.login import login

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('RegisterH_UAT.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrangeindex = wb['RegisterH_Index']
print(".")
print("Halaman index, masukan baris yang akan dibaca. . .")

index  = input("")


@mark.fixture_test()
def test_RTH_007():
    print(' == NEXT == ( RTH-007 ) / Melakukan Perpanjangan Pengasingan ')
    sleep(driver)

    print(
        ' == NEXT ==  - ( RTH-004 ) / Melakukan pencarian data identitas WBP lalu mendaftarkannya dengan memilih kategori pencarian kemudian input kata kunci dan klik button Cari')
    driver.implicitly_wait(60)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'filterColumn')))
    sleep(driver)
    driver.find_element(By.ID, 'filterColumn').click()

    if filterColumnTambah == 'nama':
        sleep(driver)
        driver.find_element(By.ID, 'filterColumn').send_keys('nama')
        Log.info('Klik Search Kategori berdasarkan Nama')
        attach(data=driver.get_screenshot_as_png())

        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="nama"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.ID, 'kataKunci').send_keys(namaTambah)
        Log.info('search Nama')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnTambah == 'jenisKejahatan':
        sleep(driver)
        driver.find_element(By.ID, 'filterColumn').send_keys('jenis')
        Log.info('Klik Search Kategori berdasarkan semua')
        attach(data=driver.get_screenshot_as_png())

        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="jenisKejahatan"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.ID, 'kataKunci').send_keys(jenisKejahatanTambah)
        Log.info('search Jenis Kejahatan')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnTambah == 'noRegistrasi':
        sleep(driver)
        driver.find_element(By.ID, 'filterColumn').send_keys('No')
        Log.info('Klik Search Kategori berdasarkan semua')
        attach(data=driver.get_screenshot_as_png())

        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="nomorReg"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.ID, 'kataKunci').send_keys(noRegistrasiTambah)
        Log.info('search Nomor Registrasi')
        attach(data=driver.get_screenshot_as_png())

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    Log.info('Klik Button Search')
    attach(data=driver.get_screenshot_as_png())

    Log.info('(BERHASIL RTH-004) / Menampilkan data WBP sesuai kategori yang dipilih dan kata kunci yang diinputkan')

    Log.info('(RTH-006) / Menampilkan alert berhasil kemudian data ditampilkan pada tabel Halaman Daftar Pengasingan')
    attach(data=driver.get_screenshot_as_png())