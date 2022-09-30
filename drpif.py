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

wb = load_workbook(filename=r"C:\Users\wilda\Documents\Automationpython\Filexel\demoqa.xlsx")
sheetrange = wb['drpif']
drpif = sheetrange['A2'].value

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://demoqa.com/select-menu')

if drpif == 'Black' :
            dropdown = driver.find_element(By.ID, "oldSelectMenu")
            dropdown.find_element(By.XPATH, "//option[. = 'Black']").click()
elif drpif == 'blue' :
            dropdown = driver.find_element(By.ID, "oldSelectMenu")
            dropdown.find_element(By.XPATH, "//option[. = 'Blue']").click()

