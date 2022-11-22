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
from os import environ, path
from pytest import mark
import platform
import time
import os
import pytest
import json
import sys

from TF1_Penempatan_Index import test_Ossetup, test_loggin, test_akses_menu_penempatan
test_Ossetup()
test_loggin()
test_akses_menu_penempatan()

@mark.fixture_Tambah_penerimaan
def test_menujuhalamantambahpenempatan():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.ID, 'createButton').click()


