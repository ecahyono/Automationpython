import logging
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
import sys

from dotenv import load_dotenv
load_dotenv()

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR")) 
elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))

from Settings.setup import initDriver, loadDataPath
from Settings.login import login


Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('result.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


def test():
    Log.info('Info masehhhhajeegggg ')
def test1():
    Log.info('Info masehhhhajeegggg ')
def test2():
    Log.info('Info masehhhhajeegggg ')
def test3():
    Log.info('Info masehhhhajeegggg ')
def test4():
    Log.info('Info masehhhhajeegggg ')
def test5():
    Log.info('Info masehhhhajeegggg ')
def test6():
    Log.info('Info masehhhhajeegggg ')
def test7():
    Log.info('Info masehhhhajeegggg ')
def test8():
    Log.info('Info masehhhhajeegggg ')




