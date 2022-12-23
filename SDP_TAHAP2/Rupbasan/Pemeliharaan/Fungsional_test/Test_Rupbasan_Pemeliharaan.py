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

from Settings.setup import initDriver, loadDataPath, sleep, hold
from Settings.login import login, oprupbasanbdg


Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Test_Rupbasan_Pemeliharaan.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("RUPEXEL"))
sheetrange = wb['Pemeliharan']
i = 4

tglPemeliharaan		= sheetrange['A'+str(i)].value #Tanggal Pemeliharaan
jnspemeliharaan		= sheetrange['B'+str(i)].value #Jenis Pemeliharaan
KgiPemeliharaan		= sheetrange['C'+str(i)].value #Kegiatan Pemeliharaan
Keterangan			= sheetrange['D'+str(i)].value #Keterangan

ketpelaksana	 = sheetrange['E'+str(i)].value #Ketua Pelaksana
ptgsinternal	 = sheetrange['F'+str(i)].value #Petugas Pemeliharaan (Internal)
ptgsexternal	 = sheetrange['G'+str(i)].value #Petugas Pemeliharaan (Eksternal)

#tab Detail Pemeliharan
jumlhdetail		= sheetrange['H'+str(i)].value #jumlah
namabarang		= sheetrange['I'+str(i)].value #Nama Barang
kndbrng			= sheetrange['J'+str(i)].value #Kondisi Barang
subkonbrg		= sheetrange['K'+str(i)].value #Sub Kondisi Barang
jmlhbaik		= sheetrange['L'+str(i)].value #Jumlah Baik
jmlhRpar		= sheetrange['M'+str(i)].value #Jumlah Rusak Parah
jmlhRring		= sheetrange['N'+str(i)].value #Jumlah Rusak Ringan
ketdetail		= sheetrange['O'+str(i)].value #Keterangan

#tab identitas
jmlhbahan		= sheetrange['P'+str(i)].value #jumlah
namabahan		= sheetrange['Q'+str(i)].value #Nama Bahan
jmlhpakai		= sheetrange['R'+str(i)].value #Jumlah Pakai
satuan			= sheetrange['S'+str(i)].value #Satuan
satlain			= sheetrange['T'+str(i)].value #Satuan Lain
ketbahan		= sheetrange['U'+str(i)].value #Keterangan

# init driver by os
@mark.fixture_pemeliharaan
def test_Ossetup_1():
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')

@mark.fixture_pemeliharaan
def test_loggin_2():
	# login(driver)
	oprupbasanbdg(driver)
	Log.info('Memasukan User name dan Password di halaman Login)')

@mark.fixture_pemeliharaan
def test_PML_001():
	hold(driver)
	Log.info('Mengakses menu Pemeliharaan dengan memilih modul Rupbasan kemudian pilih menu Pemeliharaan')
	nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['Rupbasan'])
	ActionChains(driver).move_to_element(nav1).perform()
	time.sleep(1)
	driver.find_element(By.LINK_TEXT, 'Pemeliharaan').click()
	driver.find_element(By.ID, 'kataKunci').click()
	attach(data=driver.get_screenshot_as_png())


plm = wb['Pemeliharan']
j = 3
tglplm  = plm['A'+str(j)].value #Tanggal Pemeliharaan

@mark.fixture_pemeliharaan
def test_PML_002():#pencarian data
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
	hold(driver)
	Log.info('Pengecekan data yang telah di filter')
	driver.find_element(By.ID, 'filterColumn').click()
	time.sleep(1)
	driver.find_element(By.ID, 'tglPemeliharaan').click()
	tgl = driver.find_element(By.ID, 'filterTanggal')
	tgl.send_keys(tglplm)
	driver.find_element(By.ID, 'searchButton').click()

@mark.fixture_pemeliharaan
def test_PML_003_0():
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
	hold(driver)
	Log.info('Membuka halaman tambah penerimaan dengan klik button tambah')
	driver.find_element(By.ID, 'createButton').click()
	attach(data=driver.get_screenshot_as_png())

@mark.fixture_pemeliharaan
def test_PML_003_1():
	tglpem = driver.find_element(By.XPATH, '//*[@id="tglPemeliharaan"]')
	tglpem.send_keys(tglPemeliharaan)
	tglpem.send_keys(Keys.ENTER)
