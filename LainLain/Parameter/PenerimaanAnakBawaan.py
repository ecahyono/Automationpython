from turtle import rt
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import pytest
from openpyxl import load_workbook
import time

@pytest.fixture()
def test_setup():
    global driver
    
    s = Service('/Users/will/Downloads/chromedriver')
    driver = webdriver.Chrome(service=s)
    url = "http://kumbang.torche.id:32400/"
    driver.get(url)
    # seting windows nya jadi max   
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    

def test_penerimaanAnakBawaan(test_setup):

    wb = load_workbook(filename=r"/Users/will/Documents/Automationpython/Filexel/lainlain.xlsx")
    sheetrange = wb['PenerimaanAnakBawaan']
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
    element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/nav/ul/li[1]/div")                                   
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)
    element2 = driver.find_element(By.XPATH, "//div[3]/div/ul/li[5]/div")
    
    actions2 = ActionChains(driver)
    actions2.move_to_element(element2).perform()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Penerimaan Anak Bawaan").click()
    
    i = 2

    # nge baca mulai dari tabel A
    while i <= len(sheetrange['A']):
        # deklarasi bahwa NIP itu ada di A 
        NoInduk = sheetrange['A'+str(i)].value

        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".is-plain:nth-child(2)").click()
        try:      
            driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div/div/div/input").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div/div/div/input").send_keys(NoInduk)
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, ".el-select-dropdown__item:nth-child(1) tr:nth-child(2) > .el-descriptions__cell:nth-child(1)").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div[1]/div/form/button[1]").click()
        
    
        except TimeoutException:
            print("MASIH ADA ERROR, CEK LAGI PAK WIL")
            pass
        time.sleep(5)
        i = i + 1
    print("DONE PAK WILDAN, SEBATS DULU")