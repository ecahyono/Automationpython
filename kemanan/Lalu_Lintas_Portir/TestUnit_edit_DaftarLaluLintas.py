
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
    elif platform.system() == 'Windows':
        driver = webdriver.Chrome(service=swin)
        driver.get("http://192.168.2.11:32400/")
        driver.maximize_window()
        driver.implicitly_wait(5)
    print('.')
    print('=================================================================================Setup OS berhasil================================================================================= ')

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
    print('=================================================================================Login berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_akses_menu():
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
    print('=================================================================================akses menu daftar lalu lintas================================================================================= ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_Dropdown_Nama():
    driver.implicitly_wait(10)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filterColumn"]')))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
    print('.')
    print('=================================================================================Click Button Tambah Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_Input_Search_Nama():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('EYONO BIN CAS')
    print('.')
    print('=================================================================================Input Nama Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_Click_Button_Cari():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button').click()
    print('.') 
    print('=================================================================================Click Button Cari Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_Click_Button_UBAH():
    driver.implicitly_wait(10)
    time.sleep(6)
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    driver.find_element(By.CSS_SELECTOR, ".text-green-500 .h-5").click()
    print('.')
    print('=================================================================================Click Button Update Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_Muat_Ulang():
    time.sleep(10)
    driver.implicitly_wait(10)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonReset"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonReset"]').click()
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click() 
    time.sleep(10)
    print('.')
    print('=================================================================================Click Button Muat Ulang Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png()) 

@mark.fixture_test()
def test_Ubah_Deskripsi():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="deskripsi"]')))
    driver.find_element(By.XPATH, '//*[@id="deskripsi"]').clear()
    driver.find_element(By.XPATH, '//*[@id="deskripsi"]').send_keys('deskripsi baru')
    print('.')
    print('=================================================================================Ubah Deskripsi Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png()) 
@mark.fixture_test()
def test_Ubah_Tanggal_Keluar():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "keluarKeamanan")))
    driver.find_element(By.ID, "keluarKeamanan").clear()
    driver.find_element(By.ID, "keluarKeamanan").send_keys(Keys.ENTER)
    print('.')
    print('=================================================================================Ubah Tanggal Keluar Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png()) 

@mark.fixture_test()
def test_Ubah_Tanggal_kembali():
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').clear()
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').send_keys(Keys.ENTER)
    print('.')
    print('=================================================================================Ubah Tanggal Kembali Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png()) 
    time.sleep(10)


@mark.fixture_test()
def test_Ubah_Jenis_Keluar():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jenisKeluar"]')))
    driver.find_element(By.XPATH, '//*[@id="jenisKeluar"]').clear()

    time.sleep(10)

    print('.')
    print('=================================================================================Ubah Jenis Keluar Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png())

def teardown():
    print('.')
    print('====================================================================================================== TEST SELESAI  ======================================================================================================')
    time.sleep(10)
    driver.close()
    driver.quit










    



    