@mark.fixture_pemeliharaan
def test_PML_003_2():
	driver.find_element(By.ID, 'inputJenisPemeliharaan').click()
	WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.ID , 'JPB1')))
	if jnspemeliharaan =='Pemeliharaan Basan dan Baran Umum':
		driver.find_element(By.ID, 'JPB1').click()
	elif jnspemeliharaan == 'Pemeliharaan Basan dan Baran Khusus':
		driver.find_element(By.ID, 'JPB2').click()
@mark.fixture_pemeliharaan
def test_PML_003_3():
	driver.find_element(By.ID, 'inputKegiatanPemeliharaan').click()
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'KPB1')))	
	if KgiPemeliharaan == 'Pemeliharaan Berkala (Preventive Maintenance)':
		driver.find_element(By.ID, 'KPB1').click()
	elif KgiPemeliharaan == 'Pemeliharaan Darurat (Emergency)':
		driver.find_element(By.ID, 'KPB2').click()
@mark.fixture_pemeliharaan
def test_PML_003_4():
	driver.find_element(By.ID, 'keterangan').send_keys(KgiPemeliharaan)#Keterangan kegiatan

@mark.fixture_pemeliharaan
def test_PML_003_5():
	ketu = driver.find_element(By.ID, 'cariKetua')
	ketu.click()
	ketu.send_keys(ketpelaksana) #Ketua Pelaksana
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'cariKetua0')))
	driver.find_element(By.ID, 'cariKetua0').click()
@mark.fixture_pemeliharaan
def test_PML_003_6():
	ptginter = driver.find_element(By.ID, 'cariPetugasInternal')
	ptginter.click()
	ptginter.send_keys(ptgsinternal) #Petugas Pemeliharaan (Internal)
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'cariPetugasInternal0')))
	driver.find_element(By.ID, 'cariPetugasInternal0').click()
@mark.fixture_pemeliharaan
def test_PML_003_7():
	ptgexter = driver.find_element(By.ID, 'cariPetugasEksternal')
	ptgexter.click()
	ptgexter.send_keys(ptgsexternal) #Petugas Pemeliharaan (Eksternal)
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'cariPetugasEksternal0')))
	driver.find_element(By.ID, 'cariPetugasEksternal0').click()
#
#test_PML_003_8 #jumlah Detail pemeliharaan
#
#
#
#
#
#
@mark.fixture_pemeliharaan
def test_PML_003_9():
	nabar = driver.find_element(By.ID, 'namaBarang0')
	nabar.click()
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'nama_barang-0-0')))
	nabar.send_keys(namabarang)
	nabar.send_keys(Keys.DOWN)
	nabar.send_keys(Keys.ENTER)
@mark.fixture_pemeliharaan
def test_PML_003_10():
	konbar = driver.find_element(By.ID, 'KondisiBarang0')
	konbar.click()
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'kondisi_barang-0-0')))
	konbar.send_keys(kndbrng)
	konbar.send_keys(Keys.DOWN)
	konbar.send_keys(Keys.ENTER)
@mark.fixture_pemeliharaan
def test_PML_003_11():
	if kndbrng == 'Rusak':
		subkonbar = driver.find_element(By.ID, 'subKondisiBarang0').click()
		WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'sub_kondisi_barang-0-0')))
		Subkonbar.send_keys(subkonbrg)
		Subkonbar.send_keys(Keys.DOWN)
		Subkonbar.send_keys(Keys.ENTER)
	else:
		pass
@mark.fixture_pemeliharaan
def test_PML_003_12():
	driver.find_element(By.ID,'jumlahBaik0').send_keys(jmlhbaik)
@mark.fixture_pemeliharaan
def test_PML_003_13():
	driver.find_element(By.ID,'jumlahRusakParah0').send_keys(jmlhRpar)
@mark.fixture_pemeliharaan
def test_PML_003_14():
	driver.find_element(By.ID,'jumlahRusakRingan0').send_keys(jmlhRring)
@mark.fixture_pemeliharaan
def test_PML_003_15():
	driver.find_element(By.ID,'keteranganBarang0').send_keys(ketdetail)

@mark.fixture_pemeliharaan
def test_PML_003_16():
	driver.find_element(By.ID,'tab-bahan_pemeliharaan').click()

#
#test_PML_003_17 #jumlah Detail pemeliharaan
#
#
#
#
#
#
@mark.fixture_pemeliharaan
def test_PML_003_18():
	driver.find_element(By.ID,'tab-bahan_pemeliharaan').click()
