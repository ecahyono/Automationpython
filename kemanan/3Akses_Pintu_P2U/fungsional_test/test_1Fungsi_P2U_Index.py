
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
def test_1_setup_index():
    global driver
    swin = Service(r'C:/Users/user/Documents/TRCH/chromedriver.exe')
    smac = Service('/Users/will/Documents/chromedriver')
    if platform.system() == 'Darwin':
        driver = webdriver.Chrome(service=smac)
        driver.get("http://192.168.2.11:32400/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        print('.')
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
def test_2_login_index():
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
def test_3_akses_menu_index():
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
        driver.find_element(By.LINK_TEXT, 'Akses Pintu P2U').click()
        print('.')
        print('==========akses menu daftar lalu lintas==========')
        vars["x"] = driver.execute_script("return arguments[0]+1", vars["x"])
      # 17 | repeatIf | ${x}<15 | 
        condition = driver.execute_script("return (arguments[0]<1)", vars["x"])
        attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_1_search_data_kategori_nama_Index(): #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(20) 
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div/div/div/button'))) 
    #BUTTON CARI
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div/div/div/button'))) 
    #BUTTON CARI
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys('nama') 
    #KETIK NAMA
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama Lengkap\')]").click() 
    #PILIH DROPDOWN NAMA LENGKAP
    driver.find_element(By.XPATH, "(//input[@type=\'text\'])[2]").send_keys("galih") 
    #KETIK GALIH DI FORM MASUKAN KATA KUNCI
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div/div/div/button').click() 
    #KLIK BUTTON CARI

@mark.fixture_test()
def test_1_search_data_kategori_nomoID_Index(): #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(20) 
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div/div/div/button'))) 
    #BUTTON CARI
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div/div/div/button'))) 
    #BUTTON CARI
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys('Nomor') 
    #KETIK NOMOR
    driver.find_element(By.XPATH, "//li[contains(.,\'Nomor Identitas\')]").click() 
    #PILIH DROPDOWN NOMOR IDENTITAS
    driver.find_element(By.XPATH, "(//input[@type=\'text\'])[2]").send_keys("31") 
    #KETIK GALIH DI FORM MASUKAN KATA KUNCI
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div/div/div/button').click() 
    #KLIK BUTTON CARI


"""
@mark.fixture_test()
def test_5_search_data_kategori_NoInduk_Index(): #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
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
def test_6_clik_clear_value_Index(): 
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
def test_7_sortir_data_table_NoInduk_Index():
    driver.implicitly_wait(10)
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, "//span/i[2]").click()
    print('.')
    print('================================================================================= Sortir No induk ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_8_sortir_data_table_nama_Index():
    driver.implicitly_wait(10)
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, "//th[3]/div/span").click()
    print('.')
    print('================================================================================= Sortir nama')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_9_sortir_data_table_Jenis_Index():
    driver.implicitly_wait(10)
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, "//th[4]/div").click()
    print('.')
    print('================================================================================= Sortir jenis ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_10_sortir_data_table_tglkeluar_Index():
    driver.implicitly_wait(10)
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, "//th[5]/div/span/i").click()
    print('.')
    print('================================================================================= Sortir Tanggal Keluar ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_11_sortir_data_table_tglkembali_Index():
    driver.implicitly_wait(10)
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, "//th[6]/div/span/i").click()
    print('.')
    print('================================================================================= Sortir tanggal kembali ')
    attach(data=driver.get_screenshot_as_png())

#Pilih 5 jumlah data per halaman (di pagging) lalu data table yang ditampilkan sesuai(hanya 5 data per 1 halaman)
@mark.fixture_test()
def test_12_sortir_5_Halaman_Index():
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
def test_13_sortir_10_Halaman_Index():
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
def test_14_sortir_20_Halaman_Index():
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
def test_15_sortir_50_Halaman_Index():
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
def test_16_sortir_100_Halaman_Index():
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
def test_17_membuka_halaman_tambah_Index():
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
def test_18_back_index():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="backButton"]')))
    driver.find_element(By.XPATH, '//*[@id="backButton"]').click()
    print('.')
    print('========================================================== Back Ke Halaman Index  ')

#Membuka halaman detail melalui klik tombol aksi icon detail
@mark.fixture_test()
def test_19_membuka_halaman_ubah_Index(): 
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
def test_20_membuka_halaman_detail_Index(): 
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
def test_21_export_exel_Index():
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
def test_22_export_pdf_Index(): 
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
def test_23_cetak_Index(): 
    time.sleep(1)
    driver.implicitly_wait(10)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="printButton"]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[5]/div[3]/div/div/div/div[2]/div/button[2]').click()
    print('.')
    print('================================================================================= Cetak    ')
    attach(data=driver.get_screenshot_as_png())
"""


def teardown():
    time.sleep(9)
    print('.')
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

    