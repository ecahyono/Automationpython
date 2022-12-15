from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pytest_html_reporter import attach
import os, platform, time, pytest
from selenium import webdriver
from os import environ, path
from pathlib import Path
from pytest import mark
import platform
import logging
from openpyxl import load_workbook
import sys
import pyautogui

from dotenv import load_dotenv
load_dotenv()

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR")) 
elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))

from Settings.setup import initDriver, loadDataPath, sleep, quit
from Settings.login import login, oprupbasanbdg



Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Penerimaan_2_TambahPenerimaan.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("RUPEXEL"))
sheetrange = wb['TambahubahPenerimaan']
i = 15

JenisRegistrasi    = sheetrange['A'+str(i)].value #Jenis Registrasi
tglPenerimaan      = sheetrange['B'+str(i)].value #Tanggal Penerimaan
Noregrup           = sheetrange['C'+str(i)].value #Nomor Registrasi Rupbasan
instansi           = sheetrange['D'+str(i)].value #Instansi
Noregins           = sheetrange['E'+str(i)].value #Nomor Registrasi Instansi
NoSIP              = sheetrange['F'+str(i)].value # Nomor Surat Izin Penyitaan
tglSIP             = sheetrange['G'+str(i)].value #Tanggal Surat Izin Penyitaan
Ppenyita           = sheetrange['H'+str(i)].value #Pengadilan Penyita
NoSP               = sheetrange['I'+str(i)].value #Nomor Surat Penyitaan
tglSP              = sheetrange['J'+str(i)].value #Tanggal Surat Penyitaan
pasal              = sheetrange['K'+str(i)].value #Pasal
NBAST              = sheetrange['L'+str(i)].value #No. BA Serah Terima
Keterangan         = sheetrange['M'+str(i)].value #Keterangan

Ptgpenerima        = sheetrange['N'+str(i)].value #Petugas Penerima
pilihPTG           = sheetrange['O'+str(i)].value #Petugas Penyrah

#tab identitas
jumlahidentitas    = sheetrange['P'+str(i)].value #jumlh identitas
identitas1         = sheetrange['Q'+str(i)].value #identitas 1
identitas2         = sheetrange['R'+str(i)].value #identitas 2

jumlahpenyerah     = sheetrange['S'+str(i)].value #jumlah penyerah
# status1            = sheetrange['T'+str(i)].value #status1
Penyerah1          = sheetrange['U'+str(i)].value #penyerah1
# status2            = sheetrange['v'+str(i)].value #Penyerah1
Penyerah2          = sheetrange['W'+str(i)].value #Penyerah2

jumlahsaksi        = sheetrange['X'+str(i)].value #jumlah saksi
statusaksi1        = sheetrange['Y'+str(i)].value #statussaksi1
saksi1             = sheetrange['Z'+str(i)].value #saksi1
statusaksi2        = sheetrange['AA'+str(i)].value #statussaksi2
saksi2             = sheetrange['AB'+str(i)].value #saksi2

sheetrange1 = wb['TambahubahPenerimaan']
j = 3
Noregrupsan       = sheetrange1['C'+str(j)].value



# init driver by os
@mark.fixture_penerimaan
def test_00():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')

@mark.fixture_penerimaan
def test_00_loggin():
    # login(driver)
    oprupbasanbdg(driver)
    Log.info('Memasukan User name dan Password di halaman Login)')

@mark.fixture_penerimaan
def test_PNM_001():
	sleep(driver)
	nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['Rupbasan'])
	ActionChains(driver).move_to_element(nav1).perform()
	driver.find_element(By.LINK_TEXT, 'Penerimaan').click()
	driver.find_element(By.ID,'kataKunci').click()
	attach(data=driver.get_screenshot_as_png())
	Log.info('Mengakses menu Penerimaan dengan memilih modul Rupbasan kemudian pilih menu Penerimaan')

