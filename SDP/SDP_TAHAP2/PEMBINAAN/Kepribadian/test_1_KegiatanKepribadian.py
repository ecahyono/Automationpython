from Source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_1_KegiatanKepribadian.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

@pytest.mark.webtest
def test1_LoginOperatorKepribadian():
    print('Login aplikasi menggunakan akun dengan role Operator')
    sorong(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role operator")
    attach(data=driver.get_screenshot_as_png())
    # input('Press Enter to continue...')

@pytest.mark.webtest
def test2_AksesMenuKepribadianOperator():
    print('Operator mengakses Operator mengakses submenu Kegiatan Pembinaan')
    sleep(driver)
    KepribadianKegiatanPembinaan(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')
    attach(data=driver.get_screenshot_as_png())


@pytest.mark.webtest
def test3_createProgramPembinaanKepribadian():

    sleep(driver)
    vars = {}
    vars["x"] = driver.execute_script("return 1")
    condition = True
    while condition:
        fake = Faker('id_ID')
        JenisPembinaan                                          = ['optionJenisPembinaan-0','optionJenisPembinaan-1','optionJenisPembinaan-2','optionJenisPembinaan-3','optionJenisPembinaan-4','optionJenisPembinaan-5','optionJenisPembinaan-6','optionJenisPembinaan-7','optionJenisPembinaan-8']
        # OptionSarana                                            = ['optionSarana-0','optionSarana-1','optionSarana-2','optionSarana-3']
        OptionSarana                                            = ['optionSarana-0']
        # OptionPrasarana                                         = ['optionPrasarana-0','optionPrasarana-1','optionPrasarana-2','optionPrasarana-3']
        OptionPrasarana                                         = ['optionPrasarana-0']
        # OptionMitra                                             = ['optionMitra-0','optionMitra-1','optionMitra-2','optionMitra-3']
        OptionMitra                                             = ['optionMitra-0']
        PerluKelulusan                                          = ['Ya']
        tanggal                                                 = fake.date_between(start_date='today', end_date='today').strftime('%d')

        for i in range(1):
            JenisPembinaanFaker                                 = random.choice(JenisPembinaan)
            OptionSaranaFaker                                   = random.choice(OptionSarana)
            OptionPrasaranaFaker                                = random.choice(OptionPrasarana)
            OptionMitraFaker                                    = random.choice(OptionMitra)
            PerluKelulusanFaker                                 = random.choice(PerluKelulusan)
            

            # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buttonSearch > span")))
            # print('Operator menambahkan Program Pembinaan Kepribadian')
            sleep(driver)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "createButton"))).click()

            print('Operator memilih Jenis Pembinaan')
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "selectJenisPembinaan")))
            driver.find_element(By.ID, "selectJenisPembinaan").click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, JenisPembinaanFaker))).click()
            Log.info ('Pilih Jenis Pembinaan')

            print('Operator Input Nama Program Pembinaan')
            driver.find_element(By.ID, "inputNamaProgram").send_keys(fake.text(10) + " WL")
            Log.info ('Input Nama Program Pembinaan')

            print('Operator Input Tempat Pelaksanaan')
            driver.find_element(By.ID, "inputTempatPelaksanaan").send_keys(fake.city())
            Log.info ('Input Tempat Pelaksanaan')

            print('Operator Input Tanggal Pelaksanaan')
            driver.find_element(By.ID, "inputWaktuPelaksanaan").click()


            print('Operator Input Tanggal Pelaksanaan')
            driver.find_element(By.CSS_SELECTOR, ".w-full > .el-input__inner").send_keys(fake.date_between(start_date='today', end_date='today').strftime('%d/%m/%Y'))
            # input('Press Enter to continue...')
            driver.find_element(By.CSS_SELECTOR, ".w-full > .el-input__inner").send_keys(Keys.TAB)
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, ".w-full > .el-input__inner").send_keys(Keys.ENTER)
            Log.info('Operator mengisi jam pelatihan keterampilan ')
            
            driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(5) > #submitButton > span").click()

            print('Operator Input sarana')
            time.sleep(2)
            driver.find_element(By.XPATH,"(//input[@type='text'])[5]").click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ""+OptionSaranaFaker+""))).click()
            driver.find_element(By.XPATH,"(//input[@type='text'])[5]").send_keys(Keys.TAB)
            Log.info ('Input sarana')

            time.sleep(3)
            print('Operator Input prasarana')
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div/form/div[7]/div/div/div/div[1]/input').click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ""+OptionPrasaranaFaker+""))).click()
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div/form/div[7]/div/div/div/div[1]/input').send_keys(Keys.TAB)
            

            Log.info ('Input prasarana')

            print('Operator Mitra')
            driver.find_element(By.ID, "selectMitra").click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ""+OptionMitraFaker+""))).click()
            Log.info ('Input Mitra')

            print('input insruktur')

            driver.find_element(By.ID, "selectJenisInstruktur").click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "optionJenisInstruktur-0"))).click()
            Log.info ('Input Jenis Instruktur')

            print('Operator Input Nama Instruktur')
            driver.find_element(By.ID, "selectInstruktur").click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "optionInstruktur-0"))).click()
            Log.info ('Input Nama Instruktur')

            print(' Input Penanggung jawab ')
            driver.find_element(By.ID, "selectPenanggungJawab").click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "optionPenanggungJawab-0"))).click()
            Log.info ('Input Penanggung jawab')
            print('Perlu Kelulusan')

            if PerluKelulusanFaker == "Ya":
                driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(12) .el-switch__action").click()
                Log.info ('Perlu Kelulusan')

                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "createButtonPeserta"))).click()
                Log.info ('Tambah Peserta')

                print('Input Nama Peserta')
                # driver.find_element(By.CSS_SELECTOR, ".el-input--default > .el-input__inner").click()
                # driver.find_element(By.XPATH, "//span[contains(.,'200/halaman')]").click()
                # input('Press Enter to continue...')
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Pilih')]")))
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "checkPeserta-0")))
                # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkAllPeserta .el-checkbox__inner"))).click()
                # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "checkPeserta-1"))).click()
                input('Press Enter to continue input peserta...')
                Log.info ('Input Nama Peserta')

                print('Pilih Peserta')
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Pilih')]"))).click()
                Log.info ('Pilih Peserta')

            elif PerluKelulusanFaker == "Tidak":
                pass

            print('Input Materi')
            driver.find_element(By.ID, "inputMateri").send_keys(fake.text(100))
            Log.info ('Input Materi')
            driver.find_element(By.ID, "inputKeterangan").send_keys(fake.text(100))
            Log.info ('Input Keterangan')  


            print('Input Keterangan')
            driver.find_element(By.ID, "submitButton").click()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buttonSearch > span")))
            # input('Press Enter to continue...')

            vars["x"] = driver.execute_script("return arguments[0]+1", vars["x"])
            condition = driver.execute_script("return (arguments[0]<2)", vars["x"])

            Log.info ('Operator menambahkan Program Pembinaan Kepribadian')
            # input('Press Enter to continue...')

            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Berhasil Ditambahkan')]")))
       
            LogOut(driver)


