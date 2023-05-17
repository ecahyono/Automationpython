from pytest_html_reporter import attach
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os, platform, time, pytest
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def bapas(driver):
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, '15')))
    nav1 = driver.find_element(By.ID, "15")
    ActionChains(driver).move_to_element(nav1).perform()

def pendaftaran(driver):
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'bp-01')))
    nav2 = driver.find_element(By.ID, "bp-01")
    ActionChains(driver).move_to_element(nav2).perform()

def daftar_klien(driver):
    bapas(driver)
    pendaftaran(driver)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.LINK_TEXT, "Daftar Klien")))
    driver.find_element(By.LINK_TEXT, "Daftar Klien").click()
    
def register(driver):
    bapas(driver)
    pendaftaran(driver)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'REG01')))
    nav3 = driver.find_element(By.ID, "REG01")
    ActionChains(driver).move_to_element(nav3).perform()
    
def register_litmas(driver):
    bapas(driver)
    pendaftaran(driver)
    register(driver)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.LINK_TEXT, "Register Litmas")))
    driver.find_element(By.LINK_TEXT, "Register Litmas").click()

def RegisterPendampingan(driver):
    bapas(driver)
    pendaftaran(driver)
    register(driver)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.LINK_TEXT, "Register Pendampingan")))
    driver.find_element(By.LINK_TEXT, "Register Pendampingan").click()

def RegisterPembimbingan(driver):
    bapas(driver)
    pendaftaran(driver)
    register(driver)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.LINK_TEXT, "Register Pembimbingan")))
    driver.find_element(By.LINK_TEXT, "Register Pembimbingan").click()

def RegisterPengawasan(driver):
    bapas(driver)
    pendaftaran(driver)
    register(driver)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.LINK_TEXT, "Register Pengawasan")))
    driver.find_element(By.LINK_TEXT, "Register Pengawasan").click()