@mark.fixture_penerimaan
def test_PNM_002():
    sleep(driver)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
    driver.find_element(By.ID, 'filterColumn').click()
    time.sleep(1)
    driver.find_element(By. ID, 'no_reg').click()

    driver.find_element(By. ID, 'kataKunci').send_keys(Noregrupsan)

    driver.find_element(By.ID , 'searchButton').click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
    attach(data=driver.get_screenshot_as_png()) 
    Log.info('Melakukan pengecekan filtering data berdasarkan kategori')

@mark.fixture_penerimaan
def test_PNM003_1():
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
    driver.find_element(By.ID, 'createButton').click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Membuka halaman tambah penerimaan dengan klik button tambah')

@mark.fixture_penerimaan
def test_PNM003_2():
    # WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.XPATH, pathData['Rupelemen']['ubahpenerimaan']['loadhalaman'])))
    driver.find_element(By.ID, 'dropdownJenisRegistrasi').click() #Jenis Registrasi
    time.sleep(1)
    if JenisRegistrasi == 'Register Barang Rampasan Negara':
        driver.find_element(By.ID, 'jenisRegistrasi0').click()
    elif JenisRegistrasi == 'Tingkat Penyidikan':
        driver.find_element(By.ID, 'jenisRegistrasi1').click()
    elif JenisRegistrasi == 'Tingkat Penuntutan':
        driver.find_element(By.ID, 'jenisRegistrasi2').click()
    elif JenisRegistrasi == 'Tingkat Pengadilan Negeri':
        driver.find_element(By.ID, 'jenisRegistrasi3').click()
    elif JenisRegistrasi == 'Tingkat Pengadilan Tinggi':
        driver.find_element(By.ID, 'jenisRegistrasi4').click()
    elif JenisRegistrasi == 'Tingkat Mahkamah Agung':
        driver.find_element(By.ID, 'jenisRegistrasi5').click()
    elif JenisRegistrasi == 'Register Khusus Tingkat Penyidikan':
        driver.find_element(By.ID, 'jenisRegistrasi6').click()
    elif JenisRegistrasi == 'Register Khusus Tingkat Penyidikan':
        driver.find_element(By.ID, 'jenisRegistrasi7').click()
    elif JenisRegistrasi == 'Register Khusus Tingkat Pengadilan Negeri':
        driver.find_element(By.ID, 'jenisRegistrasi8').click()
    elif JenisRegistrasi == 'Register Khusus Tingkat Pengadilan Tinggi':
        driver.find_element(By.ID, 'jenisRegistrasi9').click()
    elif JenisRegistrasi == 'Register Khusus Tingkat Mahkamah Agung':
        driver.find_element(By.ID, 'jenisRegistrasi10').click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Memeilih Dropdown Jenis Registrasi')

@mark.fixture_penerimaan
def test_PNM003_3():
    Tanggal_Penerimaan = driver.find_element(By.ID,'inputTglPenerimaan') #Tanggal Penerimaan
    Tanggal_Penerimaan.send_keys(tglPenerimaan)
    Tanggal_Penerimaan.send_keys(Keys.ENTER)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Menginput Tanggal Penerimaan')

@mark.fixture_penerimaan
def test_PNM003_4():
    driver.find_element(By.ID, 'inputNoRegistrasi').send_keys(Noregrup) #Nomor Registrasi Rupbasan
    Log.info('Menginput Nomor Registrasi Rupbasan')

