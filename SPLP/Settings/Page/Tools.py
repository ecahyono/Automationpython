from pytest_html_reporter import attach
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os, platform, time, pytest
from pytest import mark
import logging

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('aksesmenu.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

def test_SPPN_001(driver):
	nav1 = driver.find_element(By.ID, '90')
	ActionChains(driver).move_to_element(nav1).perform()
	time.sleep(2)
	nav2 = driver.find_element(By.ID, 'tools-konfigurasi-01')
	ActionChains(driver).move_to_element(nav2).perform()
	time.sleep(2)
	nav3 = driver.find_element(By.ID, 'SPPN')
	ActionChains(driver).move_to_element(nav3).perform()

	driver.find_element(By.LINK_TEXT, 'Peraturan Penilaian Narapidana').click()

	attach(data=driver.get_screenshot_as_png())
	Log.info('Mengakses menu Penerimaan dengan memilih modul Rupbasan kemudian pilih menu Penerimaan')

def test_SPPN_002(driver):
	nav1 = driver.find_element(By.ID, '90')
	ActionChains(driver).move_to_element(nav1).perform()
	time.sleep(2)
	nav2 = driver.find_element(By.ID, 'tools-konfigurasi-01')
	ActionChains(driver).move_to_element(nav2).perform()
	time.sleep(2)
	nav3 = driver.find_element(By.ID, 'SPPN')
	ActionChains(driver).move_to_element(nav3).perform()

	driver.find_element(By.LINK_TEXT, 'Item Penilaian Narapidana').click()

	attach(data=driver.get_screenshot_as_png())
	Log.info('Mengakses menu Penerimaan dengan memilih modul Rupbasan kemudian pilih menu Penerimaan')

