from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os, platform, time, pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




def MenuJenisRemisiLainLain(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//li[@id='601']/div")))
    nav1 = driver.find_element(By.XPATH, "//li[@id='601']/div")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.2)
    nav2 = driver.find_element(By.ID, "80")
    time.sleep(0.2)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.2)
    nav3 = driver.find_element(By.ID, "86")
    time.sleep(0.2)
    ActionChains(driver).move_to_element(nav3).perform()
    time.sleep(0.2)
    driver.find_element(By.LINK_TEXT, "Jenis Remisi").click()

def MenuSyaratRemisiLainLain(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//li[@id='601']/div")))
    nav1 = driver.find_element(By.XPATH, "//li[@id='601']/div")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.2)
    nav2 = driver.find_element(By.ID, "80")
    time.sleep(0.2)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.2)
    nav3 = driver.find_element(By.ID, "86")
    time.sleep(0.2)
    ActionChains(driver).move_to_element(nav3).perform()
    time.sleep(0.2)
    driver.find_element(By.LINK_TEXT, "Syarat Remisi").click()

def MenuWaktuRemisiLainLain(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//li[@id='601']/div")))
    nav1 = driver.find_element(By.XPATH, "//li[@id='601']/div")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.2)
    nav2 = driver.find_element(By.ID, "80")
    time.sleep(0.2)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.2)
    nav3 = driver.find_element(By.ID, "86")
    time.sleep(0.2)
    ActionChains(driver).move_to_element(nav3).perform()
    time.sleep(0.2)
    driver.find_element(By.LINK_TEXT, "Pemberian Remisi").click()