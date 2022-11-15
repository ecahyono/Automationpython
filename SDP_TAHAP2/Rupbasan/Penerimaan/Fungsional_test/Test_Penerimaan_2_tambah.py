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

from module.setup import initDriver, loadDataPath
from module.login import login

# init driver by os
@mark.fixture_Tambah_penerimaan
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_Tambah_penerimaan
def test_login():
    login(driver)

@mark.fixture_Tambah_penerimaan
def test_akses_menu():
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.LINK_TEXT, 'Penerimaan').click()
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_Tambah_penerimaan
def test_Buka_halaman_tambah():
    driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['tambah']).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, pathData ['Id Navigate Button']['Back Button'])))

@mark.fixture_Tambah_penerimaan
def test_input_text():
    driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Nomor Registrasi Rupbasan']).send_keys('NoRegRup-001')
    driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Nomor Registrasi Instansi']).send_keys('NoRegIns-001')
    driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Nomor Surat Izin Penyitaan']).send_keys('NoSurIzPen-001')
    driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Nomor Surat Penyitaan']).send_keys('NoSurPen-001')
    driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Pasal']).send_keys('Pasal 1 Ayat 1 No 5')
    driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['No. BA Serah Terima']).send_keys('NoBASerTrim-001')

@mark.fixture_Tambah_penerimaan
def test_Input_text_area():
    driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Keterangan']).send_keys('*&+_-Keterangan @ Penerimaan Rupb454N')

@mark.fixture_Tambah_penerimaan
def test_Input_date():
    Tanggal_Penerimaan = driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Tanggal Penerimaan'])
    Tanggal_Penerimaan.click()
    Tanggal_Penerimaan.send_keys('01/11/2022')
    Tanggal_Penerimaan.send_keys(Keys.ENTER)

    Tanggal_Surat_Izin_Penyitaan = driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Tanggal Surat Izin Penyitaan'])
    Tanggal_Surat_Izin_Penyitaan.click()
    Tanggal_Surat_Izin_Penyitaan.send_keys('01/11/2022')
    Tanggal_Surat_Izin_Penyitaan.send_keys(Keys.ENTER)

    Tanggal_Surat_Penyitaan = driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Tanggal Surat Penyitaan'])
    Tanggal_Surat_Penyitaan.click()
    Tanggal_Surat_Penyitaan.send_keys('01/11/2022')
    Tanggal_Surat_Penyitaan.send_keys(Keys.ENTER)

@mark.fixture_Tambah_penerimaan
def test_Input_dropdown():
    Jenis_Registrasi = driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Jenis Registrasi'])
    Jenis_Registrasi.click()
    time.sleep(2)
    Jenis_Registrasi.send_keys('Register Barang Rampasan Negara')
    Jenis_Registrasi.send_keys(Keys.DOWN)
    Jenis_Registrasi.send_keys(Keys.ENTER)
    
    Instansi = driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Instansi'])
    Instansi.click()
    time.sleep(2)
    Instansi.send_keys('POLDA METRO JAYA')
    Instansi.send_keys(Keys.DOWN)
    Instansi.send_keys(Keys.ENTER)

    Pengadilan_Penyita = driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Pengadilan Penyita'])
    Pengadilan_Penyita.click()
    time.sleep(2)
    Pengadilan_Penyita.send_keys('Pengadilan Negeri Jakarta Pusat barat')
    Pengadilan_Penyita.send_keys(Keys.DOWN)
    Pengadilan_Penyita.send_keys(Keys.ENTER)

    Petugas_Penerima = driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Petugas Penerima'])
    Petugas_Penerima.click()
    Petugas_Penerima.send_keys('Ananda Septiana Lestari')
    driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1)> .el-descriptions__label ').click()
    time.sleep(2)
    PetugasygMenyerahkan = driver.find_element(By.XPATH, pathData['Rupbasan']['+rupbasan']['Petugas yang Menyerahkan'])
    PetugasygMenyerahkan.click()
    PetugasygMenyerahkan.send_keys('Rehan')
    element = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1)> .el-descriptions__label ')
    driver.implicitly_wait(10)
    ActionChains(wait).move_to_element(element).click(element).perform()

