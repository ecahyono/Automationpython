
from os import PRIO_PGRP
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
def test_setup():
    global driver
    swin = Service(r'C:/Users/user/Documents/TRCH/chromedriver.exe')
    smac = Service('/Users/will/Documents/chromedriver')
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
    print('==========setup OS ==========')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▓▒▒▒▒▒▒▒▒▓▒')
    print('▒▒▓▓▓▓▓▓▓▓▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')


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
def test_search_data_kategori_nama_HALDEX(): #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(20)
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filterColumn"]')))
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').send_keys('nama')
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, '//*[@id="namaLengkap"]').click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('EYONO BIN CAS')
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button').click()
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    print('.')
    print('=================================================================================Search Data Form Kategori Nama ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_search_data_kategori_NoInduk_HALDEX(): #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(20)
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filterColumn"]')))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').send_keys('induk')
    driver.find_element(By.XPATH, '//*[@id="nomorInduk"]').click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('50120')
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button').click()
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    print('.')
    print('================================================================================= Search Data Form Kategori No Induk  ')
    attach(data=driver.get_screenshot_as_png())

#Mengosongkan kata kunci dan kategori dengan klik button clear value
@mark.fixture_test()
def test_clik_clear_value_HALDEX(): 
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.XPATH, '//*[@id="filterColumn"]')
    actions = ActionChains(driver)
    actions.move_to_element(nav1).perform()
    element2 = driver.find_element(By.CSS_SELECTOR, ".el-select__caret:nth-child(2) > svg")
    time.sleep(1)
    actions2 = ActionChains(driver)
    actions2.move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-select__caret:nth-child(2) > svg").click()
    print('.')
    print('=================================================================================Click Clear Value Button filter Colum  ')
    attach(data=driver.get_screenshot_as_png())

    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('tessssst') #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci yang tidak sesuai lalu data table yang ditampilkan kosong
    time.sleep(0.5)
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.XPATH, '//*[@id="kataKunci"]')
    actions = ActionChains(driver)
    actions.move_to_element(nav1).perform()
    element2 = driver.find_element(By.CSS_SELECTOR, ".el-input__clear > svg")
    time.sleep(1)
    actions2 = ActionChains(driver)
    actions2.move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-input__clear > svg").click()
    print('.')
    print('================================================================================= Click Clear Value Button Kata Kunci dan inputan data tidak sesuai  ')
    attach(data=driver.get_screenshot_as_png())





#SORTIR TABLE HALAMAN INDEX
@mark.fixture_test()
def test_sortir_data_table__NoInduk_HALDEX():
    driver.implicitly_wait(10)
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, "//span/i[2]").click()
    print('.')
    print('================================================================================= Sortir No induk ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_sortir_data_table_nama__HALDEX():
    driver.implicitly_wait(10)
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, "//th[3]/div/span").click()
    print('.')
    print('================================================================================= Sortir nama')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_sortir_data_table_Jenis__HALDEX():
    driver.implicitly_wait(10)
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, "//th[4]/div").click()
    print('.')
    print('================================================================================= Sortir jenis ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_sortir_data_table_tglkeluar__HALDEX():
    driver.implicitly_wait(10)
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, "//th[5]/div/span/i").click()
    print('.')
    print('================================================================================= Sortir Tanggal Keluar ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_sortir_data_table_tglkembali__HALDEX():
    driver.implicitly_wait(10)
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, "//th[6]/div/span/i").click()
    print('.')
    print('================================================================================= Sortir tanggal kembali ')
    attach(data=driver.get_screenshot_as_png())

#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_sortir_5_Halaman_HALDEX():
    #5 HALAMAN
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[4]/div/span[2]/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'5/halaman\')]").click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys('100') #Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    print('================================================================================= Menampilkan 5  ')
    attach(data=driver.get_screenshot_as_png())


#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_sortir_10_Halaman_HALDEX():
    #10 HALAMAN
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[4]/div/span[2]/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'10/halaman\')]").click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys('2')
    time.sleep(1)
    print('.')
    print('================================================================================= Menampilkan 10  ')
    attach(data=driver.get_screenshot_as_png())


#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_sortir_20_Halaman_HALDEX():
     #20 HALAMAN
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[4]/div/span[2]/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'20/halaman\')]").click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys('2')
    time.sleep(1)
    print('.')
    print('================================================================================= Menampilkan 20  ')
    attach(data=driver.get_screenshot_as_png())


