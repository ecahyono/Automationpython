import platform, sys, json
from os import environ, path
from selenium import webdriver
from pytest import mark
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def buttonTambah(driver):
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButton"]')))
    print('.')

def buttonSubmit(driver):
    driver.implicitly_wait(60)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    print('.')

def selectKategoriPegawai(driver):
    driver.implicitly_wait(60)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "pegawai").click()
    print('.')

def selectKategoriTamuDinas(driver):
    driver.implicitly_wait(60)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "tamuDinas").click()
    print('.')


def quit(driver):
    time.sleep(5)
    print('.')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▓▒▒▒▒▒▒▒▒▓▒')
    print('▒▒▓▓▓▓▓▓▓▓▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')

    driver.close()
    driver.quit()