@pytest.mark.webtest
def test4_LoginKasieVerifikasi_KasieProgram():
    print('Login aplikasi menggunakan akun dengan role kasie')
    kasie_SPPN_Sorong(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role kasie")
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    PersetujuanProgramDanPesertaKegiatan(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')
    attach(data=driver.get_screenshot_as_png())
    sleep(driver)

@pytest.mark.webtest
def test5_KasieVerifikasi_KasieProgram():
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buttonVerifikasiOtorisasi0 .h-5"))).click()
    driver.find_element(By.CSS_SELECTOR, "#selectStatus").click()
    driver.find_element(By.CSS_SELECTOR, "#selectStatus").send_keys(Keys.DOWN)
    driver.find_element(By.CSS_SELECTOR, "#selectStatus").send_keys(Keys.ENTER)
    driver.find_element(By.ID, "submitButton").click()
    time.sleep(2)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Berhasil Memverifikasi Data')]")))
    LogOut(driver)


@pytest.mark.webtest
def test6_Login_KalapasOtorisasiProgramKepribadian():
    print('Login aplikasi menggunakan akun dengan role kalapas')
    Kalapas_SPPN_sorong(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role kasie")

    PersetujuanProgramDanPesertaKegiatan(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
@pytest.mark.webtest
def test7_KalapasOtorisasiProgramKepribadian():
    time.sleep(2)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buttonVerifikasiOtorisasi0 .h-5"))).click()
    driver.find_element(By.CSS_SELECTOR, "#selectStatus").click()
    driver.find_element(By.CSS_SELECTOR, "#selectStatus").send_keys(Keys.DOWN)
    driver.find_element(By.CSS_SELECTOR, "#selectStatus").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Berhasil Memverifikasi Data')]")))
    time.sleep(1)
    LogOut(driver)



@pytest.mark.webtest
def test8_Login_Operator_CatatAbsensiOperator():
    print('Login aplikasi menggunakan akun dengan role Operator')
    sorong(driver)
    CatatAbsensi(driver)

@pytest.mark.webtest
def test9_Operator_CatatAbsensiOperator():
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/div[4]/div/div[3]/div/div/div/table/tbody/tr/td/div/div").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buttonCatatAbsensi-0-0 > span"))).click()
    input('Press Enter to continue...')
    # time.sleep(5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".el-input--large .el-input__suffix-inner svg"))).click()
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="selectPeserta"]'))).click()
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".el-select-group__title"))).click()
    driver.find_element(By.CSS_SELECTOR, ".el-select__input").click()
    
    driver.find_element(By.CSS_SELECTOR, ".el-select-group__title").click()
    driver.find_element(By.ID, "submitButton").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".mt-6 > #submitButton > span").click()

    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Berhasil Ditambahkan')]")))

    LogOut(driver)

