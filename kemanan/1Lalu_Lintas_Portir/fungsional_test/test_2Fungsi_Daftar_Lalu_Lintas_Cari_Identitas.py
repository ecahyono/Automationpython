
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
def test_1_setup_cari_identitas():
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
def test_2_login():
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
def test_3_akses_menu():
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


#==============++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++===================

#HALAMAN CARI
#Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai 
#Halaman Manajemen Administrasi Keamanan - Cari Identitas

 #Membuka halaman Tambah Data / Cari Identitas melalui klik tombol tambah
@mark.fixture_test()
def test_4_membuka_halaman_tambah_index():
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
def test_5_Button_Next_Prev():
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.CSS_SELECTOR, ".btn-next svg").click()
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".btn-prev svg").click()



@mark.fixture_test()
def test_6_sortir_table_cari_noreg_cari_identitas():

    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/label/div/div/div/input').click()
    driver.find_element(By.XPATH, '//*[@id="nomorReg"]').click()
    print('.')
    print('================================================================================= Memilih Dropdown Noregis  ')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div/input')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div/input').send_keys('123')
    print('.')
    print('================================================================================= Input Noregis  ')

    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button').click()
    print('.')
    print('==========Click Button Cari  ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_7_sortir_table_cari_nama_cari_identitas():
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
def test_8_sortir_table_cari_JenisKejahatan_cari_identitas():
    driver.implicitly_wait(10)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/label/div/div/div/input').click()
    driver.find_element(By.XPATH, '//*[@id="jenisKejahatan"]').click()
    print('.')
    print('================================================================================= Memilih Dropdown No Regis  ')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div/input')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div/input').send_keys('Korupsi')
    print('.')
    print('================================================================================= Input No Regis  ')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button').click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    print('.')
    print('==========Click Button Cari  ==========')
    attach(data=driver.get_screenshot_as_png())
    
@mark.fixture_test()
def test_9_search_data_aktif_cari_identitas():
    driver.implicitly_wait(10)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/label/div/div/div/input').click()
    driver.find_element(By.XPATH, '//*[@id="semua"]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/form/div/div[2]/div/label[1]/span[1]/span').click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button').click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/form/div/div[2]/div/label[1]/span[1]/span').click()
    print('.')
    print('================================================================================= Search Data Aktiv  ')
    attach(data=driver.get_screenshot_as_png())
    
@mark.fixture_test()
def test_10_search_residivis_cari_identitas():
    driver.implicitly_wait(10)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/label/div/div/div/input').click()
    driver.find_element(By.XPATH, '//*[@id="semua"]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[2]/div/label[2]/span[1]/span').click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button').click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[2]/div/label[2]/span[1]/span').click()
    print('.')
    print('================================================================================= Search Residivis  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_11_Sortir_5_Halaman_cari_identitas():
    #5 HALAMAN
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div/span[2]/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'5/halaman\')]").click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div/span[3]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div/span[3]/div/input').send_keys('3') #Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    print('================================================================================= Menampilkan 5 halaman cari  ')
    attach(data=driver.get_screenshot_as_png())



@mark.fixture_test()
def test_12_sortir_10_Halaman_cari_identitas():
    #10 HALAMAN
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div/span[2]/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'10/halaman\')]").click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div/span[3]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div/span[3]/div/input').send_keys('3') #Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    print('================================================================================= Menampilkan 10 halaman cari ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_13_sortir_20_Halaman_cari_identitas():
    #20 HALAMAN
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div/span[2]/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'20/halaman\')]").click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div/span[3]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div/span[3]/div/input').send_keys('3') #Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    print('================================================================================= Menampilkan 20 halaman cari ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_14_sortir_50_Halaman_cari_identitas():
    #50 HALAMAN
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div/span[2]/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'50/halaman\')]").click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div/span[3]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div/span[3]/div/input').send_keys('3') #Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    print('================================================================================= Menampilkan 50 halaman cari ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_15_sortir_100_Halaman_cari_identitas():
    #100 HALAMAN
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div/span[2]/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'100/halaman\')]").click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div/span[3]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div/span[3]/div/input').send_keys('3') #Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    print('================================================================================= Menampilkan 100 halaman cari ')
    attach(data=driver.get_screenshot_as_png())





def teardown():
    
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

    