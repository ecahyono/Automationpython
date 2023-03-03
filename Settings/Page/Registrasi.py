from pytest_html_reporter import attach
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os, platform, time, pytest
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('aksesmenu.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

def Registrasi_Penerimaan(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, 'PP0')
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.LINK_TEXT, 'Penerimaan').click()

def Registrasi_penolakan(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, 'PP0')
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/registrasi/penolakan").click()
    

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/registrasi/registrasi-tahanan-narapidana").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    nav3 = driver.find_element(By.ID, "RGTRS01")
    ActionChains(driver).move_to_element(nav3).perform()
    driver.find_element(By.ID, "/registrasi/masa-habis-penahanan").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    nav3 = driver.find_element(By.ID, "RGTRS01")
    ActionChains(driver).move_to_element(nav3).perform()
    driver.find_element(By.ID, "/registrasi/perpanjangan-tahanan").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    nav3 = driver.find_element(By.ID, "RGTRS01")
    ActionChains(driver).move_to_element(nav3).perform()
    driver.find_element(By.ID, "/registrasi/penahanan-lanjutan").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    nav3 = driver.find_element(By.ID, "RGTRS01")
    ActionChains(driver).move_to_element(nav3).perform()
    driver.find_element(By.ID, "/registrasi/tahanan-luar").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    nav3 = driver.find_element(By.ID, "RGTRS02")
    ActionChains(driver).move_to_element(nav3).perform()
    nav4 = driver.find_element(By.ID, "RO1")
    ActionChains(driver).move_to_element(nav4).perform()
    driver.find_element(By.ID, "/registrasi/dashboard-remisi").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    nav3 = driver.find_element(By.ID, "RGTRS02")
    ActionChains(driver).move_to_element(nav3).perform()
    nav4 = driver.find_element(By.ID, "RO1")
    ActionChains(driver).move_to_element(nav4).perform()
    driver.find_element(By.ID, "/registrasi/daftar-buku-masuk").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    nav3 = driver.find_element(By.ID, "RGTRS02")
    ActionChains(driver).move_to_element(nav3).perform()
    nav4 = driver.find_element(By.ID, "RO1")
    ActionChains(driver).move_to_element(nav4).perform()
    driver.find_element(By.ID, "/registrasi/daftar-usulan").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    nav3 = driver.find_element(By.ID, "RGTRS02")
    ActionChains(driver).move_to_element(nav3).perform()
    nav4 = driver.find_element(By.ID, "RO1")
    ActionChains(driver).move_to_element(nav4).perform()
    driver.find_element(By.ID, "/registrasi/laporan-usulan").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    nav3 = driver.find_element(By.ID, "RGTRS02")
    ActionChains(driver).move_to_element(nav3).perform()
    nav4 = driver.find_element(By.ID, "RO1")
    ActionChains(driver).move_to_element(nav4).perform()
    nav5 = driver.find_element(By.ID, "RO3").click()
    ActionChains(driver).move_to_element(nav5).perform()
    driver.find_element(By.ID, "/registrasi/surat-keputusan-remisi").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    nav3 = driver.find_element(By.ID, "RGTRS02")
    ActionChains(driver).move_to_element(nav3).perform()
    nav4 = driver.find_element(By.ID, "RO1")
    ActionChains(driver).move_to_element(nav4).perform()
    nav5 = driver.find_element(By.ID, "RO3").click()
    ActionChains(driver).move_to_element(nav5).perform()
    driver.find_element(By.ID, "/registrasi/otorisasi-surat-keputusan").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    nav3 = driver.find_element(By.ID, "RGTRS02")
    ActionChains(driver).move_to_element(nav3).perform()
    nav4 = driver.find_element(By.ID, "RO1")
    ActionChains(driver).move_to_element(nav4).perform()
    nav5 = driver.find_element(By.ID, "RO3").click()
    ActionChains(driver).move_to_element(nav5).perform()
    driver.find_element(By.ID, "/registrasi/pencabutan-perbaikan-surat-keputusan").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    nav4 = driver.find_element(By.ID, "RO1")
    ActionChains(driver).move_to_element(nav4).perform()
    nav5 = driver.find_element(By.ID, "RO3").click()
    ActionChains(driver).move_to_element(nav5).perform()
    driver.find_element(By.ID, "/registrasi/surat-keputusan-remisi-kepala").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    nav3 = driver.find_element(By.ID, "RGTRS02")
    ActionChains(driver).move_to_element(nav3).perform()
    driver.find_element(By.ID, "/registrasi/grasi").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    nav3 = driver.find_element(By.ID, "RGTRS02")
    ActionChains(driver).move_to_element(nav3).perform()
    driver.find_element(By.ID, "/registrasi/remisi-perubahan-pidana").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    nav3 = driver.find_element(By.ID, "RGTRS02")
    ActionChains(driver).move_to_element(nav3).perform()
    nav4 = driver.find_element(By.ID, "3AA").click()
    ActionChains(driver).move_to_element(nav4).perform()
    driver.find_element(By.ID, "/registrasi/pembayaran-denda").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    nav3 = driver.find_element(By.ID, "RGTRS02")
    ActionChains(driver).move_to_element(nav3).perform()
    nav4 = driver.find_element(By.ID, "3AA").click()
    ActionChains(driver).move_to_element(nav4).perform()
    driver.find_element(By.ID, "/registrasi/pembayaran-uang-pengganti").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    nav3 = driver.find_element(By.ID, "RGTRS02")
    ActionChains(driver).move_to_element(nav3).perform()
    nav4 = driver.find_element(By.ID, "3AA").click()
    ActionChains(driver).move_to_element(nav4).perform()
    driver.find_element(By.ID, "/registrasi/pembayaran-restitusi").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/registrasi/mutasi-golongan").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/registrasi/masih-ada-perkara").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/registrasi/mutasi-upt").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/registrasi/pengeluaran-dan-pembebasan").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/registrasi/melarikan-diri").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/registrasi/masuk-kembali").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/registrasi/surat-sidang").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/registrasi/meninggal-dunia").click()

