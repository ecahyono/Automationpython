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
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, pathData['Other Search']['Search Button'])))
    field = driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['filterabledropdownindex'])
    field.click()
    field.send_keys('No Registrasi')
    field.send_keys(Keys.DOWN)
    field.send_keys(Keys.ENTER)

    katkun = driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['maskakunci'])
    katkun.click()
    katkun.send_keys('124436487')
    driver.find_element(By.XPATH, pathData['Other Search']['Search Button']).click()
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, pathData['Other Search']['Search Button'])))
    time.sleep(3)
    driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['daftarbarang']).click()

###Kelengkapan Basan & Baran
@mark.fixture_Barang_penerimaan
def test_Tambah_Daftarbarang_TabKBB():
    driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['Nama Barang']).send_keys('Barang nama barang')
    driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['Jumlah']).send_keys('5')
    driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['Jumlah Baik']).send_keys('5')
    driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['jumlah Rusak Ringan']).send_keys('5')
    driver.find_element(By.XPATH, pathData['Rupbasan']['indexrupbasan']['Jumlah Rusak Berat']).send_keys('5')
    
    Jenis_Barang = driver.find_element(By.ID, 'input_jenis_baran_basan')
    Jenis_Barang.click()
    Jenis_Barang.send_keys('berharga')
    Jenis_Barang.send_keys(Keys.DOWN)
    Jenis_Barang.send_keys(Keys.ENTER)

    Satuan = driver.find_element(By.ID, 'input_satuan_baran_basan')
    Satuan.click()
    Satuan.send_keys('Unit')
    Satuan.send_keys(Keys.DOWN)
    Satuan.send_keys(Keys.ENTER)

# def test_Tambah_Daftarbarang_TabPenelitian():
def test_pindah_tab_penelitian():
    driver.find_element(By.ID, 'tab-penelitian').click()

    pilihgolongan = driver.find_element(By. XPATH, pathData['Rupbasan']['barangrupbasan']['Golongan'])
    pilihgolongan.click()
    pilihgolongan.send_keys('Senjata Tajam')
    pilihgolongan.send_keys(Keys.DOWN)
    pilihgolongan.send_keys(Keys.ENTER)

    kondisibarang = driver.find_element(By.ID, 'input_kondisi_baran_basan')
    kondisibarang.click()
    kondisibarang.send_keys('Baik')
    kondisibarang.send_keys(Keys.DOWN)
    kondisibarang.send_keys(Keys.ENTER)

    subkondisibarang = driver.find_element(By.ID, 'input_sub_kondisi_baran_basan')
    subkondisibarang.click()
    subkondisibarang.send_keys('rusak ringan')
    subkondisibarang.send_keys(Keys.DOWN)
    subkondisibarang.send_keys(Keys.ENTER)

    PemeliharaanKhusus = driver.find_element(By.XPATH, pathData['Rupbasan']['barangrupbasan']['PemeliharaanKhusus'])
    PemeliharaanKhusus.click()
    PemeliharaanKhusus.send_keys('kendaraan')
    PemeliharaanKhusus.send_keys(Keys.DOWN)
    PemeliharaanKhusus.send_keys(Keys.ENTER)

    driver.find_element(By.XPATH, pathData['Rupbasan']['barangrupbasan']['Nomor Penelitian']).send_keys('NoPen/003')
    driver.find_element(By.XPATH, pathData['Rupbasan']['barangrupbasan']['Nomor SK Peneliti']).send_keys('NoSKPen/003')
    driver.find_element(By.XPATH, pathData['Rupbasan']['barangrupbasan']['Keadaan Segel Penyita']).send_keys('Keadaan Segel Penyita02p')
    driver.find_element(By.XPATH, pathData['Rupbasan']['barangrupbasan']['Sifat']).send_keys('Sdd3ifat02p')
    driver.find_element(By.XPATH, pathData['Rupbasan']['barangrupbasan']['Merek Dan Kondisi']).send_keys('Merek Dan Kondisi 0987')
    driver.find_element(By.XPATH, pathData['Rupbasan']['barangrupbasan']['Berat']).send_keys('Berat')
    driver.find_element(By.XPATH, pathData['Rupbasan']['barangrupbasan']['Berat']).send_keys('Berat')

