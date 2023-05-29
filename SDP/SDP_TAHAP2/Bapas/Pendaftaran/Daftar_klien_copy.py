from src import *
from data import *
# init driver by os
@mark.fixture_penerimaan
def testconfig():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()

@mark.fixture_penerimaan
def testLogin():
	Log.info('Memasukan User name dan Password di halaman Login')
	bapasbdg(driver)

@mark.fixture_penerimaan
def testaksesmenu():
    Log.info('Mengakses Menu Daftar Klien APH')
    daftar_klien(driver)

@mark.fixture_penerimaan
def test_Masukhalamantambah():
    Log.info('Membuka Halaman Penerimaan Klien APH')
    driver.find_element(By.ID, 'createButton').click()

@mark.fixture_penerimaan
def test_isiFormdatatab1():
    #========================Input Tab Biodata ============================
    # Log.Info('Membuka tab Identitas Klien APH')
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'tab-1')))
    time.sleep(2)
    # driver.find_element(By.ID, 'tab-1').click()
    #========================Input Tab Biodata ============================
    driver.find_element(By.ID, 'namKlien').send_keys(NamaKlien)
    driver.find_element(By.ID, 'nik').send_keys(NIK) 
    #----------------------------------------------------------------
    if Residivis == 'Iya':
        driver.find_element(By.XPATH, "//*/text()[normalize-space(.)='Residivis']/parent::*").click()
    elif Residivis == 'Tidak':
        pass
    #----------------------------------------------------------------
    driver.find_element(By.ID, 'namaAlias1').send_keys(NamaAlias1)
    driver.find_element(By.ID, 'namaAlias2').send_keys(NamaAlias2)
    driver.find_element(By.ID, 'namaAlias3').send_keys(NamaAlias3)
    driver.find_element(By.ID, 'namaKecil1').send_keys(NamaKecil1)
    driver.find_element(By.ID, 'namaKecil2').send_keys(NamaKecil2)
    driver.find_element(By.ID, 'namaKecil3').send_keys(NamaKecil3)
    # --------------------------------------------------------------
    if WBPBeresikoTinggi == 'Tidak':
        print ('default')
    elif WBPBeresikoTinggi == 'Iya':
        driver.find_element(By.ID, 'wbpBeresikoTinggiMenarikPerhatianMasyarakat').click()
    if MemilikiPengaruh == 'Iya':
        driver.find_element(By.ID, 'memilikiPengaruhTerhadapMasyarakat').click()
    elif MemilikiPengaruh == 'Tidak':
        print('default')
    # --------------------------------------------------------------
    driver.find_element(By.ID, 'tempatAsal').click()   
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'tempatAsal0')))
    driver.find_element(By.XPATH, "//li[contains(.,'"+TempatAsal+"')]").click()
    #-------------------------------------------------------------- 
    t4lahir = driver.find_element(By.ID, 'tempatLahir')
    t4lahir.click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'tempatLahir0')))
    t4lahir.send_keys(TempatLahir) 
    t4lahir.send_keys(Keys.DOWN)
    t4lahir.send_keys(Keys.ENTER)
    #-------------------------------------------------------------- 
    tgllahir = driver.find_element(By.ID, 'tanggalLahir')
    tgllahir.send_keys(TanggalLahir)
    tgllahir.send_keys(Keys.ENTER)
    # #-------------------------------------------------------------- 
    if JenisKelamin == 'Laki-laki':
        driver.find_element(By.ID, "laki").click()
    elif JenisKelamin == 'Perempuan':
        driver.find_element(By.ID, "perempuan").click()
    # #--------------------------------------------------------------
    if Kewarganegaraan == 'WNI':
        driver.find_element(By.ID, "wni").click()
    elif Kewarganegaraan == 'WNA':
        driver.find_element(By.ID, "wna").click()
        driver.find_element(By.ID, 'negara').send_keys(Negara)
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'negara0')))
        driver.find_element(By.XPATH, "//li[contains(.,'"+Negara+"')]").click()
    # #--------------------------------------------------------------
    driver.find_element(By.ID, 'agama').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'agama0'))) 
    driver.find_element(By.XPATH, "//li[contains(.,'"+ Agama+"')]").click() 
    if Agama == 'Lain-Lainn':
        driver.find_element(By.ID, 'agamaLain').send_keys(Agamalain)
    else:
        pass
    #--------------------------------------------------------------
    sukpu = driver.find_element(By.ID, 'suku')
    sukpu.click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'suku0')))
    sukpu.send_keys(Suku) 
    sukpu.send_keys(Keys.DOWN) 
    sukpu.send_keys(Keys.ENTER) 
    if Suku == 'Lain-lain':
        driver.find_element(By.ID, 'sukuLain').send_keys(SukuLain)
    elif Suku == Suku:
        pass
    #------------------------------------------------------------------------------
    driver.find_element(By.ID, 'statusPerkawinan').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'statusPerkawinan0'))) 
    driver.find_element(By.XPATH, "//li[contains(.,'"+ StatusPerkawinan+"')]").click() 
    #------------------------------------------------------------------------------
    prov = driver.find_element(By.ID, 'provinsi')
    prov.click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'provinsi0'))) 
    prov.send_keys(Provinsi)
    prov.send_keys(Keys.DOWN)
    prov.send_keys(Keys.ENTER)
    #------------------------------------------------------------------------------
    kotkab = driver.find_element(By.ID, 'kotaKabupaten')
    kotkab.click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'kotaKabupaten0')))
    kotkab.send_keys(Kota) 
    kotkab.send_keys(Keys.DOWN) 
    kotkab.send_keys(Keys.ENTER) 
    #------------------------------------------------------------------------------	  
    driver.find_element(By.ID, 'alamatLain').send_keys(AlamatRumah)	 
    lainalamat = driver.find_element(By.XPATH, "//textarea[@placeholder='Masukan alamat lain']")
    lainalamat.send_keys(AlamatLain)  
        #tidak ada bedanya sama seka
    driver.find_element(By.ID, 'telepon').send_keys(Telepon)
    driver.find_element(By.ID, 'kodepos').send_keys(KodePOS)
