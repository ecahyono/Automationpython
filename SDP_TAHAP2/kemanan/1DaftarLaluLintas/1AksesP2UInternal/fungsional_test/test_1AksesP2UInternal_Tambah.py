from distutils.archive_util import make_archive
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
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
from Settings.login import loginOperatorSumedang, Op_Keamanan_p2u

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Log1_P2Uinternal.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("KeamananUAT"))
sheetrangeIndex = wb['P2U_Internal']

@mark.fixture_test()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')

@mark.fixture_test()
def test_2_login():
    Op_Keamanan_p2u(driver)
    Log.info('Login Operator Keamanan P2U')


@mark.fixture_test()
def test_3_Input():
    print('.')

    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Akses P2U Internal').click()
    sleep(driver)
    print('.')
    Log.info('Akses halaman Daftar Lalu Lintas P2U Internal')
    attach(data=driver.get_screenshot_as_png())


    i = 2
        
    while i <= len(sheetrangeIndex['A']):
    
        NamaInput                                 = sheetrangeIndex['A'+str(i)].value
        Nosk                                      = sheetrangeIndex['B'+str(i)].value
        jenisKeluar                               = sheetrangeIndex['C'+str(i)].value
        TanggalKeluar                             = sheetrangeIndex['D'+str(i)].value
        tanggalKembali                            = sheetrangeIndex['E'+str(i)].value
        deskripsi                                 = sheetrangeIndex['F'+str(i)].value
        JenisPengawal                             = sheetrangeIndex['G'+str(i)].value
        namaPengawalExternal                      = sheetrangeIndex['H'+str(i)].value
        namaPengawalInternal                      = sheetrangeIndex['I'+str(i)].value
                
        driver.implicitly_wait(10)


        try:
            print('.')
            print('Click Button Create')
            sleep(driver)
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
            driver.find_element(By.ID, 'createButton').click()
            Log.info('Click Button Create')


            print('Pilih Dropdown Nama')
            sleep(driver)
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))

            attach(data=driver.get_screenshot_as_png())
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))

            print('== NEXT == Input kata kunci nama')
            sleep(driver)
            driver.find_element(By.XPATH, '//*[@id="kataKunci"]').clear()
            driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NamaInput)
            Log.info('Search Nama WBP')
            driver.find_element(By.ID, 'buttonSearch' ).click()
            Log.info('Click Button Search')
            sleep(driver)

            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
            driver.find_element(By.CSS_SELECTOR, ".h-5 > path").click()
            Log.info('Click Button Detile')
            
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'createButton')))
            driver.find_element(By.ID, 'createButton').click()
            Log.info('Click Button Tambah WBP')

            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'buttonSubmit')))
            driver.find_element(By.ID, 'noSK').send_keys(Nosk)
            Log.info('Input No SK')

            sleep(driver)
            driver.find_element(By.XPATH, "//div[@id=\'fileSK\']/div/button").click()
            
            sleep(driver)
            pyautogui.write("///////users/will/test.pdf")
            pyautogui.press('return')
            pyautogui.write("///////users/will/test.pdf")
        
            pyautogui.press('return')
            time.sleep(0.5)
            pyautogui.press('escape')
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(0.5)
            Log.info('Upload SK')

            driver.find_element(By.ID, 'jenisKeluar').click()
            sleep(driver)
            
            if jenisKeluar == 'Pembebasan Bersyarat':
                driver.find_element(By.ID, 'jenisKeluar').send_keys('Pembebasan Bersyarat')
                driver.find_element(By.XPATH, "//li[contains(.,\'Pembebasan Bersyarat\')]").click()

            elif jenisKeluar == 'Anak Kembali ke Orang Tua':
                driver.find_element(By.ID, 'jenisKeluar').send_keys('Anak Kembali ke Orang Tua')
                driver.find_element(By.XPATH, "//li[contains(.,\'Anak Kembali ke Orang Tua\')]").click()

            elif jenisKeluar == 'Asimilasi':
                driver.find_element(By.ID, 'jenisKeluar').send_keys('Asimilasi')
                driver.find_element(By.XPATH, "//li[contains(.,\'Asimilasi\')]").click()

            elif jenisKeluar == 'Asimilasi di Rumah':
                driver.find_element(By.ID, 'jenisKeluar').send_keys('Asimilasi di Rumah')
                driver.find_element(By.XPATH, "//li[contains(.,\'Asimilasi di Rumah\')]").click()

            elif jenisKeluar == 'Bebas Biasa':
                driver.find_element(By.ID, 'jenisKeluar').send_keys('Bebas Biasa')
                driver.find_element(By.XPATH, "//li[contains(.,\'Bebas Biasa\')]").click()

            elif jenisKeluar == 'Bebas dari Dakwaan':
                driver.find_element(By.ID, 'jenisKeluar').send_keys('Bebas dari Dakwaan')
                driver.find_element(By.XPATH, "//li[contains(.,\'Bebas dari Dakwaan\')]").click()

            elif jenisKeluar == 'Bebas Dari Tuntutan':
                driver.find_element(By.ID, 'jenisKeluar').send_keys('Bebas Dari Tuntutan')
                driver.find_element(By.XPATH, "//li[contains(.,\'Bebas Dari Tuntutan\')]").click()

            elif jenisKeluar == 'Cuti Menjelang Bebas':
                driver.find_element(By.ID, 'jenisKeluar').send_keys('Cuti Menjelang Bebas')
                driver.find_element(By.XPATH, "//li[contains(.,\'Cuti Menjelang Bebas\')]").click()

            elif jenisKeluar == 'Cuti Bersyarat':
                driver.find_element(By.ID, 'jenisKeluar').send_keys('Cuti Bersyarat')
                driver.find_element(By.XPATH, "//li[contains(.,\'Cuti Bersyarat\')]").click()

            elif jenisKeluar == 'Dikeluarkan Demi Hukum':
                driver.find_element(By.ID, 'jenisKeluar').send_keys('Dikeluarkan Demi Hukum')
                driver.find_element(By.XPATH, "//li[contains(.,\'Dikeluarkan Demi Hukum\')]").click()

            elif jenisKeluar == 'Dikembalikan ke Pihak Penahan':
                driver.find_element(By.ID, 'jenisKeluar').send_keys('Dikembalikan ke Pihak Penahan')
                driver.find_element(By.XPATH, "//li[contains(.,\'Dikembalikan ke Pihak Penahan\')]").click()

            elif jenisKeluar == 'Dirawat Dirumah Sakit':
                driver.find_element(By.ID, 'jenisKeluar').send_keys('Dirawat Dirumah Sakit')
                driver.find_element(By.XPATH, "//li[contains(.,\'Dirawat Dirumah Sakit\')]").click()

            elif jenisKeluar == 'Diversi':
                driver.find_element(By.ID, 'jenisKeluar').send_keys('Diversi')
                driver.find_element(By.XPATH, "//li[contains(.,\'Diversi\')]").click()

            Log.info('Input Jenis Keluar')

            driver.find_element(By.ID, "keluarKeamanan").click()
            sleep(driver)
            driver.find_element(By.ID, "keluarKeamanan").send_keys(TanggalKeluar)
            Log.info('Input Tanggal Keluar')
            sleep(driver)

            driver.find_element(By.ID, "tanggalKembali").click()
            sleep(driver)
            driver.find_element(By.ID, "tanggalKembali").send_keys(tanggalKembali)
            Log.info('Input Tanggal Kembali')

            driver.find_element(By.ID, "deskripsi").click()
            driver.find_element(By.ID, "deskripsi").send_keys(deskripsi)
            Log.info('Input Deskripsi')

            driver.find_element(By.ID, "jenis0").click()
            sleep(driver)
            if JenisPengawal == 'Eksternal':
                driver.find_element(By.ID, "Eksternal0").click()
                driver.find_element(By.ID, 'pengawal0').click()
                driver.find_element(By.XPATH, "//td[contains(.,'"+ namaPengawalExternal +"')]").click()
                Log.info('input pengawal external')

            elif JenisPengawal == 'Internal':
                driver.find_element(By.ID, "Internal0").click()
                driver.find_element(By.ID, 'pengawalInternal0').click()
                driver.find_element(By.XPATH, "//td[contains(.,'"+ namaPengawalInternal +"')]").click()
                Log.info('input pengawal internal')

            driver.find_element(By.ID, 'buttonSubmit').click()
            Log.info('click button submit')

                
        
            sleep(driver)


        except TimeoutException:
            print("ERRROR")
            pass
                
        sleep(driver)
        i = i + 1
    print('DONE')

def teardown():
    quit(driver)

        

  
        






