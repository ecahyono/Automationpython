from json import load
from lib2to3.pgen2 import driver
import string
from turtle import rt
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys 

from openpyxl import load_workbook
import time

#target halaman excel ada dimana , wb = variablenya
wb = load_workbook(filename=r"/Users/will/Documents/Automationpython/Filexel/registrasi.xlsx")

# jadi ini bisa read sheet yang dibawah itu yang di excel
sheetrange = wb['reg']

# ini web driver disimpen dimana, kalo disimpen di path kosongin aja
driver = webdriver.Chrome(r"/Users/will/Downloads/chromedriver")

# link nya ini dimana
driver.get("http://kumbang.torche.id:32400/")
#url = "http://192.168.2.11:32400/"
# seting windows nya jadi max   
driver.maximize_window()
# script gakan di eksekusi kalo web ga muncul. kalo lebih dari 10 detik ga muncul error
driver.implicitly_wait(10)
# ini letak xpath icon login
driver.find_element(By.XPATH, "//div/span").click()
# ini masuk ke form input username
driver.find_element(By.ID, "username").click()
# masukin input username
driver.find_element(By.ID, "username").send_keys("rono")
# masukin input password
driver.find_element(By.ID, "password").send_keys("rene")
# click button login
driver.find_element(By.ID, "kc-login").click()
time.sleep(2)
# variable element nyari dimana letak menu lain lain
element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/nav/ul/li[1]/div")
time.sleep(2)
actions = ActionChains(driver)
actions.move_to_element(element).perform()
time.sleep(2)
#WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"el-popper-container-7971\"]/div[3]/div/ul/li[2]")))
time.sleep(2)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx anak ke 2
element2 = driver.find_element(By.XPATH, "//div/ul/li[2]/div")
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx anak ke 2

time.sleep(2)
actions2 = ActionChains(driver)
actions2.move_to_element(element2).perform()
driver.find_element(By.LINK_TEXT, "Registrasi Tahanan/ Narapidana").click()
                                        
i = 2

# nge baca mulai dari tabel A
while i <= len(sheetrange['A']):
    # deklarasi bahwa NIP itu ada di A 
    NoInduk = sheetrange['A'+str(i)].value
    # deklarasi bahwa NAMA itu ada di B 
    noregis = sheetrange['B'+str(i)].value
    # deklarasi bahwa NAMA itu ada di B 
    TglSuratPenahanan = sheetrange['C'+str(i)].value
    NomorSuratPenahanan = sheetrange['D'+str(i)].value
    NamaPetugasInstansi = sheetrange['E'+str(i)].value
    Kejaksaan = sheetrange['F'+str(i)].value
    AsalInstansi = sheetrange['G'+str(i)].value
    Keterangan = sheetrange['H'+str(i)].value
    Penyidik = sheetrange['I'+str(i)].value
    menahan10 = sheetrange['J'+str(i)].value
    menahan3 = sheetrange['K'+str(i)].value
    menahan1 = sheetrange['L'+str(i)].value
    LokasiDokumen = sheetrange['M'+str(i)].value
    time.sleep(1)

    driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/button[3]").click()
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div/form/button[2]')))
   
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@type=\'text\']").click()
    time.sleep(2)
    #driver.find_element(By.XPATH, "//div[2]/div/div/div/div/input").click()
    #driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div/div/div/div/input").click()
    driver.find_element(By.XPATH, "//div[10]/div/div/div/ul/li[9]").click()
    
   
    try:

        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div/div/div/div/input").send_keys(NoInduk)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".el-select-dropdown__item:nth-child(1) tr:nth-child(2) > .el-descriptions__cell:nth-child(1)").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div[1]/div/form/button[1]").click()
        
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]')))
        driver.find_element(By.CSS_SELECTOR, ".el-dialog__close > svg").click()
# input sesuai excell
        driver.find_element(By.CSS_SELECTOR, ".el-col-lg-12 > .is-required:nth-child(1) .el-input__inner").send_keys(noregis)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[1]/div[2]/div/div/input").send_keys(TglSuratPenahanan)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[1]/div[2]/div/div/input").send_keys(Keys.ENTER)
        time.sleep(1)
        #driver.find_element(By.CSS_SELECTOR, ".el-col-lg-12 > .is-required:nth-child(1) .el-input__inner").send_keys(TglSuratPenahanan)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[1]/div[3]/div/div/input").send_keys(NomorSuratPenahanan)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[1]/div[4]/div/div/input").send_keys(NamaPetugasInstansi)
        time.sleep(1)


        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[1]/div[5]/div/div/div/div/input").send_keys(Kejaksaan)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[1]/div[5]/div/div/div/div/input").send_keys(Keys.DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[1]/div[5]/div/div/div/div/input").send_keys(Keys.ENTER)
        time.sleep(1)


        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[1]/div[6]/div/div/input").send_keys(AsalInstansi)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[1]/div[7]/div/div/textarea").send_keys(Keterangan)

        #xxxxxxxxxxxxxxxxxxxxxxxxxxx
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[1]/div[8]/div/div/div/div/input").send_keys(Penyidik)
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="el-popper-container-5040"]/div[7]')))
        
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[1]/div[8]/div/div/div/div/input").send_keys(Keys.DOWN)
        
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[1]/div[8]/div/div/div/div/input").send_keys(Keys.ENTER)
        time.sleep(3)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxx
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[2]/div[1]/div/div/input").send_keys(menahan10)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[2]/div[1]/div/div/input").send_keys(Keys.DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[2]/div[1]/div/div/input").send_keys(Keys.ENTER)
        time.sleep(1)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxx
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[2]/div[2]/div/div/input").send_keys(menahan3)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[2]/div[2]/div/div/input").send_keys(Keys.DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[2]/div[2]/div/div/input").send_keys(Keys.ENTER)
        time.sleep(1)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxx
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[2]/div[3]/div/div/input").send_keys(menahan1)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[2]/div[3]/div/div/input").send_keys(Keys.DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[2]/div[3]/div/div/input").send_keys(Keys.ENTER)
        time.sleep(1)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxx
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div[3]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/textarea").send_keys(LokasiDokumen)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxx
        driver.find_element(By.XPATH, "").send_keys(LokasiDokumen)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxx
        driver.find_element(By.XPATH, "").send_keys(LokasiDokumen)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxx
        driver.find_element(By.XPATH, "").send_keys(LokasiDokumen)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxx
        driver.find_element(By.XPATH, "").send_keys(LokasiDokumen)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxx
        driver.find_element(By.XPATH, "").send_keys(LokasiDokumen)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxx
        driver.find_element(By.XPATH, "").send_keys(LokasiDokumen)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxx
        driver.find_element(By.XPATH, "").send_keys(LokasiDokumen)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxx
        driver.find_element(By.XPATH, "").send_keys(LokasiDokumen)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxx
        driver.find_element(By.XPATH, "").send_keys(LokasiDokumen)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxx
        driver.find_element(By.XPATH, "").send_keys(LokasiDokumen)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxx


    except TimeoutException:
        print("ga muncul")
        pass
    time.sleep(5)
    i = i + 1
print("done")



    
