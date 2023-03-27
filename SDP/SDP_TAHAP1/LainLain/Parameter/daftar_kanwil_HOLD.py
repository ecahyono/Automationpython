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
import pyautogui

wb = load_workbook(filename=r"C:\Users\wilda\Documents\Automationpython\Filexel/lainlain.xlsx")

# jadi ini bisa read sheet yang dibawah itu yang di excel
sheetrange = wb['Kanwil']

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

element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/nav/ul/li[7]/div")

actions = ActionChains(driver)
actions.move_to_element(element).perform()


element2 = driver.find_element(By.XPATH, "//div[9]/div/ul/li/div")

actions2 = ActionChains(driver)
actions2.move_to_element(element2).perform()
driver.find_element(By.LINK_TEXT, "Kanwil").click()

i = 2

# nge baca mulai dari tabel A
while i <= len(sheetrange['A']):
    # deklarasi bahwa NIP itu ada di A 
    kanwil = sheetrange['A'+str(i)].value
    # deklarasi bahwa NAMA itu ada di B 
    alamat = sheetrange['B'+str(i)].value
    # deklarasi bahwa NAMA itu ada di B 
    telpon = sheetrange['C'+str(i)].value
    fax = sheetrange['D'+str(i)].value
    wilayah = sheetrange['E'+str(i)].value
    kota = sheetrange['F'+str(i)].value
    KepalaKanwil = sheetrange['G'+str(i)].value
    NamaJabatan = sheetrange['H'+str(i)].value
    Pangkat1 = sheetrange['I'+str(i)].value
    Nip1 = sheetrange['J'+str(i)].value
    PejabatKanwil = sheetrange['K'+str(i)].value
    NamaJabatan = sheetrange['L'+str(i)].value
    Pangkat2 = sheetrange['M'+str(i)].value
    Nip2 = sheetrange['N'+str(i)].value
    time.sleep(1)

    try:
        driver.find_element(By.CSS_SELECTOR, ".is-plain:nth-child(2)").click()
        driver.execute_script("window.scrollTo(0,214)")
        driver.find_element(By.ID, "uraian").click()
        driver.find_element(By.ID, "uraian").send_keys(kanwil)
        driver.find_element(By.CSS_SELECTOR, ".el-col:nth-child(1)").click()
        driver.find_element(By.ID, "alamat").click()
        driver.find_element(By.ID, "alamat").send_keys(alamat)
        driver.find_element(By.ID, "telpon").click()
        driver.find_element(By.ID, "telpon").send_keys(telpon)
        driver.find_element(By.ID, "fax").click()
        driver.find_element(By.ID, "fax").send_keys(fax)

        """
DROPDOWN TIDAK BISA MELAKUKAN SEARCH JADI DI HOLD DULU YA

        driver.find_element(By.ID, "id_provinsi").send_keys(wilayah)
        time.sleep(3)
        driver.find_element(By.ID, "id_provinsi").click()
        time.sleep(5)
        pyautogui.typewrite(wilayah)

        driver.find_element(By.ID, "id_dati2").send_keys(kota)
        time.sleep(3)
        driver.find_element(By.ID, "id_dati2").click()
        time.sleep(5)
        pyautogui.typewrite(kota)
        """
        
        driver.find_element(By.ID, "kepala_kanwil").click()
        driver.find_element(By.ID, "kepala_kanwil").send_keys(KepalaKanwil)
        driver.find_element(By.ID, "jabatan_kw").click()
        driver.find_element(By.ID, "jabatan_kw").send_keys(NamaJabatan)
        driver.find_element(By.ID, "pangkat_kw").click()
        driver.find_element(By.ID, "pangkat_kw").send_keys(Pangkat1)
        driver.find_element(By.ID, "nip_kw").click()
        driver.find_element(By.ID, "nip_kw").send_keys(Nip1)
        driver.find_element(By.ID, "pejabat_kanwil").click()
        driver.find_element(By.ID, "pejabat_kanwil").send_keys(PejabatKanwil)
        driver.find_element(By.ID, "jabatan_pw").click()
        driver.find_element(By.ID, "jabatan_pw").send_keys(NamaJabatan)
        driver.find_element(By.ID, "pangkat_pw").click()
        driver.find_element(By.ID, "pangkat_pw").send_keys(Pangkat2)
        driver.find_element(By.ID, "nip_pw").click()
        driver.find_element(By.ID, "nip_pw").send_keys(Nip2)
        driver.find_element(By.CSS_SELECTOR, ".w-full > .text-light-blue-900 > span").click()
      
    except TimeoutException:
        print("MASIH ADA ERROR, CEK LAGI PAK WIL")
        pass
    time.sleep(5)
    i = i + 1
print("DONE PAK WILDAN, SEBATS DULU")
