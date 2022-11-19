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


from module.setup import initDriver, loadDataPath, buttonTambah
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

    driver.find_element(By.LINK_TEXT, "Sektor Gudang").click()
    attach(data=driver.get_screenshot_as_png())

driver.find_element(By.ID, "createButton").click()

driver.find_element(By. XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[1]/div[2]/div/div/input').send_keys('Test Sektor Pribadi')
driver.find_element(By. XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[1]/div[3]/div/div/input').send_keys('12000')
driver.find_element(By. XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div[2]/div/div/div/textarea').send_keys('Keterangan di dalam Sektor gudang')

driver.find_element(By. XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[1]/div/div/div[1]/div/div/input').send_keys('Baris aman')

nourut = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[1]/div/div/div[2]/div/div/div/div/div')
for x in range(5):
    x = nourut.click()

Gudang = driver.find_element(By.ID, 'input_kondisi_baran_basan')
Gudang.click()
time.sleep(2)
Gudang.send_keys('Gudang Berharga')
Gudang.send_keys(Keys.DOWN)
Gudang.send_keys(Keys.ENTER)

driver.find_element(By.ID, 'submitButton').click()

# i =3 

# while i <= len(sheetrange['A']):
#     Id_Lookup = sheetrange['A'+str(i)].value
#     Groups = sheetrange['B'+str(i)].value
#     Deskripsi = sheetrange['C'+str(i)].value
#     Catatan = sheetrange['D'+str(i)].value

#     time.sleep(1)

#     # driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/div[1]/button").click()
#     

#     try:
#         WebDriverWait(driver,6).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div/h1')))
#         time.sleep(2)
#         driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/input').send_keys(Id_Lookup)

#         driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[2]/div/div/div/div/input').click()
#         driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[2]/div/div/div/div/input').send_keys(Groups)
#         driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[2]/div/div/div/div/input').send_keys(Keys.DOWN)
#         driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[2]/div/div/div/div/input').send_keys(Keys.ENTER)

#         driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div[1]/input').send_keys(Deskripsi)

#         driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[4]/div/div/textarea').send_keys(Catatan)
        
#         driver.find_element(By.ID, 'submitButton').click()
#     except TimeoutException:
#         pass
#     i = i + 1
# print ("Success Created")