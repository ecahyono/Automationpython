from pytest_html_reporter import attach
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os, platform, time, pytest
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def p2uinternal(driver):
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA01")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Akses P2U Internal").click()

def p2ueksternal(driver):
    nav1 = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA01")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Akses P2U Eksternal").click()

def manajemenblokdankamar(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA02")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Manajemen Blok dan Kamar").click()

def manajemenpenghunibaru(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA02")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Manajemen Penghuni Baru").click()

def manajemenkamar(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA02")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/manajemen-kamar").click()

def suratmutasiblokkamar(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA02")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/surat-mutasi-blok-kamar").click()

def riwayatpenempatan(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA02")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/riwayat-penempatan").click()

def RegisterH(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/pengasingan").click()

def laporan6a(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-6a").click()

def laporan6b(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-6b").click()

def laporan6c(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-6c").click()

def laporan6d(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-6d").click()

def laporan6e(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-6e").click()

def laporan6f(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-6f").click()

def laporan7a(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-7a").click()

def laporan7b(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/formulir-kamtib-7b").click()

def laporan7c(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-7c").click()

def laporan7d(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-7d").click()

def laporan7e(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-7e").click()

def laporan8a(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-8a").click()

def laporan8b(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-8b").click()

def laporan9a(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-9a").click()