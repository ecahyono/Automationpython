import platform
import time
from os import environ
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pytest_html_reporter import attach

from selenium.webdriver.support import expected_conditions as EC

def OpKemandirian(driver):
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "username")))
    # driver.find_element(By.ID, "username").send_keys("Fuad Zaidan")
    driver.find_element(By.ID, "username").send_keys("eko-suryono")
    
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 30)
    print('.')
    print('========== Login ==========')
    
    attach(data=driver.get_screenshot_as_png())

def KasieGiatja(driver):
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "username")))
    
    # driver.find_element(By.ID, "username").send_keys("Rehan Ardian")
    driver.find_element(By.ID, "username").send_keys("riksa-paradila")
    
    
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 30)
    print('.')
    print('========== Login ==========')
    
    attach(data=driver.get_screenshot_as_png())

def KalapasGiatja(driver):
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "username")))
    # driver.find_element(By.ID, "username").send_keys("miftahul-huda")
    driver.find_element(By.ID, "username").send_keys("andika-almunawar")
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 30)
    print('.')
    print('========== Login ==========')
    
    attach(data=driver.get_screenshot_as_png())



def Op_Keterampilan(driver):
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
   
    driver.find_element(By.ID, "username").send_keys("Alya Zaen")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 30)
    print('.')
    print('========== Login ==========')
    
    attach(data=driver.get_screenshot_as_png())

def kasieKeterampilan(driver):
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
   
    driver.find_element(By.ID, "username").send_keys("riksa-paradila")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 30)
    print('.')
    print('========== Login ==========')
    
    attach(data=driver.get_screenshot_as_png())

def KalapasKeterampilan(driver):
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").send_keys("andika-almunawar")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 30)
    print('.')
    print('========== Login ==========')
    
    attach(data=driver.get_screenshot_as_png())

def kanwilPembinaan(driver):
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").send_keys("Wildan Khaus")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 30)
    print('.')
    print('========== Login ==========')
    
    attach(data=driver.get_screenshot_as_png())



def PusatPembinaan(driver):
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").send_keys("dewi-sartika")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 30)
    print('.')
    print('========== Login ==========')
    
    attach(data=driver.get_screenshot_as_png())

def Op_SPPN(driver): 
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").send_keys("suri-suryanto")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 30)
    print('.')
    print('========== Login ==========')
    
    attach(data=driver.get_screenshot_as_png())

def Op_SPPN(driver): 
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").send_keys("suri-suryanto")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 30)
    print('.')
    print('========== Login ==========')
    
    attach(data=driver.get_screenshot_as_png())



def kasie_SPPN(driver): 
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").send_keys("nasya-putri-ryani")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 30)
    print('.')
    print('========== Login ==========')
    
    attach(data=driver.get_screenshot_as_png())

def Kalapas_SPPN(driver): 
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").send_keys("andika-almunawar")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 30)
    print('.')
    print('========== Login ==========')
    
    attach(data=driver.get_screenshot_as_png())