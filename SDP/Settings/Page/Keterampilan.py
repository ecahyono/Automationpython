from pytest_html_reporter import attach
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os, platform, time, pytest
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def MenuKegiatanPelatihan(driver):
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.ID, "pembinaan-pelatihan-keterampilan")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Kegiatan Pelatihan").click()

def MenuPresensiKegiatan(driver):
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.ID, "pembinaan-pelatihan-keterampilan")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Presensi Kegiatan").click()

def MenuLaporanPelatihanKeterampilan(driver):
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.ID, "pembinaan-pelatihan-keterampilan")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Laporan Pelatihan Keterampilan").click()

def MenuPersetujuanPesertaKegiatan(driver):
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.ID, "pembinaan-pelatihan-keterampilan")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Persetujuan Peserta Kegiatan").click()

def MenuPersetujuanPresensiPesertaKegiatan(driver):
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.ID, "pembinaan-pelatihan-keterampilan")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Persetujuan Presensi Peserta Kegiatan").click()

def VerifikasiKelulusanPesertaKegiatan(driver):
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.ID, "pembinaan-pelatihan-keterampilan")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Verifikasi Kelulusan Peserta Kegiatan").click()

def LaporanPelatihanKeterampilan(driver):
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.ID, "pembinaan-pelatihan-keterampilan")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Laporan Pelatihan Keterampilan").click()

   

def LogOut(driver):
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.ID, "avatar")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.XPATH, "//li[contains(.,'Logout')]")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.XPATH, "//li[contains(.,'Logout')]").click()