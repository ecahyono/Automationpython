from turtle import rt
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import pytest
from openpyxl import load_workbook
import time

@pytest.fixture()
def test_setup():
    global driver
    
    s = Service('/Users/will/Downloads/chromedriver')
    driver = webdriver.Chrome(service=s)
    url = "http://kumbang.torche.id:32400/"
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    #driver.close()
    #driver.quit()
def test_negara(test_setup):
    
    wb = load_workbook(filename=r"/Users/will/Documents/Automationpython/Filexel/Registrasi.xlsx")

    sheetrange = wb['reg']
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//div/span')))
        
    driver.find_element(By.XPATH, "//div/span").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    # masukin input username
    driver.find_element(By.ID, "username").send_keys("rono")
    # masukin input password
    driver.find_element(By.ID, "password").send_keys("rene")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    time.sleep(1)
    element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/nav/ul/li[1]/div")
    time.sleep(1)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    element2 = driver.find_element(By.XPATH, "//div/ul/li[2]/div")
    time.sleep(2)
    actions2 = ActionChains(driver)
    actions2.move_to_element(element2).perform()
    driver.find_element(By.LINK_TEXT, "Registrasi Tahanan/ Narapidana").click()
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/h1")))
       
    i = 2

    # nge baca mulai dari tabel A
    while i <= len(sheetrange['A']):
        # deklarasi bahwa NIP itu ada di A 
        NoInduk = sheetrange['A'+str(i)].value
        noregis = sheetrange['B'+str(i)].value
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

        #======================== Halaman Index ============================
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/button[3]/i").click()
        #WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div[1]/div/div/div/h1")))
        time.sleep(2)
        
        try:      
            #======================== Halaman Cari ============================
            
            driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input__inner").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//li[contains(.,\'B I\')]").click()
            driver.find_element(By.XPATH, "(//input[@type=\'text\'])[2]").click()
            driver.find_element(By.XPATH, "(//input[@type=\'text\'])[2]").send_keys(NoInduk)
            driver.find_element(By.CSS_SELECTOR, ".el-select-dropdown__item:nth-child(1) tr:nth-child(2) > .el-descriptions__cell:nth-child(1)").click()
            #======================== Button Cari ============================
            driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div[1]/div/form/button[1]").click()
            #======================== masuk ke halaman input ============================
            """
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]')))
            driver.find_element(By.CSS_SELECTOR, ".el-dialog__close > svg").click()

        

            
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
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]')))
            driver.find_element(By.CSS_SELECTOR, ".el-dialog__close > svg").click()
            """

        except TimeoutException:
            print("MASIH ADA ERROR, CEK LAGI PAK WIL")
            pass
        time.sleep(5)
        i = i + 1
    print("DONE PAK WILDAN, SEBATS DULU")

