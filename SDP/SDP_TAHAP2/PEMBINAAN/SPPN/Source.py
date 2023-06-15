from openpyxl import Workbook
from faker import Faker
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
from datetime import datetime
import pytest
from selenium import webdriver

import sys
from os import environ, path
from dotenv import load_dotenv
load_dotenv()
from openpyxl import load_workbook

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR"))
    wb = load_workbook(environ.get("data"))
    file_path = environ.get("fakersppn")

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))
    wb = load_workbook(environ.get("KeamananUATWin"))
import random

from Settings.setupPembinaan import initDriver, loadDataPath, quit, sleep, upload, uploadGambar
from Settings.loginPembinaan import *
from Settings.Page.Pembinaan import *
import random
import logging

sheetrangeIndex = wb['listWbpSumedang']

random1 = random.randint(1,9)


PetugasSheet                                 = sheetrangeIndex['E'+str(random1)].value
# print(PetugasSheet)

time.sleep(3)

workbook = Workbook()
worksheet = workbook.active
worksheet.title = 'SheetSppn'

fake = Faker('id_ID')

KegiatanKerja   = ['Manufaktur','Jasa']
nums = '01234567891011121415161716'





for i in range(1):
    NoSkFaker                = "W"+ fake.isbn10() + ".PASS" + ".PASS" + random.choice(nums) +".PK." + fake.date_between(start_date='today', end_date='today').strftime('%d.%m.%Y') + "-" + random.choice(nums)
    NamaFaker                = fake.name()
    PegawaiFaker             = PetugasSheet

    worksheet.append([
        NoSkFaker,
        NamaFaker,
        PegawaiFaker
       
     
        ])
        
workbook.save(file_path)

workbook = load_workbook(filename=file_path)
worksheet = workbook.active

   



global driver, pathData
driver = initDriver()
pathData = loadDataPath()   