from turtle import rt
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import os, sys
from os import environ, path
import pyautogui
from pytest import mark
import pytest
import time
import platform
from pathlib import Path
import logging
from faker import Faker
from datetime import datetime
import openpyxl
from faker.providers import date_time
from datetime import datetime, timedelta
import random
from pytest_html_reporter import attach
import pyautogui

import sys
from os import environ, path
from dotenv import load_dotenv
load_dotenv()
from openpyxl import load_workbook


fake = Faker('id_ID')
from dotenv import load_dotenv
load_dotenv()

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR"))

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))


from Settings.SetupAll import *
from Settings.login import *
from Settings.Page.accessmenu import *

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Registrasi.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


@mark.webtest()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')

@mark.webtest()
def test_2_login():
    sorong(driver)
    Log.info('Login')


@mark.webtest()
def test_Input():
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Lainlain']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Daftar Pegawai').click()
    print('.')
    Log.info('Akses halaman Lainlian Daftar Pegawai')
    attach(data=driver.get_screenshot_as_png())
        # nge baca mulai dari tabel A
    while True:
        number = fake.random_int(min=0, max=100) 
       
        Nip                             = fake.year()+"1"f"{number+1:05}"
        Nama                            = fake.name()
        TempatLahir                     = fake.city()
        tanggal_lahir_acak              = fake.date_of_birth(tzinfo=None, minimum_age=23, maximum_age=50)
        TanggalLahir                    = tanggal_lahir_acak.strftime('%d/%m/%Y')
        JenisKelamin                    = random.choice(['L','P'])
        Alamat                          = fake.address()
        Jabatan                         = fake.job()
        Pangkat                         = fake.job()
        Golongan                        = fake.job()
        Bagian                          = fake.job()
        Email                           = fake.email()
        Telepon                         = fake.phone_number()
        
        driver.implicitly_wait(30)


        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
            driver.find_element(By.ID, "createButton").click()
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'Nip')))

            driver.find_element(By.ID, "Nip").click()
            driver.find_element(By.ID, "Nip").send_keys(Nip)
            driver.find_element(By.ID, "Nip").send_keys(fake.random_int(min=0, max=100))

            driver.find_element(By.ID, "Nama").send_keys(Nama)
            driver.find_element(By.ID, "tempatLahir").send_keys(TempatLahir)
            driver.find_element(By.ID, "tglLahir").click()
            driver.find_element(By.ID, "tglLahir").send_keys(TanggalLahir)
            driver.find_element(By.ID, "tglLahir").send_keys(Keys.ENTER)

            driver.find_element(By.ID, "jenisKelamin").click()
            if JenisKelamin == 'P':
                driver.find_element(By.ID, "Perempuan").click()
            else:
                driver.find_element(By.ID, "Laki-laki").click()
            
            driver.find_element(By.ID, "Alamat").click()
            driver.find_element(By.ID, "Alamat").send_keys(Alamat)

            driver.find_element(By.ID, "Jabatan").click()
            driver.find_element(By.ID, "Jabatan").send_keys(Jabatan)

            driver.find_element(By.ID, "Pangkat").click()
            driver.find_element(By.ID, "Pangkat").send_keys(Pangkat)

            driver.find_element(By.ID, "Golongan").click()
            driver.find_element(By.ID, "Golongan").send_keys(Golongan)

            driver.find_element(By.ID, "Bagian").click()
            driver.find_element(By.ID, "Bagian").send_keys(Bagian)

            driver.find_element(By.ID, "Email").click()
            driver.find_element(By.ID, "Email").send_keys(Email)

            driver.find_element(By.ID, "Telepon").click()
            driver.find_element(By.ID, "Telepon").send_keys(Telepon)

            driver.find_element(By.ID, 'submitButton').click()
                    
        except TimeoutException:
            print("ERRROR")
            pass
        # time.sleep(5)
        # i = i + 1

  
        

@mark.webtest()
def test_exit():
    quit(driver)