@mark.fixture_pemeliharaan
def test_PML_003_19():
	driver.find_element(By.ID, 'namaBahan0').send_keys(namabahan)
@mark.fixture_pemeliharaan
def test_PML_003_20():
	driver.find_element(By.ID, 'jmlPakai0').send_keys(jmlhpakai)
@mark.fixture_pemeliharaan
def test_PML_003_21():
	stuan = driver.find_element(By.ID, 'satuanBarang0')
	stuan.click()
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'satuan-0-0')))
	stuan.send_keys(satuan)
	stuan.send_keys(Keys.DOWN)
	stuan.send_keys(Keys.ENTER)
@mark.fixture_pemeliharaan
def test_PML_003_22():
	driver.find_element(By.ID, 'satuanLain0').send_keys(satlain)
@mark.fixture_pemeliharaan
def test_PML_003_23():
	driver.find_element(By.ID, 'keteranganBahan0').send_keys(ketbahan)

@mark.fixture_pemeliharaan
def test_PML_003_24():
	hold(driver)
	Log.info('Menekan Button nsubmit data pemeliharan')
	driver.find_element(By.ID, 'submitButton').click()

#####################################################################################################################
#####################################################################################################################

@mark.fixture_pemeliharaan
def test_Edit_Pemeliharaan():
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
	hold(driver)
	Log.info('Pengecekan data yang telah di filter')
	driver.find_element(By.ID, 'filterColumn').click()
	time.sleep(1)
	driver.find_element(By.ID, 'tglPemeliharaan').click()
	tgl = driver.find_element(By.ID, 'filterTanggal')
	tgl.send_keys(tglPemeliharaan)
	driver.find_element(By.ID, 'searchButton').click()

updt = wb['Pemeliharan']
k = 3

tglPemelih		= updt['A'+str(k)].value #Tanggal Pemeliharaan
jnspemelih		= updt['B'+str(k)].value #Jenis Pemeliharaan
KgiPemelih		= updt['C'+str(k)].value #Kegiatan Pemeliharaan
Ktrangan		= updt['D'+str(k)].value #Keterangan

ketpelak	 = updt['E'+str(k)].value #Ketua Pelaksana
ptgsinte	 = updt['F'+str(k)].value #Petugas Pemeliharaan (Internal)
ptgsexte	 = updt['G'+str(k)].value #Petugas Pemeliharaan (Eksternal)

#tab Detail Pemeliharan
jumlhdet	= updt['H'+str(k)].value #jumlah
namabar		= updt['I'+str(k)].value #Nama Barang
kndb		= updt['J'+str(k)].value #Kondisi Barang
subkon		= updt['K'+str(k)].value #Sub Kondisi Barang
jmlhb		= updt['L'+str(k)].value #Jumlah Baik
jmlhR		= updt['M'+str(k)].value #Jumlah Rusak Parah
jmlhRr		= updt['N'+str(k)].value #Jumlah Rusak Ringan
ketdet		= updt['O'+str(k)].value #Keterangan

#tab identitas
jmlhba		= updt['P'+str(k)].value #jumlah
namaba		= updt['Q'+str(k)].value #Nama Bahan
jmlhpa		= updt['R'+str(k)].value #Jumlah Pakai
sat			= updt['S'+str(k)].value #Satuan
satl		= updt['T'+str(k)].value #Satuan Lain
ketba		= updt['U'+str(k)].value #Keterangan

@mark.fixture_pemeliharaan
def test_PLM_004_0():
	Log.info('menekan tombol Ubah')
	hold(driver)
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
	driver.find_element(By.CSS_SELECTOR, "#update-0").click()
	Log.info('Mengubah Pemeliharaan')

@mark.fixture_pemeliharaan
def test_PML_004_1():
	WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.XPATH, pathData['Rupelemen']['loading']['loadhalaman'])))
	hold(driver)
	tglpem = driver.find_element(By.ID, 'tglPemeliharaan')
	tglpem.send_keys(tglPemelih)
	tglpem.send_keys(Keys.ENTER)
@mark.fixture_pemeliharaan
def test_PML_004_2():
	driver.find_element(By.ID, 'inputJenisPemeliharaan').click()
	WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.ID , 'JPB1')))
	if jnspemelih =='Pemeliharaan Basan dan Baran Umum':
		driver.find_element(By.ID, 'JPB1').click()
	elif jnspemelih == 'Pemeliharaan Basan dan Baran Khusus':
		driver.find_element(By.ID, 'JPB2').click()
