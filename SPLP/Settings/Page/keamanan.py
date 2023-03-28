from pytest_html_reporter import attach
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os, platform, time, pytest
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def p2uinternal(driver):
    nav1 = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA01")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/p2u-internal").click()

def p2ueksternal():
    nav1 = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA01")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/p2u-eksternal").click()

def manajemenblokdankamar():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA02")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/manajemen-blok-dan-kamar").click()

def manajemenpenghunibaru():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA02")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/manajemen-penghuni-baru").click()

def manajemenkamar():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA02")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/manajemen-kamar").click()

def suratmutasiblokkamar():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA02")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/surat-mutasi-blok-kamar").click()

def riwayatpenempatan():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA02")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/riwayat-penempatan").click()

def RegisterH():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "/keamanan/pengasingan").click()

def laporan6a():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/formulir-kamtib-6a").click()

def laporan6b():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/formulir-kamtib-6b").click()

def laporan6c():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/formulir-kamtib-6c").click()

def laporan6d():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/formulir-kamtib-6d").click()

def laporan6e():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/formulir-kamtib-6e").click()

def laporan6f():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/formulir-kamtib-6f").click()

def laporan7a():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/formulir-kamtib-7a").click()

def laporan7b():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/formulir-kamtib-7b").click()

def laporan7c():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/formulir-kamtib-7c").click()

def laporan7d():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/formulir-kamtib-7d").click()

def laporan7e():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/formulir-kamtib-7e").click()

def laporan8a():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/formulir-kamtib-8a").click()

def laporan8b():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/formulir-kamtib-8b").click()

def laporan9a():
    nav1  = driver.find_element(By.ID, "KEA00")
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "KEA04")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/keamanan/formulir-kamtib-9a").click()