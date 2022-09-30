from json import load
from lib2to3.pgen2 import driver
import string
from turtle import rt
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys 

from openpyxl import load_workbook
import time
import pyautogui

wb = load_workbook(filename=r"C:\Users\wilda\Documents\Automationpython\Backup\contohkasus.xlsx")
sheetrange = wb['drpif']
drpif = sheetrange['A2'].value

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://demoqa.com/select-menu')

 #======================== AKSI lain ============================

driver.find_element(By.XPATH, "//div[2]/div[2]/div[2]/div[2]/div/div/div/div").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[2]/div[2]/div[2]/div[2]/div/div/div/div").click()

 #======================== Dropdown If ============================

if drpif == 'Black' :
            dropdown = driver.find_element(By.ID, "oldSelectMenu")
            dropdown.find_element(By.XPATH, "//option[. = 'Black']").click()
elif drpif == 'Red' :
            dropdown = driver.find_element(By.ID, "oldSelectMenu")
            dropdown.find_element(By.XPATH, "//option[. = 'Red']").click()
elif drpif == 'Green' :
            dropdown = driver.find_element(By.ID, "oldSelectMenu")
            dropdown.find_element(By.XPATH, "//option[. = 'Green']").click()
elif drpif == 'White' :
            dropdown = driver.find_element(By.ID, "oldSelectMenu")
            dropdown.find_element(By.XPATH, "//option[. = 'White']").click()
elif drpif == 'Violet' :
            dropdown = driver.find_element(By.ID, "oldSelectMenu")
            dropdown.find_element(By.XPATH, "//option[. = 'Violet']").click()
elif drpif == 'Indigo' :
            dropdown = driver.find_element(By.ID, "oldSelectMenu")
            dropdown.find_element(By.XPATH, "//option[. = 'Indigo']").click()
elif drpif == 'Aque' :
            dropdown = driver.find_element(By.ID, "oldSelectMenu")
            dropdown.find_element(By.XPATH, "//option[. = 'Aque']").click()
elif drpif == 'Yellow' :
            dropdown = driver.find_element(By.ID, "oldSelectMenu")
            dropdown.find_element(By.XPATH, "//option[. = 'Yellow']").click()
 #======================== Dropdown If END ============================

 #======================== AKSI lain ============================

driver.find_element(By.XPATH, "//div[2]/div[2]/div[2]/div[2]/div/div/div/div").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[2]/div[2]/div[2]/div[2]/div/div/div/div").click()