@mark.fixture_pemeliharaan
def test_PML_004_3():
	driver.find_element(By.ID, 'inputKegiatanPemeliharaan').click()
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'KPB1')))	
	if KgiPemelih == 'Pemeliharaan Berkala (Preventive Maintenance)':
		driver.find_element(By.ID, 'KPB1').click()
	elif KgiPemelih == 'Pemeliharaan Darurat (Emergency)':
		driver.find_element(By.ID, 'KPB2').click()
@mark.fixture_pemeliharaan
def test_PML_004_4():
	ngan = driver.find_element(By.ID, 'keterangan')
	ngan.clear()
	gan.send_keys(Ktrangan)#Keterangan kegiatan

@mark.fixture_pemeliharaan
def test_PML_004_5():
	pilketu = driver.find_element(By.ID, 'cariKetua')
	pilketu.click()
	pilketu.send_keys(ketpelak) #Ketua Pelaksana
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'cariKetua0')))
	driver.find_element(By.ID, 'cariKetua0').click()
@mark.fixture_pemeliharaan
def test_PML_004_6():
	pitern = driver.find_element(By.ID, 'cariPetugasInternal')
	pitern.click()
	pitern.send_keys(ptgsinte) #Petugas Pemeliharaan (Internal)
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'cariPetugasInternal0')))
	driver.find_element(By.ID, 'cariPetugasInternal0').click()
@mark.fixture_pemeliharaan
def test_PML_004_7():
	pgexer = driver.find_element(By.ID, 'cariPetugasEksternal')
	pgexer.click()
	pgexer.send_keys(ptgsexte) #Petugas Pemeliharaan (Eksternal)
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'cariPetugasEksternal0')))
	driver.find_element(By.ID, 'cariPetugasEksternal0').click()
#
#test_PML_004_8 #jumlah Detail pemeliharaan
#
#
#
#
#
#
@mark.fixture_pemeliharaan
def test_PML_004_9():
	nabran = driver.find_element(By.ID, 'namaBarang0')
	nabran.click()
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'nama_barang-0-0')))
	nabran.send_keys(namabar)
	nabran.send_keys(Keys.DOWN)
	nabran.send_keys(Keys.ENTER)
@mark.fixture_pemeliharaan
def test_PML_004_10():
	kobar = driver.find_element(By.ID, 'KondisiBarang0')
	kobar.click()
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'kondisi_barang-0-0')))
	kobar.send_keys(kndb)
	kobar.send_keys(Keys.DOWN)
	kobar.send_keys(Keys.ENTER)
@mark.fixture_pemeliharaan
def test_PML_004_11():
	Log.info('Jika Kondisi barang =Rusak maka akan mengisi Subkondisi Barang')
	if kndb == 'Rusak':
		subkobar = driver.find_element(By.ID, 'subKondisiBarang0').click()
		WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'sub_kondisi_barang-0-0')))
		Subkobar.send_keys(subkon)
		Subkobar.send_keys(Keys.DOWN)
		Subkobar.send_keys(Keys.ENTER)
	elif kndb == 'Baik':
		pass
@mark.fixture_pemeliharaan
def test_PML_004_12():
	driver.find_element(By.ID,'jumlahBaik0').send_keys(jmlhb)
@mark.fixture_pemeliharaan
def test_PML_004_13():
	driver.find_element(By.ID,'jumlahRusakParah0').send_keys(jmlhR)
@mark.fixture_pemeliharaan
def test_PML_004_14():
	driver.find_element(By.ID,'jumlahRusakRingan0').send_keys(jmlhRr)
@mark.fixture_pemeliharaan
def test_PML_004_15():
	driver.find_element(By.ID,'keteranganBarang0').send_keys(ketdet)

@mark.fixture_pemeliharaan
def test_PML_004_16():
	driver.find_element(By.ID,'tab-bahan_pemeliharaan').click()

#
#test_PML_004_17 #jumlah Detail pemeliharaan
#
#
#
#
#
#
@mark.fixture_pemeliharaan
def test_PML_004_18():
	driver.find_element(By.ID,'tab-bahan_pemeliharaan').click()

