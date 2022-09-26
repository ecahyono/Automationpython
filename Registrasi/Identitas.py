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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

import time 
from openpyxl import load_workbook
import pyautogui



#target halaman excel ada dimana , wb = variablenya
# wb = load_workbook(filename="C:\chromedriver\Data.xlsx")
wb = load_workbook(filename=r"C:\Users\user\Documents\TRCH\Automationpython\Filexel\Registrasi.xlsx")
# jadi ini bisa read sheet yang dibawah itu yang di excel
sheetrange = wb['Identitas']

#permition of camera and mic
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,     # 1:allow, 2:block 
    "profile.default_content_setting_values.media_stream_camera": 1,  # 1:allow, 2:block 
    "profile.default_content_setting_values.geolocation": 1,          # 1:allow, 2:block 
    "profile.default_content_setting_values.notifications": 1         # 1:allow, 2:block 
    })

driver = webdriver.Chrome(chrome_options=options)  


# ini web driver disimpen dimana, kalo disimpen di path kosongin aja
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\user\Documents\TRCH\chromedriver.exe')
# driver = webdriver.Chrome(executable_path=r'C:\Users\user\Documents\TRCH\chromedriver.exe')

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
time.sleep(1)

#Identitas
driver.find_element(By.LINK_TEXT, "Daftar Identitas").click()
time.sleep(1)

i = 2 

