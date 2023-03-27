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
from selenium.webdriver.common.keys import Keys 

from openpyxl import load_workbook
import time


wb = load_workbook(filename=r"/Users/will/Documents/Automationpython/Filexel/lainlain.xlsx")

# jadi ini bisa read sheet yang dibawah itu yang di excel
sheetrange = wb['pekerjaan']

# ini web driver disimpen dimana, kalo disimpen di path kosongin aja
driver = webdriver.Chrome(r"/Users/will/Downloads/chromedriver")

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
driver.find_element(By.ID, "username").send_keys("rono")
# masukin input password
driver.find_element(By.ID, "password").send_keys("rene")
# click button login
driver.find_element(By.ID, "kc-login").click()
time.sleep(2)
element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/nav/ul/li[7]/div")
time.sleep(2)
actions = ActionChains(driver)
actions.move_to_element(element).perform()
time.sleep(2)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx anak ke 2


element2 = driver.find_element(By.XPATH, "//div[9]/div/ul/li/div")
time.sleep(2)
actions2 = ActionChains(driver)
actions2.move_to_element(element2).perform()
driver.find_element(By.LINK_TEXT, "Jenis Pekerjaan").click()

i = 2

# nge baca mulai dari tabel A
while i <= len(sheetrange['A']):
    # deklarasi bahwa NIP itu ada di A 
    pekerjaan = sheetrange['A'+str(i)].value
    # deklarasi bahwa NAMA itu ada di B 
    
    time.sleep(1)


    driver.find_element(By.CSS_SELECTOR, ".is-plain:nth-child(2)").click()

    try:

        driver.find_element(By.XPATH, "//input[@type=\'text\']").click()
        driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div[2]/div/div[2]/div/div/form/div/div/div/input").send_keys(pekerjaan)
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, ".el-form-item__content > .w-full").click()
        driver.find_element(By.CSS_SELECTOR, ".w-full > .text-light-blue-900 > span").click()

    except TimeoutException:
        print("ga muncul")
        pass
    time.sleep(5)
    i = i + 1
print("done")


