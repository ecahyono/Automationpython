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
    wb = load_workbook(environ.get("RegSelenium"))

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))
    wb = load_workbook(environ.get("RegSelenium"))

from Settings.setup import initDriver, loadDataPath, hold
from Settings.login import *
from Settings.Page.accessmenu import *
from Settings.setupPembinaan import uploadGambar, hold, upload


import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Registrasi.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrange = wb['RegSelenium']

@mark.webtest
# init driver by os
def test_setup():
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
@mark.webtest
def test_loggin():
	# login(driver)
	Testing(driver)

@mark.webtest
def test_aksesmenu():
	registrasitahanannarapidana(driver)

@mark.webtest
def test_Registrasi():
	i = 2
	while i <= len(sheetrange['A']):
		NamaWBP                             = sheetrange['A'+str(i)].value
		print('Success read csv')





		#faker Random Input
		nums = '01234567891011121415161716'
		# jenis_registrasi 	= ['A I','B I']
		# jenis_registrasi 	= ['B I']
		jenis_registrasi 			= random.choice(['B I'])
		NoRegistrasi				= "REG"+ fake.isbn10() + ".PASS" + ".PASS" + random.choice(nums) +".WL." + fake.date_between(start_date='today', end_date='today').strftime('%d.%m.%Y') + "-" + random.choice(nums)
		tgl_Surat_Penahanan			= fake.date_between(start_date='-365d', end_date='-250d').strftime('%d.%m.%Y')
		NomorSuratPenahanan			= "SP.PAS/" + fake.date_between(start_date='-1years', end_date='-1years').strftime('%d.%m.%Y')
		namapetugas					= fake.name()
		Kejaksaan					= random.choice(['#kejaksaanOption-0 > span','#kejaksaanOption-1 > span','#kejaksaanOption-2 > span','#kejaksaanOption-3 > span','#kejaksaanOption-4 > span','#kejaksaanOption-5 > span'])
		instansiPenyidik			= random.choice(['id_instansi_penyidik-0','id_instansi_penyidik-1','id_instansi_penyidik-2','id_instansi_penyidik-3','id_instansi_penyidik-4','id_instansi_penyidik-5'])
		LokasiDokumen				= fake.address()
		AsalTahanan 				= random.choice(['APH ','RUTAN ','LAPAS ']) + fake.administrative_unit()
		tgl_Penangkapan				= tgl_Surat_Penahanan #apakah harus ada validasi mengenai tanggal penangkapan terharap surat penahanan
		tgl_BA8						= fake.date_between(start_date='-250d', end_date='-200d').strftime('%d.%m.%Y') #masih belum tau tanggal ba8 itu di dapat dari mana, rulesnya seperti apa
		tgl_putusan_akhir			= tgl_BA8 #tanggal putusan akhir tidak tau rulesnya seperti apa
		# Jenis_putusan				= random.choice(['PPN','PPT','PMA','PK'])
		Jenis_putusan				= random.choice(['PPN'])
		tgl_menjalani_cabutpb		= tgl_BA8 
		tgl_ba8						= tgl_BA8	

		#TAB PERKARA
		KejahatanUtama				= random.choice(['Cyber Crime','Organized Crime','Victimless Crime ','White Collar Crime'])
		terminologi 				= random.choice(['kejahatan.0.id_terminologi-0','kejahatan.0.id_terminologi-1','kejahatan.0.id_terminologi-2','kejahatan.0.id_terminologi-3','kejahatan.0.id_terminologi-4','kejahatan.0.id_terminologi-5'])
		tempatKejahatan				= fake.administrative_unit()
		Tanggal_Putusan				= tgl_BA8

		#TAB PUTUSAN
		NomorPutusan				= "PTS"+ fake.isbn10() + ".PASS" + ".PASS" + random.choice(nums) +".WL." + tgl_BA8 + "-" + random.choice(nums)
		namahakimketua				= fake.name()
		HakimAnggota1				= fake.name()
		HakimAnggota2				= fake.name()
		panitera					= fake.name()
		NamaJaksa					= fake.name()

		# jenis_hukuman				=random.choice(['id_jenis_hukuman-0-0','id_jenis_hukuman-0-1','id_jenis_hukuman-0-2'])
		jenis_hukuman				= random.choice(['id_jenis_hukuman-0-1','id_jenis_hukuman-0-2'])
		PidanaTahun					= fake.random_int(min=1, max=10)
		jenisRemisi					= random.choice(['jenis_remisi-0-0','jenis_remisi-0-1','jenis_remisi-0-2','jenis_remisi-0-3','jenis_remisi-0-4'])






		

		
		print('Success generate faker')


		
			# nge baca mulai dari tabel A
		
			# deklarasi bahwa NIP itu ada di A 
		
		
		
	

	
		
		WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'cari')))
		Log.info('Click Button Cari')

		WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(.,\'Registrasi Baru\')]')))
		driver.find_element(By.XPATH, "//span[contains(.,\'Registrasi Baru\')]").click()
		Log.info('Click Button Registrasi')
		hold(driver)
						 
		try:
			WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'findButton')))
			driver.find_element(By.ID, "jenisRegistrasi").send_keys(jenis_registrasi)
			WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,\'"+ jenis_registrasi +"')]"))).click()
			time.sleep(0.5)
			Log.info("Click Button Jenis Registrasi '"+ jenis_registrasi +"' ")
			hold(driver)

			driver.find_element(By.ID, "noRegistrasi").click()
			# input('Tekan Enter Untuk Melanjutkan')
			Log.info("Input No Registrasi")		
			hold(driver)
			driver.find_element(By.ID, "noRegistrasi").send_keys(NamaWBP)	
			hold(driver)
			
			if jenis_registrasi == 'A I':
				pass

			elif jenis_registrasi == 'B I':
				WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//li[@id='noRegistrasiOption-0']/div/div/table/tbody/tr[2]/td"))).click()
				Log.info("Click Button No Registrasi")
				hold(driver)

				driver.find_element(By.ID, "findButton").click()
				Log.info("Click Button cari")
				hold(driver)

				WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.el-dialog__headerbtn')))
				driver.find_element(By.CSS_SELECTOR, ".el-dialog__headerbtn").click()
				Log.info('close Pop Up')
				hold(driver)

				driver.find_element(By.ID, "nmr_reg_gol").click()
				driver.find_element(By.ID, "nmr_reg_gol").send_keys(NoRegistrasi)
				Log.info('input no registrasi ')
				hold(driver)

				driver.find_element(By.ID, "tgl_srt_thn").click()
				driver.find_element(By.ID, "tgl_srt_thn").send_keys(tgl_Surat_Penahanan)
				driver.find_element(By.ID, "tgl_srt_thn").send_keys(Keys.ENTER)
				Log.info('input tanggal surat ')
				hold(driver)

				driver.find_element(By.ID, "nmr_srt_thn").click()
				driver.find_element(By.CSS_SELECTOR, ".el-col > .is-required:nth-child(3)").click()
				driver.find_element(By.ID, "nmr_srt_thn").send_keys(NomorSuratPenahanan)
				driver.find_element(By.CSS_SELECTOR, ".el-row:nth-child(4) > .el-col:nth-child(1)").click()
				driver.find_element(By.CSS_SELECTOR, ".is-success:nth-child(3) > .el-form-item__label").click()
				Log.info('input nomor surat penahanan')
				hold(driver)

				driver.find_element(By.ID, "nm_pjbt_thn").click()
				driver.find_element(By.ID, "nm_pjbt_thn").send_keys(namapetugas)
				Log.info('input nama petugas')
				hold(driver)

				driver.find_element(By.ID, "kejaksaan").click()
				WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, Kejaksaan))).click()
				Log.info('Pilih Kejaksaan')
				hold(driver)

				driver.find_element(By.ID, "instansi_thn").send_keys("Kejaksaan Agung Republik Indonesia")
				Log.info('Input Instansi')
				hold(driver)

				driver.find_element(By.ID, "id_instansi_penyidik").click()
				WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, instansiPenyidik))).click()
				Log.info('pilih instansi penyidik')
				hold(driver)

				driver.find_element(By.ID, "lokasi_dokumen").send_keys(LokasiDokumen)
				Log.info('input lokasi dokumen')
				hold(driver)

				driver.find_element(By.ID, "asal_tahanan").send_keys(AsalTahanan)
				Log.info('input asal tahanan')
				hold(driver)

				driver.find_element(By.ID, "kepolisian").send_keys(AsalTahanan)
				Log.info('input kepolisian')
				hold(driver)

				driver.find_element(By.ID, "tgl_penangkapan").click()
				driver.find_element(By.ID, "tgl_penangkapan").send_keys(tgl_Penangkapan)
				driver.find_element(By.ID, "tgl_penangkapan").send_keys(Keys.ENTER)
				Log.info('input tanggal penangkapan')
				hold(driver)

				driver.find_element(By.ID, "tgl_ba8").click()
				driver.find_element(By.ID, "tgl_ba8").send_keys(tgl_BA8)
				driver.find_element(By.ID, "tgl_ba8").send_keys(Keys.ENTER)
				Log.info('input tanggal BA 8')
				hold(driver)

				driver.find_element(By.ID, "tgl_menjalani_putusan_akhir").click()
				driver.find_element(By.ID, "tgl_menjalani_putusan_akhir").send_keys(tgl_putusan_akhir)
				driver.find_element(By.ID, "tgl_menjalani_putusan_akhir").send_keys(Keys.ENTER)
				Log.info('input tanggal menjalani putusan akhir')
				hold(driver)

				driver.find_element(By.CSS_SELECTOR, ".el-tooltip__trigger:nth-child(5) > .el-form-item__label").click()
				driver.find_element(By.ID, "jenis_putusan").click()
				driver.find_element(By.ID, Jenis_putusan).click()
				Log.info('input jenis putusan')
				hold(driver)

				driver.find_element(By.ID, "tgl_menjalani_cabutpb").click()
				driver.find_element(By.ID, "tgl_menjalani_cabutpb").send_keys(tgl_menjalani_cabutpb)
				driver.find_element(By.ID, "tgl_menjalani_cabutpb").send_keys(Keys.ENTER)
				Log.info('tanggal menjalani pencaputan PB')
				hold(driver)

				driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(22) > .el-form-item__content").click()

				driver.find_element(By.CSS_SELECTOR, ".el-row:nth-child(2) > .el-col-xs-24:nth-child(2)").click()
				hold(driver)
            
				driver.find_element(By.ID, "tab-perkara").click()
				driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) > .el-form-item .el-switch__action").click()
				driver.find_element(By.CSS_SELECTOR, ".is-required .el-switch__action").click()
				Log.info('pilih TAB perkara')
				hold(driver)
				

				driver.find_element(By.ID, "kejahatan.0.deskripsi").click()
				driver.find_element(By.ID, "kejahatan.0.deskripsi").send_keys(KejahatanUtama)
				driver.find_element(By.ID, "kejahatan.0.uu_kejahatan").send_keys(KejahatanUtama)
				Log.info('input kejahatan utama')
				hold(driver)

				driver.find_element(By.ID, "kejahatan.0.pasal_utama").click()
				driver.find_element(By.ID, "kejahatan.0.pasal_utama").send_keys("pasal " + KejahatanUtama)
				Log.info('input pasal utama')
				hold(driver)

				driver.find_element(By.ID, "kejahatan.0.id_terminologi").click()
				driver.find_element(By.ID, terminologi).click()
				Log.info('input Kejahatan')
				hold(driver)

				driver.find_element(By.ID, "kejahatan.0.wilayah").click()
				driver.find_element(By.ID, "kejahatan.0.wilayah").send_keys(tempatKejahatan)
				Log.info('input tempat kejadian')
				hold(driver)
				driver.find_element(By.XPATH, "//div[6]/div/div/span").click()

				driver.find_element(By.ID, "eksekusi_jaksa").click()
				driver.find_element(By.ID, "EKS1").click()
				Log.info('input eksekusi jaksa')
				hold(driver)


				if Jenis_putusan == 'PPN':
					driver.find_element(By.ID, "tab-putusan_pengadilan_negeri").click()
					Log.info('pilih jenis putusan Pengadilan Negeri')
					hold(driver)

					driver.find_element(By.XPATH, "//form/div[5]/div/div/div/span").click()
					hold(driver)

					driver.find_element(By.ID, "tgl_putusan-0").click()
					driver.find_element(By.ID, "tgl_putusan-0").send_keys(Tanggal_Putusan)
					Log.info('Input tanggal putusan akhir')
					hold(driver)

					driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) > .el-form-item:nth-child(1) > .el-form-item__content:nth-child(2)").click()

					driver.find_element(By.ID, "nmr_putusan-0").send_keys(NomorPutusan)
					Log.info('input nomor putusan ')
					hold(driver)

					driver.find_element(By.CSS_SELECTOR, ".px-2").click()

					driver.find_element(By.ID, "pasal-0").send_keys(KejahatanUtama)
					Log.info('input pasal')
					hold(driver)

					driver.find_element(By.ID, "hakim_ketua-0").send_keys(namahakimketua)
					Log.info('Input nama hakim ketua')
					hold(driver)


					driver.find_element(By.ID, "hakim_anggota1-0").send_keys(HakimAnggota1)
					Log.info('input hakim anggota 1')
					hold(driver)

					driver.find_element(By.ID, "hakim_anggota2-0").send_keys(HakimAnggota2)
					Log.info('input hakim anggota 2')
					hold(driver)

					driver.find_element(By.CSS_SELECTOR, ".el-form > div:nth-child(5)").click()
					driver.find_element(By.ID, "panitera-0").click()
					driver.find_element(By.ID, "panitera-0").send_keys(panitera)
					Log.info('input panitera')
					hold(driver)

					driver.find_element(By.ID, "jaksa-0").click()
					driver.find_element(By.ID, "jaksa-0").send_keys(NamaJaksa)
					Log.info('input nama jaksa')
					hold(driver)

					driver.find_element(By.XPATH, "//input[@id='instansi-0']").click()
					driver.find_element(By.XPATH, "//li[contains(.,\'Pengadilan Negeri Jakarta Pusat\')]").click()
					Log.info('input pengadilan')
					hold(driver)

					driver.find_element(By.ID, "tgl_dijalankan_ptsn-0").click()
					driver.find_element(By.ID, "tgl_dijalankan_ptsn-0").send_keys(tgl_BA8)
					driver.find_element(By.ID, "tgl_dijalankan_ptsn-0").send_keys(Keys.ENTER)
					Log.info('input tanggal dijalankan putusan')
					hold(driver)

					driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) > .el-form-item:nth-child(11) > .el-form-item__content").click()
					driver.find_element(By.ID, "peranan_kejahatan-0").click()
					driver.find_element(By.ID, "peranan_kejahatan-0").send_keys("pelaku utama")
					Log.info('Input Tersangka')
					hold(driver)

					driver.find_element(By.ID, "status_hukum_basan_baran-0").click()
					driver.find_element(By.ID, "status_hukum_basan_baran-0-0").click()
					Log.info('status hukum basan baran')
					hold(driver)

					driver.find_element(By.ID, "id_jenis_hukuman-0").click()
					hold(driver)

					if jenis_hukuman == 'id_jenis_hukuman-0-0':
						driver.find_element(By.ID, "id_jenis_hukuman-0-0").click()
						Log.info('pilih jenis hukuman  mati')
						hold(driver)

					else :
						driver.find_element(By.ID, "id_jenis_hukuman-0-1").click()
						Log.info('pilih jenis hukuman pidana ')
						hold(driver)

						driver.find_element(By.ID, "thn_kurung-0").click()
						driver.find_element(By.ID, "thn_kurung-0").send_keys(PidanaTahun)
						Log.info("input pidana")

						driver.find_element(By.CSS_SELECTOR, ".px-2").click()
						driver.find_element(By.ID, "jenis_remisi-0").click()
						driver.find_element(By.ID, jenisRemisi).click()
						driver.find_element(By.CSS_SELECTOR, ".el-form > div:nth-child(5)").click()
						Log.info('input jenis remisi')

				

				

					








				elif Jenis_putusan =='PPT':
					driver.find_element(By.ID, "tab-putusan_pengadilan_tinggi").click()
					Log.info('pilih jenis putusan')


				# elif Jenis_putusan =='PMA':
				# 	driver.find_element(By.ID, "tab-putusan_mahkamah_agung").click()
				# 	Log.info('pilih jenis putusan')
				# elif Jenis_putusan =='PK':
				# 	driver.find_element(By.ID, "tab-putusan_kasasi").click()
				# 	Log.info('pilih jenis putusan')
				driver.find_element(By.ID, "tab-registrasi").click()
				Log.info('pilih tab registrasi')

				driver.find_element(By.ID, "tgl_pertama_ditahan").click()
				driver.find_element(By.ID, "tgl_pertama_ditahan").send_keys(tgl_BA8)
				driver.find_element(By.ID, "tgl_pertama_ditahan").send_keys(Keys.ENTER)
				Log.info('input tanggal pertama ditahan')
				hold(driver)

				time.sleep(2)
				driver.find_element(By.ID, "tgl_akhir_ditahan").click()
				driver.find_element(By.ID, "tgl_akhir_ditahan").send_keys(tgl_BA8)
				driver.find_element(By.ID, "tgl_akhir_ditahan").send_keys(Keys.ENTER)
				Log.info('Input tanggal akhir ditahan')
				hold(driver)

				driver.find_element(By.CSS_SELECTOR, ".el-row:nth-child(4) .el-form-item__content").click()

				driver.find_element(By.ID, "tgl_awal_tahan_golongan").click()
				driver.find_element(By.ID, "tgl_awal_tahan_golongan").send_keys(tgl_BA8)
				driver.find_element(By.ID, "tgl_awal_tahan_golongan").send_keys(Keys.ENTER)
				Log.info('Input tanggal awal ditahan golongan')
				hold(driver)

				driver.find_element(By.CSS_SELECTOR, ".el-row:nth-child(4) .el-form-item__content").click()
				driver.find_element(By.CSS_SELECTOR, ".el-row:nth-child(3) > .el-col:nth-child(2) svg").click()

				driver.find_element(By.ID, "tgl_msk_lapas").click()
				driver.find_element(By.ID, "tgl_msk_lapas").send_keys(tgl_BA8)
				driver.find_element(By.ID, "tgl_msk_lapas").send_keys(Keys.ENTER)

				time.sleep(4)
				Log.info('Input tanggal masuk lapas')
				hold(driver)
           

				driver.find_element(By.ID, "tab-file_dokumen").click()


				WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "chooseFile-0")))
				driver.find_element(By.ID, "chooseFile-0").click()
				upload(driver)

				driver.find_element(By.ID, "chooseFile-1").click()
				upload(driver)

				driver.find_element(By.ID, "chooseFile-2").click()
				upload(driver)

				driver.find_element(By.ID, "chooseFile-3").click()
				upload(driver)

				driver.find_element(By.ID, "chooseFile-4").click()
				upload(driver)

				driver.find_element(By.ID, "chooseFile-5").click()
				upload(driver)

				driver.find_element(By.ID, "chooseFile-6").click()
				upload(driver)

				driver.find_element(By.ID, "chooseFile-7").click()
				upload(driver)

				driver.find_element(By.ID, "chooseFile-8").click()
				upload(driver)

				driver.find_element(By.ID, "chooseFile-15").click()
				upload(driver)

				driver.find_element(By.ID, "chooseFile-16").click()
				upload(driver)

				driver.find_element(By.ID, "chooseFile-17").click()
				upload(driver)

				driver.find_element(By.ID, "chooseFile-20").click()
				upload(driver)

				driver.find_element(By.ID, "chooseFile-21").click()
				upload(driver)
			

			

	
			# input('Tekan Enter Untuk Melanjutkan')
			driver.find_element(By.ID, 'submitButton').click() 
			WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.ID, 'cari')))

		

		except TimeoutException:
			print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!LOADING TERLALU LAMA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
			pass
		i = i + 1
		
	print ('Success Created')
