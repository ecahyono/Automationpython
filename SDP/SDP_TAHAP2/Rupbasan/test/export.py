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
import pyautogui
import platform
import logging
import sys
from openpyxl import load_workbook

from dotenv import load_dotenv
load_dotenv()

if platform.system() == 'Darwin':
	sys.path.append(environ.get("MACPARENTDIR")) 
elif platform.system() == 'Windows':
	sys.path.append(environ.get("WINPARENTDIR"))

from Settings.setup import initDriver, loadDataPath, hold
from Settings.login import  oprupbasanbdg
from Settings.Page.Rupbasan import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Export.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

# init driver by os
@mark.fixture_export
def test_00_setup():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()

@mark.fixture_export
def test_00_loggin():
	Log.info('Memasukan User name dan Password di halaman Login')
	oprupbasanbdg(driver)

@mark.fixture_export
def test_export_penerimaan():
	Log.info('Mengakses menu Penerimaan dengan memilih modul Rupbasan kemudian pilih menu Penerimaan')
	Rupbasan(driver)
	childmenu1(driver)
	alihkan(driver)
	hold(driver)
	Log.info('Berhasil mencetak data penerimaan sesuai dengan total halaman yang dipilih dengan format PDF (.pdf)')
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) dengan menekan Button Export Excel')
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) yang terhubung langsung dengan perangkat tambahan (printer)')
	exportPDF(driver)
	exportexcel(driver)
	tprint(driver)

@mark.fixture_export
def test_export_penempatan():
	Log.info('Mengakses menu Penerimaan dengan memilih modul Rupbasan kemudian pilih menu Penerimaan')
	Rupbasan(driver)
	childmenu2(driver)
	alihkan(driver)
	hold(driver)
	Log.info('Berhasil mencetak data penerimaan sesuai dengan total halaman yang dipilih dengan format PDF (.pdf)')
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) dengan menekan Button Export Excel')
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) yang terhubung langsung dengan perangkat tambahan (printer)')
	exportPDF(driver)
	exportexcel(driver)
	tprint(driver)

@mark.fixture_export
def test_export_pemeliharaan():
	Log.info('Mengakses menu Penerimaan dengan memilih modul Rupbasan kemudian pilih menu Penerimaan')
	Rupbasan(driver)
	childmenu3(driver)
	alihkan(driver)
	hold(driver)
	Log.info('Berhasil mencetak data penerimaan sesuai dengan total halaman yang dipilih dengan format PDF (.pdf)')
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) dengan menekan Button Export Excel')
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) yang terhubung langsung dengan perangkat tambahan (printer)')
	exportPDF(driver)
	exportexcel(driver)
	tprint(driver)

@mark.fixture_export
def test_export_Pengamanan():
	Log.info('Mengakses menu Penerimaan dengan memilih modul Rupbasan kemudian pilih menu Penerimaan')
	Rupbasan(driver)
	childmenu4(driver)
	alihkan(driver)
	hold(driver)
	Log.info('Berhasil mencetak data penerimaan sesuai dengan total halaman yang dipilih dengan format PDF (.pdf)')
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) dengan menekan Button Export Excel')
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) yang terhubung langsung dengan perangkat tambahan (printer)')
	exportPDF(driver)
	exportexcel(driver)
	tprint(driver)

@mark.fixture_export
def test_export_mutasi():
	Log.info('Mengakses menu Penerimaan dengan memilih modul Rupbasan kemudian pilih menu Penerimaan')
	Rupbasan(driver)
	childmenu5(driver)
	alihkan(driver)
	hold(driver)
	Log.info('Berhasil mencetak data penerimaan sesuai dengan total halaman yang dipilih dengan format PDF (.pdf)')
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) dengan menekan Button Export Excel')
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) yang terhubung langsung dengan perangkat tambahan (printer)')
	exportPDF(driver)
	exportexcel(driver)
	tprint(driver)

@mark.fixture_export
def test_export_pengeluaran():
	Log.info('Mengakses menu Penerimaan dengan memilih modul Rupbasan kemudian pilih menu Penerimaan')
	Rupbasan(driver)
	childmenu6(driver)
	alihkan(driver)
	hold(driver)
	Log.info('Berhasil mencetak data penerimaan sesuai dengan total halaman yang dipilih dengan format PDF (.pdf)')
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) dengan menekan Button Export Excel')
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) yang terhubung langsung dengan perangkat tambahan (printer)')
	exportPDF(driver)
	exportexcel(driver)
	tprint(driver)

# @mark.fixture_export
# def test_export_laporan(): #lewat karena ID
# 	Log.info('Mengakses menu Penerimaan dengan memilih modul Rupbasan kemudian pilih menu Penerimaan')
# 	Rupbasan(driver)
# 	childmenu6(driver)
# alihkan(driver)	
# hold(driver)

@mark.fixture_export
def test_export_Gudang():
	lainlain(driver)
	childlain(driver)
	childlain1(driver)
	Log.info('Berhasil mencetak data penerimaan sesuai dengan total halaman yang dipilih dengan format PDF (.pdf)')
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) dengan menekan Button Export Excel')
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) yang terhubung langsung dengan perangkat tambahan (printer)')
	exportPDF(driver)
	exportexcel(driver)
	tprint(driver)

@mark.fixture_export
def test_export_SektorGudang():
	lainlain(driver)
	childlain(driver)
	childlain2(driver)
	Log.info('Berhasil mencetak data penerimaan sesuai dengan total halaman yang dipilih dengan format PDF (.pdf)')
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) dengan menekan Button Export Excel')
	Log.info('Mencetak data penerimaan (sesuai dengan jumlah halaman) yang terhubung langsung dengan perangkat tambahan (printer)')
	exportPDF(driver)
	exportexcel(driver)
	tprint(driver)