@mark.fixture_penerimaan
def test_PNM003_5():
    driver.find_element(By.ID, 'dropdownInstansi').click() #Instansi
    time.sleep(2)
    if instansi == 'POLDA JABAR':
        pyautogui.typewrite(instansi)
        driver.find_element(By.ID, 'instansi0').click()
    elif instansi == 'POLRES BANDUNG':
        pyautogui.typewrite(instansi)
        driver.find_element(By.ID, 'instansi3').click()
    elif instansi == 'POLRES CIMAHI':
        pyautogui.typewrite(instansi)
        driver.find_element(By.ID, 'instansi10').click()
    elif instansi == 'POLRES CIREBON':
        pyautogui.typewrite(instansi)
        driver.find_element(By.ID, 'instansi18').click()
    elif instansi == 'POLRES KUNINGAN':
        pyautogui.typewrite(instansi)
        driver.find_element(By.ID, 'instansi21').click()
    elif instansi == 'POLRESTA SURAKARTA':
        pyautogui.typewrite(instansi)
        driver.find_element(By.ID, 'instansi38').click()
    elif instansi == 'POLRES CIAMIS':
        pyautogui.typewrite(instansi)
        driver.find_element(By.ID, 'instansi15').click()
    elif instansi == 'POLRES BANJAR KOTA':
        pyautogui.typewrite(instansi)
        driver.find_element(By.ID, 'instansi16').click()
    elif instansi == 'POLRES MAJALENGKA':
        pyautogui.typewrite(instansi)
        driver.find_element(By.ID, 'instansi19').click()
    elif instansi == 'POLRES INDRAMAYU':
        pyautogui.typewrite(instansi)
        driver.find_element(By.ID, 'instansi20').click()
    elif instansi == 'POLRES JAKARTA BARAT':
        pyautogui.typewrite(instansi)
        driver.find_element(By.ID, 'instansi24').click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Memilih Opsi instansi')

@mark.fixture_penerimaan
def test_PNM003_6():
    driver.find_element(By.ID, 'inputNoRegInstansi').send_keys(Noregins) #Nomor Registrasi Instansi
    attach(data=driver.get_screenshot_as_png())
    Log.info('Menginput Nomor Registrasi Instansi')

@mark.fixture_penerimaan
def test_PNM003_7():
    driver.find_element(By.ID,'inputNoSuratIzinPenyitaan').send_keys(NoSIP) #Nomor Surat Izin Penyitaan
    attach(data=driver.get_screenshot_as_png())
    Log.info('Menginput Nomor Surat Izin Penyitaan')

@mark.fixture_penerimaan
def test_PNM003_8():
    Tanggal_Surat_Izin_Penyitaan = driver.find_element(By.ID,'inputTglSuratIzinPenyitaan') #Tanggal Surat Izin Penyitaan
    Tanggal_Surat_Izin_Penyitaan.send_keys(tglSIP)
    Tanggal_Surat_Izin_Penyitaan.send_keys(Keys.ENTER)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Menginput Tanggal Surat Izin Penyitaan')

@mark.fixture_penerimaan
def test_PNM003_9():
    driver.find_element(By.ID, 'dropdownPengadilanPenyita').click()
    time.sleep(2)
    if Ppenyita == 'Pengadilan Negeri Jakarta Utara':
        pyautogui.typewrite(Ppenyita)
        driver.find_element(By.ID, 'pengadilanNegeri2').click()
    elif Ppenyita == 'Pengadilan Negeri Bandung':
        pyautogui.typewrite(Ppenyita)
        driver.find_element(By.ID, 'pengadilanNegeri7').click()
    elif Ppenyita == 'Pengadilan Negeri Sukabumi':
        pyautogui.typewrite(Ppenyita)
        driver.find_element(By.ID, 'pengadilanNegeri9').click()
    elif Ppenyita == 'Pengadilan Negeri Tasikmalaya': 
        pyautogui.typewrite(Ppenyita)
        driver.find_element(By.ID, 'pengadilanNegeri15').click()
    elif Ppenyita == 'Pengadilan Negeri Majalengka': 
        pyautogui.typewrite(Ppenyita)
        driver.find_element(By.ID, 'pengadilanNegeri19').click()
    elif Ppenyita == 'Pengadilan Negeri Ciamis': 
        pyautogui.typewrite(Ppenyita)
        driver.find_element(By.ID, 'pengadilanNegeri20').click()
    elif Ppenyita == 'Pengadilan Negeri Kuningan': 
        pyautogui.typewrite(Ppenyita)
        driver.find_element(By.ID, 'pengadilanNegeri21').click()
    elif Ppenyita == 'Pengadilan Negeri Subang':
        driver.find_element(By.ID, 'pengadilanNegeri23').click()
        pyautogui.typewrite(Ppenyita)
    elif Ppenyita == 'Pengadilan Negeri Bangkalan': 
        pyautogui.typewrite(Ppenyita)
        driver.find_element(By.ID, 'pengadilanNegeri39').click()
    elif Ppenyita == 'Pengadilan Negeri Yogyakarta': 
        pyautogui.typewrite(Ppenyita)
        driver.find_element(By.ID, 'pengadilanNegeri147').click()
    elif Ppenyita == 'Pengadilan Negeri Bondowoso': 
        pyautogui.typewrite(Ppenyita)
        driver.find_element(By.ID, 'pengadilanNegeri48').click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Memilih Opsi Pengadilan Penyita')

