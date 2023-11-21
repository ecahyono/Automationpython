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
from Settings.Page.accessmenu import Registrasi_identitas
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
	manokwari(driver)

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
		Residivis			   				= "Tidak"
		Nama_Lengkap						= fake.first_name() + " " + fake.last_name()
		Kewarganegaraan						= "WNI"
		nik					 				= fake.msisdn()+"5"f"{1:09}"
		Tempat_Asal			 				= "Bandung"
		Tempat_lahir						= "Bandung"
		tanggal_hari_ini 					= datetime.now()
		tahun_awal 							= tanggal_hari_ini.year - 23
		tahun_akhir 						= tanggal_hari_ini.year - 22
		tanggal_lahir_acak 					= fake.date_of_birth(tzinfo=None, minimum_age=23, maximum_age=50)
		Tanggal_lahir		   				= tanggal_lahir_acak.strftime('%d/%m/%Y')
		Jenis_kelamin		   				= fake.random_element(elements=('Laki-laki','Perempuan'))
		Negara				  				= "Indonesia"
		Agama				   				= fake.random_element(elements=('Budha','Hindu','Islam','Katholik','Kong hu chu','Protestan'))
		Agama_lain			  				= "Agnostik"
		Status_perkawinan	  				= "Belum Kawin"
		Provinsi							= "Jawa Barat"
		Kota								= "Sumedang"
		Alamat_rumah						= fake.address()
		Jenis_Pekerjaan		 				= "Karyawan Swasta"
		Bekerjadi			   				= "Torche"
		Tingkat_penghasilan	 				= "Tidak Ada"
		Tingkat_pendidikan	  				= random.choice(["idJenisPendidikan-0","idJenisPendidikan-1","idJenisPendidikan-2","idJenisPendidikan-3","idJenisPendidikan-4"])
		Keahlian1			   				= "Tidak Memiliki Keahlian"
		Keahlian2			   				= "Tidak Memiliki Keahlian"
		Nama_ayah			   				= fake.first_name() + " "+fake.last_name()
		Nama_ibu							= fake.first_name() + " " +fake.last_name()
		Tinggi_badan						= "170"
		Berat_badan				 			= "70"
		Bentuk_rambut		   				= fake.random_element(elements=('Lurus','Ikal','Keriting','Tipis','Tebal'))
		Warna_rambut						= fake.random_element(elements=('Coklat','Pirang','Hitam'))
		Bentuk_bibir						= fake.random_element(elements=('Tebal','Tipis','Sumbing','Normal'))
		Berkacamata			 				= fake.random_element(elements=('Ya','Tidak'))
		Bentuk_mata			 				= fake.random_element(elements=('Normal','Sipit'))
		Warna_mata			  				= fake.random_element(elements=('Hitam','Coklat tua','Biru','Coklat Muda'))
		Hidung				  				= fake.random_element(elements=('Mancung','Pesek','Biasa'))
		Raut_muka			   				= fake.random_element(elements=('Bulat','Lonjong','Oval'))
		Telinga				 				= fake.random_element(elements=('Lebar','Kecil','Caplang'))
		Mulut				   				= fake.random_element(elements=('Normal','Cacat'))
		Lengan				  				= fake.random_element(elements=('Panjang','Pendek'))
		Tangan				  				= fake.random_element(elements=('Normal','Cacat'))
		Kaki								= fake.random_element(elements=('Normal','Cacat'))
		Warna_kulit			 				= fake.random_element(elements=('Hitam','Kuning','Putih','Sawo Matang'))
		
		wait=WebDriverWait 
		find=driver.find_element
		wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'createButton')))
		find(By.ID, 'createButton').click()								 
		try:
			wait(driver,90).until(EC.element_to_be_clickable((By.ID, 'btn_residivis')))
			#======================================================================
			find(By.ID, 'tab-1').click()
			#========================Input Tab Biodata ============================
			find(By.ID, 'btn_residivis').click()
			wait(driver,90).until(EC.element_to_be_clickable((By.ID, 'residivisOption-0')))
			if Residivis == 'Tidak':
				find(By.ID, 'residivisOption-0').click()
			elif Residivis == 'Ya':
				find(By.ID, 'residivisOption-1').click()
				resike = find(By.XPATH, '//*[@id="btn_residivis_counter"]/div/input')
				resike.clear()
				resike.send_keys("Rke")
				
			#--------------------------------------------------------------									  
			find(By.ID, 'btn_nama_lengkap').send_keys(Nama_Lengkap)
			
			# --------------------------------------------------------------
			find(By.ID, 'btn_id_jenis_warganegara').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisWarganegara-0')))
			if Kewarganegaraan == 'WNI':
				find(By.ID, 'jenisWarganegara-1').click()
			elif Kewarganegaraan == 'WNA':
				find(By.ID, 'jenisWarganegara-0').click()
			#--------------------------------------------------------------
			find(By.ID, 'btn_nik').send_keys(nik) 
			#-------------------------------------------------------------- 
			if Kewarganegaraan == 'WNI':
				find(By.ID, 'btn_id_tempat_asal').click()   
				wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'tempatAsal-0')))
				find(By.ID, 'btn_id_tempat_asal').send_keys(Tempat_Asal)								
				find(By.ID, 'btn_id_tempat_asal').send_keys(Keys.DOWN)								
				find(By.ID, 'btn_id_tempat_asal').send_keys(Keys.ENTER)
			elif Kewarganegaraan == 'WNA':   
				find(By.ID, 'btn_id_tempat_asal_lain').send_keys(Tempat_Asal)
			# --------------------------------------------------------------
			if Kewarganegaraan == 'WNI':
				find(By.ID, 'btn_id_tempat_lahir').click()		  
				wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'tempatLahir-0')))  
				find(By.ID, 'btn_id_tempat_lahir').send_keys(Tempat_lahir)		  
				find(By.ID, 'btn_id_tempat_lahir').send_keys(Keys.DOWN)		
				find(By.ID, 'btn_id_tempat_lahir').send_keys(Keys.ENTER)		  
			elif Kewarganegaraan == 'WNA':
				# find(By.ID, '').click()		  
				find(By.ID, 'btn_id_tempat_lahir_lain').send_keys(Tempat_lahir)
			#------untuk tanggal Data format exel di sesuaikan-----------------------------
			find(By.XPATH, '//div[5]/div/div/div/div/div/input').send_keys(Tanggal_lahir)
			find(By.XPATH, '//div[5]/div/div/div/div/div/input').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			find(By.ID, 'btn_id_jenis_kelamin').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisKelamin-0'))) 
			if Jenis_kelamin == 'Laki-laki':
				find(By.ID, 'jenisKelamin-0').click()
			elif Jenis_kelamin == 'Perempuan':
				find(By.ID, 'jenisKelamin-1').click()
			#--------------------------------------------------------------
			find(By.ID, 'btn_id_negara_asing').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'negaraAsing-0'))) 
			find(By.ID, 'btn_id_negara_asing').send_keys(Negara)
			find(By.ID, 'btn_id_negara_asing').send_keys(Keys.DOWN)
			find(By.ID, 'btn_id_negara_asing').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			find(By.ID, 'btn_id_jenis_agama').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisAgama-0'))) 
			find(By.ID, 'btn_id_jenis_agama').send_keys(Agama)
			find(By.ID, 'btn_id_jenis_agama').send_keys(Keys.DOWN)
			find(By.ID, 'btn_id_jenis_agama').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			# if Agama == 'Lain-lain':
			# 	find(By.ID, 'btn_id_jenis_agama_lain').send_keys(Agama_lain)
			# else:
			# 	pass
			#--------------------------------------------------------------
			# find(By.ID, 'btn_id_jenis_suku').click()
			# wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisSuhu-0'))) 
			# find(By.ID, 'btn_id_jenis_suku').send_keys(suku) 
			# find(By.ID, 'btn_id_jenis_suku').send_keys(Keys.DOWN) 
			# find(By.ID, 'btn_id_jenis_suku').send_keys(Keys.ENTER) 
			#------------------------------------------------------------------------------
			find(By.ID, 'btn_id_jenis_status_perkawinan').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'statusPerkawinan-0'))) 
			find(By.ID, 'btn_id_jenis_status_perkawinan').send_keys(Status_perkawinan)
			find(By.ID, 'btn_id_jenis_status_perkawinan').send_keys(Keys.DOWN)
			find(By.ID, 'btn_id_jenis_status_perkawinan').send_keys(Keys.ENTER)
			#------------------------------------------------------------------------------
			if Kewarganegaraan == 'WNI':
				find(By.ID, 'btn_id_propinsi').click()
				wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'provinsi-0'))) 
				find(By.ID, 'btn_id_propinsi').send_keys(Provinsi)
				find(By.ID, 'btn_id_propinsi').send_keys(Keys.DOWN)
				find(By.ID, 'btn_id_propinsi').send_keys(Keys.ENTER)
			elif Kewarganegaraan == 'WNA':
				find(By.ID, 'btn_id_propinsi_lain').send_keys(Provinsi)
			#------------------------------------------------------------------------------
			if Kewarganegaraan == 'WNI':
				find(By.ID, 'btn_id_kota').click()
				wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'kota-0'))) 
				find(By.ID, 'btn_id_kota').send_keys(Kota)
				find(By.ID, 'btn_id_kota').send_keys(Keys.DOWN)
				find(By.ID, 'btn_id_kota').send_keys(Keys.ENTER)
			elif Kewarganegaraan == 'WNA':
				find(By.ID, 'btn_id_kota_lain').send_keys(Kota)
			#------------------------------------------------------------------------------	  
			find(By.ID, 'btn_alamat').send_keys(Alamat_rumah)	   
			# # # ------------------------------------------------------------------------------
			# find(By.ID, 'btn_telepon').send_keys(Telepon)
			# # #------------------------------------------------------------------------------
			# find(By.ID, 'btn_kodepos').send_keys(Kode_pos)
			# # # ------------------------------------------------------------------------------
			# find(By.ID, 'btn_alamat_alternatif').send_keys(Alamat_lain)
			# # ======================================================================
			find(By.ID, 'tab-2').click()
			# ========================Input Tab Pekerjaan===========================
			find(By.ID, 'id_jenis_pekerjaan').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'idJenisPekerjaan-0'))) 
			find(By.ID, 'id_jenis_pekerjaan').send_keys(Jenis_Pekerjaan)
			find(By.ID, 'id_jenis_pekerjaan').send_keys(Keys.DOWN)
			find(By.ID, 'id_jenis_pekerjaan').send_keys(Keys.ENTER)
			# --------------------------------------------------------------
			# if Jenis_Pekerjaan == 'pegawai negeri sipil':
			# 	find(By.ID, 'nama_instansi_pns').send_keys(namaipemerintah)
			# 	find(By.ID, 'nip').send_keys(noindpegawai)		
			# elif Jenis_Pekerjaan == 'lain-lain':
			# 	find(By.ID, 'id_jenis_pekerjaan_lain').send_keys(Jenis_Pekerjaan_Lain)
			# -----------------------------------------------------------
			find(By.ID, 'alamat_pekerjaan').send_keys(Bekerjadi)
			#--------------------------------------------------------------
			# find(By.ID, 'keterangan_pekerjaan').send_keys(Keterangan_pekerjaan)
			#--------------------------------------------------------------
			find(By.ID, 'id_tingkat_penghasilan').click()		
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'idTingkatPenghasilan-0'))) 
			find(By.ID, 'id_tingkat_penghasilan').send_keys(Tingkat_penghasilan)
			find(By.ID, 'id_tingkat_penghasilan').send_keys(Keys.DOWN)
			find(By.ID, 'id_tingkat_penghasilan').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			# --------------------------------------------------------------
			find(By.ID, 'id_jenis_keahlian_1').click()		
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'idjenisKeahlian-0'))) 
			find(By.ID, 'id_jenis_keahlian_1').send_keys(Keahlian1)
			find(By.ID, 'id_jenis_keahlian_1').send_keys(Keys.DOWN)
			find(By.ID, 'id_jenis_keahlian_1').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			find(By.ID, 'id_jenis_pendidikan').click()		
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'idJenisPendidikan-0'))) 
			find(By.ID, Tingkat_pendidikan).click()
	
			# find(By.ID, 'id_jenis_level_1').click()		
			# wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'idJenisLevel-0'))) 
			# if Level_keahlian1 == 'Ahli':
			# 	find(By.ID, 'idJenisLevel-0').click()
			# elif Level_keahlian1 == 'Cukup Ahli':
			# 	find(By.ID, 'idJenisLevel-1').click()
			# elif Level_keahlian1 == 'Kurang Ahli':
			# 	find(By.ID, 'idJenisLevel-2').click()
			#--------------------------------------------------------------
			find(By.ID, 'id_jenis_keahlian_2').click()
			time.sleep(2) 
			find(By.ID, 'id_jenis_keahlian_2').send_keys(Keahlian2)
			find(By.ID, 'id_jenis_keahlian_2').send_keys(Keys.DOWN)
			find(By.ID, 'id_jenis_keahlian_2').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			# find(By.ID, 'id_jenis_level_2').click()
			# wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'idJenisLevel2-0'))) 
			# find(By.ID, 'id_jenis_level_2').send_keys(Level_keahlian2)
			# find(By.ID, 'id_jenis_level_2').send_keys(Keys.DOWN)
			# find(By.ID, 'id_jenis_level_2').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			# if quran == 'ya' :
			# 	find(By.XPATH, '//*[@id="is_baca_quran"]/span[1]/span').click()
			# 	print (quran)
			# elif quran == 'Tidak':
			# 	print ('tidak di check')
			# # # #----------------------------------------------------------------------
			# if latin == 'ya' :
			# 	find(By.XPATH, '//*[@id="is_baca_latin"]').click()
			# 	print (latin)
			# elif latin == 'Tidak':
			# 	print ('tidak di check')
			# #----------------------------------------------------------------------
			# find(By.ID, 'minat').send_keys(Minat)
			#======================================================================
			find(By.ID, 'tab-3').click()
			#========================Input Tab Keluarga============================ 
			#------------------------------------------------------------------------------
			find(By.ID, 'nm_ayah').send_keys(Nama_ayah)
			#------------------------------------------------------------------------------
			# find(By.ID, 'tmp_tgl_ayah').send_keys(Alamat_ayah)
			#------------------------------------------------------------------------------
			find(By.ID, 'nm_ibu').send_keys(Nama_ibu)
			#------------------------------------------------------------------------------	  
			# find(By.ID, 'tmp_tgl_ibu').send_keys(Alamat_ibu)
			#------------------------------------------------------------------------------
			# find(By.XPATH, '//*[@id="anakke"]/div/input').click()
			# pyautogui.hotkey('backspace')		
			# find(By.XPATH, '//*[@id="anakke"]/div/input').send_keys(Anak_ke)
			# pyautogui.press('enter')
			# find(By.XPATH, '//*[@id="jml_saudara"]/div/input').click()
			# pyautogui.hotkey('backspace')		
			# find(By.XPATH, '//*[@id="jml_saudara"]/div/input').send_keys(Dari)
			# pyautogui.press('enter')
			# if Dari == 2:	
			# 	find(By.ID, 'nm_saudara_1').send_keys(Nama_saudara1)
			# elif Dari == 3:	
			# 	find(By.ID, 'nm_saudara_1').send_keys(Nama_saudara1)
			# 	find(By.ID, 'nm_saudara_2').send_keys(Nama_saudara2)
			# elif Dari == 4:   
			# 	find(By.ID, 'nm_saudara_1').send_keys(Nama_saudara1)	
			# 	find(By.ID, 'nm_saudara_2').send_keys(Nama_saudara2) 
			# 	find(By.ID, 'nm_saudara_3').send_keys(Nama_saudara3)
			# elif Dari == 5:   
			# 	find(By.ID, 'nm_saudara_1').send_keys(Nama_saudara1) 
			# 	find(By.ID, 'nm_saudara_2').send_keys(Nama_saudara2)
			# 	find(By.ID, 'nm_saudara_3').send_keys(Nama_saudara3)
			# 	find(By.ID, 'nm_saudara_4').send_keys(Nama_saudara4)
			# elif Dari == 1 :
			# 	print ('anak satu satunya')
			# if Status_perkawinan == 'Belum Kawin':
			# 	print('default')
			# elif Status_perkawinan == 'Duda':
			# 	find(By.ID, 'jml_istri_suami').click()
			# 	pyautogui.hotkey('backspace')
			# 	find(By.XPATH, '//*[@id="jml_istri_suami"]/div/input' ).send_keys(jml_istrsuam) 
			# 	pyautogui.press('enter')
			# 	find(By.ID, 'nm_istri_suami_1').send_keys(Nm_istrsuam)
			# 	find(By.ID, 'tmp_tgl_istri_suami').send_keys(alm_istrsuam)
			# 	find(By.XPATH, '//*[@id="jml_anak"]/div/input').click()
			# 	pyautogui.hotkey('backspace')
			# 	jumlah = find(By.XPATH, '//*[@id="jml_anak"]/div/input' ).send_keys(jumlah_anak) 
			# 	pyautogui.press('enter')
			# 	if jumlah_anak == 1:   
			# 		find(By.ID, 'nm_anak_1').send_keys(Nama_anak1)
			# 	elif jumlah_anak == 2:	
			# 		find(By.ID, 'nm_anak_1').send_keys(Nama_anak1)	 
			# 		find(By.ID, 'nm_anak_2').send_keys(Nama_anak2)
			# 	elif jumlah_anak == 3:	
			# 		find(By.ID, 'nm_anak_1').send_keys(Nama_anak1)	
			# 		find(By.ID, 'nm_anak_2').send_keys(Nama_anak2)  
			# 		find(By.ID, 'nm_anak_3').send_keys(Nama_anak3)
			# 	elif  jumlah_anak == 0: 
			# 		print('masa ga punya anak')
			# 	#--------------------------------------------------------------
			# 	# find(By.XPATH, '//*[@id="telephone_keluarga"]').send_keys(Telepon_keluarga)
			# elif Status_perkawinan == 'Janda':
			# 	find(By.ID, 'jml_istri_suami').click()
			# 	pyautogui.hotkey('backspace')
			# 	find(By.XPATH, '//*[@id="jml_istri_suami"]/div/input' ).send_keys(jml_istrsuam) 
			# 	pyautogui.press('enter')
			# 	find(By.ID, 'nm_istri_suami_1').send_keys(Nm_istrsuam)
			# 	find(By.ID, 'tmp_tgl_istri_suami').send_keys(alm_istrsuam)
			# 	find(By.XPATH, '//*[@id="jml_anak"]/div/input').click()
			# 	pyautogui.hotkey('backspace')
			# 	jumlah = find(By.XPATH, '//*[@id="jml_anak"]/div/input' ).send_keys(jumlah_anak) 
			# 	pyautogui.press('enter')
			# 	if jumlah_anak == 1:
			# 		find(By.ID, 'nm_anak_1').send_keys(Nama_anak1)
			# 	elif jumlah_anak == 2:
			# 		find(By.ID, 'nm_anak_1').send_keys(Nama_anak1)		
			# 		find(By.ID, 'nm_anak_2').send_keys(Nama_anak2)
			# 	elif jumlah_anak == 3:
			# 		find(By.ID, 'nm_anak_1').send_keys(Nama_anak1)		
			# 		find(By.ID, 'nm_anak_2').send_keys(Nama_anak2)
			# 		find(By.ID, 'nm_anak_3').send_keys(Nama_anak3)
			# 	elif  jumlah_anak == 0: 
			# 		print('masa ga punya anak')
			# 	#--------------------------------------------------------------
			# 	# find(By.XPATH, '//*[@id="telephone_keluarga"]').send_keys(Telepon_keluarga)
			# elif Status_perkawinan == 'Kawin':
			# 	find(By.ID, 'jml_istri_suami').click()
			# 	pyautogui.hotkey('backspace')
			# 	find(By.XPATH, '//*[@id="jml_istri_suami"]/div/input' ).send_keys(jml_istrsuam) 
			# 	pyautogui.press('enter')
			# 	find(By.ID, 'nm_istri_suami_1').send_keys(Nm_istrsuam)
			# 	find(By.ID, 'tmp_tgl_istri_suami').send_keys(alm_istrsuam)
			# 	find(By.XPATH, '//*[@id="jml_anak"]/div/input').click()
			# 	pyautogui.hotkey('backspace')
			# 	jumlah = find(By.XPATH, '//*[@id="jml_anak"]/div/input' ).send_keys(jumlah_anak) 
			# 	pyautogui.press('enter')
			# 	if jumlah_anak == 1:
			# 		find(By.ID, 'nm_anak_1').send_keys(Nama_anak1)
			# 	elif jumlah_anak == 2:
			# 		find(By.ID, 'nm_anak_1').send_keys(Nama_anak1)		
			# 		find(By.ID, 'nm_anak_2').send_keys(Nama_anak2)
			# 	elif jumlah_anak == 3:
			# 		find(By.ID, 'nm_anak_1').send_keys(Nama_anak1)		
			# 		find(By.ID, 'nm_anak_2').send_keys(Nama_anak2)
			# 		find(By.ID, 'nm_anak_3').send_keys(Nama_anak3)
			# 	elif  jumlah_anak == 0: 
			# 		print('masa ga punya anak')
				#--------------------------------------------------------------
				# find(By.XPATH, '//*[@id="telephone_keluarga"]').send_keys(Telepon_keluarga)
				#======================================================================
			find(By.ID, 'tab-4').click()
			#========================Input Tab Data Fisik========================== 
			find(By.XPATH, '//*[@id="tinggi"]/div/input').click()
			pyautogui.hotkey('backspace')
			find(By.XPATH, '//*[@id="tinggi"]/div/input' ).send_keys(Tinggi_badan) 
			#--------------------------------------------------------------
			find(By.XPATH, '//*[@id="berat"]/div/input').click()
			pyautogui.hotkey('backspace')
			find(By.XPATH, '//*[@id="berat"]/div/input').send_keys(Berat_badan)
			#--------------------------------------------------------------
			find(By.ID, 'id_bentukrambut').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'bentukRambut-0'))) 
			find(By.ID, 'id_bentukrambut').send_keys(Bentuk_rambut)
			find(By.ID, 'id_bentukrambut').send_keys(Keys.DOWN)
			find(By.ID, 'id_bentukrambut').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			find(By.ID, 'id_jenis_rambut').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisRambut-0'))) 
			find(By.ID, 'id_jenis_rambut').send_keys(Warna_rambut)
			find(By.ID, 'id_jenis_rambut').send_keys(Keys.DOWN)
			find(By.ID, 'id_jenis_rambut').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			find(By.ID, 'id_bentukbibir').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'bentukBibir-0'))) 
			find(By.ID, 'id_bentukbibir').send_keys(Bentuk_bibir)
			find(By.ID, 'id_bentukbibir').send_keys(Keys.DOWN)
			find(By.ID, 'id_bentukbibir').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			find(By.ID, 'id_kacamata').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'kacamata-0'))) 
			find(By.ID, 'id_kacamata').send_keys(Berkacamata)
			find(By.ID, 'id_kacamata').send_keys(Keys.DOWN)
			find(By.ID, 'id_kacamata').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			find(By.ID, 'id_bentuk_mata').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'bentukMata-0'))) 
			find(By.ID, 'id_bentuk_mata').send_keys(Bentuk_mata)
			find(By.ID, 'id_bentuk_mata').send_keys(Keys.DOWN)
			find(By.ID, 'id_bentuk_mata').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			find(By.ID, 'id_warna_mata').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'warnaMata-0'))) 
			find(By.ID, 'id_warna_mata').send_keys(Warna_mata)
			find(By.ID, 'id_warna_mata').send_keys(Keys.DOWN)
			find(By.ID, 'id_warna_mata').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			find(By.ID, 'id_jenis_hidung').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisHidung-0'))) 
			find(By.ID, 'id_jenis_hidung').send_keys(Hidung)
			find(By.ID, 'id_jenis_hidung').send_keys(Keys.DOWN)
			find(By.ID, 'id_jenis_hidung').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			find(By.ID, 'id_jenis_muka').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisMuka-0'))) 
			find(By.ID, 'id_jenis_muka').send_keys(Raut_muka)
			find(By.ID, 'id_jenis_muka').send_keys(Keys.DOWN)
			find(By.ID, 'id_jenis_muka').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			find(By.ID, 'id_telinga').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'telinga-0'))) 
			find(By.ID, 'id_telinga').send_keys(Telinga)
			find(By.ID, 'id_telinga').send_keys(Keys.DOWN)
			find(By.ID, 'id_telinga').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			find(By.ID, 'id_jenis_mulut').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisMulut-0'))) 
			find(By.ID, 'id_jenis_mulut').send_keys(Mulut)
			find(By.ID, 'id_jenis_mulut').send_keys(Keys.DOWN)
			find(By.ID, 'id_jenis_mulut').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			find(By.ID, 'id_lengan').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'lengan-0'))) 
			find(By.ID, 'id_lengan').send_keys(Lengan)
			find(By.ID, 'id_lengan').send_keys(Keys.DOWN)
			find(By.ID, 'id_lengan').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			find(By.ID, 'id_jenis_tangan').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisTangan-0'))) 
			find(By.ID, 'id_jenis_tangan').send_keys(Tangan)
			find(By.ID, 'id_jenis_tangan').send_keys(Keys.DOWN)
			find(By.ID, 'id_jenis_tangan').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			find(By.ID, 'id_jenis_kaki').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisKaki-0'))) 
			find(By.ID, 'id_jenis_kaki').send_keys(Kaki)
			find(By.ID, 'id_jenis_kaki').send_keys(Keys.DOWN)
			find(By.ID, 'id_jenis_kaki').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			find(By.ID, 'id_warnakulit').click()
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'warnaKulit-0'))) 
			find(By.ID, 'id_warnakulit').send_keys(Warna_kulit)
			find(By.ID, 'id_warnakulit').send_keys(Keys.DOWN)
			find(By.ID, 'id_warnakulit').send_keys(Keys.ENTER)
			#--------------------------------------------------------------
			# find(By.ID, 'cacat').send_keys(Cacat_tubuh)
			# #--------------------------------------------------------------
			# time.sleep(4)
			# find(By.XPATH, '//*[@id="upload_foto_ciri_1"]').click()
			# time.sleep(4)
			# pyautogui.write(r'C:\Users\user\Documents\TRCH\Automationpython\assets\Filefoto\Gambar.jpg')
			# pyautogui.press('enter')
			# time.sleep(4)
			# find(By.XPATH, '//*[@id="upload_foto_ciri_2"]').click()
			# time.sleep(4)
			# pyautogui.write(r'C:\Users\user\Documents\TRCH\Automationpython\assets\Filefoto\Gambar.jpg')
			# pyautogui.press('enter')
			# time.sleep(4)
			# find(By.XPATH, '//*[@id="upload_foto_ciri_3"]').click()
			# time.sleep(4)
			# pyautogui.write(r'C:\Users\user\Documents\TRCH\Automationpython\assets\Filefoto\Gambar.jpg')
			# pyautogui.press('enter')
			# time.sleep(4)
			# #--------------------------------------------------------------
			# find(By.ID, 'ciri').send_keys(Catatancirikhusus1)  
			# # #--------------------------------------------------------------
			# find(By.ID, 'ciri2').send_keys(Catatancirikhusus2) 
			# # #--------------------------------------------------------------
			# find(By.ID, 'ciri3').send_keys(Catatancirikhusus3)
			# # ======================================================================
			# find(By.ID, 'tab-5').click()
			# # # ========================Input Tab Sidik Jari==========================
			# # #--------------------------------------------------------------
			# find(By.ID, 'no_paspor').send_keys(Nopaspor)
			# # #--------------------------------------------------------------
			# find(By.ID, 'rumus_daktil').send_keys(Rumus)
			# # #--------------------------------------------------------------
			# find(By.ID, 'nomor_daktil').send_keys(Nopaspor)
			# # #--------------------------------------------------------------
			# find(By.ID, 'pengambil_sj').send_keys(Pengambilansidikjari)
			# find(By.ID, 'pengambil_sj').send_keys(Keys.ENTER)
			# #--------------------------------------------------------------
			# find(By.XPATH, '//*[@id="pane-5"]/div/form/div/div[2]/div[2]/div/div/input').send_keys(Tanggalpengambilan)
			#======================================================================
			if platform.system() == 'Darwin':

				if Jenis_kelamin == "Laki-laki":
					find(By.ID, 'tab-6').click()
					#========================Input Tab Foto========================== 
					# DEPAN
					find(By.XPATH,   '//*[@id="pane-6"]/form/div/div[2]/div/div/div/div/div[1]/button').click()
					uploadGambarDepanL(driver)
					# KIRI
					find(By.XPATH,   '//*[@id="pane-6"]/form/div/div[1]/div/div/div/div/div[1]/button').click()
					uploadGambarKiriL(driver)
					
					# KANAN
					find(By.XPATH,   '//*[@id="pane-6"]/form/div/div[3]/div/div/div/div/div[1]/button').click()
					uploadGambarKananL(driver)
				elif Jenis_kelamin == "Perempuan":

					find(By.ID, 'tab-6').click()
					#========================Input Tab Foto========================== 
					# KIRI
					find(By.XPATH,   '//*[@id="pane-6"]/form/div/div[1]/div/div/div/div/div[1]/button').click()
					uploadGambarKiriP(driver)
					# DEPAN
					find(By.XPATH,   '//*[@id="pane-6"]/form/div/div[2]/div/div/div/div/div[1]/button').click()
					uploadGambarDepanP(driver)
					# KANAN
					find(By.XPATH,   '//*[@id="pane-6"]/form/div/div[3]/div/div/div/div/div[1]/button').click()
					uploadGambarKananP(driver)
					
			
			elif platform.system() == 'Windows':
			#======================================================================
				find(By.ID, 'tab-6').click()
				#========================Input Tab Foto========================== 
				find(By.XPATH,   '//*[@id="pane-6"]/form/div/div[1]/div/div/div/div/div[1]/button').click()
				time.sleep(3)
				pyautogui.write(environ.get(r'FOTBRG1'))
				pyautogui.press('enter')

				find(By.XPATH,   '//*[@id="pane-6"]/form/div/div[2]/div/div/div/div/div[1]/button').click()
				time.sleep(3)
				pyautogui.write(environ.get(r'FOTBRG1'))
				pyautogui.press('enter')

				find(By.XPATH,   '//*[@id="pane-6"]/form/div/div[3]/div/div/div/div/div[1]/button').click()
				time.sleep(3)
				pyautogui.write(environ.get(r'FOTBRG1'))
				pyautogui.press('enter')
			#======================================================================
			# find(By.ID, 'tab-7').click()
			#========================Input Tab Identitas lama========================== 
			#Submit
			time.sleep(3)
			find(By.ID, 'submitButton').click() 
			wait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'createButton')))

		except TimeoutException:
				print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!LOADING TERLALU LAMA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
				pass
		# i = i + 1
	print ('Success Created')