@mark.fixture_penerimaan
def test_isiFormdatatab2():
    # ========================Informasi Penahanan===========================
    driver.find_element(By.ID, 'tab-2').click()
    #------------------------------------------------------------------------------ 
    driver.find_element(By.ID, 'instansi').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'instansi0'))) 
    driver.find_element(By.XPATH, "//li[contains(.,'"+ AsalInstansi+"')]").click() 
    # --------------------------------------------------------------
    driver.find_element(By.ID, 'jenisKejahatan').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'kejahatan0'))) 
    driver.find_element(By.XPATH, "//li[contains(.,'"+ JenisKejahatan+"')]").click() 
    # --------------------------------------------------------------
    driver.find_element(By.ID, 'uraianKegiatan').send_keys(UraianKejahatan)
    driver.find_element(By.ID, 'pasalUtama').send_keys('Pasal Utama Kejahatan')
    driver.find_element(By.ID, 'pasalTambahan').send_keys('Pasal Tambahan Kejahatan')
    # --------------------------------------------------------------
    if Ditahan == 'Iya':
        driver.find_element(By.XPATH, '//*[@id="pane-2"]/form/div/div[2]/div[2]/div/div/div').click()
        tglditghan = driver.find_element(By.ID, 'tanggalDitahan')
        tglditghan.send_keys(TanggalDitahan)
        tglditghan.send_keys(Keys.ENTER)
        driver.find_element(By.ID, 'noSuratPenahanan').send_keys(NoSuratPenahanan)
    elif Ditahan == 'Tidak':
        pass
