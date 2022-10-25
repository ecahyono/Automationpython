
import os
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


@mark.fixture_test()
def test_setup():
    global driver
    swin = Service(r'C:/Users/user/Documents/TRCH/chromedriver.exe')
    smac = Service('/Users/will/Downloads/chromedriver')
    if platform.system() == 'Darwin':
        driver = webdriver.Chrome(service=smac)
        driver.get("http://192.168.2.11:32400/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        print('.')
        print('==========setup OS Mac berhasil==========')
    elif platform.system() == 'Windows':
        driver = webdriver.Chrome(service=swin)
        driver.get("http://192.168.2.11:32400/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        print('.')
        print('==========setup OS Win berhasil==========')
   

@mark.fixture_test()
def test_login():
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//div/span").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("wildan")
    driver.find_element(By.ID, "password").send_keys("wildan")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    print('.')
    print('==========Login berhasil==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_akses_menu():
    driver.implicitly_wait(10)
    element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/nav/ul/li[8]/div")
    time.sleep(1)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/nav/ul/li[8]/div")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element2 = driver.find_element(By.XPATH, "//div[10]/div/ul/li/div")
    actions2 = ActionChains(driver)
    actions2.move_to_element(element2).perform()
    driver.find_element(By.LINK_TEXT, "Daerah Tingkat II").click()

    print('xxx')
    print('==========akses menu daftar Lain-Lain ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_button_tambah():
    driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/div[1]/button").click()
    time.sleep(10)




def teardown():
    driver.close()
    driver.quit()