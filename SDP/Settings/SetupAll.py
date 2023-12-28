import platform, sys, json
from os import environ, path
from selenium import webdriver
from pytest import mark
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options
import pyautogui
from pytest_html_reporter import attach

from dotenv import load_dotenv
load_dotenv()
import requests
import random


def initDriverEksisting():
    
    options = webdriver.ChromeOptions()

    if platform.system() == 'Darwin':
        # driver = webdriver.Chrome(environ.get("CHROMEDRIVERMAC"))
        # driver.implicitly_wait(20)

        # options.add_argument('--remote-debugging-port=9222') # port number bisa diubah sesuai keinginan
        # tentukan path ke driver Chrome
        path_to_chromedriver = environ.get("CHROMEDRIVERMAC")
        # jalankan Chrome dengan opsi dan path yang ditentukan
        driver = webdriver.Chrome(executable_path=path_to_chromedriver, chrome_options=options)

    elif platform.system() == 'Windows':
        swin = Service(environ.get("CHROMEDRIVERWIN"))
        driver = webdriver.Chrome(service=swin)
    driver.get(environ.get("hostEksisting"))
    #driver.get(environ.get("HOST"))
    driver.maximize_window()
    # pyautogui.press('f12')
    
    return driver

def initDriver():
    
    options = webdriver.ChromeOptions()

    if platform.system() == 'Darwin':
        # driver = webdriver.Chrome(environ.get("CHROMEDRIVERMAC"))
        # driver.implicitly_wait(20)

        # options.add_argument('--remote-debugging-port=9222') # port number bisa diubah sesuai keinginan
        # tentukan path ke driver Chrome
        path_to_chromedriver = environ.get("CHROMEDRIVERMAC")
        # jalankan Chrome dengan opsi dan path yang ditentukan
        driver = webdriver.Chrome(executable_path=path_to_chromedriver, chrome_options=options)

    elif platform.system() == 'Windows':
        swin = Service(environ.get("CHROMEDRIVERWIN"))
        driver = webdriver.Chrome(service=swin)
    driver.get(environ.get("HOSTDO"))
    #driver.get(environ.get("HOST"))
    driver.maximize_window()
    # pyautogui.press('f12')
    
    return driver

# def initDriver():
    
#     options = Options()
#     print('.')
#  
#     if platform.system() == 'Darwin':
#         
#         options = webdriver.ChromeOptions()
#     
#         # tentukan path ke driver Chrome
#         path_to_chromedriver = environ.get("CHROMEDRIVERMAC")
#         # jalankan Chrome dengan opsi dan path yang ditentukan
#         driver = webdriver.Chrome(executable_path=path_to_chromedriver, chrome_options=options)

#     elif platform.system() == 'Windows':
#         swin = Service(environ.get("CHROMEDRIVERWIN"))
#         driver = webdriver.Chrome(service=swin)
#     driver.get(environ.get("HOSTDO"))
#     #driver.get(environ.get("HOST"))
#     driver.maximize_window()
#     # pyautogui.press('f12')
    
#     return driver

def loadDataPath():
    if platform.system() == 'Darwin':
        file = open(environ.get("MACJSONDATA"), 'r')
    elif platform.system() == 'Windows':
        file = open(environ.get("WINJSONDATA"), 'r')

    data = json.load(file)
    return data

def buttonTambah(driver):
    driver.implicitly_wait(20)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButton"]')))
    print('.')

def buttonSubmit(driver):
    driver.implicitly_wait(20)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    print('.')

def selectKategoriPegawai(driver):
    driver.implicitly_wait(20)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "pegawai").click()
    print('.')

def selectKategoriTamuDinas(driver):
    driver.implicitly_wait(20)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "tamuDinas").click()
    print('.')

def sleep(driver):
    driver.implicitly_wait(20)
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'

    print('=')
    print(driver.current_url)
    status_code = requests.get(driver.current_url).status_code
    status = True
    while status:
        if status_code != 200:
            print("Status code is not 200")
            quit(driver)
        else:
            print("status code is 200")
            status = False

            #time.sleep(5)
            print("-")
            time.sleep(0.1)
            #input("")
            print('wait . . . . . . . . . . . . . . . . . . . . . ')

    

def waituntill(driver):
    driver.implicitly_wait(20)
    
def quit(driver):
    time.sleep(3)
    print('.')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▓▒▒▒▒▒▒▒▒▓▒')
    print('▒▒▓▓▓▓▓▓▓▓▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')

    driver.close()
    time.sleep(1)
    driver.quit()