@mark.fixture_penerimaan
def test_isiFormdatatab3():
    # ========================Informasi===========================
    driver.find_element(By.ID, 'tab-3').click()
    # --------------------------------------------------------------
    if JenisPekerjaan == 'Lain-lain':
        driver.find_element(By.ID, 'id_jenis_pekerjaan_lain').send_keys(JenisPekerjaanLain)
    elif JenisPekerjaan == JenisPekerjaan:
        driver.find_element(By.ID, 'id_jenis_pekerjaan').click()
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'idJenisPekerjaan-0'))) 
        driver.find_element(By.XPATH, "//li[contains(.,'"+ JenisPekerjaan+"')]").click()
    # -----------------------------------------------------------
    driver.find_element(By.ID, 'tempatBekerja').send_keys(TempatBekerja)
    driver.find_element(By.ID, 'keteranganPekerjaan').send_keys(KeteranganKerja)
    #--------------------------------------------------------------
    if Pendidikan == 'Lain-lain':
        driver.find_element(By.ID, 'id_jenis_pendidikan_lain').send_keys(TnktPendidikanLain)
    elif Pendidikan == Pendidikan:
        driver.find_element(By.ID, 'id_jenis_pendidikan').click()
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'idJenisPendidikan-0'))) 
        driver.find_element(By.XPATH, "//li[contains(.,'"+ Pendidikan+"')]").click()
    #--------------------------------------------------------------
    if Keahlian1 == 'Lain-lain':
        driver.find_element(By.ID, 'id_jenis_keahlian_1_lain').send_keys(Keahlian1Lain)
    elif Keahlian1 == Keahlian1:
        driver.find_element(By.ID, 'id_jenis_keahlian_1').click()
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'idjenisKeahlian-0'))) 
        driver.find_element(By.XPATH, "//li[contains(.,'"+ Keahlian1+"')]").click
    driver.find_element(By.ID, 'id_jenis_level_1').click()      
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'idJenisLevel-0'))) 
    driver.find_element(By.XPATH, "//li[contains(.,'"+ LevelKeahlian1+"')]").click()
    #--------------------------------------------------------------
    if Keahlian2 == 'Lain-lain':
        driver.find_element(By.ID, 'id_jenis_keahlian_1_lain').send_keys(Keahlian1Lain)
    elif Keahlian2 == Keahlian2:
        ahli2 = driver.find_element(By.ID, 'id_jenis_keahlian_2')
        ahli2.click()
        ahli2.send_keys(Keahlian2)
        ahli2.send_keys(Keys.DOWN)
        ahli2.send_keys(Keys.ENTER)
    #--------------------------------------------------------------
    level2 = driver.find_element(By.ID, 'id_jenis_level_2')
    level2.click()
    level2.send_keys(LevelKeahlian2)
    level2.send_keys(Keys.DOWN)
    level2.send_keys(Keys.ENTER)
    # #----------------------------------------------------------------------
    driver.find_element(By.ID, 'minat').send_keys(Minat) 
