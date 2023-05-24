from pytest_html_reporter import attach
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os, platform, time, pytest
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def MenuGiatja(driver):
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "kegiatan-kerja-dan-produksi-2")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Kegiatan Kerja").click()

def MenuPemasaran(driver):
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "kegiatan-kerja-dan-produksi-2")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Pemasaran").click()



def MenuPNBP(driver):
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "kegiatan-kerja-dan-produksi-2")
    time.sleep(0.5)
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "PNBP").click()

def MenuLaporan(driver):
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "kegiatan-kerja-dan-produksi-2")
    time.sleep(0.5)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.5)
    driver.find_element(By.LINK_TEXT, "Laporan Kegiatan Kerja dan Produksi").click()

def LogOut(driver):
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.ID, "avatar")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.XPATH, "//li[contains(.,'Logout')]")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.XPATH, "//li[contains(.,'Logout')]").click()