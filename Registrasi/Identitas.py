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
from selenium.webdriver.common.keys import Keys
import time 
from openpyxl import load_workbook
import pyautogui


#target halaman excel ada dimana , wb = variablenya
# wb = load_workbook(filename="C:\chromedriver\Data.xlsx")
wb = load_workbook(filename=r"C:\Users\user\Documents\TRCH\Automationpython\Filexel\Registrasi.xlsx")

# jadi ini bisa read sheet yang dibawah itu yang di excel
sheetrange = wb['Identitas']

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
time.sleep(3)

#Registrasi
element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/nav/ul/li[1]/div")                                   
actions = ActionChains(driver)
actions.move_to_element(element).perform()
time.sleep(3)

#Identitas
driver.find_element(By.LINK_TEXT, "Daftar Identitas").click()
time.sleep(3)

i = 2 

while i <= len(sheetrange['A']):
    # deklarasi per colom pada sheet
    #--------------------------------------------------------------
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
    Tanggal_lahir           = sheetrange['M'+str(i)].value
    Jenis_kelamin           = sheetrange['N'+str(i)].value
    Negara                  = sheetrange['O'+str(i)].value
    Agama                   = sheetrange['P'+str(i)].value
    suku                    = sheetrange['Q'+str(i)].value
    Status_perkawinan       = sheetrange['R'+str(i)].value
    Provinsi                = sheetrange['S'+str(i)].value
    Kota                    = sheetrange['T'+str(i)].value
    Alamat_rumah            = sheetrange['U'+str(i)].value
    Telepon                 = sheetrange['V'+str(i)].value
    Kode_pos                = sheetrange['W'+str(i)].value
    Alamat_lain             = sheetrange['X'+str(i)].value
    #--------------------------------------------------------------
    # Jenis_Pekerjaan         = sheetrange['Y'+str(i)].value
    # Bekerjadi               = sheetrange['Z'+str(i)].value
    # Keterangan_pekerjaan    = sheetrange['AA'+str(i)].value
    # Tingkat_penghasilan     = sheetrange['AB'+str(i)].value
    # Tingkat_pendidikan      = sheetrange['AC'+str(i)].value
    # Keahlian1               = sheetrange['AD'+str(i)].value
    # Level_keahlian1         = sheetrange['AE'+str(i)].value
    # Keahlian2               = sheetrange['AF'+str(i)].value
    # Levelkeahlian2          = sheetrange['AG'+str(i)].value
    # Minat                   = sheetrange['AH'+str(i)].value
    # #--------------------------------------------------------------
    # Nama_ayah               = sheetrange['AI'+str(i)].value
    # Alamat_ayah             = sheetrange['AJ'+str(i)].value
    # Nama_ibu                = sheetrange['AK'+str(i)].value
    # Alamat_ibu              = sheetrange['AL'+str(i)].value
    #--------------------------------------------------------------
    # Tinggi_badan            = sheetrange['AM'+str(i)].value
    # Berat_badan             = sheetrange['AN'+str(i)].value
    # Bentuk_rambut           = sheetrange['AO'+str(i)].value
    # Warna_rambut            = sheetrange['AP'+str(i)].value
    # Bentuk_bibir            = sheetrange['AQ'+str(i)].value
    # Berkacamata             = sheetrange['AR'+str(i)].value
    # Bentuk_mata             = sheetrange['AS'+str(i)].value
    # Warna_mata              = sheetrange['AT'+str(i)].value
    # Hidung                  = sheetrange['AU'+str(i)].value
    # Raut_muka               = sheetrange['AV'+str(i)].value
    # Telinga                 = sheetrange['AW'+str(i)].value
    # Mulut                   = sheetrange['AX'+str(i)].value
    # Lengan                  = sheetrange['AY'+str(i)].value
    # Tangan                  = sheetrange['AZ'+str(i)].value
    # Kaki                    = sheetrange['BA'+str(i)].value
    # Warna_kulit             = sheetrange['BB'+str(i)].value
    # Cacat_tubuh             = sheetrange['BC'+str(i)].value
    # Catatancirikhusus1      = sheetrange['BD'+str(i)].value
    # Catatancirikhusus2      = sheetrange['BE'+str(i)].value
    # Catatancirikhusus3      = sheetrange['BF'+str(i)].value
    #--------------------------------------------------------------
    # Nopaspor                = sheetrange['BG'+str(i)].value
    # Rumus                   = sheetrange['BH'+str(i)].value
    # Nodaktolskopi           = sheetrange['BI'+str(i)].value
    # Pengambilansidikjari    = sheetrange['BJ'+str(i)].value
    # Tanggalpengambilan      = sheetrange['BK'+str(i)].value

    time.sleep(5)
    #button +Tambah
    driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/div[1]/button").click()                                 

    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div/h1')))
        #======================================================================
        #========================Input Tab Biodata ============================
        #--------------------------------------------------------------
        # driver.find_element(By.ID, "btn_residivis").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_residivis").send_keys(Residivis)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_residivis").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_residivis").send_keys(Keys.ENTER)
        driver.find_element(By.ID, "btn_residivis").click()
        time.sleep(2)
        pyautogui.typewrite(Residivis)
        time.sleep(2)
        pyautogui.keyDown('enter') 
        
        
        # #--------------------------------------------------------------        
        # time.sleep(3)                              
        # driver.find_element(By.ID, "btn_nama_lengkap").send_keys(Nama_Lengkap)
        # #----------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_nama_alias1").send_keys(Nama_Alias1)
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_nama_alias2").send_keys(Nama_Alias2)
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_nama_alias3").send_keys(Nama_Alias3)
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_nama_kecil1").send_keys(Nama_Kecil1)
        # #---------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_nama_kecil2").send_keys(Nama_Kecil2)
        # #----------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_nama_kecil3").send_keys(Nama_Kecil3)
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "btn_id_jenis_warganegara").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_warganegara").send_keys(Kewarganegaraan) 
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_warganegara").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_warganegara").send_keys(Keys.ENTER) 
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_nik").send_keys(nik) 
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "btn_id_tempat_asal").click()                                    
        # time.sleep(3)                                
        # driver.find_element(By.ID, "btn_id_tempat_asal").send_keys(Tempat_Asal)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_tempat_asal").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_tempat_asal").send_keys(Keys.ENTER) 
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "btn_id_tempat_lahir").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "btn_id_tempat_lahir").send_keys(Tempat_lahir)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_tempat_lahir").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_tempat_lahir").send_keys(Keys.ENTER)
        # #----------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.XPATH, "//div[5]/div/div/div/div/div/input").click()
        # time.sleep(3)
        # driver.find_element(By.XPATH, "//div[5]/div/div/div/div/div/input").send_keys(Tanggal_lahir) 
        # time.sleep(3)
        # driver.find_element(By.XPATH, "//div[5]/div/div/div/div/div/input").send_keys(Keys.ENTER)  
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_kelamin").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "btn_id_jenis_kelamin").send_keys(Jenis_kelamin)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_kelamin").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_kelamin").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_negara_asing").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "btn_id_negara_asing").send_keys(Negara)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_negara_asing").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_negara_asing").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_agama").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "btn_id_jenis_agama").send_keys(Agama)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_agama").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_agama").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_suku").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "btn_id_jenis_suku").send_keys(suku)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_suku").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_suku").send_keys(Keys.ENTER)
        # #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_status_perkawinan").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "btn_id_jenis_status_perkawinan").send_keys(Status_perkawinan)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_status_perkawinan").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_status_perkawinan").send_keys(Keys.ENTER)
        
        # #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_propinsi").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "btn_id_propinsi").send_keys(Provinsi)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_propinsi").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_propinsi").send_keys(Keys.ENTER)
        # #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_kota").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "btn_id_kota").send_keys(Kota)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_kota").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_kota").send_keys(Keys.ENTER)
        # #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_alamat").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "btn_alamat").send_keys(Alamat_rumah)
        # #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_telepon").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "btn_telepon").send_keys(Telepon)
        # #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_kodepos").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "btn_kodepos").send_keys(Kode_pos)
        # #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_alamat_alternatif").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "btn_alamat_alternatif").send_keys(Alamat_lain)
        # time.sleep(3)
        # #======================================================================
        # driver.find_element(By.ID, "tab-2").click()
        # #========================Input Tab Pekerjaan===========================
        # #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_pekerjaan").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "id_jenis_pekerjaan").send_keys(Jenis_Pekerjaan)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_pekerjaan").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_pekerjaan").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "alamat_pekerjaan").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "alamat_pekerjaan").send_keys(Bekerjadi)
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "keterangan_pekerjaan").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "keterangan_pekerjaan").send_keys(Keterangan_pekerjaan)
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "id_tingkat_penghasilan").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "id_tingkat_penghasilan").send_keys(Tingkat_penghasilan)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_tingkat_penghasilan").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_tingkat_penghasilan").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_pendidikan").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "id_jenis_pendidikan").send_keys(Tingkat_pendidikan)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_pendidikan").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_pendidikan").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_keahlian_1").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "id_jenis_keahlian_1").send_keys(Keahlian1)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_keahlian_1").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_keahlian_1").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_level_1").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "id_jenis_level_1").send_keys(Level_keahlian1)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_level_1").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_level_1").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_keahlian_2").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "id_jenis_keahlian_2").send_keys(Levelkeahlian2)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_keahlian_2").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_keahlian_2").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "minat").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "minat").send_keys(Minat)
        # time.sleep(3)
        # #======================================================================
        # driver.find_element(By.ID, "tab-3").click()
        # #========================Input Tab Keluarga============================ 
        # #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "nm_ayah").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "nm_ayah").send_keys(Nama_ayah)
        # #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "nm_ayah").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "nm_ayah").send_keys(Alamat_ayah)
        # #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "nm_ayah").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "nm_ayah").send_keys(Nama_ibu)
        # #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "nm_ayah").click()
        # time.sleep(3)        
        # driver.find_element(By.ID, "nm_ayah").send_keys(Alamat_ibu)
        # #======================================================================
        # driver.find_element(By.ID, "tab-4").click()
        # #========================Input Tab Data Fisik========================== 
        # #------------------------------------------------------------------------------
        # driver.find_element(By.ID, "tinggi").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "tinggi").send_keys(Tinggi_badan) 
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "berat").click()        
        # time.sleep(3)
        # # driver.find_element(By.ID, "berat").clear_field() 
        # # time.sleep(3)
        # driver.find_element(By.ID, "berat").send_keys(Berat_badan) 
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "id_bentukrambut").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "id_bentukrambut").send_keys(Bentuk_rambut) 
        # time.sleep(3)
        # driver.find_element(By.ID, "id_bentukrambut").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_bentukrambut").send_keys(Keys.ENTER) 
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "id_jenis_rambut").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_rambut").send_keys(Warna_rambut) 
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_rambut").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_rambut").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "id_bentukbibir").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "id_bentukbibir").send_keys(Bentuk_bibir) 
        # time.sleep(3)
        # driver.find_element(By.ID, "id_bentukbibir").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_bentukbibir").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "id_kacamata").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "id_kacamata").send_keys(Berkacamata) 
        # time.sleep(3)
        # driver.find_element(By.ID, "id_kacamata").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_kacamata").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "id_bentuk_mata").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "id_bentuk_mata").send_keys(Bentuk_mata) 
        # time.sleep(3)
        # driver.find_element(By.ID, "id_bentuk_mata").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_bentuk_mata").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "id_warna_mata").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "id_warna_mata").send_keys(Warna_mata) 
        # time.sleep(3)
        # driver.find_element(By.ID, "id_warna_mata").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_warna_mata").send_keys(Keys.ENTER) 
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "id_jenis_hidung").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_hidung").send_keys(Hidung) 
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_hidung").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_hidung").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "id_jenis_muka").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_muka").send_keys(Raut_muka) 
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_muka").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_muka").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "id_telinga").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "id_telinga").send_keys(Telinga) 
        # time.sleep(3)
        # driver.find_element(By.ID, "id_telinga").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_telinga").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "id_jenis_mulut").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_mulut").send_keys(Mulut) 
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_mulut").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_mulut").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "id_lengan").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "id_lengan").send_keys(Lengan) 
        # time.sleep(3)
        # driver.find_element(By.ID, "id_lengan").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_lengan").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "id_jenis_kaki").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_kaki").send_keys(Kaki) 
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_kaki").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_jenis_kaki").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "id_warnakulit").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "id_warnakulit").send_keys(Warna_kulit) 
        # time.sleep(3)
        # driver.find_element(By.ID, "id_warnakulit").send_keys(Keys.DOWN)
        # time.sleep(3)
        # driver.find_element(By.ID, "id_warnakulit").send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "cacat").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "cacat").send_keys(Cacat_tubuh)
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "ciri").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "ciri").send_keys(Catatancirikhusus1)  
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "ciri2").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "ciri2").send_keys(Catatancirikhusus2) 
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "ciri3").click()
        # time.sleep(3)
        # driver.find_element(By.ID, "ciri3").send_keys(Catatancirikhusus3) 
        #Submit
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div/div/form/div[4]/div/template/button[2]").click()
        
    except TimeoutException:
        # print("d")
        pass
    time.sleep(5)   
    i = i + 1
print ("Success Created")