@mark.fixture_penerimaan
def test_isiFormdatatab4():   
    #========================Input Tab Keluarga============================ 
    driver.find_element(By.ID, 'tab-4').click()
    #========================Input Tab Keluarga============================ 
    driver.find_element(By.ID, 'nm_ayah').send_keys(NamaAyah)
    driver.find_element(By.ID, 'tmp_tgl_ayah').send_keys(AlamatAyah)
    driver.find_element(By.ID, 'nm_ibu').send_keys(NamaIbu)
    driver.find_element(By.ID, 'tmp_tgl_ibu').send_keys(AlamatIbu)
    # ------------------------------------------------------------------------------
    keanak = driver.find_element(By.XPATH, '//*[@id="anakke"]/div/input')
    keanak.click()
    pyautogui.hotkey('backspace')        
    keanak.send_keys(AnakKe)
    pyautogui.press('enter')
    saudarajumlh = driver.find_element(By.XPATH, '//*[@id="jml_saudara"]/div/input')
    saudarajumlh.click()
    pyautogui.hotkey('backspace')        
    saudarajumlh.send_keys(Dari)
    pyautogui.press('enter')
    if Dari == 2:	
        driver.find_element(By.ID, 'nm_saudara_1').send_keys(NamaSudara1)
    elif Dari == 3:	
        driver.find_element(By.ID, 'nm_saudara_1').send_keys(NamaSudara1)
        driver.find_element(By.ID, 'nm_saudara_2').send_keys(NamaSudara2)
    elif Dari == 4:   
        driver.find_element(By.ID, 'nm_saudara_1').send_keys(NamaSudara1)	
        driver.find_element(By.ID, 'nm_saudara_2').send_keys(NamaSudara2) 
        driver.find_element(By.ID, 'nm_saudara_3').send_keys(NamaSudara3)
    elif Dari == 5:   
        driver.find_element(By.ID, 'nm_saudara_1').send_keys(NamaSudara1) 
        driver.find_element(By.ID, 'nm_saudara_2').send_keys(NamaSudara2)
        driver.find_element(By.ID, 'nm_saudara_3').send_keys(NamaSudara3)
        driver.find_element(By.ID, 'nm_saudara_4').send_keys(NamaSudara4)
    elif Dari == 1 :
        print ('anak satu satunya')   
    if StatusPerkawinan == 'Belum Kawin':
        print('default')
    elif (StatusPerkawinan == 'Duda' or StatusPerkawinan == 'Janda' or  StatusPerkawinan == 'Kawin'):
        driver.find_element(By.ID, 'jml_istri_suami').click()
        pyautogui.hotkey('backspace')
        driver.find_element(By.XPATH, '//*[@id="jml_istri_suami"]/div/input' ).send_keys(JumlahIstriSuami) 
        pyautogui.press('enter')
        driver.find_element(By.ID, 'nm_istri_suami_1').send_keys(NamaIstriSuami1)
        driver.find_element(By.ID, 'tmp_tgl_istri_suami').send_keys(AlamatIstriSuami)
        anaknya = driver.find_element(By.XPATH, '//*[@id="jml_anak"]/div/input')
        anaknya.click()
        pyautogui.hotkey('backspace')
        anaknya.send_keys(JumlahAnak) 
        pyautogui.press('enter')	
        if JumlahAnak == 1:  
            driver.find_element(By.ID, 'nm_anak_1').send_keys(NamaAnak1)
        elif JumlahAnak == 2:	
            driver.find_element(By.ID, 'nm_anak_1').send_keys(NamaAnak1)	 
            driver.find_element(By.ID, 'nm_anak_2').send_keys(NamaAnak2)
        elif JumlahAnak == 3:	
            driver.find_element(By.ID, 'nm_anak_1').send_keys(NamaAnak1)	
            driver.find_element(By.ID, 'nm_anak_2').send_keys(NamaAnak2)  
            driver.find_element(By.ID, 'nm_anak_3').send_keys(NamaAnak3)
        elif  JumlahAnak == 0: 
            pass
            print('masa ga punya anak')
        #--------------------------------------------------------------
        driver.find_element(By.XPATH, '//*[@id="telephone_keluarga"]').send_keys(TeleponKeluarga)