while i <= len(sheetrange['A']):
    # deklarasi per colom pada sheet
    # #--------------------------------------------------------------
    # Residivis               = sheetrange['A'+str(i)].value
    # Nama_Lengkap            = sheetrange['B'+str(i)].value
    # Nama_Alias1             = sheetrange['C'+str(i)].value
    # Nama_Alias2             = sheetrange['D'+str(i)].value
    # Nama_Alias3             = sheetrange['E'+str(i)].value
    # Nama_Kecil1             = sheetrange['F'+str(i)].value
    # Nama_Kecil2             = sheetrange['G'+str(i)].value
    # Nama_Kecil3               = sheetrange['H'+str(i)].value
    # chcktab1                = sheetrange['BN'+str(i)].value
    # Kewarganegaraan         = sheetrange['I'+str(i)].value
    # nik                     = sheetrange['J'+str(i)].value
    # Tempat_Asal             = sheetrange['K'+str(i)].value
    # Tempat_lahir            = sheetrange['L'+str(i)].value
    # Tanggal_lahir           = sheetrange['M'+str(i)].value
    # Jenis_kelamin           = sheetrange['N'+str(i)].value
    # Negara                  = sheetrange['O'+str(i)].value
    # Agama                   = sheetrange['P'+str(i)].value
    # suku                    = sheetrange['Q'+str(i)].value
    # Status_perkawinan       = sheetrange['R'+str(i)].value
    # Provinsi                = sheetrange['S'+str(i)].value
    # Kota                    = sheetrange['T'+str(i)].value
    # Alamat_rumah            = sheetrange['U'+str(i)].value
    # Telepon                 = sheetrange['V'+str(i)].value
    # Kode_pos                = sheetrange['W'+str(i)].value
    # Alamat_lain             = sheetrange['X'+str(i)].value

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
    # chcktab2                = sheetrange['BL'+str(i)].value
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

    time.sleep(3)
    #button +Tambah
    driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/div[1]/button").click()                                 

    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div/h1')))
        #======================================================================
        # driver.find_element(By.ID, "tab-1").click()
        #========================Input Tab Biodata ============================
        #--------------------------------------------------------------
        # driver.find_element(By.ID, "btn_residivis").click()
        # time.sleep(2)
        # pyautogui.typewrite(Residivis)
        # pyautogui.keyDown('down')
        # pyautogui.press('enter')
        #--------------------------------------------------------------        
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
        # cekbocktab1 = driver.find_element(By.ID, "btn_is_pengaruh_terhadap_masyarakat").click()
        # if chcktab1 == True :
        #     driver.find_element(By.ID, "btn_is_pengaruh_terhadap_masyarakat").click()
        #     print ("uncheckh")
        # else: 
        #     print ("Masih default")

        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "btn_id_jenis_warganegara").click()
        # time.sleep(3)
        # pyautogui.typewrite(Kewarganegaraan)
        # time.sleep(2)
        # pyautogui.keyDown('down')
        # pyautogui.press('enter')
        # # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_nik").send_keys(nik) 
        # #--------------------------------------------------------------                                
        # driver.find_element(By.XPATH, "//*[@id=\"pane-1\"]/form/div[1]/div[2]/div[3]/div/div").click()   
        # time.sleep(2)
        # pyautogui.typewrite(Tempat_Asal)
        # pyautogui.keyDown('down')
        # pyautogui.press('enter')
        # #--------------------------------------------------------------
        # driver.find_element(By.XPATH, "//*[@id=\"pane-1\"]/form/div[1]/div[2]/div[4]/div/div").click()          
        # time.sleep(2)
        # pyautogui.typewrite(Tempat_lahir)
        # pyautogui.keyDown('down')
        # pyautogui.press('enter')
        # #----------------------------------------------------------------
        # driver.find_element(By.XPATH, "//div[5]/div/div/div/div/div/input").click()
        # time.sleep(2)
        # pyautogui.typewrite(Tanggal_lahir)
        # pyautogui.press('enter') 
        # # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_kelamin").click()
        # time.sleep(2)
        # pyautogui.typewrite(Jenis_kelamin)
        # pyautogui.keyDown('down')
        # pyautogui.press('enter')
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_negara_asing").click()
        # time.sleep(2)
        # pyautogui.typewrite(Negara)
        # pyautogui.keyDown('down')
        # pyautogui.press('enter')
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_agama").click()
        # time.sleep(2)
        # pyautogui.typewrite(Agama)
        # pyautogui.keyDown('down')
        # pyautogui.press('enter')
        # #--------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_suku").click()
        # time.sleep(2)
        # pyautogui.typewrite(suku)
        # pyautogui.keyDown('down')
        # pyautogui.press('enter')
        # #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_jenis_status_perkawinan").click()
        # time.sleep(2)
        # pyautogui.typewrite(Status_perkawinan)
        # pyautogui.keyDown('down')
        # pyautogui.press('enter')
        # #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_propinsi").click()
        # time.sleep(2)
        # pyautogui.typewrite(Provinsi)
        # pyautogui.keyDown('down')
        # pyautogui.press('enter')
        # #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_id_kota").click()
        # time.sleep(2)
        # pyautogui.typewrite(Kota)
        # pyautogui.keyDown('down')
        # pyautogui.press('enter')
        # #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_alamat").click()
        # time.sleep(3)        
        # pyautogui.typewrite(Alamat_rumah)
        # #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_telepon").click()
        # time.sleep(2)
        # pyautogui.typewrite(Telepon)
        # #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_kodepos").click()
        # time.sleep(2)
        # pyautogui.typewrite(Kode_pos)
        #------------------------------------------------------------------------------
        # time.sleep(3)
        # driver.find_element(By.ID, "btn_alamat_alternatif").click()
        # time.sleep(2)
        # pyautogui.typewrite(Alamat_lain)

        # if chck == True:
        #     driver.find_element(By.ID, "btn_is_pengaruh_terhadap_masyarakat").click()
        # elif chck == False :
        #     driver.find_element(By.ID, "btn_is_pengaruh_terhadap_masyarakat").click()
        
        #======================================================================
        # driver.find_element(By.ID, "tab-2").click()
        #========================Input Tab Pekerjaan===========================
        #------------------------------------------------------------------------------
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
        # if chcktab2 == 'ya' :
        #     driver.find_element(By.XPATH, "//*[@id=\"is_baca_quran\"]/span[1]/span").click()
        #     print (chcktab2)
        # elif chcktab2 == 'Tidak':
        #     print ("tidak di check")
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
        # pyautogui.hotkey("backspace")
        # time.sleep(2)
        # driver.find_element(By.XPATH, "//*[@id=\"tinggi\"]/div/input" ).send_keys(Tinggi_badan) 
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "berat").click()
        # pyautogui.hotkey("backspace")
        # time.sleep(2)
        # driver.find_element(By.ID, "//*[@id=\"berat\"]/div/input").send_keys(Berat_badan) 
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
        #======================================================================
        # driver.find_element(By.ID, "tab-5").click()
        #========================Input Tab Sidik Jari========================== 
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "no_paspor").click()
        # driver.find_element(By.ID, "no_paspor").send_keys(Nopaspor)
        # # #--------------------------------------------------------------
        # driver.find_element(By.ID, "rumus_daktil").click()
        # driver.find_element(By.ID, "rumus_daktil").send_keys(Rumus)
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "nomor_daktil").click()
        # driver.find_element(By.ID, "nomor_daktil").send_keys(Nopaspor)
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, "pengambil_sj").click()
        # driver.find_element(By.ID, "pengambil_sj").send_keys(Pengambilansidikjari)
        # #--------------------------------------------------------------
        # time.sleep(1)
        # driver.find_element(By.XPATH, "//*[@id=\"pane-5\"]/div/form/div/div[2]/div[2]/div/div/input").click()
        # driver.find_element(By.XPATH, "//*[@id=\"pane-5\"]/div/form/div/div[2]/div[2]/div/div/input").send_keys(Tanggalpengambilan)
        #======================================================================
        driver.find_element(By.ID, "tab-6").click()
        #========================Input Tab Foto========================== 
        #--------------------------------------------------------------
        driver.find_element(By.XPATH, "//*[@id=\"pane-6\"]/form/div/div[1]/div/div/div/button[1]").click()


        # desired_cap = {
        #     'version': 'latest',
        #     'platform': 'WIN10',
        #     'browserName': 'chrome',

        #     'chromeOptions': {
        #         'args': ["--use-fake-device-for-media-stream", "--use-fake-ui-for-media-stream"]
        #     }
        # }
        # driver = webdriver.Remote(command_executor='https://API_KEY:API_SECRET@hub.testingbot.com/wd/hub', desired_capabilities=desired_cap)
        # time.sleep(2)
        # driver.find_element(By.XPATH, "//*[@id=\"pane-6\"]/form/div/div[1]/div/div/div/button[1]").click()
        # chrome_opt.add_argument("use-fake-ui-for-media-stream")
        # driver.find_element(By.XPATH, "//div[6]/form/div/div[1]/div/div/div/div/div[1]/button").click()
        # driver.find_element(By.XPATH, "//div[6]/form/div/div[1]/div/div/div/div/div[1]/button").send_keys(r"C:\Users\user\Pictures\Screenshots\lim.jpg")
        # //*[@id="pane-6"]/form/div/div[1]/div/div/div/button[1]   


        #Submit
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div/div/form/div[4]/div/template/button[2]").click()
        
    except TimeoutException:
        # print("d")
        pass
    time.sleep(5)   
    i = i + 1
print ("Success Created")