@pytest.mark.webtest
def test10_Login_Kasie_VerifikasiPresensi():
    print('Login aplikasi menggunakan akun dengan role kalapas')
    kasie_SPPN_Sorong(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role kasie")

@pytest.mark.webtest
def test11_Kasie_VerifikasiPresensi():
    sleep(driver)
    VerifikasiPresensi(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div/div[4]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[1]/div/div').click()
    time.sleep(2)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buttonVerifikasiOtorisasi0-0 path:nth-child(2)"))).click()
    driver.find_element(By.CSS_SELECTOR, "#selectStatus").click()
    driver.find_element(By.CSS_SELECTOR, "#selectStatus").send_keys(Keys.DOWN)
    driver.find_element(By.CSS_SELECTOR, "#selectStatus").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Berhasil Memverifikasi Data')]")))
    time.sleep(1)
    LogOut(driver)

@pytest.mark.webtestx
def test12_Login_Operator_tambahKelulusan():
    print('Login aplikasi menggunakan akun dengan role kalapas')
    sorong(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role kasie")

@pytest.mark.webtestx
def test13_Operator_tambahKelulusan():
    sleep(driver)
    KelulusanPeserta(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    driver.find_element(By.ID, "catatKelulusan-0").click()
    i = 4
    for i in range(10):
        print(i)
        try:
            yoga = "#catatKelulusan" + str(i) + " .h-5"
            print(yoga)
        
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, yoga))).click()
            print(yoga)
            driver.find_element(By.ID, "no_sertifikat").send_keys(fake.isbn10())
            driver.find_element(By.ID, "pilihFile").click()
            Sertifikat(driver)
            driver.find_element(By.ID, "nilai").click()
            driver.find_element(By.ID, "nilai").send_keys("90")
            driver.find_element(By.ID, "nilai").send_keys("90")
            driver.find_element(By.ID, "predikat").click()
            driver.find_element(By.ID, "opt-baik").click()
            driver.find_element(By.XPATH, '//*[@id="submitButton"]').click()  
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Berhasil Ditambahkan')]")))
            time.sleep(2)
        except TimeoutException:
            print('No More Pages')
            
        i = i + 1
    LogOut(driver)
            
@pytest.mark.webtestx
def test14_LoginKasie_VerifikasiKelulusan():

    print('Login aplikasi menggunakan akun dengan role kasie')
    kasie_SPPN_Sorong(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role kasie")
    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtestx
def test15_Kasie_VerifikasiKelulusan():
    input('/n click enter untuk melanjutkan')
    sleep(driver)
    VerifikasiKelulusanPesertaKepribadian(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')
    attach(data=driver.get_screenshot_as_png())
   
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buttonVerifikasiOtorisasi0 .h-5"))).click()
    driver.find_element(By.CSS_SELECTOR, "#selectStatus").click()
    driver.find_element(By.CSS_SELECTOR, "#selectStatus").send_keys(Keys.DOWN)
    driver.find_element(By.CSS_SELECTOR, "#selectStatus").send_keys(Keys.ENTER)
    driver.find_element(By.ID, "submitButton").click()
    time.sleep(2)
    LogOut(driver)

@pytest.mark.webtestx
def test16_Login_Kalapas_otorisasiKelulusan():
    print('Login aplikasi menggunakan akun dengan role kalapas')
    Kalapas_SPPN_sorong(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role kasie")

    VerifikasiKelulusanPesertaKepribadian(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))

@pytest.mark.webtestx
def test17_Kalapas_otorisasiKelulusan():
    time.sleep(2)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buttonVerifikasiOtorisasi0 .h-5"))).click()
    driver.find_element(By.CSS_SELECTOR, "#selectStatus").click()
    driver.find_element(By.CSS_SELECTOR, "#selectStatus").send_keys(Keys.DOWN)
    driver.find_element(By.CSS_SELECTOR, "#selectStatus").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.ID, "submitButton").click()
    time.sleep(1)
    LogOut(driver)



      
    
       
      
         
