
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
    print('==========setup OS berhasil==========')

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
    print('==========Login berhasil==========')

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
    print('xxx')
    print('==========akses menu daftar lalu lintas==========')

@mark.fixture_test()
def test_button_tambah ():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    print('.')
    print('==========Click Button Tambah Berhasil==========')


@mark.fixture_test()
def test_Dropdown_Nama():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/label/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
    print('.')
    print('========== Memilih Dropdown Nama Berhasil ==========')

@mark.fixture_test()
def test_Input_Search_Nama():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div/input')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div/input').send_keys('WILLLD BINTI eko cah cah ge')
    print('.')
    print('========== Input Nama Berhasil ==========')

@mark.fixture_test()
def test_Click_Button_Cari():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button').click()
    print('.')
    print('==========Click Button Cari Berhasil ==========')

@mark.fixture_test()
def test_Click_Button_Update():
    driver.implicitly_wait(10)
    time.sleep(2)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.CSS_SELECTOR, ".h-5 > path").click()
    print('.')
    print('==========Click Button Update Berhasil ==========')

@mark.fixture_test()
def test_Click_Button_Tambah_WBP():
    driver.implicitly_wait(10)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div/div[2]/button').click()
    print('.')
    print('==========Click Button Tambah WBP Berhasil ==========')

@mark.fixture_test()
def test_Input_Tanggal_Keluar():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="keluarKeamanan"]')))
    driver.find_element(By.XPATH, '//*[@id="keluarKeamanan"]').send_keys('24/12/2018')
    driver.find_element(By.XPATH, '//*[@id="keluarKeamanan"]').send_keys(Keys.ENTER)

    print('.')
    print('========== Input Tanggal Keluar Berhasil ==========')

@mark.fixture_test()
def test_Input_Tanggal_Harus_Kembali():
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').send_keys('29/12/2018')
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').send_keys(Keys.ENTER)
    print('.')
    print('========== Input Tanggal Harus Kembali Berhasil ==========')

@mark.fixture_test()
def test_Input_Jenis_Keluar():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jenisKeluar"]')))
    driver.find_element(By.XPATH, '//*[@id="jenisKeluar"]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Cuti Bersyarat\')]").click()
    print('.')
    print('========== Input Jenis Keluar Berhasil ==========')

@mark.fixture_test()
def test_Input_Deskripsi():
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="deskripsi"]').send_keys('deskripsi')
    print('.')
    print('========== Input Deskripsi Behasil ==========')

def teardown():
    print('====================================================================================================== TEST BERHASIL  ======================================================================================================')
    time.sleep(10)
    driver.close()
    driver.quit











    



    