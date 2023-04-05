from pytest_html_reporter import attach
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os, platform, time, pytest
from pytest import mark
import time
from Settings.setup import loadDataPath

global pathData
pathData = loadDataPath()

def alihkan(driver):
	driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/h1').click()
	
def Penerimaan(driver):
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'RUP00')))
	nav1 = driver.find_element(By.ID, 'RUP00')
	ActionChains(driver).move_to_element(nav1).perform()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Penerimaan')))
	driver.find_element(By.LINK_TEXT, 'Penerimaan').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	attach(data=driver.get_screenshot_as_png())

def Penempatan(driver):
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'RUP00')))
	nav1 = driver.find_element(By.ID, 'RUP00')
	ActionChains(driver).move_to_element(nav1).perform()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Penempatan')))
	driver.find_element(By.LINK_TEXT, 'Penempatan').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	attach(data=driver.get_screenshot_as_png())
	
def childmenu3(driver):
	driver.find_element(By.LINK_TEXT, 'Pemeliharaan').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	attach(data=driver.get_screenshot_as_png())

def childmenu4(driver):
	driver.find_element(By.LINK_TEXT, 'Pengamanan').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'createButton')))
	attach(data=driver.get_screenshot_as_png())

def childmenu5(driver):
	driver.find_element(By.LINK_TEXT, 'Mutasi').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
	attach(data=driver.get_screenshot_as_png())

def childmenu6(driver):
	driver.find_element(By.ID, '/rupbasan/pengeluaran').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'cetakBa-0')))
	attach(data=driver.get_screenshot_as_png())

def childmenu7(driver):
	driver.find_element(By.LINK_TEXT, 'Laporan Bulanan UPT').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	attach(data=driver.get_screenshot_as_png())

def daftarpegawai(driver):
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, '601')))
	element = driver.find_element(By.ID, '601')
	ActionChains(driver).move_to_element(element).perform()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Daftar Pegawai')))
	driver.find_element(By. LINK_TEXT, 'Daftar Pegawai').click()
	
def childlain(driver):
	element2 = driver.find_element(By.ID, '80')
	ActionChains(driver).move_to_element(element2).perform()

def Gudang(driver):
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, '601')))
	nav1 = driver.find_element(By.ID, '601')
	ActionChains(driver).move_to_element(nav1).perform()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, '80')))
	nav2 = driver.find_element(By.ID, '80')
	ActionChains(driver).move_to_element(nav2).perform()
	driver.find_element(By.LINK_TEXT, "Gudang").click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	attach(data=driver.get_screenshot_as_png())

def SektorGudang(driver):
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, '601')))
	nav1 = driver.find_element(By.ID, '601')
	ActionChains(driver).move_to_element(nav1).perform()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, '80')))
	nav2 = driver.find_element(By.ID, '80')
	ActionChains(driver).move_to_element(nav2).perform()
	driver.find_element(By.LINK_TEXT, "Sektor Gudang").click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
	attach(data=driver.get_screenshot_as_png())

def exportPDF(driver):
	driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportPDF']).click()
	time.sleep(1)
	driver.find_element(By.ID, 'thisButton').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportPDF'])))
	attach(data=driver.get_screenshot_as_png())

def exportexcel(driver):
	driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportexcel']).click()
	time.sleep(1)
	driver.find_element(By.ID, 'thisButton').click()
	WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportexcel'])))
	attach(data=driver.get_screenshot_as_png())

def tprint(driver):
	driver.find_element(By.ID, 'printButton').click()
	time.sleep(1)
	driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['cetakinisaja']).click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'printButton')))
	attach(data=driver.get_screenshot_as_png())
