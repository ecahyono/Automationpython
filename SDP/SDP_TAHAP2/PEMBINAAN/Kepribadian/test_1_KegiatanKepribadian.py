from Source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_1_KegiatanKepribadian.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


@pytest.mark.webtest
def test_TC_SPPN_001_LoginOperator():
    print('Login aplikasi menggunakan akun dengan role Operator')
    Op_SPPN(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role operator")
    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtest
def test_TC_SPPN_002_AksesMenuKepribadian():
    print('Operator mengakses Operator mengakses submenu Kegiatan Pembinaan')
    sleep(driver)
    KepribadianKegiatanPembinaan(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')
    attach(data=driver.get_screenshot_as_png())


@pytest.mark.webtest
def test_TC_SPPN_003_AksesHalamanTambahKegiatanPembinaan():

    sleep(driver)
    vars = {}
    vars["x"] = driver.execute_script("return 1")
    condition = True
    while condition:
        fake = Faker('id_ID')
        JenisPembinaan                                          = ['optionJenisPembinaan-0','optionJenisPembinaan-1','optionJenisPembinaan-2','optionJenisPembinaan-3','optionJenisPembinaan-4','optionJenisPembinaan-5','optionJenisPembinaan-6','optionJenisPembinaan-7','optionJenisPembinaan-8']
        OptionSarana                                            = ['optionSarana-0','optionSarana-1','optionSarana-2','optionSarana-3']
        OptionPrasarana                                         = ['optionPrasarana-0','optionPrasarana-1','optionPrasarana-2','optionPrasarana-3']
        OptionMitra                                             = ['optionMitra-0','optionMitra-1','optionMitra-2','optionMitra-3']

        for i in range(1):
            JenisPembinaanFaker                                 = random.choice(JenisPembinaan)
            OptionSaranaFaker                                   = random.choice(OptionSarana)
            OptionPrasaranaFaker                                = random.choice(OptionPrasarana)
            OptionMitraFaker                                    = random.choice(OptionMitra)
            

        
            print('Operator menambahkan Program Pembinaan Kepribadian')
            sleep(driver)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch"))).click()
            driver.find_element(By.ID, "createButton").click()

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


            print('Operator Input Tanggal Pelaksanaan')
            driver.find_element(By.CSS_SELECTOR, ".w-full > .el-input__inner").click()
            time.sleep(3)

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'1')]")))
            driver.find_element(By.XPATH, "//span[contains(.,'4')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "(//input[@name=''])[4]").click()
            driver.find_element(By.CSS_SELECTOR, ".el-form--label-top").click()
            driver.find_element(By.XPATH, "(//button[@id='submitButton']/span)[2]").click()
            Log.info ('Input Tanggal Pelaksanaan')

            print('Operator Input sarana')
            time.sleep(2)
            driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[6]/div/div/div/div/input").click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ""+OptionSaranaFaker+""))).click()
            Log.info ('Input sarana')

            print('Operator Input prasarana')
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div/form/div[7]/div/div/div/div[1]/input').click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ""+OptionPrasaranaFaker+""))).click()

            Log.info ('Input prasarana')

            print('Operator Mitra')
            driver.find_element(By.ID, "selectMitra").click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ""+OptionMitraFaker+""))).click()
            Log.info ('Input Mitra')




            vars["x"] = driver.execute_script("return arguments[0]+1", vars["x"])
            condition = driver.execute_script("return (arguments[0]<2)", vars["x"])



            Log.info ('Operator menambahkan Program Pembinaan Kepribadian')






            quit(driver)

