import imp
from json import load
from lib2to3.pgen2 import driver
import string
from turtle import rt
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains


from openpyxl import load_workbook
import time

#target halaman excel ada dimana , wb = variablenya
wb = load_workbook(filename=r"/Users/will/Documents/Automationpython/Filexel/registrasi.xlsx")

# jadi ini bisa read sheet yang dibawah itu yang di excel
sheetrange = wb['reg']

# ini web driver disimpen dimana, kalo disimpen di path kosongin aja
driver = webdriver.Chrome(r"/Users/will/Downloads/chromedriver")

# link nya ini dimana
driver.get("http://kumbang.torche.id:32400/")
# seting windows nya jadi max   
driver.maximize_window()
# script gakan di eksekusi kalo web ga muncul. kalo lebih dari 10 detik ga muncul error
driver.implicitly_wait(10)
# ini letak xpath icon login
driver.find_element(By.XPATH, "//div/span").click()
# ini masuk ke form input username
driver.find_element(By.ID, "username").click()
# masukin input username
driver.find_element(By.ID, "username").send_keys("wildan")
# masukin input password
driver.find_element(By.ID, "password").send_keys("wildan")
# click button login
driver.find_element(By.ID, "kc-login").click()
time.sleep(2)
# variable element nyari dimana letak menu lain lain
element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/nav/ul/li[1]/div")
time.sleep(2)
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element2 = driver.find_element(By.XPATH, "//div/ul/li[2]/div")
actions2 = ActionChains(driver)
actions2.move_to_element(element2).perform()
driver.find_element(By.LINK_TEXT, "Registrasi Tahanan/ Narapidana").click()
                                        
i = 2

# nge baca mulai dari tabel A
while i <= len(sheetrange['A']):
    # deklarasi bahwa NIP itu ada di A 
    nip = sheetrange['A'+str(i)].value
    # deklarasi bahwa NAMA itu ada di B 
    nama = sheetrange['B'+str(i)].value
    # deklarasi bahwa NAMA itu ada di B 
    tempatlahir = sheetrange['C'+str(i)].value
    tanggallahir = sheetrange['D'+str(i)].value
    jeniskelamin = sheetrange['E'+str(i)].value
    alamat = sheetrange['F'+str(i)].value
    jabatan = sheetrange['G'+str(i)].value
    pangkat = sheetrange['H'+str(i)].value
    golongan = sheetrange['I'+str(i)].value
    bagian = sheetrange['J'+str(i)].value
    email = sheetrange['K'+str(i)].value
    telepon = sheetrange['L'+str(i)].value
    time.sleep(1)

    driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/button[3]").click()
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div/form/button[2]')))
   
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@type=\'text\']").click()
    time.sleep(2)
    #driver.find_element(By.XPATH, "//div[2]/div/div/div/div/input").click()
    #driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div/div/div/div/input").click()
    driver.find_element(By.XPATH, "//div[10]/div/div/div/ul/li[9]").click()
    
   
    try:

        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div/div/div/div/input").send_keys(nip)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".el-select-dropdown__item:nth-child(1) tr:nth-child(2) > .el-descriptions__cell:nth-child(1)").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div[1]/div/form/button[1]").click()
        
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]')))
        driver.find_element(By.CSS_SELECTOR, ".el-dialog__close > svg").click()


    except TimeoutException:
        print("ga muncul")
        pass
    time.sleep(5)
    i = i + 1
print("done")


    
