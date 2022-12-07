from distutils.archive_util import make_archive
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import platform
from pytest import mark
import time
from pytest_html_reporter import attach

import sys
from os import environ, path
from dotenv import load_dotenv
load_dotenv()

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR"))
    sys.path.append("/Users/will/Documents/work/Automationpython")
elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))

from Settings.setup import initDriver, loadDataPath, quit
from Settings.login import login

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('result.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


@pytest.fixture()
def test_setup(self):
    global driver
    global wb
    swin = Service(r'C:/Users/user/Documents/TRCH/chromedriver.exe')
    smac = Service('/Users/will/Documents/chromedriver')

    if platform.system() == 'Darwin':
        driver = webdriver.Chrome(service=smac)
        # url = "http://kumbang.torche.id:32400/"
        url = "http://192.168.2.11:32400/"

        driver.get(url)
        # seting windows nya jadi max
        wb = load_workbook(filename=r"/Users/will/Documents/work/Automationpython/Filexel/Keamanan.xlsx")
        driver.maximize_window()
        driver.implicitly_wait(5)
        yield
        print(' ===== done pak will berhasil uyeee =====')
        time.sleep(5)
        driver.close()
        driver.quit()

    elif platform.system() == 'Windows':
        driver = webdriver.Chrome(service=swin)
        # url = "http://kumbang.torche.id:32400/"
        url = "http://192.168.2.11:32400/"

        driver.get(url)
        # seting windows nya jadi max
        wb = load_workbook(filename=r"C:\Users\user\Documents\TRCH\Automationpython\Filexel\Keamanan.xlsx")
        driver.maximize_window()
        driver.implicitly_wait(5)
        yield
        print(' ===== done pak will berhasil uyeee =====')
        time.sleep(5)
        driver.close()
        driver.quit()


def test_DaftarLaluLintas_Input(test_setup):
    driver.implicitly_wait(60)
    sheetrange = wb['DaftarLaluLintas_Input']

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div/div[2]/div/div/div[1]/canvas")))

    driver.find_element(By.XPATH, "//div/span").click()

    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("test-user")
    driver.find_element(By.ID, "password").send_keys("password")
    driver.find_element(By.ID, "kc-login").click()
    print('login done')
    nav1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/nav/ul/li[2]/div')
    actions = ActionChains(driver)
    actions.move_to_element(nav1).perform()

    element2 = driver.find_element(By.XPATH, "//div[4]/div/ul/li/div")
    time.sleep(1)
    actions2 = ActionChains(driver)
    actions2.move_to_element(element2).perform()
    time.sleep(1)

    driver.find_element(By.LINK_TEXT, 'Daftar Lalu Lintas').click()

    i = 2

    while i <= len(sheetrange['A']):

        Drpdownsearch = sheetrange['A' + str(i)].value
        Nama = sheetrange['B' + str(i)].value
        JenisKeluar = sheetrange['C' + str(i)].value
        TanggalKeluar = sheetrange['D' + str(i)].value
        TanggalHarusKembali = sheetrange['E' + str(i)].value
        deskripsi = sheetrange['F' + str(i)].value

        driver.implicitly_wait(60)


        try:
            driver.implicitly_wait(60)






        except TimeoutException:
            print("MASIH ADA ERROR, CEK LAGI PAK WIL")
            pass
        i = i + 1
    print("DONE PAK WILDAN, SEBATS DULU")