@mark.fixture_penerimaan
def test_isiFormdatatab5():
    #========================Input Tab Data Fisik========================== 
    driver.find_element(By.ID, 'tab-5').click()
    #========================Input Tab Data Fisik==========================
    driver.find_element(By.XPATH, '//*[@id="tinggi"]/div/input').click()
    pyautogui.hotkey('backspace')
    driver.find_element(By.XPATH, '//*[@id="tinggi"]/div/input' ).send_keys(Tinggi) 
    #--------------------------------------------------------------
    driver.find_element(By.XPATH, '//*[@id="berat"]/div/input').click()
    pyautogui.hotkey('backspace')
    driver.find_element(By.XPATH, '//*[@id="berat"]/div/input').send_keys(Berat)
    #--------------------------------------------------------------
    driver.find_element(By.ID, 'id_bentukrambut').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'bentukRambut-0'))) 
    driver.find_element(By.ID, 'id_bentukrambut').send_keys(BentukRambut)
    driver.find_element(By.ID, 'id_bentukrambut').send_keys(Keys.DOWN)
    driver.find_element(By.ID, 'id_bentukrambut').send_keys(Keys.ENTER)
    #--------------------------------------------------------------
    driver.find_element(By.ID, 'id_jenis_rambut').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisRambut-0'))) 
    driver.find_element(By.ID, 'id_jenis_rambut').send_keys(WarnaRambut)
    driver.find_element(By.ID, 'id_jenis_rambut').send_keys(Keys.DOWN)
    driver.find_element(By.ID, 'id_jenis_rambut').send_keys(Keys.ENTER)
    #--------------------------------------------------------------
    driver.find_element(By.ID, 'id_bentukbibir').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'bentukBibir-0'))) 
    driver.find_element(By.ID, 'id_bentukbibir').send_keys(BentukBibir)
    driver.find_element(By.ID, 'id_bentukbibir').send_keys(Keys.DOWN)
    driver.find_element(By.ID, 'id_bentukbibir').send_keys(Keys.ENTER)
    #--------------------------------------------------------------
    driver.find_element(By.ID, 'id_kacamata').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'kacamata-0'))) 
    driver.find_element(By.ID, 'id_kacamata').send_keys(Berkacamata)
    driver.find_element(By.ID, 'id_kacamata').send_keys(Keys.DOWN)
    driver.find_element(By.ID, 'id_kacamata').send_keys(Keys.ENTER)
    #--------------------------------------------------------------
    driver.find_element(By.ID, 'id_bentuk_mata').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'bentukMata-0'))) 
    driver.find_element(By.ID, 'id_bentuk_mata').send_keys(BentukMata)
    driver.find_element(By.ID, 'id_bentuk_mata').send_keys(Keys.DOWN)
    driver.find_element(By.ID, 'id_bentuk_mata').send_keys(Keys.ENTER)
    #--------------------------------------------------------------
    driver.find_element(By.ID, 'id_warna_mata').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'warnaMata-0'))) 
    driver.find_element(By.ID, 'id_warna_mata').send_keys(WarnaMata)
    driver.find_element(By.ID, 'id_warna_mata').send_keys(Keys.DOWN)
    driver.find_element(By.ID, 'id_warna_mata').send_keys(Keys.ENTER)
    #--------------------------------------------------------------
    driver.find_element(By.ID, 'id_jenis_hidung').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisHidung-0'))) 
    driver.find_element(By.ID, 'id_jenis_hidung').send_keys(Hidung)
    driver.find_element(By.ID, 'id_jenis_hidung').send_keys(Keys.DOWN)
    driver.find_element(By.ID, 'id_jenis_hidung').send_keys(Keys.ENTER)
    #--------------------------------------------------------------
    driver.find_element(By.ID, 'id_jenis_muka').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisMuka-0'))) 
    driver.find_element(By.ID, 'id_jenis_muka').send_keys(RautMuka)
    driver.find_element(By.ID, 'id_jenis_muka').send_keys(Keys.DOWN)
    driver.find_element(By.ID, 'id_jenis_muka').send_keys(Keys.ENTER)
    #--------------------------------------------------------------
    driver.find_element(By.ID, 'id_telinga').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'telinga-0'))) 
    driver.find_element(By.ID, 'id_telinga').send_keys(Telinga)
    driver.find_element(By.ID, 'id_telinga').send_keys(Keys.DOWN)
    driver.find_element(By.ID, 'id_telinga').send_keys(Keys.ENTER)
    #--------------------------------------------------------------
    driver.find_element(By.ID, 'id_jenis_mulut').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisMulut-0'))) 
    driver.find_element(By.ID, 'id_jenis_mulut').send_keys(Mulut)
    driver.find_element(By.ID, 'id_jenis_mulut').send_keys(Keys.DOWN)
    driver.find_element(By.ID, 'id_jenis_mulut').send_keys(Keys.ENTER)
    #--------------------------------------------------------------
    driver.find_element(By.ID, 'id_lengan').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'lengan-0'))) 
    driver.find_element(By.ID, 'id_lengan').send_keys(Lengan)
    driver.find_element(By.ID, 'id_lengan').send_keys(Keys.DOWN)
    driver.find_element(By.ID, 'id_lengan').send_keys(Keys.ENTER)
    #--------------------------------------------------------------
    driver.find_element(By.ID, 'id_jenis_tangan').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisTangan-0'))) 
    driver.find_element(By.ID, 'id_jenis_tangan').send_keys(Tangan)
    driver.find_element(By.ID, 'id_jenis_tangan').send_keys(Keys.DOWN)
    driver.find_element(By.ID, 'id_jenis_tangan').send_keys(Keys.ENTER)
    #--------------------------------------------------------------
    driver.find_element(By.ID, 'id_jenis_kaki').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisKaki-0'))) 
    driver.find_element(By.ID, 'id_jenis_kaki').send_keys(Kaki)
    driver.find_element(By.ID, 'id_jenis_kaki').send_keys(Keys.DOWN)
    driver.find_element(By.ID, 'id_jenis_kaki').send_keys(Keys.ENTER)
    #--------------------------------------------------------------
    driver.find_element(By.ID, 'id_warnakulit').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'warnaKulit-0'))) 
    driver.find_element(By.ID, 'id_warnakulit').send_keys(WarnaKulit)
    driver.find_element(By.ID, 'id_warnakulit').send_keys(Keys.DOWN)
    driver.find_element(By.ID, 'id_warnakulit').send_keys(Keys.ENTER)
    #--------------------------------------------------------------
    driver.find_element(By.ID, 'cacat').send_keys(normalTubuh)
    #--------------------------------------------------------------
    # driver.find_element(By.XPATH, '//*[@id="upload_foto_ciri_1"]').click()
    # time.sleep(3)
    # pyautogui.write(environ.get(r'Gambar'))
    # pyautogui.press('enter')
    # time.sleep(3)
    # driver.find_element(By.XPATH, '//*[@id="upload_foto_ciri_2"]').click()
    # time.sleep(3)
    # pyautogui.write(environ.get(r'Gambar'))
    # pyautogui.press('enter')
    # time.sleep(3)
    # driver.find_element(By.XPATH, '//*[@id="upload_foto_ciri_3"]').click()
    # time.sleep(3)
    # pyautogui.write(environ.get(r'Gambar'))
    # pyautogui.press('enter')
    # #--------------------------------------------------------------
    # driver.find_element(By.ID, 'ciri').send_keys(CiriKhusus1)  
    # driver.find_element(By.ID, 'ciri2').send_keys(CiriKhusus2) 
    # driver.find_element(By.ID, 'ciri3').send_keys(CiriKhusus3) 