#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_sortir_50_Halaman_HALDEX():
    #50 HALAMAN
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[4]/div/span[2]/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'50/halaman\')]").click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys('2')
    time.sleep(1)
    print('.')
    print('================================================================================= Menampilkan 50  ')
    attach(data=driver.get_screenshot_as_png())

#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_sortir_100_Halaman_HALDEX():
    #100 HALAMAN
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[4]/div/span[2]/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'100/halaman\')]").click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys('2')
    time.sleep(1)
    print('.')
    print('================================================================================= Menampilkan 100  ')
    attach(data=driver.get_screenshot_as_png())

 #Membuka halaman Tambah Data / Cari Identitas melalui klik tombol tambah
@mark.fixture_test()
def test_membuka_halaman_tambah_HALDEX():
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

#==============++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++===================

#HALAMAN CARI
#Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai 
#Halaman Manajemen Administrasi Keamanan - Cari Identitas

@mark.fixture_test()
def test_Button_Next_Prev():
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.CSS_SELECTOR, ".btn-next svg").click()
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".btn-prev svg").click()


@mark.fixture_test()
def test_sortir_table_cari_nama_HALCAR():
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
def test_sortir_table_cari_noreg_HALCAR():

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
def test_sortir_table_cari_JenisKejahatan_HALCAR():
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
def test_search_data_aktif_HALCAR():
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
def test_search_residivis_HALCAR():
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
def test_sortir_5_Halaman_HALCAR():
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
def test_sortir_10_Halaman_HALCAR():
    #5 HALAMAN
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
def test_sortir_20_Halaman_HALCAR():
    #5 HALAMAN
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
def test_sortir_50_Halaman_HALCAR():
    #5 HALAMAN
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
def test_sortir_100_Halaman_HALCAR():
    #5 HALAMAN
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div/span[2]/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'100/halaman\')]").click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div/span[3]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div/span[3]/div/input').send_keys('3') #Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir
    time.sleep(1)
    print('.')
    print('================================================================================= Menampilkan 100 halaman cari ')
    attach(data=driver.get_screenshot_as_png())




# END HALAMAN CARI

@mark.fixture_test()
def test_back():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="backButton"]')))
    driver.find_element(By.XPATH, '//*[@id="backButton"]').click()
    print('.')
    print('========================================================== Back Ke Halaman Index  ')

#Membuka halaman detail melalui klik tombol aksi icon detail
@mark.fixture_test()
def test_membuka_halaman_ubah_HALDEX(): 
    driver.implicitly_wait(10)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 path")))
    driver.find_element(By.CSS_SELECTOR, ".text-green-500 path").click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[1]/div/button')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="backButton"]').click()
    print('================================================================================= Membuka Halaman Ubah  ')
    attach(data=driver.get_screenshot_as_png())




#Membuka form ubah melalui klik tombol aksi icon ubah
@mark.fixture_test()
def test_membuka_halaman_detail_HALDEX(): 
    driver.implicitly_wait(10)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-blue-500 .h-5")))
    driver.find_element(By.CSS_SELECTOR, ".text-blue-500 .h-5").click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]/div/div/div[3]/button')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="backButton"]').click()
    print('================================================================================= Membuka Halaman Detail  ')
    attach(data=driver.get_screenshot_as_png())



#Melakukan export data tabel ke excel
@mark.fixture_test()
def test_export_exel_HALDEX():
    driver.implicitly_wait(10)
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div[1]/button').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div[1]/div/div/div/div[2]/div/button[2]').click()
    print('.')
    print('================================================================================= Export Excel   ')
    attach(data=driver.get_screenshot_as_png())




#Melakukan export data tabel ke pdf
@mark.fixture_test()
def test_export_pdf_HALDEX(): 
    driver.implicitly_wait(10)
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[5]/div[2]/button').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[5]/div[2]/div/div/div/div[2]/div/button[2]').click()
    print('.')
    print('================================================================================= Export PDF    ')
    attach(data=driver.get_screenshot_as_png())



#Melakukan cetak
@mark.fixture_test()
def test_cetak_HALDEX(): 
    time.sleep(1)
    driver.implicitly_wait(10)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="printButton"]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[5]/div[3]/div/div/div/div[2]/div/button[2]').click()
    print('.')
    print('================================================================================= Cetak    ')
    attach(data=driver.get_screenshot_as_png())



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

    
