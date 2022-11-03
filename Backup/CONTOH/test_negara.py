
# Runing this file using comannd:
# pytest test_negara.py -v -s --html-report=./reportresultl/negara.html
# note : if you want to generate new html report just change name of .html file

import string
from turtle import rt
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys 
# from openpyxl import load_workbook
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import platform
from pytest import mark
import time
from pytest_html_reporter import attach

@mark.fixture_negara
def test_setup():
    global driver
    swin = Service(r'C:/Users/user/Documents/TRCH/chromedriver.exe')
    smac = Service('/Users/will/Downloads/chromedriver')
    if platform.system() == 'Darwin':
        driver = webdriver.Chrome(service=smac)
        driver.get("http://192.168.2.11:32400/")
        driver.maximize_window()
        driver.implicitly_wait(5)
    elif platform.system() == 'Windows':
        driver = webdriver.Chrome(service=swin)
        driver.get("http://192.168.2.11:32400/")
        driver.maximize_window()
        driver.implicitly_wait(5)
    attach(data=driver.get_screenshot_as_png())
    print('setupberhasil')

@mark.fixture_negara
def test_login():
    driver.find_element(By.XPATH, "//div/span").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("waru")
    driver.find_element(By.ID, "password").send_keys("waru")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    attach(data=driver.get_screenshot_as_png())
    print('Login berhasil')

@mark.fixture_negara
def test_akses_menu():
    element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/nav/ul/li[8]/div")
    WebDriverWait(driver, 5)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    WebDriverWait(driver, 5)

    element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/nav/ul/li[8]/div")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    element2 = driver.find_element(By.XPATH, "//div[10]/div/ul/li/div")
    actions2 = ActionChains(driver)
    actions2.move_to_element(element2).perform()

    driver.find_element(By.LINK_TEXT, 'Negara').click()

    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    attach(data=driver.get_screenshot_as_png())
    print('akses menu')

@mark.fixture_negara
def test_input():
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/input').send_keys('Kejaksaan Agung Bandung')
    attach(data=driver.get_screenshot_as_png())
    print('input berhasil')

@mark.fixture_negara
def test_submit():
    driver.find_element(By.ID, 'submitButton').click()
    attach(data=driver.get_screenshot_as_png())
    print('ditambah sudah')