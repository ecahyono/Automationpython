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


wb = load_workbook(filename=r"C:\Users\wilda\Documents\Automationpython\Filexel/lainlain.xlsx")

# jadi ini bisa read sheet yang dibawah itu yang di excel
sheetrange = wb['DaftarUpt']

# ini web driver disimpen dimana, kalo disimpen di path kosongin aja
driver = webdriver.Chrome()

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

element2 = driver.find_element(By.XPATH, "//div[9]/div/ul/li/div")
time.sleep(2)
actions2 = ActionChains(driver)
actions2.move_to_element(element2).perform()
driver.find_element(By.LINK_TEXT, "Daftar UPT").click()

i = 2

# nge baca mulai dari tabel A
while i <= len(sheetrange['A']):
    # deklarasi bahwa NIP itu ada di A 
    NamaUPT = sheetrange['A'+str(i)].value
    # deklarasi bahwa NAMA itu ada di B 
    Kanwil = sheetrange['B'+str(i)].value
    # deklarasi bahwa NAMA itu ada di B 
    AlamatUPT = sheetrange['C'+str(i)].value
    Telpon = sheetrange['D'+str(i)].value
    JenisUPT = sheetrange['E'+str(i)].value
    KelasUPT = sheetrange['F'+str(i)].value
    KapasitasUPT = sheetrange['G'+str(i)].value
    wilayah = sheetrange['H'+str(i)].value
    Fax = sheetrange['I'+str(i)].value
    KepalaUPT = sheetrange['J'+str(i)].value
    NamaJabatan1 = sheetrange['K'+str(i)].value
    Pangkat1 = sheetrange['L'+str(i)].value
    Nip1 = sheetrange['M'+str(i)].value
    PejabatUPT = sheetrange['N'+str(i)].value
    NamaJabatan2 = sheetrange['O'+str(i)].value
    Pangkat2 = sheetrange['P'+str(i)].value
    Nip2 = sheetrange['Q'+str(i)].value
    time.sleep(1)

    try:
        driver.find_element(By.XPATH, "//span[contains(.,\'Tambah\')]").click()
    
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div")))
        driver.execute_script("window.scrollTo(0,258)")
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div/div[1]/div[2]/div/div[1]/input").send_keys(NamaUPT)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div/div[1]/div[3]/div/div/div/div/input").send_keys(Kanwil)
        time.sleep(10)
        ds
        
        #driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div/div[1]/div[3]/div/div/div/div/input").send_keys(Kanwil)
        #driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div/div[1]/div[3]/div/div/div/div/input").send_keys(Keys.DOWN)
       # driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div/div[1]/div[3]/div/div/div/div/input").send_keys(Keys.ENTER)


    except TimeoutException:
        print("ga muncul")
        pass
    time.sleep(5)
    i = i + 1
print("done")
