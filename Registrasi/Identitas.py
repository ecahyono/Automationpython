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
import os
import pyautogui
import pytest
import time
import autoit 

@pytest.fixture()
def test_setup():
    global driver
    s = Service(r'C:\Users\user\Documents\TRCH\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    url = "http://kumbang.torche.id:32400/"
    # url = "http://192.168.2.11:32400/"

    #url = "http://192.168.2.11:32400/"

    driver.get(url)
    # seting windows nya jadi max   
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield
    driver.close()
    driver.quit()
    

def test_Web(test_setup):

    wb = load_workbook(filename=r"C:\Users\user\Documents\TRCH\Automationpython\Filexel\Registrasi.xlsx")
    # jadi ini bisa read sheet yang dibawah itu yang di excel
    sheetrange = wb['Identitas']

    # Menuju login
    driver.find_element(By.XPATH, "//div/span").click()
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("rono")
    driver.find_element(By.ID, "password").send_keys("rene")
    # click button login
    driver.find_element(By.ID, "kc-login").click()

    time.sleep(3)
    #Registrasi
    element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/nav/ul/li[1]/div")                                   
    time.sleep(1)
    actions = ActionChains(driver)
    time.sleep(1)
    actions.move_to_element(element).perform()
    time.sleep(1)
    #Identitas
    driver.find_element(By.LINK_TEXT, "Daftar Identitas").click()
    time.sleep(1)

    i = 3 
    while i <= len(sheetrange['A']):
        # deklarasi per colom pada sheet
        # #--------------------------------------------------------------
        # #Tab Biodata---------------------------------------------------
        # #--------------------------------------------------------------
        # Residivis               = sheetrange['A'+str(i)].value
        # Rke                     = sheetrange['B'+str(i)].value
        # Nama_Lengkap            = sheetrange['C'+str(i)].value
        # Nama_Alias1             = sheetrange['D'+str(i)].value
        # Nama_Alias2             = sheetrange['E'+str(i)].value
        # Nama_Alias3             = sheetrange['F'+str(i)].value
        # Nama_Kecil1             = sheetrange['G'+str(i)].value
        # Nama_Kecil2             = sheetrange['H'+str(i)].value
        # Nama_Kecil3             = sheetrange['I'+str(i)].value
        # chcktab1                = sheetrange['J'+str(i)].value
        # chcktab2                = sheetrange['K'+str(i)].value
        # Kewarganegaraan         = sheetrange['L'+str(i)].value
        # nik                     = sheetrange['M'+str(i)].value
        # Tempat_Asal             = sheetrange['N'+str(i)].value
        # Tempat_lahir            = sheetrange['O'+str(i)].value
        # Tanggal_lahir           = sheetrange['P'+str(i)].value
        # Jenis_kelamin           = sheetrange['Q'+str(i)].value
        # Negara                  = sheetrange['R'+str(i)].value
        # Agama                   = sheetrange['S'+str(i)].value
        # Agama_lain              = sheetrange['T'+str(i)].value
        # suku                    = sheetrange['U'+str(i)].value
        # Status_perkawinan       = sheetrange['F'+str(i)].value
        # Provinsi                = sheetrange['W'+str(i)].value
        # Kota                    = sheetrange['X'+str(i)].value
        # Alamat_rumah            = sheetrange['Y'+str(i)].value
        # Telepon                 = sheetrange['Z'+str(i)].value
        # Kode_pos                = sheetrange['AA'+str(i)].value
        # Alamat_lain             = sheetrange['AB'+str(i)].value
        #--------------------------------------------------------------
        # #Tab Pekerjaan------------------------------------------------
        # #--------------------------------------------------------------
        # Jenis_Pekerjaan         = sheetrange[''+str(i)].value
        # namaipemerintah         = sheetrange[''+str(i)].value
        # noindpegawai            = sheetrange[''+str(i)].value
        # Bekerjadi               = sheetrange[''+str(i)].value
        # Keterangan_pekerjaan    = sheetrange[''+str(i)].value
        # Tingkat_penghasilan     = sheetrange[''+str(i)].value
        # Tingkat_pendidikan      = sheetrange[''+str(i)].value
        # Keahlian1               = sheetrange[''+str(i)].value
        # Level_keahlian1         = sheetrange[''+str(i)].value
        # Keahlian2               = sheetrange[''+str(i)].value
        # Levelkeahlian2          = sheetrange[''+str(i)].value
        # Minat                   = sheetrange[''+str(i)].value
        # latin                   = sheetrange[''+str(i)].value
        # quran                   = sheetrange[''+str(i)].value
        # #--------------------------------------------------------------
        # # #Tab Keluarga------------------------------------------------
        # #--------------------------------------------------------------
        # Nama_ayah               = sheetrange[''+str(i)].value
        # Alamat_ayah             = sheetrange[''+str(i)].value
        # Nama_ibu                = sheetrange[''+str(i)].value
        # Alamat_ibu              = sheetrange[''+str(i)].value
        # Anak_ke                 = sheetrange[''+str(i)].value
        # Dari                    = sheetrange[''+str(i)].value
        # Nama_saudara1           = sheetrange[''+str(i)].value
        # Nama_saudara2           = sheetrange[''+str(i)].value
        # Nama_saudara3           = sheetrange[''+str(i)].value
        # Nama_saudara4           = sheetrange[''+str(i)].value
        # jml_istr/suam           = sheetrange[''+str(i)].value
        # Nm_istr/suam            = sheetrange[''+str(i)].value
        # alm_istr/suam           = sheetrange[''+str(i)].value
        # jumlah_anak             = sheetrange[''+str(i)].value
        # Nama_anak1              = sheetrange[''+str(i)].value
        # Nama_anak2              = sheetrange[''+str(i)].value
        # Telepon_keluarga        = sheetrange[''+str(i)].value
        #--------------------------------------------------------------
        # #Tab Data Fisik----------------------------------------------
        # --------------------------------------------------------------
        # Tinggi_badan            = sheetrange[''+str(i)].value
        # Berat_badan             = sheetrange[''+str(i)].value
        # Bentuk_rambut           = sheetrange[''+str(i)].value
        # Warna_rambut            = sheetrange[''+str(i)].value
        # Bentuk_bibir            = sheetrange[''+str(i)].value
        # Berkacamata             = sheetrange[''+str(i)].value
        # Bentuk _mata             = sheetrange[''+str(i)].value
        # Warna_mata              = sheetrange[''+str(i)].value
        # Hidung                  = sheetrange[''+str(i)].value
        # Raut_muka               = sheetrange[''+str(i)].value
        # Telinga                 = sheetrange[''+str(i)].value
        # Mulut                   = sheetrange[''+str(i)].value
        # Lengan                  = sheetrange[''+str(i)].value
        # Tangan                  = sheetrange[''+str(i)].value
        # Kaki                    = sheetrange[''+str(i)].value
        # Warna_kulit             = sheetrange[''+str(i)].value
        # Cacat_tubuh             = sheetrange[''+str(i)].value
        # Catatancirikhusus1      = sheetrange[''+str(i)].value
        # Catatancirikhusus2      = sheetrange[''+str(i)].value
        # Catatancirikhusus3      = sheetrange[''+str(i)].value
        #--------------------------------------------------------------
        #Tab Sidik Jari------------------------------------------------
        # --------------------------------------------------------------
        # Nopaspor                = sheetrange[''+str(i)].value
        # Rumus                   = sheetrange[''+str(i)].value
        # Nodaktolskopi           = sheetrange[''+str(i)].value
        # Pengambilansidikjari    = sheetrange[''+str(i)].value
        # Tanggalpengambilan      = sheetrange[''+str(i)].value

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
            # time.sleep(5)
            # pyautogui.typewrite(Residivis)
            # pyautogui.keyDown('down')
            # pyautogui.press('enter')
            # time.sleep(3)
            # if Residivis == 'Ya':
            #     driver.find_element(By.ID, "btn_residivis_counter").click()
            #     time.sleep(1)
            #     pyautogui.hotkey("backspace")
            #     time.sleep(1)
            #     driver.find_element(By.XPATH, "//*[@id=\"btn_residivis_counter\"]/div/input").send_keys(Rke)
            # elif Residivis == 'Tidak':
            #     print ('Residivis done')
            # time.sleep(2)
            # #--------------------------------------------------------------        
            # # time.sleep(3)                              
            # driver.find_element(By.ID, "btn_nama_lengkap").send_keys(Nama_Lengkap)
            # #----------------------------------------------------------------
            # # time.sleep(3)
            # driver.find_element(By.ID, "btn_nama_alias1").send_keys(Nama_Alias1)
            # #--------------------------------------------------------------
            # # time.sleep(3)
            # driver.find_element(By.ID, "btn_nama_alias2").send_keys(Nama_Alias2)
            # #--------------------------------------------------------------
            # # time.sleep(3)
            # driver.find_element(By.ID, "btn_nama_alias3").send_keys(Nama_Alias3)
            # #--------------------------------------------------------------
            # # time.sleep(3)
            # driver.find_element(By.ID, "btn_nama_kecil1").send_keys(Nama_Kecil1)
            # #---------------------------------------------------------------
            # # time.sleep(3)
            # driver.find_element(By.ID, "btn_nama_kecil2").send_keys(Nama_Kecil2)
            # #----------------------------------------------------------------
            # # time.sleep(3)
            # driver.find_element(By.ID, "btn_nama_kecil3").send_keys(Nama_Kecil3)
            # #--------------------------------------------------------------
            # # cekbocktab1 = driver.find_element(By.ID, "btn_is_pengaruh_terhadap_masyarakat").click()
            # if chcktab1 == 'Tidak' :
            #     driver.find_element(By.ID, "btn_is_pengaruh_terhadap_masyarakat").click()
            #     print ("uncheckh")
            # elif chcktab1 == 'ya' :
            #     print ("Masih default")
            # time.sleep(2)
            # if chcktab2 == 'Tidak' :
            #     driver.find_element(By.ID, "btn_is_pengaruh_terhadap_masyarakat").click()
            #     print ("uncheckh")
            # elif chcktab2 == 'ya' :
            #     print ("Masih default")
            #--------------------------------------------------------------
            # time.sleep(3)
            # driver.find_element(By.ID, "btn_id_jenis_warganegara").click()
            # time.sleep(4)
            # if Kewarganegaraan == 'WNI':
            #     pyautogui.typewrite(Kewarganegaraan)
            #     # driver.find_element(By.XPATH, "//*[@id=\"el-popper-container-6249\"]/div[12]/div/div/div[1]/ul/li[2]").click()
            #     time.sleep(2)
            #     pyautogui.keyDown('down')
            #     pyautogui.press('enter')
            # elif Kewarganegaraan == 'WNA':
            #     pyautogui.typewrite(Kewarganegaraan)
            #     # driver.find_element(By.XPATH, "//*[@id=\"el-popper-container-6249\"]/div[12]/div/div/div[1]/ul/li[1]").click()
            #     pyautogui.keyDown('down')
            #     pyautogui.press('enter')
            # # #--------------------------------------------------------------
            # # time.sleep(3)
            # # driver.find_element(By.ID, "btn_nik").send_keys(nik) 
            # # #-------------------------------------------------------------- 
            # time.sleep(3)
            # driver.find_element(By.XPATH, "//*[@id=\"pane-1\"]/form/div[1]/div[2]/div[3]/div/div").click()   
            # if Kewarganegaraan == 'WNI':
            #     time.sleep(2)                               
            #     pyautogui.typewrite(Tempat_Asal)
            #     pyautogui.keyDown('down')
            #     pyautogui.press('enter')
            # elif Kewarganegaraan == 'WNA':
            #     pyautogui.typewrite(Tempat_Asal)
            # #--------------------------------------------------------------
            # time.sleep(3)
            # driver.find_element(By.XPATH, "//*[@id=\"pane-1\"]/form/div[1]/div[2]/div[4]/div/div").click()          
            # if Kewarganegaraan == 'WNI':
            #     time.sleep(2)  
            #     pyautogui.typewrite(Tempat_lahir)
            #     pyautogui.keyDown('down')
            #     pyautogui.press('enter')
            # elif Kewarganegaraan == 'WNA':
            #     pyautogui.typewrite(Tempat_lahir)
            # #----------------------------------------------------------------
            # # untuk tanggal Data format exel di sesuaikan-------------------
            # time.sleep(2)  
            # driver.find_element(By.XPATH, "//div[5]/div/div/div/div/div/input").click()
            # time.sleep(2)
            # pyautogui.typewrite(Tanggal_lahir)
            # pyautogui.press('enter') 
            # #--------------------------------------------------------------
            # time.sleep(3)
            # driver.find_element(By.ID, "btn_id_jenis_kelamin").click()
            # time.sleep(2)
            # pyautogui.typewrite(Jenis_kelamin)
            # pyautogui.keyDown('down')
            # pyautogui.press('enter')
            # #--------------------------------------------------------------
            # time.sleep(3)
            # driver.find_element(By.ID, "btn_id_negara_asing").click()
            # time.sleep(4)
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
            # # ------------------------------------------------------------------------------
            # time.sleep(3)
            # driver.find_element(By.ID, "btn_alamat_alternatif").click()
            # time.sleep(2)
            # pyautogui.typewrite(Alamat_lain)
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
            # driver.find_element(By.XPATH, "//*[@id=\"pane-6\"]/form/div/div[1]/div/div/div/button[1]").click()
            
            # element_present = EC.presence_of_element_located((By.XPATH, "//*[@id=\"pane-6\"]/form/div/div[1]/div/div/div/div"))
            
            # WebDriverWait(driver, 10).until(element_present).click()
            # pyautogui.write("\Filefoto\lim.jpg") 
            # pyautogui.press('enter')
            # driver.find_element(By.XPATH, "//div[6]/form/div/div/div/div/div/div/div/button/span").click()
            # pyautogui.write(r"C:\Users\user\Documents\lim.jpg")
            # pyautogui.press("enter")
            # upload_photo = driver.find_element_by_xpath("//*div[@id=':f']/div")
            # upload_photo.send_keys(r"C:\Users\user\Documents\lim.jpg")
            upload = driver.find_element(By.XPATH, "//div[6]/form/div/div[2]/div/div/div/div/div/button/span")
            upload.send_keys("C:/Users/user/Documents/lim.jpg")
            # pyautogui.typewriter('C:\Users\user\Pictures\Saved_Pictures\limvo.png')
            # autoit.win_activate("Open")
            # autoit.control_send("Open","Edit1",r"C:\Users\user\Documents\TRCH\Automationpython\Filefoto\lim.jpg")
            # autoit.control_send("Open","Edit1","{ENTER}")
            # driver.find_element(By.ID,"pane-6").send_keys(os.getcwd()+ "/lim.jpg")
            # WinActivate("open")
            # send('C:\Users\user\Documents\lim.jpg')
            # src = 'C:\Users\user\Documents\lim.jpg'
            # driver.find_element_by_id("pane-6").get_attribute("src")
            time.sleep(5)    
            #======================================================================
            # driver.find_element(By.ID, "tab-7").click()
            #========================Input Tab Foto========================== 
            #--------------------------------------------------------------

            #Submit
            # time.sleep(2)
            # driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/div[1]/div[2]/div/div/form/div[4]/div/template/button[2]").click()
            
        except TimeoutException:
            print(ERROR)
            pass
        time.sleep(5)   
        i = i + 1
    print ("Success Created")
