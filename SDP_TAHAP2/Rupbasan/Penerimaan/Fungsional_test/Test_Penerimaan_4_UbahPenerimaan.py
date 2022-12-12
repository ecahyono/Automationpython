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

from dotenv import load_dotenv
load_dotenv()

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR")) 
elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))

from Settings.setup import initDriver, loadDataPath, sleep, quit
from Settings.login import login


Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Penerimaan_4_UbahPenerimaan.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("RUPEXEL"))
sheetrange = wb['TambahubahPenerimaan']
i = 4

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
def test_Ossetup_1():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')

@mark.fixture_penerimaan
def test_loggin_2():
    login(driver)
    Log.info('Memasukan User name dan Password di halaman Login)')

@mark.fixture_penerimaan
def test_aksesmenuPenerimaan_3():
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.LINK_TEXT, 'Penerimaan').click()
    driver.find_element(By.XPATH, pathData['Rupelemen']['indexpenempatan']['klik']).click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Menuju Menu Penerimaan dengan mengarahkan kursor ke navigasi ''Rubasan'' kemudian sub menu ''Penerimaan''')


sheetrange = wb['IndexPenerimaan']
i = 2
Carikolom       = sheetrange['A'+str(i)].value
Katkun          = sheetrange['B'+str(i)].value

@mark.fixture_penerimaan
def test_Pencariandata_4():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
	driver.find_element(By.ID, 'filterColumn').click()
	
	if Carikolom == 'No Registrasi':
		driver.find_element(By. ID, 'no_reg').click()
	elif Carikolom == 'Tgl Penerimaan':
		driver.find_element(By. ID, 'tgl_penerimaan').click()
	elif Carikolom == 'Keterangan':
		driver.find_element(By. ID, 'keterangan').click()

	
	if Carikolom == 'Tgl Penerimaan':
		kattgl = driver.find_element(By.XPATH, pathData['Rupelemen']['indexpenempatan']['kategoritanggal'])
		kattgl.click()
		kattgl.send_keys(Katkun)
	else:
		driver.find_element(By. ID, 'kataKunci').send_keys(Katkun)

	driver.find_element(By.ID , 'searchButton').click()
	
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))

	attach(data=driver.get_screenshot_as_png()) 
	Log.info('Melakukan Pencarian data berdasarkan kategori')

@mark.fixture_penerimaan
def test_membukahalamanedit_5():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
    driver.find_element(By.CSS_SELECTOR, ".h-5").click()
    # WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.XPATH, pathData['Rupelemen']['ubahpenerimaan']['loadhalaman'])))
	
# @mark.fixture_penerimaan
# def test_Inputdropdown_1():
#     WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.XPATH, pathData['Rupelemen']['ubahpenerimaan']['loadhalaman'])))
    
#     driver.find_element(By.ID, 'dropdownJenisRegistrasi').click() #Jenis Registrasi
    
#     if JenisRegistrasi == 'Register Barang Rampasan Negara':
#         driver.find_element(By.ID, 'jenisRegistrasi0').click()
#     elif JenisRegistrasi == 'Tingkat Penyidikan':
#         driver.find_element(By.ID, 'jenisRegistrasi1').click()
#     elif JenisRegistrasi == 'Tingkat Penuntutan':
#         driver.find_element(By.ID, 'jenisRegistrasi2').click()
#     elif JenisRegistrasi == 'Tingkat Pengadilan Negeri':
#         driver.find_element(By.ID, 'jenisRegistrasi3').click()
#     elif JenisRegistrasi == 'Tingkat Pengadilan Tinggi':
#         driver.find_element(By.ID, 'jenisRegistrasi4').click()
#     attach(data=driver.get_screenshot_as_png())
#     Log.info('Memeilih Dropdown Jenis Registrasi')
    

# @mark.fixture_penerimaan
# def test_Inputdate_1():
    
#     Tanggal_Penerimaan = driver.find_element(By.ID,'inputTglPenerimaan') #Tanggal Penerimaan
#     Tanggal_Penerimaan.clear()
    
#     Tanggal_Penerimaan.send_keys(tglPenerimaan)
#     Tanggal_Penerimaan.send_keys(Keys.ENTER)
    
#     Log.info('Menginput Tanggal Penerimaan')

# @mark.fixture_penerimaan
# def test_inputtext_1():
#     noregrup = driver.find_element(By.ID, 'inputNoRegistrasi')
#     noregrup.clear()
    
#     noregrup.send_keys(Noregrup) #Nomor Registrasi Rupbasan
#     Log.info('Menginput Nomor Registrasi Rupbasan')

# @mark.fixture_penerimaan
# def test_Inputdropdown_2():
#     driver.find_element(By.ID, 'dropdownInstansi').click() #Instansi
    
#     if instansi == 'POLDA JABAR':
#         driver.find_element(By.ID, 'instansi0').click()
#     elif instansi == 'POLRES BANDUNG':
#         driver.find_element(By.ID, 'instansi3').click()
#     elif instansi == 'POLRES CIMAHI':
#         driver.find_element(By.ID, 'instansi10').click()
#     elif instansi == 'POLRES CIREBON':
#         driver.find_element(By.ID, 'instansi18').click()
#     elif instansi == 'POLRES KUNINGAN':
#         driver.find_element(By.ID, 'instansi21').click()
    
#     Log.info('Memilih Opsi instansi')

# @mark.fixture_penerimaan
# def test_inputtext_2():
#     noregins = driver.find_element(By.ID, 'inputNoRegInstansi')
#     noregins.clear()
    
#     noregins.send_keys(Noregins) #Nomor Registrasi Instansi
#     Log.info('Menginput Nomor Registrasi Instansi')

# @mark.fixture_penerimaan
# def test_inputtext_3():
#     nosrIP = driver.find_element(By.ID,'inputNoSuratIzinPenyitaan')
#     nosrIP.clear()
    
#     nosrIP.send_keys(NoSIP) #Nomor Surat Izin Penyitaan
#     Log.info('Menginput Nomor Surat Izin Penyitaan')

# @mark.fixture_penerimaan
# def test_Inputdate_2():
#     Tanggal_Surat_Izin_Penyitaan = driver.find_element(By.ID,'inputTglSuratIzinPenyitaan') #Tanggal Surat Izin Penyitaan
#     Tanggal_Surat_Izin_Penyitaan.clear()
    
#     Tanggal_Surat_Izin_Penyitaan.send_keys(tglSIP)
#     Tanggal_Surat_Izin_Penyitaan.send_keys(Keys.ENTER)
#     Log.info('Menginput Tanggal Surat Izin Penyitaan')

# @mark.fixture_penerimaan
# def test_Inputdropdown_3():
#     driver.find_element(By.ID, 'dropdownPengadilanPenyita').click()
    
#     if Ppenyita == 'Pengadilan Negeri Bandung':
#         driver.find_element(By.ID, 'pengadilanNegeri7').click()
#     elif Ppenyita == 'Pengadilan Negeri Jakarta Utara':
#         driver.find_element(By.ID, 'pengadilanNegeri2').click()
#     elif Ppenyita == 'Pengadilan Negeri Sukabumi':
#         driver.find_element(By.ID, 'pengadilanNegeri9').click()
#     elif Ppenyita == 'Pengadilan Negeri Subang':
#         driver.find_element(By.ID, 'pengadilanNegeri23').click()
#     elif Ppenyita == 'Pengadilan Negeri Yogyakarta':
#         driver.find_element(By.ID, 'pengadilanNegeri147').click()
#     Log.info('Memilih Opsi Pengadilan Penyita')

# @mark.fixture_penerimaan
# def test_inputtext_4():
#     NSP = driver.find_element(By.ID, 'inputNoSuratPenyitaan')
#     NSP.clear()
    
#     NSP.send_keys(NoSP) #Nomor Surat Penyitaan
#     Log.info('menginput nomor surat Penyitaan')

# @mark.fixture_penerimaan
# def test_Inputdate_3():
#     Tanggal_Surat_Izin_Penyitaan = driver.find_element(By.ID,'inputTglSuratPenyitaan') #Tanggal Surat Penyitaan
#     Tanggal_Surat_Izin_Penyitaan.clear()
    
#     Tanggal_Surat_Izin_Penyitaan.send_keys(tglSP)
#     Tanggal_Surat_Izin_Penyitaan.send_keys(Keys.ENTER)
#     Log.info('menginput tanggal surat Penyitaan')

# @mark.fixture_penerimaan
# def test_inputtext_5():
#     psal = driver.find_element(By.ID,'inputPasal')
#     psal.clear()
    
#     psal.send_keys(pasal) #Pasal
#     Log.info('input pasal')

# @mark.fixture_penerimaan
# def test_inputtext_6():
#     NOBA = driver.find_element(By.ID, 'inputNoBaSerahTerima')
#     NOBA.clear()
    
#     NOBA.send_keys(NBAST) #No. BA Serah Terima
#     Log.info('Input field text input menggunakan varchar')

# @mark.fixture_penerimaan
# def test_Inputtextarea_1():
#     ket = driver.find_element(By.ID, 'inputKeterangan')
#     ket.clear()
    
#     ket.send_keys(Keterangan) #Keterangan
#     Log.info('Input field text area')

# @mark.fixture_penerimaan
# def test_Inputdropdown_4():
#     penerima = driver.find_element(By.ID, 'searchPetugasPenerima') #Petugas Penerima
#     penerima.click()
    
#     penerima.send_keys(Ptgpenerima)
#     driver.find_element(By.ID, 'searchPetugasPenerima0').click()
    
#     Log.info('Melakukan Pencarian data Identitas petugas Penerima')

# @mark.fixture_penerimaan
# def test_Inputdropdown_5():
#     penyerah = driver.find_element(By.ID, 'searchPetugasYangMenyerahkan') #Petugas Penyrah
#     penyerah.click()
    
#     penyerah.send_keys(pilihPTG)
#     driver.find_element(By.ID, 'searchPetugasYangMenyerahkan0').click()
    
#     Log.info('Melakukan Pencarian data Petugas yang menyerahkan')

# tab Identitas 
@mark.fixture_penerimaan
def test_Inputdropdown_6():
	WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.XPATH, pathData['Rupelemen']['ubahpenerimaan']['loadhalaman'])))
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
		identi0 = driver.find_element(By.ID, "searchIdentitas-0")
		identi0.click()

		identi0.send_keys(identitas1)
		driver.find_element(By. ID, 'searchIdentitas-00').click()
		Log.info('Melakukan Pencarian data Identitas')

		identi1 = driver.find_element(By.ID, "searchIdentitas-1")
		identi1.click()
		
		identi1.send_keys(identitas2)
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
def test_Pindahtab_1():
    driver.find_element(By.ID, "tab-petugas_instansi").click()
    Log.info('klik tab Petugas Instansi')
    

@mark.fixture_penerimaan
def test_radio_1():
    if status1 == 'Internal':
        nyerah1 = driver.find_element(By.ID, 'searchPetugasPenyerah-0')
        nyerah1.click()
        nyerah1.send_keys(Penyerah1)
        driver.find_element(By.ID,'searchPetugasPenyerah-00').click()
    elif status1 == 'External':
        driver.find_element(By.ID, 'radioButtonStatusPetugasEksternal-0').click()
        
        nyerah1 = driver.find_element(By.ID, 'searchPetugasPenyerahEksternal-0')
        nyerah1.click()
        
        nyerah1.send_keys(Penyerah1)
        
        driver.find_element(By.ID,'searchPetugasPenyerahEksternal-00').click()

    if status2 == 'Internal':
        driver.find_element(By.ID, 'radioButtonStatusPetugasInternal-1').click()
        
        Log.info('Memilih raduobutton petugas Internal')
        nyerah2 = driver.find_element(By.ID, 'searchPetugasPenyerah-1')
        nyerah2.click()
        
        nyerah2.send_keys(Penyerah2)
        
        driver.find_element(By.ID,'searchPetugasPenyerah-10').click()
        Log.info('Melakukan Pencarian data petugas penyerah internal')
    elif status2 == 'External':
        driver.find_element(By.ID, 'radioButtonStatusPetugasEksternal-1').click()
        
        Log.info('Memilih raduobutton petugas External')
        nyerah2 = driver.find_element(By.ID, 'searchPetugasPenyerahEksternal-1')
        nyerah2.click()
        
        nyerah2.send_keys(Penyerah2)
        
        driver.find_element(By.ID,'searchPetugasPenyerahEksternal-10').click()
        Log.info('Melakukan Pencarian data petugas penyerah external')

# #tab Saksi
@mark.fixture_penerimaan
def test_Pindahtabsaksii():
    driver.find_element(By.ID, "tab-saksi_penerimaan").click()
    
    Log.info('Klik tab Saksi Penerima')

@mark.fixture_penerimaan
def test_radio_2():
    if status1 == 'Internal':
        driver.find_element(By.ID, 'radioButtonStatusSaksiInternal-0').click()
        
        Log.info('memilih radiobutton status petugas Saksi Internal')
        statusaksi1 = driver.find_element(By.ID, 'searchSaksiPenerimaan-0')
        statusaksi1.click()
        
        statusaksi1.send_keys(saksi1)
        driver.find_element(By.ID,'searchSaksiPenerimaan-00').click()
        
        Log.info('melakukan pencarian data petuggas saksi internal')
    elif status1 == 'External':
        driver.find_element(By.ID, 'radioButtonStatusSaksiEksternal-0').click()
        
        Log.info('Memilih radiobutton status petugas saksi External')
        statusaksi1 = driver.find_element(By.ID, 'searchSaksiPenerimaanEksternal-0')
        statusaksi1.click()
        
        statusaksi1.send_keys(saksi1)
        
        driver.find_element(By.ID,'searchSaksiPenerimaanEksternal-00').click()
        Log.info('melakukan pencarian data petuggas saksi External')

    if status2 == 'Internal':
        driver.find_element(By.ID, 'radioButtonStatusSaksiInternal-1').click()
        
        statusaksi2 = driver.find_element(By.ID, 'searchSaksiPenerimaan-1')
        statusaksi2.click()
        
        statusaksi2.send_keys(saksi2)
        
        driver.find_element(By.ID,'searchSaksiPenerimaan-10').click()
    elif status2 == 'External':
        driver.find_element(By.ID, 'radioButtonStatusSaksiEksternal-1').click()
        
        statusaksi2 = driver.find_element(By.ID, 'searchSaksiPenerimaanEksternal-1')
        statusaksi2.click()
        
        statusaksi2.send_keys(saksi2)
        
        driver.find_element(By.ID,'searchSaksiPenerimaanEksternal-10').click()

# @mark.fixture_penerimaan
# def test_SubmitDatapenerimaan():    
#     driver.find_element(By.ID, "submitButton").click()
#     WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
#     Log.info('menekan button submit')

# @mark.fixture_penerimaan
# def keluar():
# 	quit(driver)
# 	Log.info('menyelesaikan tes dan menutup browser')