@mark.fixture_penerimaan
def test_PNM003_10():
    driver.find_element(By.ID, 'inputNoSuratPenyitaan').send_keys(NoSP) #Nomor Surat Penyitaan
    attach(data=driver.get_screenshot_as_png())
    Log.info('menginput nomor surat Penyitaan')

@mark.fixture_penerimaan
def test_PNM003_11():
    Tanggal_Surat_Izin_Penyitaan = driver.find_element(By.ID,'inputTglSuratPenyitaan') #Tanggal Surat Penyitaan
    Tanggal_Surat_Izin_Penyitaan.send_keys(tglSP)
    Tanggal_Surat_Izin_Penyitaan.send_keys(Keys.ENTER)
    attach(data=driver.get_screenshot_as_png())
    Log.info('menginput tanggal surat Penyitaan')

@mark.fixture_penerimaan
def test_PNM003_12():
    driver.find_element(By.ID,'inputPasal').send_keys(pasal) #Pasal
    attach(data=driver.get_screenshot_as_png())
    Log.info('input pasal')

@mark.fixture_penerimaan
def test_PNM003_13():
    driver.find_element(By.ID, 'inputNoBaSerahTerima').send_keys(NBAST) #No. BA Serah Terima
    attach(data=driver.get_screenshot_as_png())
    Log.info('Input field text input menggunakan varchar')
	
@mark.fixture_penerimaan
def test_PNM003_14():
    driver.find_element(By.ID, 'inputKeterangan').send_keys(Keterangan)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Input field text area')

@mark.fixture_penerimaan
def test_PNM003_15():
    penerima = driver.find_element(By.ID, 'searchPetugasPenerima') #Petugas Penerima
    penerima.click()
    penerima.send_keys(Ptgpenerima)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID,'searchPetugasPenerima0')))
    driver.find_element(By.ID, 'searchPetugasPenerima0').click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Melakukan Pencarian data Identitas petugas Penerima')

@mark.fixture_penerimaan
def test_PNM003_16():
    penyerah = driver.find_element(By.ID, 'searchPetugasYangMenyerahkan') #Petugas Penyrah
    penyerah.click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID,'searchPetugasYangMenyerahkan0')))
    penyerah.send_keys(pilihPTG)
    driver.find_element(By.ID, 'searchPetugasYangMenyerahkan0').click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Melakukan Pencarian data Petugas yang menyerahkan')

@mark.fixture_penerimaan
def test_PNM003_17():
    if jumlahidentitas == 2 :
        driver.find_element(By.ID, 'tambahIdentitas').click()
    elif jumlahidentitas == 1 :
        print('-')
        Log.info(' menambah 1 baris status petugas')
    attach(data=driver.get_screenshot_as_png())
    Log.info('Pengecekan jumlah data identitas yang akan di inputkan')

#tab Identitas 
@mark.fixture_penerimaan
def test_PNM003_18():
    identi1 = driver.find_element(By.ID, "searchIdentitas-0")
    identi1.click()
    identi1.send_keys(identitas1)
    driver.find_element(By. ID, 'searchIdentitas-00').click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Melakukan Pencarian data Identitas')

    identi2 = driver.find_element(By.ID, "searchIdentitas-1")
    identi2.click()
    identi2.send_keys(identitas2)
    driver.find_element(By. ID, 'searchIdentitas-10').click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Melakukan Pencarian data Identitas')

# Tab Petugas Instansi Yng Menyerahkan
@mark.fixture_penerimaan
def test_PNM003_19():
    driver.find_element(By.ID, "tab-petugas_instansi").click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('klik tab Petugas Instansi')
    
