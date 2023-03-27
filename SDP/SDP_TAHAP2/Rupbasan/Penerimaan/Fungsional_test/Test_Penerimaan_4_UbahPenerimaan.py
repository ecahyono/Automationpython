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
from openpyxl import load_workbook
import logging
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
fh = logging.FileHandler('Penerimaan_4_UbahPenerimaan.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("RUPEXEL"))
sheetrange = wb['TambahubahPenerimaan']
i = 12

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
status1            = sheetrange['T'+str(i)].value #status1
Penyerah1          = sheetrange['U'+str(i)].value #penyerah1
status2            = sheetrange['v'+str(i)].value #Penyerah1
Penyerah2          = sheetrange['W'+str(i)].value #Penyerah2

jumlahsaksi        = sheetrange['X'+str(i)].value #jumlah saksi
statusaksi1        = sheetrange['Y'+str(i)].value #statussaksi1
saksi1             = sheetrange['Z'+str(i)].value #saksi1
statusaksi2        = sheetrange['AA'+str(i)].value #statussaksi2
saksi2             = sheetrange['AB'+str(i)].value #saksi2

# init driver by os
@mark.fixture_penerimaan
def test_Ossetup_00():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')

@mark.fixture_penerimaan
def test_loggin_00():
    # login(driver)
    oprupbasanbdg(driver)
    Log.info('Memasukan User name dan Password di halaman Login)')

@mark.fixture_penerimaan
def test_aksesmenuPenerimaan_00():
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['Rupbasan'])
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.LINK_TEXT, 'Penerimaan').click()
    driver.find_element(By.ID,'kataKunci').click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Menuju Menu Penerimaan dengan mengarahkan kursor ke navigasi ''Rubasan'' kemudian sub menu ''Penerimaan''')


sheetrange1 = wb['TambahubahPenerimaan']
j = 10
noregistrasi       = sheetrange1['C'+str(j)].value

@mark.fixture_penerimaan
def test_Pencariandata_00():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
	driver.find_element(By.ID, 'filterColumn').click()
	time.sleep(1)
	driver.find_element(By. ID, 'no_reg').click()
	driver.find_element(By. ID, 'kataKunci').send_keys(noregistrasi)
		
	driver.find_element(By.ID , 'searchButton').click()
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))

	attach(data=driver.get_screenshot_as_png()) 
	Log.info('Melakukan Pencarian data berdasarkan kategori')

@mark.fixture_penerimaan
def test_PNM_004_1():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
    driver.find_element(By.CSS_SELECTOR, ".h-5").click()
    WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.XPATH, pathData['Rupelemen']['ubahpenerimaan']['loadhalaman'])))
	
@mark.fixture_penerimaan
def test_PNM_004_3():
    sleep(driver)
    driver.find_element(By.ID, 'dropdownJenisRegistrasi').click() #Jenis Registrasi
    time.sleep(2)
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
def test_PNM_004_4():
    Tanggal_Penerimaan = driver.find_element(By.ID,'inputTglPenerimaan') #Tanggal Penerimaan
    Tanggal_Penerimaan.clear()
    Tanggal_Penerimaan.send_keys(tglPenerimaan)
    Tanggal_Penerimaan.send_keys(Keys.ENTER)
    
    Log.info('Menginput Tanggal Penerimaan')

@mark.fixture_penerimaan
def test_PNM_004_5():
    noregrup = driver.find_element(By.ID, 'inputNoRegistrasi')
    noregrup.clear()
    noregrup.send_keys(Noregrup) #Nomor Registrasi Rupbasan

    Log.info('Menginput Nomor Registrasi Rupbasan')

@mark.fixture_penerimaan
def test_PNM_004_6():
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

    Log.info('Memilih Opsi instansi')

@mark.fixture_penerimaan
def test_PNM_004_7():
    noregins = driver.find_element(By.ID, 'inputNoRegInstansi')
    noregins.clear()
    noregins.send_keys(Noregins) #Nomor Registrasi Instansi

    Log.info('Menginput Nomor Registrasi Instansi')

@mark.fixture_penerimaan
def test_PNM_004_8():
    nosrIP = driver.find_element(By.ID,'inputNoSuratIzinPenyitaan')
    nosrIP.clear()
    nosrIP.send_keys(NoSIP) #Nomor Surat Izin Penyitaan

    Log.info('Menginput Nomor Surat Izin Penyitaan')

@mark.fixture_penerimaan
def test_PNM_004_9():
    Tanggal_Surat_Izin_Penyitaan = driver.find_element(By.ID,'inputTglSuratIzinPenyitaan') #Tanggal Surat Izin Penyitaan
    Tanggal_Surat_Izin_Penyitaan.clear()
    Tanggal_Surat_Izin_Penyitaan.send_keys(tglSIP)
    Tanggal_Surat_Izin_Penyitaan.send_keys(Keys.ENTER)

    Log.info('Menginput Tanggal Surat Izin Penyitaan')

@mark.fixture_penerimaan
def test_PNM_004_10():
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

    Log.info('Memilih Opsi Pengadilan Penyita')

@mark.fixture_penerimaan
def test_PNM_004_11():
    NSP = driver.find_element(By.ID, 'inputNoSuratPenyitaan')
    NSP.clear()
    NSP.send_keys(NoSP) #Nomor Surat Penyitaan

    Log.info('menginput nomor surat Penyitaan')

@mark.fixture_penerimaan
def test_PNM_004_12():
    TglSrtIzinPenyitaan = driver.find_element(By.ID,'inputTglSuratPenyitaan') #Tanggal Surat Penyitaan
    TglSrtIzinPenyitaan.clear()
    TglSrtIzinPenyitaan.send_keys(tglSP)
    TglSrtIzinPenyitaan.send_keys(Keys.ENTER)

    Log.info('menginput tanggal surat Penyitaan')

@mark.fixture_penerimaan
def test_PNM_004_13():
    psal = driver.find_element(By.ID,'inputPasal')
    psal.clear()
    psal.send_keys(pasal) #Pasal

    Log.info('input pasal')

@mark.fixture_penerimaan
def test_PNM_004_14():
    NOBA = driver.find_element(By.ID, 'inputNoBaSerahTerima')
    NOBA.clear()
    NOBA.send_keys(NBAST) #No. BA Serah Terima

    Log.info('Input field text input menggunakan varchar')

@mark.fixture_penerimaan
def test_PNM_004_15():
    ket = driver.find_element(By.ID, 'inputKeterangan')
    ket.clear()
    ket.send_keys(Keterangan) #Keterangan
    Log.info('Input field text area')

@mark.fixture_penerimaan
def test_PNM_004_16():
    penerima = driver.find_element(By.ID, 'searchPetugasPenerima') #Petugas Penerima
    penerima.click()
    penerima.send_keys(Ptgpenerima)
    driver.find_element(By.ID, 'searchPetugasPenerima0').click()
    
    Log.info('Melakukan Pencarian data Identitas petugas Penerima')

@mark.fixture_penerimaan
def test_PNM_004_17():
    penyerah = driver.find_element(By.ID, 'searchPetugasYangMenyerahkan') #Petugas Penyrah
    penyerah.click()
    penyerah.send_keys(pilihPTG)
    driver.find_element(By.ID, 'searchPetugasYangMenyerahkan0').click()
    
    Log.info('Melakukan Pencarian data Petugas yang menyerahkan')

# tab Identitas 
@mark.fixture_penerimaan
def test_PNM_004_18():
	if jumlahidentitas == 3:
		driver.find_element(By.ID, 'tambahIdentitas').click()
		identi0 = driver.find_element(By.ID, "searchIdentitas-0")
		identi0.click()
		identi0.send_keys(identitas1)
		driver.find_element(By. ID, 'searchIdentitas-00').click()
		Log.info('Melakukan Pencarian data Identitas pertama')

		identi1 = driver.find_element(By.ID, "searchIdentitas-1")
		identi1.click()
		identi1.send_keys(identitas2)
		driver.find_element(By. ID, 'searchIdentitas-10').click()
		Log.info('Melakukan Pencarian data Identitas kedua')
		
		identi2 = driver.find_element(By.ID, "searchIdentitas-2")
		identi2.click()
		identi2.send_keys(identitas2)
		driver.find_element(By. ID, 'searchIdentitas-20').click()
		Log.info('Melakukan Pencarian data Identitas ketiga')
	elif jumlahidentitas == 2:
		id1 = driver.find_element(By.ID, "searchIdentitas-0")
		id1.click()
		id1.send_keys(identitas1)
		driver.find_element(By. ID, 'searchIdentitas-00').click()
		Log.info('Melakukan Pencarian data Identitas')
    
		id2 = driver.find_element(By.ID, "searchIdentitas-1")
		id2.click()
		id2.send_keys(identitas2)
		driver.find_element(By. ID, 'searchIdentitas-10').click()
		Log.info('Melakukan Pencarian data Identitas')
	elif jumlahidentitas == 1:
		identi0 = driver.find_element(By.ID, "searchIdentitas-0")
		identi0.click()
		identi0.send_keys(identitas1)
		driver.find_element(By. ID, 'searchIdentitas-00').click()
		Log.info('Melakukan Pencarian data Identitas')

# Tab Petugas Instansi Yng Menyerahkan
@mark.fixture_penerimaan
def test_PNM_004_19():
    driver.find_element(By.ID, "tab-petugas_instansi").click()
    Log.info('klik tab Petugas Instansi')
    

@mark.fixture_penerimaan
def test_PNM_004_20():
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
def test_PNM_004_21():
    driver.find_element(By.ID, "tab-saksi_penerimaan").click()
    Log.info('Klik tab Saksi Penerima')

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

@mark.fixture_penerimaan
def test_PNM_004_23():    
    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
    Log.info('menekan button submit')

# @mark.fixture_penerimaan
# def test_PNM_004_():
# 	quit(driver)
# 	Log.info('menyelesaikan tes dan menutup browser')