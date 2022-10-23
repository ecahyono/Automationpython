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
    elif platform.system() == 'Windows':
        driver = webdriver.Chrome(service=swin)
        driver.get("http://192.168.2.11:32400/")
        driver.maximize_window()
        driver.implicitly_wait(5)

    print('setupberhasil')

@mark.fixture_test()
def test_login():
    driver.find_element(By.XPATH, "//div/span").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("waru")
    driver.find_element(By.ID, "password").send_keys("waru")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)

    print('Login berhasil')

@mark.fixture_test()
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

    driver.find_element(By.LINK_TEXT, 'Kejaksaan').click()

    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()

    print('akses menu')

@mark.fixture_test()
def test_imput():
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/input').send_keys('Kejaksaan Agung Bandung')
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[1]/input').send_keys('Masukkan Fax')
    print('input berhasil')

@mark.fixture_test()
def test_imput_text_area():
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[2]/div/div[1]/textarea').send_keys('Deskripsi di dalam text area Kejaksaan Agung Bandung')
    print('area berhasil')

@mark.fixture_test()
def test_imput_number():
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div[1]/input').send_keys('40151')
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div[4]/div/div[1]/input').send_keys('08765456765')
    print('NUMBER berhasil')

@mark.fixture_test()
def test_dropdown():
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/form/div[6]/div/div/div/div/input').click()
    time.sleep(2)
    ketik = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/form/div[6]/div/div/div/div/input')
    ketik.send_keys('Jawa Tengah')
    ketik.send_keys(Keys.DOWN)
    ketik.send_keys(Keys.ENTER)

    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/form/div[7]/div/div/div/div/input').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/form/div[7]/div/div/div/div/input').send_keys('Yogyakarta')
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/form/div[7]/div/div/div/div/input').send_keys(Keys.DOWN)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/form/div[7]/div/div/div/div/input').send_keys(Keys.ENTER) 
    print('dropdown berhasil')

@mark.fixture_test()
def test_submit():
    driver.find_element(By.ID, 'submitButton').click()

    print('ditambah sudah')