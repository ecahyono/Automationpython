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
import os
import pyautogui
import pytest
import time

from pathlib import Path

@pytest.fixture()
def test_setup():
    global driver
    s = Service(r'C:\Users\user\Documents\TRCH\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    # url = "http://kumbang.torche.id:32400/"
    url = "http://192.168.2.11:32400/"

    driver.get(url)
    # seting windows nya jadi max   
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield
    driver.close()
    driver.quit()
    
def test_Web(test_setup):
    wb = load_workbook(filename=r"C:\Users\user\Documents\TRCH\Automationpython\Filexel\Registrasi.xlsx")
    # jadi ini bisa read sheet yang dibawah itu yang di excel
    sheetrange = wb['sursidang']
    # Menuju login
    driver.find_element(By.XPATH, "//div/span").click()
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("rono")
    driver.find_element(By.ID, "password").send_keys("rene")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    time.sleep(3)
    #Registrasi
    element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/nav/ul/li[1]/div")                                   
    time.sleep(1)
    actions = ActionChains(driver)
    time.sleep(1)
    actions.move_to_element(element).perform()
    time.sleep(1)
    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx anak ke 2
    element2 = driver.find_element(By.XPATH, "//div/ul/li[2]/div")
    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx anak ke 2
    time.sleep(2)
    actions2 = ActionChains(driver)
    actions2.move_to_element(element2).perform()
    #Surat Sidang
    driver.find_element(By.LINK_TEXT, "Surat Sidang").click()
    time.sleep(1)

    i = 4
    while i <= len(sheetrange['A']):
        Lokasi_Sidang       = sheetrange['A'+str(i)].value
        NoS_jaksa           = sheetrange['B'+str(i)].value
        Asal_Surat          = sheetrange['C'+str(i)].value
        Kasi_Pelayanan      = sheetrange['D'+str(i)].value
        Petugas_Penerima    = sheetrange['E'+str(i)].value
        nos_Internal        = sheetrange['F'+str(i)].value
        tgl_Surat           = sheetrange['G'+str(i)].value
        tgl_sidang          = sheetrange['H'+str(i)].value
        nip_kasip           = sheetrange['I'+str(i)].value
        nippetgs            = sheetrange['J'+str(i)].value
        jlmpsrt             = sheetrange['K'+str(i)].value
        peserta             = sheetrange['L'+str(i)].value
        peserta2            = sheetrange['M'+str(i)].value
        peserta3            = sheetrange['N'+str(i)].value
        peserta4            = sheetrange['O'+str(i)].value
        peserta5            = sheetrange['P'+str(i)].value
        
        time.sleep(2) 
        #button +Tambah
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/div[1]/button").click()                                 
        try :
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[1]/div/div/div/input').click()
            pyautogui.typewrite(Lokasi_Sidang)
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[3]/div/div/div[1]/input').click()
            pyautogui.typewrite(NoS_jaksa)
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[5]/div/div/div[1]/input').click()
            pyautogui.typewrite(Asal_Surat)
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[7]/div/div/div[1]/input').click()
            pyautogui.typewrite(Kasi_Pelayanan)
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[9]/div/div/div[1]/input').click()
            pyautogui.typewrite(Petugas_Penerima)
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[2]/div/div/div[1]/input').click()
            pyautogui.typewrite(nos_Internal)
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[4]/div/div/div[1]/input').click()
            pyautogui.typewrite(tgl_Surat)
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[4]/div/div/div[1]/input').send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[6]/div/div/div/input').click()
            pyautogui.typewrite(tgl_sidang)
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[6]/div/div/div/input').send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[8]/div/div/div/input').click()
            pyautogui.typewrite(nip_kasip)
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[10]/div/div/div/input').click()

            pyautogui.typewrite(nippetgs)
            #submit
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[2]/button[2]').click()
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]/div/form')))
            time.sleep(5)
            #tambah Peserta
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/form/button').click()
            
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div/div/div[2]')))
            time.sleep(3)
            #kondisi
            # driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[1]/div/div/label/span').click()
            # time.sleep(1)
            # driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[2]/td[1]/div/div/label/span').click()
            # time.sleep(1)
            # driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[3]/td[1]/div/div/label/span').click()
            # time.sleep(1)
            # driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[4]/td[1]/div/div/label/span').click()
            # time.sleep(1)
            # driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[5]/td[1]/div/div/label/span').click()
            # time.sleep(1)
            if jlmpsrt == 1 and peserta == 'HOHOi BIN ^':
                driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[4]/td[1]/div/div/label/span/span').click()
            elif jlmpsrt == 2 :
                driver.find_element(By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/table/tbody/tr/td/div/div/label/span/span').click()
                driver.find_element(By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/table/tbody/tr[2]/td/div/div/label/span/span').click()
            elif jlmpsrt == 3 :
                driver.find_element(By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/table/tbody/tr/td/div/div/label/span/span').click()
                driver.find_element(By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/table/tbody/tr[2]/td/div/div/label/span/span').click()
                driver.find_element(By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/table/tbody/tr[3]/td/div/div/label/span/span').click()
            elif jlmpsrt == 4 :
                driver.find_element(By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/table/tbody/tr/td/div/div/label/span/span').click()
                driver.find_element(By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/table/tbody/tr[2]/td/div/div/label/span/span').click()
                driver.find_element(By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/table/tbody/tr[3]/td/div/div/label/span/span').click()
                driver.find_element(By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/table/tbody/tr[4]/td/div/div/label/span/span').click()
            elif jlmpsrt == 5 :
                driver.find_element(By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/table/tbody/tr/td/div/div/label/span/span').click()
                driver.find_element(By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/table/tbody/tr[2]/td/div/div/label/span/span').click()
                driver.find_element(By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/table/tbody/tr[3]/td/div/div/label/span/span').click()
                driver.find_element(By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/table/tbody/tr[4]/td/div/div/label/span/span').click()
                driver.find_element(By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/table/tbody/tr[5]/td/div/div/label/span/span').click()
            print('wprk')
            driver.find_element(By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[3]/button[2]/span').click()
            time.sleep(5)
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/form/div[4]/button[2]').click()
        except TimeoutException:
                print('ERROR')
                pass
        time.sleep(4)   
        i = i + 1
    print ("Success Created")