def Registrasi(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "20")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/registrasi/klasifikasi-narkotika").click()

def Registrasi_identitas(driver):
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, '/registrasi/identitas')))
    driver.find_element(By.LINK_TEXT, "Daftar Identitas").click()

def Registrasi_Barangbawaan():
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "D00").click()
    driver.find_element(By.ID, "/registrasi/barang-bawaan").click()

    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "D00").click()
    driver.find_element(By.ID, "/registrasi/mutasi").click()

    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "D00").click()
    driver.find_element(By.ID, "/registrasi/barang-bawaan-biasa").click()

    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "D00").click()
    driver.find_element(By.ID, "/registrasi/barang-bawaan-presiosa").click()

    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "D00").click()
    driver.find_element(By.ID, "/registrasi/penyerahan").click()

    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "AB0").click()
    driver.find_element(By.ID, "/registrasi/penerimaan-anak-bawaan").click()
    
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "AB0").click()
    driver.find_element(By.ID, "/registrasi/daftar-anak-bawaan").click()
    
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "AB0").click()
    driver.find_element(By.ID, "/registrasi/pengeluaran-anak-bawaan").click()

    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "INTMA").click()
    driver.find_element(By.ID, "/registrasi/perpanjangan-penahanan-ma").click()
    
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "INTMA").click()
    driver.find_element(By.ID, "/registrasi/exchange-p48").click()
    
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "INTMA").click()
    driver.find_element(By.ID, "/registrasi/exchange-ba17").click()
    
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "INTMA").click()
    driver.find_element(By.ID, "/registrasi/sinkronisasi-nik").click()
    
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "RGVDT02").click()
    driver.find_element(By.ID, "/registrasi/monitoring-verifikasi-data").click()

    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "RGVDT02").click()
    driver.find_element(By.ID, "/registrasi/ubah-status-registrasi").click()

    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "RGVDT02").click()
    driver.find_element(By.ID, "/registrasi/ubah-ekspirasi-registrasi").click()
    
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "RGVDT02").click()
    driver.find_element(By.ID, "/registrasi/validasi-tanggal-ekspirasi").click()
    
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "/registrasi/bantuan-hukum").click()
    
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "30")
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/registrasi/pembinaan-lanjutan").click()
    
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "30")
    ActionChains(driver).move_to_element(nav2).perform()
    nav3 = driver.find_element(By.ID, "LAA")
    ActionChains(driver).move_to_element(nav3).perform()
    driver.find_element(By.ID, "/regsitrasi/laporan-remisi").click()
    
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "30")
    ActionChains(driver).move_to_element(nav2).perform()
    nav3 = driver.find_element(By.ID, "LAA")
    ActionChains(driver).move_to_element(nav3).perform()
    nav4 = driver.find_element(By.ID, "53R")
    ActionChains(driver).move_to_element(nav4).perform()
    driver.find_element(By.ID, "RekapitulasiRemisi").click()
    
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "/registrasi/catatan").click()
    
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "OV0").click()
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/registrasi/daftar-overstaying").click()
    
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    nav2 = driver.find_element(By.ID, "OV0").click()
    ActionChains(driver).move_to_element(nav2).perform()
    driver.find_element(By.ID, "/registrasi/rekapitulasi-overstaying").click()
    
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "/registrasi/monitoring-sidik-jari-foto").click()
    
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "/registrasi/tahapan_pembinaan").click()
    
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "/registrasi/highprofile").click()

    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "/registrasi/eksekusi_pm").click()
    
    nav1 = driver.find_element(By.ID, '01')
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.ID, "/registrasi/nomor-daftar-narapidana").click()

