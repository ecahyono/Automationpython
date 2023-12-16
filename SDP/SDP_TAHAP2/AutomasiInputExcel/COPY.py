from turtle import rt
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import os, sys
from os import environ, path
import pyautogui
from pytest import mark
import pytest
import time
import platform
from pathlib import Path
import logging
from faker import Faker
from datetime import datetime
import openpyxl
from faker.providers import date_time
from datetime import datetime, timedelta
import random


fake = Faker('id_ID')
from dotenv import load_dotenv
load_dotenv()

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR")) 
elif platform.system() == 'Windows':
	sys.path.append(environ.get("WINPARENTDIR"))
	

from Settings.setup import initDriver, loadDataPath, hold
from Settings.login import *
from Settings.Page.accessmenu import *
from Settings.setupPembinaan import *

@mark.webtest
# init driver by os
def test_setup():
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
@mark.webtest
def test_loggin():
	# login(driver)
	sorong(driver)

@mark.webtest
def test_aksesmenu():
	driver.implicitly_wait(60)
	Registrasi_identitas(driver)

@mark.webtest
def test_eksekusi():
	# wb = load_workbook(environ.get("REGEXCEL"))
	# sheetrange = wb['Identitas']
	# i = 2
	while True:
		#deklarasi per colom pada sheet
		#------------------------------------------------------
		#Tab Biodata-------------------------------------------
		#------------------------------------------------------
		Residivis			   					= "Tidak"
		# Rke					 			= sheetrange['B'+str(i)].value
		Nama_Lengkap							= fake.first_name() + " " + fake.last_name()
	
		Kewarganegaraan							= "WNI"
		nik					 					= fake.msisdn()+"5"f"{1:09}"
		Tempat_Asal			 					= "Bandung"
		Tempat_lahir							= "Bandung"
		tanggal_hari_ini 						= datetime.now()
		tahun_awal 								= tanggal_hari_ini.year - 23
		tahun_akhir 							= tanggal_hari_ini.year - 22
		tanggal_lahir_acak 						= fake.date_of_birth(tzinfo=None, minimum_age=23, maximum_age=50)
		Tanggal_lahir		   					= tanggal_lahir_acak.strftime('%d/%m/%Y')
		Jenis_kelamin		   					= fake.random_element(elements=('Laki-laki','Perempuan'))
		Negara				  					= "Indonesia"
		Agama				   					= fake.random_element(elements=('Budha','Hindu','Islam','Katholik','Kong hu chu','Protestan'))
		Agama_lain			  					= "Agnostik"
		
		Status_perkawinan	  					= "Belum Kawin"
		Provinsi								= "Jawa Barat"
		Kota									= "Sumedang"
		Alamat_rumah							= fake.address()
		
	
		Jenis_Pekerjaan		 					= "Karyawan Swasta"
	
		Bekerjadi			   					= "Torche"
		
		Tingkat_penghasilan	 					= "Tidak Ada"
		Tingkat_pendidikan	  					= random.choice(["idJenisPendidikan-0","idJenisPendidikan-1","idJenisPendidikan-2","idJenisPendidikan-3","idJenisPendidikan-4"])
		Keahlian1			   					= "Tidak Memiliki Keahlian"
		
		Keahlian2			   					= "Tidak Memiliki Keahlian"
		
		Nama_ayah			   					= fake.first_name() + " "+fake.last_name()

		Nama_ibu								= fake.first_name() + " " +fake.last_name()
	
		#--------------------------------------------------------
		#Tab Data Fisik------------------------------------------
		# -------------------------------------------------------
		Tinggi_badan							= "170"
		Berat_badan				 				= "70"
		Bentuk_rambut		   					= fake.random_element(elements=('Lurus','Ikal','Keriting','Tipis','Tebal'))
		Warna_rambut							= fake.random_element(elements=('Coklat','Pirang','Hitam'))
		Bentuk_bibir							= fake.random_element(elements=('Tebal','Tipis','Sumbing','Normal'))
		Berkacamata			 					= fake.random_element(elements=('Ya','Tidak'))
		Bentuk_mata			 					= fake.random_element(elements=('Normal','Sipit'))
		Warna_mata			  					= fake.random_element(elements=('Hitam','Coklat tua','Biru','Coklat Muda'))
		Hidung				  					= fake.random_element(elements=('Mancung','Pesek','Biasa'))
		Raut_muka			   					= fake.random_element(elements=('Bulat','Lonjong','Oval'))
		Telinga				 					= fake.random_element(elements=('Lebar','Kecil','Caplang'))
		Mulut				   					= fake.random_element(elements=('Normal','Cacat'))
		Lengan				  					= fake.random_element(elements=('Panjang','Pendek'))
		Tangan				  					= fake.random_element(elements=('Normal','Cacat'))
		Kaki									= fake.random_element(elements=('Normal','Cacat'))
		Warna_kulit			 					= fake.random_element(elements=('Hitam','Kuning','Putih','Sawo Matang'))
		# Cacat_tubuh			 		= sheetrange['BX'+str(i)].value
	
		WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'createButton')))
		driver.find_element(By.ID, 'createButton').click()								 
		try:
			WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.ID, 'btn_residivis')))
			#======================================================================
			driver.find_element(By.ID, 'tab-1').click()
			#========================Input Tab Biodata ============================
			driver.find_element(By.ID, 'btn_residivis').click()
			WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.ID, 'residivisOption-0')))
			if Residivis == 'Tidak':
				driver.find_element(By.ID, 'residivisOption-0').click()
			elif Residivis == 'Ya':
				driver.find_element(By.ID, 'residivisOption-1').click()
				resike = driver.find_element(By.XPATH, '//*[@id="btn_residivis_counter"]/div/input')
				resike.clear()
				resike.send_keys("Rke")
				
			#--------------------------------------------------------------									  
			driver.find_element(By.ID, 'btn_nama_lengkap').send_keys(Nama_Lengkap)
			#----------------------------------------------------------------
			# driver.find_element(By.ID, 'btn_nama_alias1').send_keys(Nama_Alias1)
			# # --------------------------------------------------------------
			# driver.find_element(By.ID, 'btn_nama_alias2').send_keys(Nama_Alias2)
			# # --------------------------------------------------------------
			# driver.find_element(By.ID, 'btn_nama_alias3').send_keys(Nama_Alias3)
			# # --------------------------------------------------------------
			# driver.find_element(By.ID, 'btn_nama_kecil1').send_keys(Nama_Kecil1)
			# # ---------------------------------------------------------------
			# driver.find_element(By.ID, 'btn_nama_kecil2').send_keys(Nama_Kecil2)
			# # ----------------------------------------------------------------
			# driver.find_element(By.ID, 'btn_nama_kecil3').send_keys(Nama_Kecil3)
			# --------------------------------------------------------------
			# if chcktab1 == 'tidak' :
			# 	driver.find_element(By.ID, 'btn_is_wbp_beresiko_tinggi').click()
			# elif chcktab1 == 'ya' :
			# 	print ('wbp_beresiko_tinggi Masih default')
			# if chcktab2 == 'tidak' :
			# 	driver.find_element(By.ID, 'btn_is_pengaruh_terhadap_masyarakat').click()
			# elif chcktab2 == 'ya' :
			# 	print ('pengaruh_terhadap_masyarakat Masih default')
			# --------------------------------------------------------------
			driver.find_element(By.ID, 'btn_id_jenis_warganegara').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisWarganegara-0')))
			if Kewarganegaraan == 'WNI':
				driver.find_element(By.ID, 'jenisWarganegara-1').click()
			elif Kewarganegaraan == 'WNA':
				driver.find_element(By.ID, 'jenisWarganegara-0').click()
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'btn_nik').send_keys(nik) 
			#-------------------------------------------------------------- 
			if Kewarganegaraan == 'WNI':
				driver.find_element(By.ID, 'btn_id_tempat_asal').click()   
				WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'tempatAsal-0')))
				driver.find_element(By.ID, 'btn_id_tempat_asal').send_keys(Tempat_Asal)								
				driver.find_element(By.ID, 'btn_id_tempat_asal').send_keys(Keys.DOWN)								
				driver.find_element(By.ID, 'btn_id_tempat_asal').send_keys(Keys.ENTER)
			elif Kewarganegaraan == 'WNA':   
				driver.find_element(By.ID, 'btn_id_tempat_asal_lain').send_keys(Tempat_Asal)
			# --------------------------------------------------------------
			if Kewarganegaraan == 'WNI':
				driver.find_element(By.ID, 'btn_id_tempat_lahir').click()		  
				WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'tempatLahir-0')))  
				driver.find_element(By.ID, 'btn_id_tempat_lahir').send_keys(Tempat_lahir)		  
				driver.find_element(By.ID, 'btn_id_tempat_lahir').send_keys(Keys.DOWN)		
				driver.find_element(By.ID, 'btn_id_tempat_lahir').send_keys(Keys.ENTER)		  
			elif Kewarganegaraan == 'WNA':
				# driver.find_element(By.ID, '').click()		  
				driver.find_element(By.ID, 'btn_id_tempat_lahir_lain').send_keys(Tempat_lahir)
			#------untuk tanggal Data format exel di sesuaikan-----------------------------
			driver.find_element(By.XPATH, '//div[5]/div/div/div/div/div/input').send_keys(Tanggal_lahir)
			driver.find_element(By.XPATH, '//div[5]/div/div/div/div/div/input').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'btn_id_jenis_kelamin').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisKelamin-0'))) 
			if Jenis_kelamin == 'Laki-laki':
				driver.find_element(By.ID, 'jenisKelamin-0').click()
			elif Jenis_kelamin == 'Perempuan':
				driver.find_element(By.ID, 'jenisKelamin-1').click()
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'btn_id_negara_asing').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'negaraAsing-0'))) 
			driver.find_element(By.ID, 'btn_id_negara_asing').send_keys(Negara)
			driver.find_element(By.ID, 'btn_id_negara_asing').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'btn_id_negara_asing').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'btn_id_jenis_agama').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisAgama-0'))) 
			driver.find_element(By.ID, 'btn_id_jenis_agama').send_keys(Agama)
			driver.find_element(By.ID, 'btn_id_jenis_agama').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'btn_id_jenis_agama').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			# if Agama == 'Lain-lain':
			# 	driver.find_element(By.ID, 'btn_id_jenis_agama_lain').send_keys(Agama_lain)
			# else:
			# 	pass
			#--------------------------------------------------------------
			# driver.find_element(By.ID, 'btn_id_jenis_suku').click()
			# WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisSuhu-0'))) 
			# driver.find_element(By.ID, 'btn_id_jenis_suku').send_keys(suku) 
			# driver.find_element(By.ID, 'btn_id_jenis_suku').send_keys(Keys.DOWN) 
			# driver.find_element(By.ID, 'btn_id_jenis_suku').send_keys(Keys.ENTER) 
			#------------------------------------------------------------------------------
			driver.find_element(By.ID, 'btn_id_jenis_status_perkawinan').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'statusPerkawinan-0'))) 
			driver.find_element(By.ID, 'btn_id_jenis_status_perkawinan').send_keys(Status_perkawinan)
			driver.find_element(By.ID, 'btn_id_jenis_status_perkawinan').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'btn_id_jenis_status_perkawinan').send_keys(Keys.ENTER)
			#------------------------------------------------------------------------------
			if Kewarganegaraan == 'WNI':
				driver.find_element(By.ID, 'btn_id_propinsi').click()
				WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'provinsi-0'))) 
				driver.find_element(By.ID, 'btn_id_propinsi').send_keys(Provinsi)
				driver.find_element(By.ID, 'btn_id_propinsi').send_keys(Keys.DOWN)
				driver.find_element(By.ID, 'btn_id_propinsi').send_keys(Keys.ENTER)
			elif Kewarganegaraan == 'WNA':
				driver.find_element(By.ID, 'btn_id_propinsi_lain').send_keys(Provinsi)
			#------------------------------------------------------------------------------
			if Kewarganegaraan == 'WNI':
				driver.find_element(By.ID, 'btn_id_kota').click()
				WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'kota-0'))) 
				driver.find_element(By.ID, 'btn_id_kota').send_keys(Kota)
				driver.find_element(By.ID, 'btn_id_kota').send_keys(Keys.DOWN)
				driver.find_element(By.ID, 'btn_id_kota').send_keys(Keys.ENTER)
			elif Kewarganegaraan == 'WNA':
				driver.find_element(By.ID, 'btn_id_kota_lain').send_keys(Kota)
			#------------------------------------------------------------------------------	  
			driver.find_element(By.ID, 'btn_alamat').send_keys(Alamat_rumah)	   
			# # # ------------------------------------------------------------------------------
			# driver.find_element(By.ID, 'btn_telepon').send_keys(Telepon)
			# # #------------------------------------------------------------------------------
			# driver.find_element(By.ID, 'btn_kodepos').send_keys(Kode_pos)
			# # # ------------------------------------------------------------------------------
			# driver.find_element(By.ID, 'btn_alamat_alternatif').send_keys(Alamat_lain)
			# # ======================================================================
			driver.find_element(By.ID, 'tab-2').click()
			# ========================Input Tab Pekerjaan===========================
			driver.find_element(By.ID, 'id_jenis_pekerjaan').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'idJenisPekerjaan-0'))) 
			driver.find_element(By.ID, 'id_jenis_pekerjaan').send_keys(Jenis_Pekerjaan)
			driver.find_element(By.ID, 'id_jenis_pekerjaan').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'id_jenis_pekerjaan').send_keys(Keys.ENTER)
			# --------------------------------------------------------------
			# if Jenis_Pekerjaan == 'pegawai negeri sipil':
			# 	driver.find_element(By.ID, 'nama_instansi_pns').send_keys(namaipemerintah)
			# 	driver.find_element(By.ID, 'nip').send_keys(noindpegawai)		
			# elif Jenis_Pekerjaan == 'lain-lain':
			# 	driver.find_element(By.ID, 'id_jenis_pekerjaan_lain').send_keys(Jenis_Pekerjaan_Lain)
			# -----------------------------------------------------------
			driver.find_element(By.ID, 'alamat_pekerjaan').send_keys(Bekerjadi)
			#--------------------------------------------------------------
			# driver.find_element(By.ID, 'keterangan_pekerjaan').send_keys(Keterangan_pekerjaan)
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'id_tingkat_penghasilan').click()		
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'idTingkatPenghasilan-0'))) 
			driver.find_element(By.ID, 'id_tingkat_penghasilan').send_keys(Tingkat_penghasilan)
			driver.find_element(By.ID, 'id_tingkat_penghasilan').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'id_tingkat_penghasilan').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			# --------------------------------------------------------------
			driver.find_element(By.ID, 'id_jenis_keahlian_1').click()		
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'idjenisKeahlian-0'))) 
			driver.find_element(By.ID, 'id_jenis_keahlian_1').send_keys(Keahlian1)
			driver.find_element(By.ID, 'id_jenis_keahlian_1').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'id_jenis_keahlian_1').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'id_jenis_pendidikan').click()		
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'idJenisPendidikan-0'))) 
			driver.find_element(By.ID, Tingkat_pendidikan).click()
	
			# driver.find_element(By.ID, 'id_jenis_level_1').click()		
			# WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'idJenisLevel-0'))) 
			# if Level_keahlian1 == 'Ahli':
			# 	driver.find_element(By.ID, 'idJenisLevel-0').click()
			# elif Level_keahlian1 == 'Cukup Ahli':
			# 	driver.find_element(By.ID, 'idJenisLevel-1').click()
			# elif Level_keahlian1 == 'Kurang Ahli':
			# 	driver.find_element(By.ID, 'idJenisLevel-2').click()
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'id_jenis_keahlian_2').click()
			time.sleep(2) 
			driver.find_element(By.ID, 'id_jenis_keahlian_2').send_keys(Keahlian2)
			driver.find_element(By.ID, 'id_jenis_keahlian_2').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'id_jenis_keahlian_2').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			# driver.find_element(By.ID, 'id_jenis_level_2').click()
			# WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'idJenisLevel2-0'))) 
			# driver.find_element(By.ID, 'id_jenis_level_2').send_keys(Level_keahlian2)
			# driver.find_element(By.ID, 'id_jenis_level_2').send_keys(Keys.DOWN)
			# driver.find_element(By.ID, 'id_jenis_level_2').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			# if quran == 'ya' :
			# 	driver.find_element(By.XPATH, '//*[@id="is_baca_quran"]/span[1]/span').click()
			# 	print (quran)
			# elif quran == 'Tidak':
			# 	print ('tidak di check')
			# # # #----------------------------------------------------------------------
			# if latin == 'ya' :
			# 	driver.find_element(By.XPATH, '//*[@id="is_baca_latin"]').click()
			# 	print (latin)
			# elif latin == 'Tidak':
			# 	print ('tidak di check')
			# #----------------------------------------------------------------------
			# driver.find_element(By.ID, 'minat').send_keys(Minat)
			#======================================================================
			driver.find_element(By.ID, 'tab-3').click()
			#========================Input Tab Keluarga============================ 
			#------------------------------------------------------------------------------
			driver.find_element(By.ID, 'nm_ayah').send_keys(Nama_ayah)
			#------------------------------------------------------------------------------
			# driver.find_element(By.ID, 'tmp_tgl_ayah').send_keys(Alamat_ayah)
			#------------------------------------------------------------------------------
			driver.find_element(By.ID, 'nm_ibu').send_keys(Nama_ibu)
			#------------------------------------------------------------------------------	  
			# driver.find_element(By.ID, 'tmp_tgl_ibu').send_keys(Alamat_ibu)
			#------------------------------------------------------------------------------
			# driver.find_element(By.XPATH, '//*[@id="anakke"]/div/input').click()
			# pyautogui.hotkey('backspace')		
			# driver.find_element(By.XPATH, '//*[@id="anakke"]/div/input').send_keys(Anak_ke)
			# pyautogui.press('enter')
			# driver.find_element(By.XPATH, '//*[@id="jml_saudara"]/div/input').click()
			# pyautogui.hotkey('backspace')		
			# driver.find_element(By.XPATH, '//*[@id="jml_saudara"]/div/input').send_keys(Dari)
			# pyautogui.press('enter')
			# if Dari == 2:	
			# 	driver.find_element(By.ID, 'nm_saudara_1').send_keys(Nama_saudara1)
			# elif Dari == 3:	
			# 	driver.find_element(By.ID, 'nm_saudara_1').send_keys(Nama_saudara1)
			# 	driver.find_element(By.ID, 'nm_saudara_2').send_keys(Nama_saudara2)
			# elif Dari == 4:   
			# 	driver.find_element(By.ID, 'nm_saudara_1').send_keys(Nama_saudara1)	
			# 	driver.find_element(By.ID, 'nm_saudara_2').send_keys(Nama_saudara2) 
			# 	driver.find_element(By.ID, 'nm_saudara_3').send_keys(Nama_saudara3)
			# elif Dari == 5:   
			# 	driver.find_element(By.ID, 'nm_saudara_1').send_keys(Nama_saudara1) 
			# 	driver.find_element(By.ID, 'nm_saudara_2').send_keys(Nama_saudara2)
			# 	driver.find_element(By.ID, 'nm_saudara_3').send_keys(Nama_saudara3)
			# 	driver.find_element(By.ID, 'nm_saudara_4').send_keys(Nama_saudara4)
			# elif Dari == 1 :
			# 	print ('anak satu satunya')
			# if Status_perkawinan == 'Belum Kawin':
			# 	print('default')
			# elif Status_perkawinan == 'Duda':
			# 	driver.find_element(By.ID, 'jml_istri_suami').click()
			# 	pyautogui.hotkey('backspace')
			# 	driver.find_element(By.XPATH, '//*[@id="jml_istri_suami"]/div/input' ).send_keys(jml_istrsuam) 
			# 	pyautogui.press('enter')
			# 	driver.find_element(By.ID, 'nm_istri_suami_1').send_keys(Nm_istrsuam)
			# 	driver.find_element(By.ID, 'tmp_tgl_istri_suami').send_keys(alm_istrsuam)
			# 	driver.find_element(By.XPATH, '//*[@id="jml_anak"]/div/input').click()
			# 	pyautogui.hotkey('backspace')
			# 	jumlah = driver.find_element(By.XPATH, '//*[@id="jml_anak"]/div/input' ).send_keys(jumlah_anak) 
			# 	pyautogui.press('enter')
			# 	if jumlah_anak == 1:   
			# 		driver.find_element(By.ID, 'nm_anak_1').send_keys(Nama_anak1)
			# 	elif jumlah_anak == 2:	
			# 		driver.find_element(By.ID, 'nm_anak_1').send_keys(Nama_anak1)	 
			# 		driver.find_element(By.ID, 'nm_anak_2').send_keys(Nama_anak2)
			# 	elif jumlah_anak == 3:	
			# 		driver.find_element(By.ID, 'nm_anak_1').send_keys(Nama_anak1)	
			# 		driver.find_element(By.ID, 'nm_anak_2').send_keys(Nama_anak2)  
			# 		driver.find_element(By.ID, 'nm_anak_3').send_keys(Nama_anak3)
			# 	elif  jumlah_anak == 0: 
			# 		print('masa ga punya anak')
			# 	#--------------------------------------------------------------
			# 	# driver.find_element(By.XPATH, '//*[@id="telephone_keluarga"]').send_keys(Telepon_keluarga)
			# elif Status_perkawinan == 'Janda':
			# 	driver.find_element(By.ID, 'jml_istri_suami').click()
			# 	pyautogui.hotkey('backspace')
			# 	driver.find_element(By.XPATH, '//*[@id="jml_istri_suami"]/div/input' ).send_keys(jml_istrsuam) 
			# 	pyautogui.press('enter')
			# 	driver.find_element(By.ID, 'nm_istri_suami_1').send_keys(Nm_istrsuam)
			# 	driver.find_element(By.ID, 'tmp_tgl_istri_suami').send_keys(alm_istrsuam)
			# 	driver.find_element(By.XPATH, '//*[@id="jml_anak"]/div/input').click()
			# 	pyautogui.hotkey('backspace')
			# 	jumlah = driver.find_element(By.XPATH, '//*[@id="jml_anak"]/div/input' ).send_keys(jumlah_anak) 
			# 	pyautogui.press('enter')
			# 	if jumlah_anak == 1:
			# 		driver.find_element(By.ID, 'nm_anak_1').send_keys(Nama_anak1)
			# 	elif jumlah_anak == 2:
			# 		driver.find_element(By.ID, 'nm_anak_1').send_keys(Nama_anak1)		
			# 		driver.find_element(By.ID, 'nm_anak_2').send_keys(Nama_anak2)
			# 	elif jumlah_anak == 3:
			# 		driver.find_element(By.ID, 'nm_anak_1').send_keys(Nama_anak1)		
			# 		driver.find_element(By.ID, 'nm_anak_2').send_keys(Nama_anak2)
			# 		driver.find_element(By.ID, 'nm_anak_3').send_keys(Nama_anak3)
			# 	elif  jumlah_anak == 0: 
			# 		print('masa ga punya anak')
			# 	#--------------------------------------------------------------
			# 	# driver.find_element(By.XPATH, '//*[@id="telephone_keluarga"]').send_keys(Telepon_keluarga)
			# elif Status_perkawinan == 'Kawin':
			# 	driver.find_element(By.ID, 'jml_istri_suami').click()
			# 	pyautogui.hotkey('backspace')
			# 	driver.find_element(By.XPATH, '//*[@id="jml_istri_suami"]/div/input' ).send_keys(jml_istrsuam) 
			# 	pyautogui.press('enter')
			# 	driver.find_element(By.ID, 'nm_istri_suami_1').send_keys(Nm_istrsuam)
			# 	driver.find_element(By.ID, 'tmp_tgl_istri_suami').send_keys(alm_istrsuam)
			# 	driver.find_element(By.XPATH, '//*[@id="jml_anak"]/div/input').click()
			# 	pyautogui.hotkey('backspace')
			# 	jumlah = driver.find_element(By.XPATH, '//*[@id="jml_anak"]/div/input' ).send_keys(jumlah_anak) 
			# 	pyautogui.press('enter')
			# 	if jumlah_anak == 1:
			# 		driver.find_element(By.ID, 'nm_anak_1').send_keys(Nama_anak1)
			# 	elif jumlah_anak == 2:
			# 		driver.find_element(By.ID, 'nm_anak_1').send_keys(Nama_anak1)		
			# 		driver.find_element(By.ID, 'nm_anak_2').send_keys(Nama_anak2)
			# 	elif jumlah_anak == 3:
			# 		driver.find_element(By.ID, 'nm_anak_1').send_keys(Nama_anak1)		
			# 		driver.find_element(By.ID, 'nm_anak_2').send_keys(Nama_anak2)
			# 		driver.find_element(By.ID, 'nm_anak_3').send_keys(Nama_anak3)
			# 	elif  jumlah_anak == 0: 
			# 		print('masa ga punya anak')
				#--------------------------------------------------------------
				# driver.find_element(By.XPATH, '//*[@id="telephone_keluarga"]').send_keys(Telepon_keluarga)
				#======================================================================
			driver.find_element(By.ID, 'tab-4').click()
			#========================Input Tab Data Fisik========================== 
			driver.find_element(By.XPATH, '//*[@id="tinggi"]/div/input').click()
			pyautogui.hotkey('backspace')
			driver.find_element(By.XPATH, '//*[@id="tinggi"]/div/input' ).send_keys(Tinggi_badan) 
			#--------------------------------------------------------------
			driver.find_element(By.XPATH, '//*[@id="berat"]/div/input').click()
			pyautogui.hotkey('backspace')
			driver.find_element(By.XPATH, '//*[@id="berat"]/div/input').send_keys(Berat_badan)
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'id_bentukrambut').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'bentukRambut-0'))) 
			driver.find_element(By.ID, 'id_bentukrambut').send_keys(Bentuk_rambut)
			driver.find_element(By.ID, 'id_bentukrambut').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'id_bentukrambut').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'id_jenis_rambut').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisRambut-0'))) 
			driver.find_element(By.ID, 'id_jenis_rambut').send_keys(Warna_rambut)
			driver.find_element(By.ID, 'id_jenis_rambut').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'id_jenis_rambut').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'id_bentukbibir').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'bentukBibir-0'))) 
			driver.find_element(By.ID, 'id_bentukbibir').send_keys(Bentuk_bibir)
			driver.find_element(By.ID, 'id_bentukbibir').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'id_bentukbibir').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'id_kacamata').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'kacamata-0'))) 
			driver.find_element(By.ID, 'id_kacamata').send_keys(Berkacamata)
			driver.find_element(By.ID, 'id_kacamata').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'id_kacamata').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'id_bentuk_mata').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'bentukMata-0'))) 
			driver.find_element(By.ID, 'id_bentuk_mata').send_keys(Bentuk_mata)
			driver.find_element(By.ID, 'id_bentuk_mata').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'id_bentuk_mata').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'id_warna_mata').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'warnaMata-0'))) 
			driver.find_element(By.ID, 'id_warna_mata').send_keys(Warna_mata)
			driver.find_element(By.ID, 'id_warna_mata').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'id_warna_mata').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'id_jenis_hidung').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisHidung-0'))) 
			driver.find_element(By.ID, 'id_jenis_hidung').send_keys(Hidung)
			driver.find_element(By.ID, 'id_jenis_hidung').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'id_jenis_hidung').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'id_jenis_muka').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisMuka-0'))) 
			driver.find_element(By.ID, 'id_jenis_muka').send_keys(Raut_muka)
			driver.find_element(By.ID, 'id_jenis_muka').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'id_jenis_muka').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'id_telinga').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'telinga-0'))) 
			driver.find_element(By.ID, 'id_telinga').send_keys(Telinga)
			driver.find_element(By.ID, 'id_telinga').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'id_telinga').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'id_jenis_mulut').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisMulut-0'))) 
			driver.find_element(By.ID, 'id_jenis_mulut').send_keys(Mulut)
			driver.find_element(By.ID, 'id_jenis_mulut').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'id_jenis_mulut').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'id_lengan').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'lengan-0'))) 
			driver.find_element(By.ID, 'id_lengan').send_keys(Lengan)
			driver.find_element(By.ID, 'id_lengan').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'id_lengan').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'id_jenis_tangan').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisTangan-0'))) 
			driver.find_element(By.ID, 'id_jenis_tangan').send_keys(Tangan)
			driver.find_element(By.ID, 'id_jenis_tangan').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'id_jenis_tangan').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'id_jenis_kaki').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisKaki-0'))) 
			driver.find_element(By.ID, 'id_jenis_kaki').send_keys(Kaki)
			driver.find_element(By.ID, 'id_jenis_kaki').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'id_jenis_kaki').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			driver.find_element(By.ID, 'id_warnakulit').click()
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'warnaKulit-0'))) 
			driver.find_element(By.ID, 'id_warnakulit').send_keys(Warna_kulit)
			driver.find_element(By.ID, 'id_warnakulit').send_keys(Keys.DOWN)
			driver.find_element(By.ID, 'id_warnakulit').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			# driver.find_element(By.ID, 'cacat').send_keys(Cacat_tubuh)
			# #--------------------------------------------------------------
			# time.sleep(4)
			# driver.find_element(By.XPATH, '//*[@id="upload_foto_ciri_1"]').click()
			# time.sleep(4)
			# pyautogui.write(r'C:\Users\user\Documents\TRCH\Automationpython\assets\Filefoto\Gambar.jpg')
			# pyautogui.press('enter')
			# time.sleep(4)
			# driver.find_element(By.XPATH, '//*[@id="upload_foto_ciri_2"]').click()
			# time.sleep(4)
			# pyautogui.write(r'C:\Users\user\Documents\TRCH\Automationpython\assets\Filefoto\Gambar.jpg')
			# pyautogui.press('enter')
			# time.sleep(4)
			# driver.find_element(By.XPATH, '//*[@id="upload_foto_ciri_3"]').click()
			# time.sleep(4)
			# pyautogui.write(r'C:\Users\user\Documents\TRCH\Automationpython\assets\Filefoto\Gambar.jpg')
			# pyautogui.press('enter')
			# time.sleep(4)
			# #--------------------------------------------------------------
			# driver.find_element(By.ID, 'ciri').send_keys(Catatancirikhusus1)  
			# # #--------------------------------------------------------------
			# driver.find_element(By.ID, 'ciri2').send_keys(Catatancirikhusus2) 
			# # #--------------------------------------------------------------
			# driver.find_element(By.ID, 'ciri3').send_keys(Catatancirikhusus3)
			# # ======================================================================
			# driver.find_element(By.ID, 'tab-5').click()
			# # # ========================Input Tab Sidik Jari==========================
			# # #--------------------------------------------------------------
			# driver.find_element(By.ID, 'no_paspor').send_keys(Nopaspor)
			# # #--------------------------------------------------------------
			# driver.find_element(By.ID, 'rumus_daktil').send_keys(Rumus)
			# # #--------------------------------------------------------------
			# driver.find_element(By.ID, 'nomor_daktil').send_keys(Nopaspor)
			# # #--------------------------------------------------------------
			# driver.find_element(By.ID, 'pengambil_sj').send_keys(Pengambilansidikjari)
			# driver.find_element(By.ID, 'pengambil_sj').send_keys(Keys.ENTER)
			# #--------------------------------------------------------------
			# driver.find_element(By.XPATH, '//*[@id="pane-5"]/div/form/div/div[2]/div[2]/div/div/input').send_keys(Tanggalpengambilan)
			#======================================================================
			if platform.system() == 'Darwin':

				if Jenis_kelamin == "Laki-laki":
					driver.find_element(By.ID, 'tab-6').click()
					#========================Input Tab Foto========================== 
					# DEPAN
					driver.find_element(By.XPATH,   '//*[@id="pane-6"]/form/div/div[2]/div/div/div/div/div[1]/button').click()
					uploadGambarDepanL(driver)
					# KIRI
					driver.find_element(By.XPATH,   '//*[@id="pane-6"]/form/div/div[1]/div/div/div/div/div[1]/button').click()
					uploadGambarKiriL(driver)
					
					# KANAN
					driver.find_element(By.XPATH,   '//*[@id="pane-6"]/form/div/div[3]/div/div/div/div/div[1]/button').click()
					uploadGambarKananL(driver)
				elif Jenis_kelamin == "Perempuan":

					driver.find_element(By.ID, 'tab-6').click()
					#========================Input Tab Foto========================== 
					# KIRI
					driver.find_element(By.XPATH,   '//*[@id="pane-6"]/form/div/div[1]/div/div/div/div/div[1]/button').click()
					uploadGambarKiriP(driver)
					# DEPAN
					driver.find_element(By.XPATH,   '//*[@id="pane-6"]/form/div/div[2]/div/div/div/div/div[1]/button').click()
					uploadGambarDepanP(driver)
					# KANAN
					driver.find_element(By.XPATH,   '//*[@id="pane-6"]/form/div/div[3]/div/div/div/div/div[1]/button').click()
					uploadGambarKananP(driver)
					
			
			elif platform.system() == 'Windows':
			#======================================================================
				driver.find_element(By.ID, 'tab-6').click()
				#========================Input Tab Foto========================== 
				driver.find_element(By.XPATH,   '//*[@id="pane-6"]/form/div/div[1]/div/div/div/div/div[1]/button').click()
				time.sleep(3)
				pyautogui.write(environ.get(r'FOTBRG1'))
				pyautogui.press('enter')

				driver.find_element(By.XPATH,   '//*[@id="pane-6"]/form/div/div[2]/div/div/div/div/div[1]/button').click()
				time.sleep(3)
				pyautogui.write(environ.get(r'FOTBRG1'))
				pyautogui.press('enter')

				driver.find_element(By.XPATH,   '//*[@id="pane-6"]/form/div/div[3]/div/div/div/div/div[1]/button').click()
				time.sleep(3)
				pyautogui.write(environ.get(r'FOTBRG1'))
				pyautogui.press('enter')
			#======================================================================
			# driver.find_element(By.ID, 'tab-7').click()
			#========================Input Tab Identitas lama========================== 
			#Submit
			time.sleep(3)
			driver.find_element(By.ID, 'submitButton').click() 
			WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'createButton')))

		except TimeoutException:
				print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!LOADING TERLALU LAMA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
				pass
		# i = i + 1
	print ('Success Created')
