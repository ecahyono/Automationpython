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

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))


from Settings.setup import initDriver, loadDataPath, quit, sleep
from Settings.login import loginSumedang, loginBanjar, loginBpsBdg, loginBogor

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Registrasi.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("Lainlain"))
sheetrange = wb['Pegawai']

@mark.fixture_test()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')

@mark.fixture_test()
def test_2_login():
    loginBogor(driver)
    Log.info('Login')


@mark.fixture_test()
def test_Input():
    driver.implicitly_wait(60)
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Lainlain']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Daftar Pegawai').click()
    print('.')
    Log.info('Akses halaman Lainlian Daftar Pegawai')
    attach(data=driver.get_screenshot_as_png())

    i = 2
        # nge baca mulai dari tabel A
    while i <= len(sheetrange['A']):
        # deklarasi bahwa NIP itu ada di A 
        Nip                             = sheetrange['A'+str(i)].value
        Nama                            = sheetrange['B'+str(i)].value
        TempatLahir                     = sheetrange['C'+str(i)].value
        TanggalLahir                    = sheetrange['D'+str(i)].value
        JenisKelamin                    = sheetrange['E'+str(i)].value
        Alamat                          = sheetrange['F'+str(i)].value
        Jabatan                         = sheetrange['G'+str(i)].value
        Pangkat                         = sheetrange['H'+str(i)].value
        Golongan                        = sheetrange['I'+str(i)].value
        Bagian                          = sheetrange['J'+str(i)].value
        Email                           = sheetrange['K'+str(i)].value
        Telepon                         = sheetrange['L'+str(i)].value
        
        driver.implicitly_wait(30)


        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
            driver.find_element(By.ID, "createButton").click()

            driver.find_element(By.ID, "Nip").click()
            driver.find_element(By.ID, "Nip").send_keys(Nip)

            driver.find_element(By.ID, "Nama").send_keys(Nama)
            driver.find_element(By.ID, "tempatLahir").send_keys(TempatLahir)
            driver.find_element(By.ID, "tglLahir").send_keys(TanggalLahir)


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
            print("MASIH ADA ERROR, CEK LAGI PAK WIL")
            pass
        time.sleep(5)
        i = i + 1
        print(i)

  
        

@mark.fixture_test()
def test_exit():
    quit(driver)