# @mark.fixture_penerimaan
# def test_isiFormdatatab6():   
    # # ======================================================================
    # driver.find_element(By.ID, 'tab-6').click()
    # # # ========================Input Tab Sidik Jari==========================
    # try:
    #     driver.find_element(By.ID, 'no_paspor').send_keys(NoPaspor)
    #     driver.find_element(By.ID, 'rumus_daktil').send_keys(RumusD)
    #     driver.find_element(By.ID, 'nomor_daktil').send_keys(NomorD)
    #     sjambil = driver.find_element(By.ID, 'pengambil_sj')
    #     sjambil.send_keys(PengambilanSJ)
    #     sjambil.send_keys(Keys.ENTER)
    #     driver.find_element(By.ID, 'tanggalPengambilan').send_keys(TanggalAmbil)
    # except NoSuchElementException:
    #     driver.close()
    #     driver.quit()
    # Log.info('Tidak ada elemen tersedia')
    # #======================================================================
@mark.fixture_penerimaan
def test_isiFormdatata7():
    driver.find_element(By.ID, 'tab-7').click()
    #========================Input Tab Foto==========================   
    driver.find_element(By.ID, 'uploadFotoKiri').click()
    time.sleep(3)
    pyautogui.write(environ.get(r'Gambar'))
    pyautogui.press('enter')
    driver.find_element(By.ID, 'uploadFotoDepan').click()
    time.sleep(3)
    pyautogui.write(environ.get(r'Gambar'))
    pyautogui.press('enter')
    driver.find_element(By.ID, 'uploadFotoKanan').click()
    time.sleep(3)
    pyautogui.write(environ.get(r'Gambar'))
    pyautogui.press('enter')
    #========================Input Tab Foto==========================
@mark.fixture_penerimaan
def test_simpanData(): 
    #Submit
    driver.find_element(By.ID, 'submitButton').click() 
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'createButton')))