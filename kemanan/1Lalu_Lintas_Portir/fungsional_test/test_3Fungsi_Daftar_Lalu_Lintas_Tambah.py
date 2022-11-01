from distutils.archive_util import make_archive
from os import PRIO_PGRP
from re import T
from threading import TIMEOUT_MAX
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
def test_setup_Tambah():
    global driver
    swin = Service(r'C:/Users/user/Documents/TRCH/chromedriver.exe')
    smac = Service('/Users/will/Documents/chromedriver')
    if platform.system() == 'Darwin':
        driver = webdriver.Chrome(service=smac)
        driver.get("http://192.168.2.11:32400/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        print('▒▒▒▒▒▒▒▒▒▒▒▒')
        print('▒▓▓▓▒▒▒▒▓▓▓▒')
        print('▒▓▒▒▓▒▒▓▒▒▓▒')
        print('▒▓▒▒▒▓▓▒▒▒▓▒')
        print('▒▓▒▒▒▒▒▒▒▒▓▒')
        print('▒▓▒▒▒▒▒▒▒▒▓▒')
        print('▒▒▒▒▒▒▒▒▒▒▒▒')
    elif platform.system() == 'Windows':
        driver = webdriver.Chrome(service=swin)
        driver.get("http://192.168.2.11:32400/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        print('▒▒▒▒▒▒▒▒▒▒▒▒')
        print('▒▓▒▒▒▒▒▒▒▒▓▒')
        print('▒▓▒▒▒▒▒▒▒▒▓▒')
        print('▒▓▒▒▒▓▓▒▒▒▓▒')
        print('▒▓▒▒▓▒▒▓▒▒▓▒')
        print('▒▓▓▓▒▒▒▒▓▓▓▒')
        print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('.')
    print('==========setup OS ==========')



@mark.fixture_test()
def test_login():
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//div/span").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("test-user")
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    print('.')
    print('==========Login ==========')
    
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_akses_menu():
    vars = {}
    vars["x"] = driver.execute_script("return 1")
    # 4 | do |  | 
    condition = True
    while condition:
        driver.implicitly_wait(10)
        nav1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/nav/ul/li[2]/div')
        actions = ActionChains(driver)
        actions.move_to_element(nav1).perform()

        element2 = driver.find_element(By.XPATH, "//div[4]/div/ul/li/div")
        time.sleep(1)
        actions2 = ActionChains(driver)
        actions2.move_to_element(element2).perform()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, 'Daftar Lalu Lintas').click()
        print('.')
        print('==========akses menu daftar lalu lintas==========')
        vars["x"] = driver.execute_script("return arguments[0]+1", vars["x"])
      # 17 | repeatIf | ${x}<15 | 
        condition = driver.execute_script("return (arguments[0]<1)", vars["x"])
        attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_membuka_halaman_tambah():
    driver.implicitly_wait(10)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5 > path")))
    #WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="backButton"]')))
    #driver.find_element(By.XPATH, '//*[@id="backButton"]').click()
    print('.')
    print('================================================================================= Membuka Halaman Tambah  ')
    attach(data=driver.get_screenshot_as_png())



@mark.fixture_test()
def test_sortir_table_cari_nama_Tambah():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/label/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
    print('.')
    print('================================================================================= Memilih Dropdown Nama  ')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div/input')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div/input').send_keys('WILLLD BINTI eko cah cah ge')
    print('.')
    print('================================================================================= Input Nama  ')

    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button').click()
    print('.')
    print('==========Click Button Cari  ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_Click_Button_Detile_Tambah():
    driver.implicitly_wait(10)
    time.sleep(2)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.CSS_SELECTOR, ".h-5 > path").click()
    print('.')
    print('==========Click Button Update  ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_Click_Button_Tambah_WBP_Tambah():
    driver.implicitly_wait(10)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div/div[2]/button').click()
    print('.')
    print('==========Click Button Tambah WBP  ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_sortir_detil_wbp_Tambah():
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tab-0"]')))
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-0"]')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[3]/div').click()
    driver.find_element(By.XPATH, '//*[@id="tab-1"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="tab-2"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="tab-3"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="tab-4"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="tab-5"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="tab-6"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="tab-7"]').click()

    print('.')
    print('================================================================================= Detile WBP')

@mark.fixture_test()
def test_detile_perkara_Tambah():

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tab-registrasi"]')))
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-registrasi"]')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[3]/div').click()
    driver.find_element(By.XPATH, '//*[@id="tab-registrasi"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="tab-sidang"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="tab-tahanan_rumah"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="tab-meninggal_dunia"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="tab-mutasi_upt"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="tab-pm"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="tab-pembebasan"]').click()
    print('.')
    print('================================================================================= Detile Perkara')








def teardown():
    time.sleep(10)
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▓▒▒▒▒▒▒▒▒▓▒')
    print('▒▒▓▓▓▓▓▓▓▓▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')

    print('░░▄███▄███▄')
    print('░░█████████')
    print('░░▒▀█████▀░')
    print('░░▒░░▀█▀')
    print('░░▒░░█░')
    print('░░▒░█')
    print('░░░█')
    print('░░█░░░░███████')
    print('░██░░░██▓▓███▓██▒')
    print('██░░░█▓▓▓▓▓▓▓█▓████')
    print('██░░██▓▓▓(◐)▓█▓█▓█')
    print('███▓▓▓█▓▓▓▓▓█▓█▓▓▓▓█')
    print('▀██▓▓█░██▓▓▓▓██▓▓▓▓▓█')
    print('░▀██▀░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█')
    print('░░░░▒░░░█▓▓▓▓▓█▓▓▓▓▓▓█')
    print('░░░░▒░░░█▓▓▓▓█▓█▓▓▓▓▓█')
    print('░▒░░▒░░░█▓▓▓█▓▓▓█▓▓▓▓█')
    print('░▒░░▒░░░█▓▓▓█░░░█▓▓▓█')
    print('░▒░░▒░░██▓██░░░██▓▓██')
    driver.close()
    driver.quit()
