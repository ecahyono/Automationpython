from src import *
# init driver by os
@mark.fixture_penerimaan
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Memasukan User name dan Password di halaman Login')
	bapasbdg(driver)

@mark.fixture_penerimaan
def test_daftarklien():
    tambah = wb['KlienAPH']
    for row in tambah.iter_rows(min_row=2, values_only=True):
        NamaKlien           = row[0]
        NIK                 = row[1]
        Residivis           = row[2]
        NamaAlias1          = row[3]
        NamaAlias2          = row[4]
        NamaAlias3          = row[5]
        NamaKecil1          = row[6]
        NamaKecil2          = row[7]
        NamaKecil3          = row[8]
        WBPBeresikoTinggi   = row[9]
        MemilikiPengaruh    = row[10]
        TempatAsal          = row[11]
        TempatLahir         = row[12]
        JenisKelamin        = row[13]
        Kewarganegaraan     = row[14]
        Negara              = row[15]
        TanggalLahir        = row[16]
        Agama               = row[17]
        Agamalain           = row[18]
        Suku                = row[19]
        SukuLain            = row[20]
        StatusPerkawinan    = row[21]
        Provinsi            = row[22]
        Kota                = row[23]
        AlamatRumah         = row[24]
        AlamatLain          = row[25]
        Telepon             = row[26]
        KodePOS             = row[27]
        AsalInstansi        = row[28]
        JenisKejahatan      = row[29]
        UraianKejahatan     = row[30]
        Ditahan             = row[31]
        TanggalDitahan      = row[32]
        NoSuratPenahanan    = row[33]
        JenisPekerjaan      = row[34]
        JenisPekerjaanLain  = row[35]
        TempatBekerja       = row[36]
        KeteranganKerja     = row[37]
        Pendidikan          = row[38]
        TnktPendidikanLain  = row[39]
        Keahlian1           = row[40]
        Keahlian1Lain       = row[41]
        LevelKeahlian1      = row[42]
        Keahlian2           = row[43]
        Keahlian2Lain       = row[44]
        LevelKeahlian2      = row[45]
        Minat               = row[46]
        NamaAyah            = row[47]
        AlamatAyah          = row[48]
        NamaIbu             = row[49]
        AlamatIbu           = row[50]
        AnakKe              = row[51]
        Dari                = row[52]
        NamaSudara1         = row[53]
        NamaSudara2         = row[54]
        NamaSudara3         = row[55]
        NamaSudara4         = row[56]
        JumlahIstriSuami    = row[57]
        NamaIstriSuami1     = row[58]
        AlamatIstriSuami    = row[59]
        JumlahAnak          = row[60]
        NamaAnak1           = row[61]
        NamaAnak2           = row[62]
        NamaAnak3           = row[63]
        TeleponKeluarga     = row[64]
        Tinggi              = row[65]
        Berat               = row[66]
        BentukRambut        = row[67]
        WarnaRambut         = row[68]
        BentukBibir         = row[69]
        Berkacamata         = row[70]
        BentukMata          = row[71]
        WarnaMata           = row[72]
        Hidung              = row[73]
        RautMuka            = row[74]
        Telinga             = row[75]
        Mulut               = row[76]
        Lengan              = row[77]
        Tangan              = row[78]
        Kaki                = row[79]
        WarnaKulit          = row[80]
        normalTubuh         = row[81]
        CiriKhusus1         = row[82]
        CiriKhusus2         = row[83]
        CiriKhusus3         = row[84]
        NoPaspor            = row[85]
        RumusD              = row[86]
        NomorD              = row[87]
        PengambilanSJ       = row[88]
        TanggalAmbil        = row[89]
 
        Log.info('Membuka Halaman Penerimaan Klien APH')
        daftarklien(driver)
        driver.find_element(By.ID, 'createButton').click()
        #========================Input Tab Biodata ============================
        driver.find_element(By.ID, 'tab-1').click()
        driver.find_element(By.ID, 'namKlien').send_keys(NamaKlien)
        driver.find_element(By.ID, 'nik').send_keys(NIK) 
        #----------------------------------------------------------------
        if Residivis == 'Iya':
            driver.find_element(By.ID, 'residivis').click()
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
        if WBPBeresikoTinggi == 'Tidak' or MemilikiPengaruh == 'Tidak':
            print ('default')
        elif WBPBeresikoTinggi == 'Iya' or MemilikiPengaruh == 'Iya':
            driver.find_element(By.ID, 'wbpBeresikoTinggiMenarikPerhatianMasyarakat').click()
            driver.find_element(By.ID, 'memilikiPengaruhTerhadapMasyarakat').click()
        # --------------------------------------------------------------
        driver.find_element(By.ID, 'tempatAsal').click()   
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'tempatAsal0')))
        driver.find_element(By.XPATH, "//li[contains(.,'"+ TempatAsal+"')]").click()
        #-------------------------------------------------------------- 
        # driver.find_element(By.ID, 'tempatLahir').click()         
        # WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, "tempatLahir0"))) 
        # driver.find_element(By.XPATH, "//li[contains(.,'"+ TempatLahir+"')]").click()
        #-------------------------------------------------------------- 
        tgllahir = driver.find_element(By.ID, 'tanggalLahir')
        tgllahir.send_keys(TanggalLahir)
        tgllahir.send_keys(Keys.ENTER)
        # #-------------------------------------------------------------- 
        if JenisKelamin == 'Laki-laki':
            driver.find_element(By.XPATH, "//*/text()[normalize-space(.)='Laki - Laki']/parent::*").click()
        elif JenisKelamin == 'Perempuan':
            driver.find_element(By.XPATH, "//*/text()[normalize-space(.)='Perempuan']/parent::*").click()
        # #--------------------------------------------------------------
        # if Kewarganegaraan == 'WNI':
        #     driver.find_element(By.ID, "//div[@id='kewarganegaraan']/label[2]").click()
        # elif Kewarganegaraan == 'WNA':
        #     driver.find_element(By.ID, "//div[@id='kewarganegaraan']/label").click()
        #     driver.find_element(By.ID, 'negara').send_keys(Negara)      
        # #--------------------------------------------------------------
        driver.find_element(By.ID, 'agama').click()
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'agama0'))) 
        driver.find_element(By.XPATH, "//li[contains(.,'"+ Agama+"')]").click() 
        if Agama == 'Lain-lain':
            driver.find_element(By.ID, 'agamaLain').send_keys(Agamalain)
        elif Agama == Agama:
            pass
        #--------------------------------------------------------------
        # driver.find_element(By.ID, 'suku').click()
        # WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'suku0'))) 
        # driver.find_element(By.XPATH, "//li[contains(.,'"+ Suku+"')]").click() 
        # if Suku == 'Lain-lain':
        #     driver.find_element(By.ID, 'sukuLain').send_keys(SukuLain)
        # elif Suku == Suku:
        #     pass
        #------------------------------------------------------------------------------
        driver.find_element(By.ID, 'statusPerkawinan').click()
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'statusPerkawinan0'))) 
        driver.find_element(By.XPATH, "//li[contains(.,'"+ StatusPerkawinan+"')]").click() 
        #------------------------------------------------------------------------------
        driver.find_element(By.ID, 'provinsi').click()
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'provinsi0'))) 
        driver.find_element(By.XPATH, "//li[contains(.,'"+ Provinsi+"')]").click() 
        #------------------------------------------------------------------------------
        driver.find_element(By.ID, 'kotaKabupaten').click()
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'kotaKabupaten0'))) 
        driver.find_element(By.XPATH, "//li[contains(.,'"+ Kota+"')]").click() 
        #------------------------------------------------------------------------------	  
        driver.find_element(By.ID, 'alamatLain').send_keys(AlamatRumah)	   
        driver.find_element(By.ID, 'alamatLain').send_keys(AlamatLain)
        driver.find_element(By.ID, 'telepon').send_keys(Telepon)
        driver.find_element(By.ID, 'kodepos').send_keys(KodePOS)
        # ========================Informasi Penahanan===========================
        driver.find_element(By.ID, 'tab-2').click()
        #------------------------------------------------------------------------------
        driver.find_element(By.ID, 'instansi').click()
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'instansi0'))) 
        driver.find_element(By.XPATH, "//li[contains(.,'"+ AsalInstansi+"')]").click() 
        #------------------------------------------------------------------------------
        driver.find_element(By.ID, 'instansi').click()
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'instansi0'))) 
        driver.find_element(By.XPATH, "//li[contains(.,'"+ AsalInstansi+"')]").click() 
        # --------------------------------------------------------------
        driver.find_element(By.ID, 'instansi').click()
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'instansi0'))) 
        driver.find_element(By.XPATH, "//li[contains(.,'"+ JenisKejahatan+"')]").click() 
        # --------------------------------------------------------------
        driver.find_element(By.ID, 'uraianKegiatan').send_keys(UraianKejahatan)
        # --------------------------------------------------------------
        if Ditahan == 'Iya':
            driver.find_element(By.ID, 'ditahan').click()
            tglditghan = driver.find_element(By.ID, 'tanggalDitahan').send_keys(TanggalDitahan)
            tglditghan.send_keys(TanggalDitahan)
            tglditghan.send_keys(Keys.ENTER)
            driver.find_element(By.ID, 'noSuratPenahanan').send_keys(NoSuratPenahanan)
        elif Ditahan == 'Tidak':
            pass
        # ========================Informasi Penahanan===========================
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
            driver.find_element(By.XPATH, "//li[contains(.,'"+ Keahlian1+"')]").click()

        driver.find_element(By.ID, 'id_jenis_level_1').click()      
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'idJenisLevel-0'))) 
        driver.find_element(By.XPATH, "//li[contains(.,'"+ LevelKeahlian1+"')]").click()
        #--------------------------------------------------------------
        if Keahlian2 == 'Lain-lain':
            driver.find_element(By.ID, 'id_jenis_keahlian_1_lain').send_keys(Keahlian1Lain)
        elif Keahlian2 == Keahlian2:
            driver.find_element(By.ID, 'id_jenis_keahlian_2').click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//li[contains(.,'"+ Keahlian2+"')]").click()
        #--------------------------------------------------------------
        driver.find_element(By.ID, 'id_jenis_level_2').click()
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'idJenisLevel2-0'))) 
        driver.find_element(By.XPATH, "//li[contains(.,'"+ LevelKeahlian2+"')]").click()
        # #----------------------------------------------------------------------
        driver.find_element(By.ID, 'minat').send_keys(Minat)
        #========================Input Tab Keluarga============================ 
        driver.find_element(By.ID, 'tab-4').click()
        driver.find_element(By.ID, 'nm_ayah').send_keys(Nama_ayah)
        driver.find_element(By.ID, 'tmp_tgl_ayah').send_keys(Alamat_ayah)
        driver.find_element(By.ID, 'nm_ibu').send_keys(Nama_ibu)
        driver.find_element(By.ID, 'tmp_tgl_ibu').send_keys(Alamat_ibu)
        #------------------------------------------------------------------------------
        driver.find_element(By.XPATH, '//*[@id="anakke"]/div/input').click()
        pyautogui.hotkey('backspace')       
        driver.find_element(By.XPATH, '//*[@id="anakke"]/div/input').send_keys(Anak_ke)
        pyautogui.press('enter')
        driver.find_element(By.XPATH, '//*[@id="jml_saudara"]/div/input').click()
        pyautogui.hotkey('backspace')       
        driver.find_element(By.XPATH, '//*[@id="jml_saudara"]/div/input').send_keys(Dari)
        pyautogui.press('enter')
        if Dari == 2:	
            driver.find_element(By.ID, 'nm_saudara_1').send_keys(Nama_saudara1)
        elif Dari == 3:	
            driver.find_element(By.ID, 'nm_saudara_1').send_keys(Nama_saudara1)
            driver.find_element(By.ID, 'nm_saudara_2').send_keys(Nama_saudara2)
        elif Dari == 4:   
            driver.find_element(By.ID, 'nm_saudara_1').send_keys(Nama_saudara1)	
            driver.find_element(By.ID, 'nm_saudara_2').send_keys(Nama_saudara2) 
            driver.find_element(By.ID, 'nm_saudara_3').send_keys(Nama_saudara3)
        elif Dari == 5:   
            driver.find_element(By.ID, 'nm_saudara_1').send_keys(Nama_saudara1) 
            driver.find_element(By.ID, 'nm_saudara_2').send_keys(Nama_saudara2)
            driver.find_element(By.ID, 'nm_saudara_3').send_keys(Nama_saudara3)
            driver.find_element(By.ID, 'nm_saudara_4').send_keys(Nama_saudara4)
        elif Dari == 1 :
            print ('anak satu satunya')
        if Status_perkawinan == 'Belum Kawin':
            print('default')
        elif Status_perkawinan == 'Duda':
            driver.find_element(By.ID, 'jml_istri_suami').click()
            pyautogui.hotkey('backspace')
            driver.find_element(By.XPATH, '//*[@id="jml_istri_suami"]/div/input' ).send_keys(jml_istrsuam) 
            pyautogui.press('enter')
            driver.find_element(By.ID, 'nm_istri_suami_1').send_keys(Nm_istrsuam)
            driver.find_element(By.ID, 'tmp_tgl_istri_suami').send_keys(alm_istrsuam)
            driver.find_element(By.XPATH, '//*[@id="jml_anak"]/div/input').click()
            pyautogui.hotkey('backspace')
            jumlah = driver.find_element(By.XPATH, '//*[@id="jml_anak"]/div/input' ).send_keys(jumlah_anak) 
            pyautogui.press('enter')
            if jumlah_anak == 1:   
                driver.find_element(By.ID, 'nm_anak_1').send_keys(Nama_anak1)
            elif jumlah_anak == 2:	
                driver.find_element(By.ID, 'nm_anak_1').send_keys(Nama_anak1)	 
                driver.find_element(By.ID, 'nm_anak_2').send_keys(Nama_anak2)
            elif jumlah_anak == 3:	
                driver.find_element(By.ID, 'nm_anak_1').send_keys(Nama_anak1)	
                driver.find_element(By.ID, 'nm_anak_2').send_keys(Nama_anak2)  
                driver.find_element(By.ID, 'nm_anak_3').send_keys(Nama_anak3)
            elif  jumlah_anak == 0: 
                print('masa ga punya anak')
            #--------------------------------------------------------------
            # driver.find_element(By.XPATH, '//*[@id="telephone_keluarga"]').send_keys(Telepon_keluarga)
        elif Status_perkawinan == 'Janda':
            driver.find_element(By.ID, 'jml_istri_suami').click()
            pyautogui.hotkey('backspace')
            driver.find_element(By.XPATH, '//*[@id="jml_istri_suami"]/div/input' ).send_keys(jml_istrsuam) 
            pyautogui.press('enter')
            driver.find_element(By.ID, 'nm_istri_suami_1').send_keys(Nm_istrsuam)
            driver.find_element(By.ID, 'tmp_tgl_istri_suami').send_keys(alm_istrsuam)
            driver.find_element(By.XPATH, '//*[@id="jml_anak"]/div/input').click()
            pyautogui.hotkey('backspace')
            jumlah = driver.find_element(By.XPATH, '//*[@id="jml_anak"]/div/input' ).send_keys(jumlah_anak) 
            pyautogui.press('enter')
            if jumlah_anak == 1:
                driver.find_element(By.ID, 'nm_anak_1').send_keys(Nama_anak1)
            elif jumlah_anak == 2:
                driver.find_element(By.ID, 'nm_anak_1').send_keys(Nama_anak1)       
                driver.find_element(By.ID, 'nm_anak_2').send_keys(Nama_anak2)
            elif jumlah_anak == 3:
                driver.find_element(By.ID, 'nm_anak_1').send_keys(Nama_anak1)       
                driver.find_element(By.ID, 'nm_anak_2').send_keys(Nama_anak2)
                driver.find_element(By.ID, 'nm_anak_3').send_keys(Nama_anak3)
            elif  jumlah_anak == 0: 
                print('masa ga punya anak')
            #--------------------------------------------------------------
            # driver.find_element(By.XPATH, '//*[@id="telephone_keluarga"]').send_keys(Telepon_keluarga)
        elif Status_perkawinan == 'Kawin':
            driver.find_element(By.ID, 'jml_istri_suami').click()
            pyautogui.hotkey('backspace')
            driver.find_element(By.XPATH, '//*[@id="jml_istri_suami"]/div/input' ).send_keys(jml_istrsuam) 
            pyautogui.press('enter')
            driver.find_element(By.ID, 'nm_istri_suami_1').send_keys(Nm_istrsuam)
            driver.find_element(By.ID, 'tmp_tgl_istri_suami').send_keys(alm_istrsuam)
            driver.find_element(By.XPATH, '//*[@id="jml_anak"]/div/input').click()
            pyautogui.hotkey('backspace')
            jumlah = driver.find_element(By.XPATH, '//*[@id="jml_anak"]/div/input' ).send_keys(jumlah_anak) 
            pyautogui.press('enter')
            if jumlah_anak == 1:
                driver.find_element(By.ID, 'nm_anak_1').send_keys(Nama_anak1)
            elif jumlah_anak == 2:
                driver.find_element(By.ID, 'nm_anak_1').send_keys(Nama_anak1)       
                driver.find_element(By.ID, 'nm_anak_2').send_keys(Nama_anak2)
            elif jumlah_anak == 3:
                driver.find_element(By.ID, 'nm_anak_1').send_keys(Nama_anak1)       
                driver.find_element(By.ID, 'nm_anak_2').send_keys(Nama_anak2)
                driver.find_element(By.ID, 'nm_anak_3').send_keys(Nama_anak3)
            elif  jumlah_anak == 0: 
                print('masa ga punya anak')
            #--------------------------------------------------------------
            # driver.find_element(By.XPATH, '//*[@id="telephone_keluarga"]').send_keys(Telepon_keluarga)
            #======================================================================
        driver.find_element(By.ID, 'tab-4').click()
        #========================Input Tab Data Fisik========================== 
        driver.find_element(By.XPATH, '//*[@id="tinggi"]/div/input').click()
        pyautogui.hotkey('backspace')
        driver.find_element(By.XPATH, '//*[@id="tinggi"]/div/input' ).send_keys(Tinggi_badan) 
        #--------------------------------------------------------------
        driver.find_element(By.XPATH, '//*[@id="berat"]/div/input').click()
        pyautogui.hotkey('backspace')
        driver.find_element(By.XPATH, '//*[@id="berat"]/div/input').send_keys(Berat_badan)
        #--------------------------------------------------------------
        driver.find_element(By.ID, 'id_bentukrambut').click()
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'bentukRambut-0'))) 
        driver.find_element(By.ID, 'id_bentukrambut').send_keys(Bentuk_rambut)
        driver.find_element(By.ID, 'id_bentukrambut').send_keys(Keys.DOWN)
        driver.find_element(By.ID, 'id_bentukrambut').send_keys(Keys.ENTER)
        #--------------------------------------------------------------
        driver.find_element(By.ID, 'id_jenis_rambut').click()
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'jenisRambut-0'))) 
        driver.find_element(By.ID, 'id_jenis_rambut').send_keys(Warna_rambut)
        driver.find_element(By.ID, 'id_jenis_rambut').send_keys(Keys.DOWN)
        driver.find_element(By.ID, 'id_jenis_rambut').send_keys(Keys.ENTER)
        #--------------------------------------------------------------
        driver.find_element(By.ID, 'id_bentukbibir').click()
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'bentukBibir-0'))) 
        driver.find_element(By.ID, 'id_bentukbibir').send_keys(Bentuk_bibir)
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
        driver.find_element(By.ID, 'id_bentuk_mata').send_keys(Bentuk_mata)
        driver.find_element(By.ID, 'id_bentuk_mata').send_keys(Keys.DOWN)
        driver.find_element(By.ID, 'id_bentuk_mata').send_keys(Keys.ENTER)
        #--------------------------------------------------------------
        driver.find_element(By.ID, 'id_warna_mata').click()
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'warnaMata-0'))) 
        driver.find_element(By.ID, 'id_warna_mata').send_keys(Warna_mata)
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
        driver.find_element(By.ID, 'id_jenis_muka').send_keys(Raut_muka)
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
        driver.find_element(By.ID, 'id_warnakulit').send_keys(Warna_kulit)
        driver.find_element(By.ID, 'id_warnakulit').send_keys(Keys.DOWN)
        driver.find_element(By.ID, 'id_warnakulit').send_keys(Keys.ENTER)
        #--------------------------------------------------------------
        # driver.find_element(By.ID, 'cacat').send_keys(Cacat_tubuh)
        # #--------------------------------------------------------------
        # time.sleep(4)
        # driver.find_element(By.XPATH, '//*[@id="upload_foto_ciri_1"]').click()
        # time.sleep(4)
        # pyautogui.write(r'C:\Users\user\Documents\TRCH\Automationpython\assets\Filefoto\Gambar.jpg')
        # pyautogui.press('enter')
        # time.sleep(4)
        # driver.find_element(By.XPATH, '//*[@id="upload_foto_ciri_2"]').click()
        # time.sleep(4)
        # pyautogui.write(r'C:\Users\user\Documents\TRCH\Automationpython\assets\Filefoto\Gambar.jpg')
        # pyautogui.press('enter')
        # time.sleep(4)
        # driver.find_element(By.XPATH, '//*[@id="upload_foto_ciri_3"]').click()
        # time.sleep(4)
        # pyautogui.write(r'C:\Users\user\Documents\TRCH\Automationpython\assets\Filefoto\Gambar.jpg')
        # pyautogui.press('enter')
        # time.sleep(4)
        # #--------------------------------------------------------------
        # driver.find_element(By.ID, 'ciri').send_keys(Catatancirikhusus1)  
        # # #--------------------------------------------------------------
        # driver.find_element(By.ID, 'ciri2').send_keys(Catatancirikhusus2) 
        # # #--------------------------------------------------------------
        # driver.find_element(By.ID, 'ciri3').send_keys(Catatancirikhusus3)
        # # ======================================================================
        # driver.find_element(By.ID, 'tab-5').click()
        # # # ========================Input Tab Sidik Jari==========================
        # # #--------------------------------------------------------------
        # driver.find_element(By.ID, 'no_paspor').send_keys(Nopaspor)
        # # #--------------------------------------------------------------
        # driver.find_element(By.ID, 'rumus_daktil').send_keys(Rumus)
        # # #--------------------------------------------------------------
        # driver.find_element(By.ID, 'nomor_daktil').send_keys(Nopaspor)
        # # #--------------------------------------------------------------
        # driver.find_element(By.ID, 'pengambil_sj').send_keys(Pengambilansidikjari)
        # driver.find_element(By.ID, 'pengambil_sj').send_keys(Keys.ENTER)
        # #--------------------------------------------------------------
        # driver.find_element(By.XPATH, '//*[@id="pane-5"]/div/form/div/div[2]/div[2]/div/div/input').send_keys(Tanggalpengambilan)
        #======================================================================
        driver.find_element(By.ID, 'tab-6').click()
        #========================Input Tab Foto========================== 
        driver.find_element(By.XPATH,   '//*[@id="pane-6"]/form/div/div[1]/div/div/div/div/div[1]/button').click()
        time.sleep(3)
        pyautogui.write(r'C:\Users\user\Documents\TRCH\Automationpython\assets\Filefoto\Gambar.jpg')
        pyautogui.press('enter')
        driver.find_element(By.XPATH,   '//*[@id="pane-6"]/form/div/div[2]/div/div/div/div/div[1]/button').click()
        time.sleep(3)
        pyautogui.write(r'C:\Users\user\Documents\TRCH\Automationpython\assets\Filefoto\Gambar.jpg')
        pyautogui.press('enter')
        driver.find_element(By.XPATH,   '//*[@id="pane-6"]/form/div/div[3]/div/div/div/div/div[1]/button').click()
        time.sleep(3)
        pyautogui.write(r'C:\Users\user\Documents\TRCH\Automationpython\assets\Filefoto\Gambar.jpg')
        pyautogui.press('enter')
        #======================================================================
        # driver.find_element(By.ID, 'tab-7').click()
        #========================Input Tab Identitas lama========================== 
        #Submit
        driver.find_element(By.ID, 'submitButton').click() 
        WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'createButton')))