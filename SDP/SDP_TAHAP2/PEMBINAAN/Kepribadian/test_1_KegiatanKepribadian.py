from Source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_1_KegiatanKepribadian.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


@pytest.mark.webtestx
def test_TC_SPPN_001_LoginOperator():
    print('Login aplikasi menggunakan akun dengan role Operator')
    Op_SPPN_Sorong(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role operator")
    attach(data=driver.get_screenshot_as_png())
    # input('Press Enter to continue...')

@pytest.mark.webtestx
def test_TC_SPPN_002_AksesMenuKepribadianOperator():
    print('Operator mengakses Operator mengakses submenu Kegiatan Pembinaan')
    sleep(driver)
    KepribadianKegiatanPembinaan(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')
    attach(data=driver.get_screenshot_as_png())


@pytest.mark.webtestx
def test_createProgramPembinaanKepribadian():

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
        tanggal                                   = fake.date_between(start_date='today', end_date='today').strftime('%d')

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
            driver.find_element(By.ID, "inputNamaProgram").send_keys(fake.text(10))
            Log.info ('Input Nama Program Pembinaan')

            print('Operator Input Tempat Pelaksanaan')
            driver.find_element(By.ID, "inputTempatPelaksanaan").send_keys(fake.city())
            Log.info ('Input Tempat Pelaksanaan')

            print('Operator Input Tanggal Pelaksanaan')
            driver.find_element(By.ID, "inputWaktuPelaksanaan").click()


            # print('Operator Input Tanggal Pelaksanaan')
            # driver.find_element(By.CSS_SELECTOR, ".w-full > .el-input__inner").click()
            # time.sleep(3)

            # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'"+tanggal+"')]")))
            # driver.find_element(By.XPATH, "//span[contains(.,'"+tanggal+"')]").click()

            # nav1 = driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div[3]/div/div/div[2]/form/div/div[2]/div/div/div/input")
            # ActionChains(driver).move_to_element(nav1).perform()
            # # waktu pelaksanaan\
            # driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div[3]/div/div/div[2]/form/div/div[2]/div/div/div/input").click()
            # Log.info('Operator mengisi jam pelatihan keterampilan ')

            # driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(5) > #submitButton > span").click()
            input('Press Enter to continue...')
            print('Operator Input sarana')
            time.sleep(2)
            driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[6]/div/div/div/div/input").click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ""+OptionSaranaFaker+""))).click()
            driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[6]/div/div/div/div/input").send_keys(Keys.TAB)
            Log.info ('Input sarana')

            time.sleep(2)
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
                input('Press Enter to continue...')
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Pilih')]")))
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "checkPeserta-0")))
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkAllPeserta .el-checkbox__inner"))).click()
                # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "checkPeserta-1"))).click()
                Log.info ('Input Nama Peserta')

                print('Pilih Peserta')
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Pilih')]"))).click()
                Log.info ('Pilih Peserta')

            elif PerluKelulusanFaker == "Tidak":
                pass

            print('Input Materi')
            driver.find_element(By.ID, "inputMateri").send_keys(fake.text(100))
            Log.info ('Input Materi')

            print('Input Keterangan')
            driver.find_element(By.ID, "inputKeterangan").send_keys(fake.text(100))
            Log.info ('Input Keterangan')  

            driver.find_element(By.ID, "submitButton").click()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buttonSearch > span")))
            # input('Press Enter to continue...')

            vars["x"] = driver.execute_script("return arguments[0]+1", vars["x"])
            condition = driver.execute_script("return (arguments[0]<2)", vars["x"])

            Log.info ('Operator menambahkan Program Pembinaan Kepribadian')
            input('Press Enter to continue...')
            LogOut(driver)


@pytest.mark.webtest
def test_Verifikasi_Kasie():
    print('Login aplikasi menggunakan akun dengan role kasie')
    kasie_SPPN_Sorong(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role kasie")
    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtest
def test_AksesMenuPersetujuan():
    sleep(driver)
    PersetujuanProgramDanPesertaKegiatan(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')
    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtest
def test_VerifikasiProgramPembinaan():
    sleep(driver)
    print('Kasie memilih filter belum verifikasi')

    # driver.find_element(By.XPATH, "(//input[@type='text'])[5]").click()
    # driver.find_element(By.XPATH, "//div[7]/div/div/div/ul/li[3]/span").click()
    # Log.info ('Kasie memilih filter belum verifikasi')
    # nav1 = driver.find_element(By.ID, "buttonSearch")
    # ActionChains(driver).move_to_element(nav1).perform()
    # driver.find_element(By.ID, "buttonSearch").click()

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".el-table__row:nth-child(1) .el-space__item > .el-button .h-5").click()
    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "WebDriverWait()el-table__row:nth-child(1) .el-space__item > .el-button .h-5"))).click()
    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buttonSearch > span"))).click()   
    driver.find_element(By.CSS_SELECTOR, ".w-full > .select-trigger .el-input__inner").click()
    driver.find_element(By.XPATH, "//div[9]/div/div/div/ul/li").click()
    driver.find_element(By.ID, "submitButton").click()
    time.sleep(1)
    input('Press Enter to continue...')
    LogOut(driver)


@pytest.mark.webtest
def test_Verifikasi_Kalapas():
    print('Login aplikasi menggunakan akun dengan role kasie')
    Kalapas_SPPN_sorong(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role kasie")
    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtest
def test_AksesMenuPersetujuanKalapas():
    sleep(driver)
    PersetujuanProgramDanPesertaKegiatan(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')
    attach(data=driver.get_screenshot_as_png())

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".el-table__row:nth-child(1) .el-space__item > .el-button .h-5").click()
    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "WebDriverWait()el-table__row:nth-child(1) .el-space__item > .el-button .h-5"))).click()
    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buttonSearch > span"))).click()   
    driver.find_element(By.CSS_SELECTOR, ".w-full > .select-trigger .el-input__inner").click()
    driver.find_element(By.XPATH, "//div[9]/div/div/div/ul/li").click()
    driver.find_element(By.ID, "submitButton").click()

    input('Press Enter to continue...')




    quit(driver)