def upload(driver):
    sleep(driver)
    time.sleep(0.2)
    pyautogui.press('x')
    time.sleep(0.2)
    pyautogui.press('enter')
    # print('upload pembinaan')
    time.sleep(0.2)
    
def uploadGambar(driver):
    time.sleep(1)
    pyautogui.press('g')
    time.sleep(1)
    pyautogui.press('enter')

def uploadGambarDepanL(driver):
    time.sleep(1)
    pyautogui.press('D')
    time.sleep(1)
    pyautogui.press('enter')

def uploadGambarKiriL(driver):
    time.sleep(0.4)
    pyautogui.press('K')
    time.sleep(0.4)
    pyautogui.press('enter')
def Sertifikat(driver):
    time.sleep(0.7)
    pyautogui.press('s')
    time.sleep(0.7)
    pyautogui.press('enter')

def uploadGambarKananL(driver):
    time.sleep(1)
    pyautogui.press('N')
    time.sleep(1)
    pyautogui.press('enter')


def uploadGambarDepanP(driver):
    time.sleep(1)
    pyautogui.press('z')
    time.sleep(1)
    pyautogui.press('enter')

def uploadGambarKiriP(driver):
    time.sleep(1)
    pyautogui.press('v')
    time.sleep(1)
    pyautogui.press('enter')

def uploadGambarKananP(driver):
    time.sleep(1)
    pyautogui.press('p')
    time.sleep(1)
    pyautogui.press('enter')

def hold(driver):
    driver.implicitly_wait(20)
    attach(data=driver.get_screenshot_as_png())
    WARNING = '\033[93m'
    # time.sleep(0.5)
    # print(WARNING +"================================================================= Press Enter to continue")
    # input("")

def ValuejenisRegistrasi(driver):
    
    ValueJenisReg = int(input("1. A I, \n 2. A II, \n 3. AIII, 4. B I, 5. B II A, 6. B II B, 7. B III, 8. A IV, 9. A V, 10. C, 11. Hukuman Mati"))
            
    if ValueJenisReg == 1:
        jenis_registrasi 			= random.choice(['A I'])
    elif ValueJenisReg == 2:
        jenis_registrasi 			= random.choice(['A II'])
    elif ValueJenisReg == 3:
        jenis_registrasi 			= random.choice(['A III'])
    elif ValueJenisReg == 4:
        jenis_registrasi 			= random.choice(['A IV'])
    elif ValueJenisReg == 5:
        jenis_registrasi 			= random.choice(['A V'])
    elif ValueJenisReg == 6:
        jenis_registrasi 			= random.choice(['B I'])
    elif ValueJenisReg == 7:
        jenis_registrasi 			= random.choice(['B II A'])
    elif ValueJenisReg == 8:
        jenis_registrasi 			= random.choice(['B II B'])
    elif ValueJenisReg == 9:
        jenis_registrasi 			= random.choice(['B III'])
    elif ValueJenisReg == 10:
        jenis_registrasi 			= random.choice(['C'])
    elif ValueJenisReg == 11:
        jenis_registrasi 			= random.choice(['Hukuman Mati'])
    else:
        print("Input Salah")

def InputDocRegis(driver):
    find = driver.find_element
    time.sleep(1)
    find(By.ID, "tab-file_dokumen").click()

    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "chooseFile-0")))
    find(By.ID, "chooseFile-0").click()
    upload(driver)

    find(By.ID, "chooseFile-1").click()
    upload(driver)

    find(By.ID, "chooseFile-2").click()
    upload(driver)

    find(By.ID, "chooseFile-3").click()
    upload(driver)

    find(By.ID, "chooseFile-4").click()
    upload(driver)

    find(By.ID, "chooseFile-5").click()
    upload(driver)

    find(By.ID, "chooseFile-6").click()
    upload(driver)

    find(By.ID, "chooseFile-7").click()
    upload(driver)

    find(By.ID, "chooseFile-8").click()
    upload(driver)

    find(By.ID, "chooseFile-15").click()
    upload(driver)

    find(By.ID, "chooseFile-16").click()
    upload(driver)

    find(By.ID, "chooseFile-17").click()
    upload(driver)

    find(By.ID, "chooseFile-20").click()
    upload(driver)

    find(By.ID, "chooseFile-21").click()
    upload(driver)