@mark.fixture_pemeliharaan
def test_PML_004_19():
	nang = driver.find_element(By.ID, 'namaBahan0')
	nang.clear()
	nang.send_keys(namaba)
@mark.fixture_pemeliharaan
def test_PML_004_20():
	jkai = driver.find_element(By.ID, 'jmlPakai0')
	jkai.clear()
	jkai.send_keys(jmlhpa)
@mark.fixture_pemeliharaan
def test_PML_004_21():
	stan = driver.find_element(By.ID, 'satuanBarang0')
	stan.click()
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'satuan-0-0')))
	stan.send_keys(sat)
	stan.send_keys(Keys.DOWN)
	stan.send_keys(Keys.ENTER)
@mark.fixture_pemeliharaan
def test_PML_004_22():
	driver.find_element(By.ID, 'satuanLain0').clear()
	driver.find_element(By.ID, 'satuanLain0').send_keys(satl)
@mark.fixture_pemeliharaan
def test_PML_004_23():
	driver.find_element(By.ID, 'keteranganBahan0').send_keys(ketba)

@mark.fixture_pemeliharaan
def test_PML_004_24():
	hold(driver)
	Log.info('Menekan Button nsubmit data pemeliharan') # ubah pemelliharaan
	driver.find_element(By.ID, 'submitButton').click()
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'searchButton')))

@mark.fixture_pemeliharaan
def test_PML_005():
	test_Edit_Pemeliharaan()
	driver.find_element(By.ID, 'detail-0').click()
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH , pathData['Rupelemen']['listbarang']['loaddetail'])))
	hold(driver)
	driver.find_element(By.ID,'tab-bahan_pemeliharaan').click()
	hold(driver)
	driver.find_element(By.ID,'backButton').click()

@mark.fixture_pemeliharaan
def test_PML_006():
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
	hold(driver)
	Log.info('Menampilkan dropdown jumlah data yang dipilih oleh pengguna dan ditampilkan pada main grid')
	driver.find_element(By.XPATH, pathData['Rupelemen']['indexpenempatan']['pilihhalmn']).click()
@mark.fixture_pemeliharaan
def test_PML_007():
	hold(driver)
	Log.info('Menampilkan jumlah data yang sesuai dengan total halaman yang dipilih')
	driver.find_element(By.XPATH, '//div[7]/div/div/div[1]/ul/li[1]').click()
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
@mark.fixture_pemeliharaan
def test_PML_008():
	hold(driver)
	navhal = driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke'])
	navhal.clear()
	navhal.send_keys('9')
	navhal.send_keys(Keys.ENTER)
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
@mark.fixture_pemeliharaan
def test_PML_009():
	test_PML_002()
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'searchButton')))
	hold(driver)
	driver.find_element(By.ID,'cetakKartu0').click()
@mark.fixture_pemeliharaan
def test_PML_010():
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'cetakKartu0')))
	hold(driver)
	driver.find_element(By.ID,'cetakBuku').click()
	Log.info('Mencetak buku dengan menekan Button Cetak Buku')
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'cetakBuku')))
@mark.fixture_pemeliharaan
def test_PML_011():
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID , 'cetakBuku')))
	hold(driver)
	Log.info('Mencetak data pemeliharaan (sesuai dengan jumlah halaman) dengan menekan Button Export PDF')
	driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportPDF']).click()
	# driver.find_element(By.ID, 'wholeButton').click()
	time.sleep(1)
	driver.find_element(By.ID, 'thisButton').click()
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_pemeliharaan
def test_PML_012():
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportPDF'])))
	hold(driver)
	Log.info('Mencetak data pemeliharaan (sesuai dengan jumlah halaman) dengan menekan Button Export Excel')
	driver.find_element(By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportexcel']).click()
	# driver.find_element(By.ID, 'wholeButton').click()
	time.sleep(1)
	driver.find_element(By.ID, 'thisButton').click()
	attach(data=driver.get_screenshot_as_png())
@mark.fixture_pemeliharaan
def test_PML_013():
	WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportexcel'])))
	hold(driver)
	Log.info('Mencetak data pemeliharaan(sesuai dengan jumlah halaman) yang terhubung langsung dengan perangkat tambahan (printer)')
	time.sleep(1)
	driver.find_element(By.ID, 'thisButton').click()
	WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.XPATH, pathData['Rupelemen']['idxpenerimaan']['exportexcel'])))
	attach(data=driver.get_screenshot_as_png())