@mark.fixture_penerimaan
def test_PNM003_20():
    if jumlahpenyerah == 2 :
        driver.find_element(By.ID, "tambahPenyerahPenerima").click()
    elif jumlahpenyerah == 1 :
        print('')
    attach(data=driver.get_screenshot_as_png())
    Log.info(' menambah 1 baris status petugas')

@mark.fixture_penerimaan
def test_PNM003_21():	
    nyerah1 = driver.find_element(By.ID, 'searchPetugasPenyerah-0')
    nyerah1.click()
    nyerah1.send_keys(Penyerah1)
    driver.find_element(By.ID,'searchPetugasPenyerah-00').click()
    Log.info('Memilih Petugas Instansi Yang menyerahkan pertama')

    nyerah2 = driver.find_element(By.ID, 'searchPetugasPenyerah-1')
    nyerah2.click()
    nyerah2.send_keys(Penyerah2)
    driver.find_element(By.ID,'searchPetugasPenyerah-10').click()
    Log.info('Melakukan Pencarian data petugas penyerah internal')
    Log.info('Memilih Petugas Instansi Yang menyerahkan kedua')

# #tab Saksi
@mark.fixture_penerimaan
def test_PNM003_22():
    driver.find_element(By.ID, "tab-saksi_penerimaan").click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Klik tab Saksi Penerima')

@mark.fixture_penerimaan
def test_PNM003_23():
    if jumlahsaksi == 2 :
        driver.find_element(By.ID, "tambahSaksi").click()
    elif jumlahsaksi == 1 :
        print('')
    attach(data=driver.get_screenshot_as_png())
    Log.info(' menambah 1 baris status petugas saksi')

@mark.fixture_penerimaan
def test_PNM003_24():
    if statusaksi1 == 'Internal':
        driver.find_element(By.ID, 'searchSaksi-0-Internal').click()
        Log.info('memilih radiobutton status petugas Saksi Internal')

        statsaks1 = driver.find_element(By.ID, 'searchSaksi-0')
        statsaks1.click()
        statsaks1.send_keys(saksi1)
        driver.find_element(By.ID,'searchSaksi-00').click()
        Log.info('melakukan pencarian data petuggas saksi internal')

    elif statusaksi1 == 'External':
        driver.find_element(By.ID, 'searchSaksi-0-Eksternal').click()
        Log.info('Memilih radiobutton status petugas saksi External')

        statusaks1 = driver.find_element(By.ID, 'searchSaksi-0')
        statusaks1.click()
        statusaks1.send_keys(saksi1)
        driver.find_element(By.ID,'searchSaksi-00').click()
        Log.info('melakukan pencarian data petuggas saksi External baris pertama')

    if statusaksi2 == 'Internal':
        driver.find_element(By.ID, 'searchSaksi-1-Internal').click()
        
        statsak2 = driver.find_element(By.ID, 'searchSaksi-1')
        statsak2.click()
        statsak2.send_keys(saksi2)
        driver.find_element(By.ID,'searchSaksi-10').click()
    elif statusaksi2 == 'External':
        driver.find_element(By.ID, 'searchSaksi-1-Eksternal').click()
        
        statsak2 = driver.find_element(By.ID, 'searchSaksi-1')
        statsak2.click()
        statsak2.send_keys(saksi2)
        driver.find_element(By.ID,'searchSaksi-10').click()
        Log.info('Melakukan Pencarian data petugas saksi external baris kedua')
        
    attach(data=driver.get_screenshot_as_png())
    Log.info('Melakukan Pencarian data petugas saksi external')

# @mark.fixture_penerimaan
# def test_PNM003_25():    
#     driver.find_element(By.ID, "submitButton").click()
#     WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
#     Log.info('menekan button submit')

# @mark.fixture_penerimaan
# def test_Pencariandata():
# 	sleep(driver)
# 	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
# 	driver.find_element(By.ID, 'filterColumn').click()
# 	time.sleep(1)
# 	driver.find_element(By.ID, 'no_reg').click()
# 	driver.find_element(By. ID, 'kataKunci').send_keys(Noregrup)
# 	driver.find_element(By.ID , 'searchButton').click()
# 	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))

