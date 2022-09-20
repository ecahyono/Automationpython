# import imp
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


from openpyxl import load_workbook
import time

#target halaman excel ada dimana , wb = variablenya
# wb = load_workbook(filename="C:\chromedriver\Data.xlsx")
wb = load_workbook(filename=r"C:\Users\user\Documents\TRCH\Automationpython\Filexel\lainlain.xlsx")

# jadi ini bisa read sheet yang dibawah itu yang di excel
sheetrange = wb['Harilibur']

# ini web driver disimpen dimana, kalo disimpen di path kosongin aja
driver = webdriver.Chrome(r'C:\Users\user\Documents\TRCH\chromedriver.exe')

# link nya ini dimana
driver.get("http://kumbang.torche.id:32400/")
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
time.sleep(5)

# variable element nyari dimana letak menu lain lain
element = driver.find_element(By.XPATH, "//div[@id=\"app\"]/div/nav/ul/li/div")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.LINK_TEXT, "Daftar Identitas").click()

i = 2 

while i <= len(sheetrange['A']):
    # deklarasi per colom pada sheet
    Residivis               = sheetrange['A'+str(i)].value
    Nama_Lengkap            = sheetrange['B'+str(i)].value
    Nama_Alias1             = sheetrange['C'+str(i)].value
    Nama_Alias2             = sheetrange['D'+str(i)].value
    Nama_Alias3             = sheetrange['E'+str(i)].value
    Nama_Kecil1             = sheetrange['F'+str(i)].value
    Nama_Kecil2             = sheetrange['G'+str(i)].value
    Nama_Kecil3             = sheetrange['H'+str(i)].value
    Kewarganegaraan         = sheetrange['I'+str(i)].value
    nik                     = sheetrange['J'+str(i)].value
    Tempat_Asal             = sheetrange['K'+str(i)].value
    Tempat_lahir            = sheetrange['L'+str(i)].value
    Jenis_kelamin           = sheetrange['M'+str(i)].value
    Negara                  = sheetrange['N'+str(i)].value
    Agama                   = sheetrange['O'+str(i)].value
    suku                    = sheetrange['P'+str(i)].value
    Status_perkawinan       = sheetrange['Q'+str(i)].value
    Provinsi                = sheetrange['R'+str(i)].value
    Kota                    = sheetrange['S'+str(i)].value
    Alamat_rumah            = sheetrange['T'+str(i)].value
    Telepon                 = sheetrange['U'+str(i)].value
    Kode_pos                = sheetrange['V'+str(i)].value
    Alamat_lain             = sheetrange['W'+str(i)].value
    Jenis_Pekerjaan         = sheetrange['X'+str(i)].value
    Bekerjadi               = sheetrange['Y'+str(i)].value
    Keterangan_pekerjaan    = sheetrange['Z'+str(i)].value
    Tingkat_penghasilan     = sheetrange['AA'+str(i)].value
    Keahlian1               = sheetrange['AB'+str(i)].value
    Level_keahlian1         = sheetrange['AC'+str(i)].value
    Keahlian2               = sheetrange['AD'+str(i)].value
    Levelkeahlian2          = sheetrange['AE'+str(i)].value
    Minat                   = sheetrange['AF'+str(i)].value
    Nama_ayah               = sheetrange['AG'+str(i)].value
    Alamat_ayah             = sheetrange['AH'+str(i)].value
    Nama_ibu                = sheetrange['AI'+str(i)].value
    Alamat_ibu              = sheetrange['AJ'+str(i)].value
    Tinggi_badan            = sheetrange['AK'+str(i)].value
    Berat_badan             = sheetrange['AL'+str(i)].value
    Bentuk_rambut           = sheetrange['AM'+str(i)].value
    Warna_rambut            = sheetrange['AN'+str(i)].value
    Bentuk_bibir            = sheetrange['AO'+str(i)].value
    Berkacamata             = sheetrange['AP'+str(i)].value
    Bentuk_mata             = sheetrange['AQ'+str(i)].value
    Warna_mata              = sheetrange['AR'+str(i)].value
    Hidung                  = sheetrange['AS'+str(i)].value
    Raut_muka               = sheetrange['AT'+str(i)].value
    Telinga                 = sheetrange['AU'+str(i)].value
    Mulut                   = sheetrange['AV'+str(i)].value
    Lengan                  = sheetrange['AW'+str(i)].value
    Tangan                  = sheetrange['AX'+str(i)].value
    Kaki                    = sheetrange['AY'+str(i)].value
    Warna_kulit             = sheetrange['AZ'+str(i)].value
    Cacat_tubuh             = sheetrange['BA'+str(i)].value
    Catatancirikhusus1      = sheetrange['BB'+str(i)].value
    Catatancirikhusus2      = sheetrange['BC'+str(i)].value
    Catatancirikhusus3      = sheetrange['BD'+str(i)].value
    Nopaspor                = sheetrange['BE'+str(i)].value
    Rumus                   = sheetrange['BF'+str(i)].value
    Nodaktolskopi           = sheetrange['BG'+str(i)].value
    Pengambilansidikjari    = sheetrange['BH'+str(i)].value
    Tanggalpengambilan      = sheetrange['BI'+str(i)].value

    time.sleep(4)
    #button +Tambah
    driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/div[1]/button").click()
                                  

    try:
        # WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div/h1')))
        #Input
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/input").send_keys(Tanggal)                                     
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[2]/div/div[1]/input").send_keys(Nama)                                      
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/input").send_keys(Tanggal)                                     
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[2]/div/div[1]/input").send_keys(Nama)                                      
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)        
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/input").send_keys(Tanggal)                                     
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[2]/div/div[1]/input").send_keys(Nama)                                      
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/input").send_keys(Tanggal)                                     
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[2]/div/div[1]/input").send_keys(Nama)                                      
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)        
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/input").send_keys(Tanggal)                                     
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[2]/div/div[1]/input").send_keys(Nama)                                      
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/input").send_keys(Tanggal)                                     
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[2]/div/div[1]/input").send_keys(Nama)                                      
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/input").send_keys(Tanggal)                                     
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[2]/div/div[1]/input").send_keys(Nama)                                      
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)
        time.sleep(2)                                
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/textarea").send_keys(Keterangan)







        #Submit
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div/div/form/div[4]/div/template/button[2]").click()
                            
    except TimeoutException:
        # print("d")
        pass
    time.sleep(5)   
    i = i + 1
print ("Success Created")