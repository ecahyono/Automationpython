
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