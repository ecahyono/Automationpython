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
    driver.find_element(By.LINK_TEXT, "Manajemen Kamar").click()

def suratmutasiblokkamar(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA02")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Surat Mutasi Blok/Kamar").click()

def riwayatpenempatan(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA02")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Riwayat Penempatan").click()

def RegisterH(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    time.sleep(0.5)
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.LINK_TEXT, "Register H").click()

def menulaporan6a(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Formulir Kamtib 6A - Asimilasi").click()

def menulaporan6b(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Formulir Kamtib 6B - Bencana Alam").click()

def menulaporan6c(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Formulir Kamtib 6C - Bencana Non Alam").click()

def menulaporan6d(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-6d").click()

def menulaporan6e(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-6e").click()

def menulaporan6f(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-6f").click()

def menulaporan7a(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-7a").click()

def menulaporan7b(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/formulir-kamtib-7b").click()

def menulaporan7c(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-7c").click()

def menulaporan7d(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-7d").click()

def menulaporan7e(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-7e").click()

def menulaporan8a(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-8a").click()

def menulaporan8b(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-8b").click()

def menulaporan9a(driver):
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "/keamanan/formulir-kamtib-9a").click()