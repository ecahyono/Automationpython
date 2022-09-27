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

wb = load_workbook(filename=r"/Users/will/Documents/Automationpython/Filexel/lainlain.xlsx")

# jadi ini bisa read sheet yang dibawah itu yang di excel
sheetrange = wb['JenisRegistrasi']

# ini web driver disimpen dimana, kalo disimpen di path kosongin aja
driver = webdriver.Chrome(r"/Users/will/Downloads/chromedriver")
driver.get("http://kumbang.torche.id:32400/")
# seting windows nya jadi max   
driver.maximize_window()
# script gakan di eksekusi kalo web ga muncul. kalo lebih dari 10 detik ga muncul error
driver.implicitly_wait(10)

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
time.sleep(1)
driver.find_element(By.LINK_TEXT, "Jenis Registrasi")
driver.find_element(By.LINK_TEXT, "Jenis Registrasi").click()


i = 2

# nge baca mulai dari tabel A
while i <= len(sheetrange['A']):
    # deklarasi bahwa NIP itu ada di A 
    NoID = sheetrange['A'+str(i)].value
    Keterangan = sheetrange['B'+str(i)].value
    NamaJenisRegistrasi = sheetrange['C'+str(i)].value
    Aktif = sheetrange['D'+str(i)].value
    LamaHukuman = sheetrange['E'+str(i)].value
    PerpanjangPertama = sheetrange['F'+str(i)].value
    PerpanjangKedua = sheetrange['G'+str(i)].value
    PerpanjangKetiga = sheetrange['G'+str(i)].value
    LamaHukumanx = sheetrange['E'+str(i)].value
    PerpanjangPertamax = sheetrange['F'+str(i)].value
    PerpanjangKeduax = sheetrange['G'+str(i)].value
    PerpanjangKetigax = sheetrange['G'+str(i)].value
    
    driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/div[1]/button").click()
    try:      
        driver.find_element(By.XPATH, "//*[@id=\"input_id_reg\"]").send_keys(NoID)
        driver.find_element(By.XPATH, "//*[@id=\"input_keterangan\"]").send_keys(Keterangan)
        driver.find_element(By.XPATH, "//*[@id=\"input_id_jenis_registrasi\"]").send_keys(NamaJenisRegistrasi)
        #
        driver.find_element(By.XPATH, "//*[@id=\"input_lama_hukuman\"]/div/input").click()
        pyautogui.hotkey("backspace")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"input_lama_hukuman\"]/div/input").send_keys(LamaHukuman) 

        driver.find_element(By.XPATH, "//*[@id=\"input_perpanjang_1\"]/div/input").click()
        pyautogui.hotkey("backspace")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"input_perpanjang_1\"]/div/input").send_keys(PerpanjangPertama) 
        
        driver.find_element(By.XPATH, "//*[@id=\"input_perpanjang_2\"]/div/input").click()
        pyautogui.hotkey("backspace")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"input_perpanjang_2\"]/div/input").send_keys(PerpanjangKedua) 

        driver.find_element(By.XPATH, "//*[@id=\"input_perpanjang_3\"]/div/input").click()
        pyautogui.hotkey("backspace")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"input_perpanjang_3\"]/div/input").send_keys(PerpanjangKetiga) 
        
        driver.find_element(By.XPATH, "//*[@id=\"input_lama_hukuman_anak\"]/div/input").click()
        pyautogui.hotkey("backspace")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"input_lama_hukuman_anak\"]/div/input").send_keys(LamaHukumanx) 

        driver.find_element(By.XPATH, "//*[@id=\"input_lama_hukuman_anak\"]/div/input").click()
        pyautogui.hotkey("backspace")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"input_lama_hukuman_anak\"]/div/input").send_keys(LamaHukumanx) 


        driver.find_element(By.XPATH, "//*[@id=\"input_perpanjang_anak_1\"]/div/input").click()
        pyautogui.hotkey("backspace")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"input_perpanjang_anak_1\"]/div/input").send_keys(PerpanjangPertamax) 


        driver.find_element(By.XPATH, "//*[@id=\"input_perpanjang_anak_2\"]/div/input").click()
        pyautogui.hotkey("backspace")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"input_perpanjang_anak_2\"]/div/input").send_keys(PerpanjangKeduax) 

        driver.find_element(By.XPATH, "//*[@id=\"input_perpanjang_anak_3\"]/div/input").click()
        pyautogui.hotkey("backspace")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"input_perpanjang_anak_3\"]/div/input").send_keys(PerpanjangKetigax) 
        time.sleep(1)
        driver.find_element(By.ID, "submite_button").click()

        
    except Timeception:
        print("MASIH ADA ERROR, CEK LAGI PAK WIL")
        pass
    time.sleep(5)
    i = i + 1
print("DONE PAK WILDAN, SEBATS DULU")
