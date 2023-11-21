from pytest_html_reporter import attach
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os, platform, time, pytest
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def MenuGiatja(driver):

    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'pembinaan-10')))
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "kegiatan-kerja-dan-produksi-2")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Kegiatan Kerja").click()

def MenuPemasaran(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'pembinaan-10')))
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "kegiatan-kerja-dan-produksi-2")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Pemasaran").click()



def MenuPNBP(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'pembinaan-10')))
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "kegiatan-kerja-dan-produksi-2")
    time.sleep(0.5)
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "PNBP").click()

def MenuLaporan(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'pembinaan-10')))
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "kegiatan-kerja-dan-produksi-2")
    time.sleep(0.5)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.5)
    driver.find_element(By.LINK_TEXT, "Laporan Kegiatan Kerja dan Produksi").click()


def MenuKegiatanPelatihan(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'pembinaan-10')))
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.ID, "pembinaan-pelatihan-keterampilan")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Program Pelatihan").click()

def MenuPresensiKegiatan(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'pembinaan-10')))
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.ID, "pembinaan-pelatihan-keterampilan")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Presensi Kegiatan").click()

def MenuLaporanPelatihanKeterampilan(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'pembinaan-10')))
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.ID, "pembinaan-pelatihan-keterampilan")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Laporan Pelatihan Keterampilan").click()

def MenuPersetujuanPesertaKegiatan(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'pembinaan-10')))
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.ID, "pembinaan-pelatihan-keterampilan")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Persetujuan Program Dan Peserta").click()

def MenuPersetujuanPresensiPesertaKegiatan(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'pembinaan-10')))
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.ID, "pembinaan-pelatihan-keterampilan")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Persetujuan Presensi Peserta Kegiatan").click()

def VerifikasiKelulusanPesertaKegiatan(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'pembinaan-10')))
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.ID, "pembinaan-pelatihan-keterampilan")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Kelulusan Peserta").click()

def LaporanPelatihanKeterampilan(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'pembinaan-10')))
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.ID, "pembinaan-pelatihan-keterampilan")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Laporan Pelatihan").click()

def MenuSPPNPenilaianPembinaan(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'pembinaan-10')))
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.ID, "SPPN-11")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Penilaian Pembinaan").click()

def MenuSPPNPerwalian(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'pembinaan-10')))
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.2)
    nav2 = driver.find_element(By.ID, "SPPN-11")
    time.sleep(0.2)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.2)
    nav3 = driver.find_element(By.ID, "perwalian-11")
    time.sleep(0.2)
    ActionChains(driver).move_to_element(nav3).perform()
    driver.find_element(By.LINK_TEXT, "Tim Perwalian").click()

def MenuSPPNPerwalianPersetujuan(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'pembinaan-10')))
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.2)
    nav2 = driver.find_element(By.ID, "SPPN-11")
    time.sleep(0.2)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.2)
    nav3 = driver.find_element(By.ID, "perwalian-11")
    time.sleep(0.2)
    ActionChains(driver).move_to_element(nav3).perform()
    time.sleep(0.2)
    driver.find_element(By.LINK_TEXT, "Persetujuan Tim Perwalian").click()
   

def LogOut(driver):
    input("Press Enter to continue...")
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'pembinaan-10')))
    nav1 = driver.find_element(By.ID, "avatar")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.XPATH, "//li[contains(.,'Logout')]")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.5)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,'Logout')]")))
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//li[contains(.,'Logout')]").click()

def MenuSkPerwalian(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='90']")))
    nav1 = driver.find_element(By.XPATH, "//div[@id='90']")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.3)
    nav2 = driver.find_element(By.ID, "tools-konfigurasi-01")
    time.sleep(0.3)
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "SK Perwalian").click()


def MenuPenilaian(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "pembinaan-10")))
    nav1 = driver.find_element(By.ID, "pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "SPPN-11")
    time.sleep(0.5)
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Penilaian Pembinaan Narapidana").click()


def LaporanBulananWali(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "pembinaan-10")))
    nav1 = driver.find_element(By.ID, "pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "SPPN-11")
    time.sleep(0.5)
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Laporan SPPN").click()

def laporanSPPN(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "pembinaan-10")))
    nav1 = driver.find_element(By.ID, "pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "SPPN-11")
    time.sleep(0.5)
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Laporan SPPN").click()

def KepribadianKegiatanPembinaan(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "pembinaan-10")))
    nav1 = driver.find_element(By.ID, "pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "kepribadian-10")
    time.sleep(0.5)
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Kegiatan Pembinaan").click()

def PersetujuanProgramDanPesertaKegiatan(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "pembinaan-10")))
    nav1 = driver.find_element(By.ID, "pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.5)
    nav2 = driver.find_element(By.ID, "kepribadian-10")
    time.sleep(0.5)
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, "Persetujuan Program Dan Peserta Kegiatan").click()
    