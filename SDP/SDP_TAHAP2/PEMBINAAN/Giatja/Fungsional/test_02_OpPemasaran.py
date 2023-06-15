from source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_2_OpPemasaran.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrangeIndex = wb['Negara']

i = random.randint(1,200)

NamaNegara                                   = sheetrangeIndex['A'+str(i)].value
KotaTujuan                                   = sheetrangeIndex['B'+str(i)].value



@pytest.mark.webtestX
def test_TC_GIATJA_008():
    OpKemandirian(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Setup Os')
    sleep(driver)
    MenuPemasaran(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Operator mengakses halaman Pemasaran')

@pytest.mark.webtestX
def test_TC_GIATJA_009():
    sleep(driver)
    vars = {}
    vars["x"] = driver.execute_script("return 1")
    condition = True
    while condition:
        fake = Faker('id_ID')
        JenisPemasaran                                          = ['jenis3']
        # JenisPemasaran                                          = ['jenis0','jenis1','jenis2','jenis3','jenis4']
        # mitra                                                   = ['mitra0','mitra1','mitra2','mitra3','mitra4']
        mitra                                                   = ['mitra0']
        produk                                                  = ['produk0-opt7','produk0-opt2','produk0-opt3','produk0-opt4']
        satuan                                                  = ['pasang','Buah','Lusin','Kotak','Kotak','Unit']
        JeniskegiatanPemasaran                                  = ['jenisBidang0-opt0','jenisBidang0-opt1','jenisBidang0-opt2']
        JeniskegiatanPemasaran1                                 = ['#jenisBidang1-opt1 > span','#jenisBidang1-opt0 > span','#jenisBidang1-opt2 > span']
    
        JenisProdukPemasaran                                    = ['jenisProduk0-opt0','jenisProduk0-opt1','jenisProduk0-opt2']
        JenisProdukPemasaran1                                  = ['jenisProduk1-opt0','jenisProduk1-opt1']
       

        ProdukPemasaran                                         = ['produk0-opt0','produk0-opt1']
        ProdukPemasaran1                                         = ['produk1-opt0','produk1-opt1']

        
        

        for i in range(1):
            JenisPemasaranFaker                                 = random.choice(JenisPemasaran)
            NamaKegiatanFaker                                   = fake.text(max_nb_chars=7)
            TanggalKegiatanFaker                                = fake.date_between(start_date='today', end_date='today').strftime('%d/%m/%Y')
            MitraFaker                                          = random.choice(mitra)
            UraianFaker                                         = fake.text(max_nb_chars=255)
            LokasiFaker                                         = fake.address()
            produkFaker                                         = random.choice(produk)
            JumlahBarangFaker                                   = fake.random_int(min=1, max=7)
            satuanFaker                                         = random.choice(satuan)
            NilaiFaker                                          = fake.random_int(min=100000, max=1000000)
            NilaiFaker1                                         = fake.random_int(min=100000, max=1000000)
            NilaiFaker2                                         = fake.random_int(min=100000, max=1000000)

            jumlahpemasaranFaker                                = random.randint(2,2)

            JenisKegiatanPemasaranFaker                         = random.choice(JeniskegiatanPemasaran)
            JenisKegiatanPemasaranFaker1                        = random.choice(JeniskegiatanPemasaran1)


            JenisProdukPemasaranFaker                           = random.choice(JenisProdukPemasaran)
            JenisProdukPemasaranFaker1                          = random.choice(JenisProdukPemasaran1)
         

            ProdukPemasaranFaker                                = random.choice(ProdukPemasaran)
            ProdukPemasaranFaker1                               = random.choice(ProdukPemasaran1)
       
            


            

            sleep(driver)

            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "createButton")))
            driver.find_element(By.ID, "createButton").click()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "backButton")))
            attach(data=driver.get_screenshot_as_png())
            Log.info('Klik Button Tambah')

            driver.find_element(By.ID, "jenisPemasaran").click()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, ""+JenisPemasaranFaker+"")))
            driver.find_element(By.ID, ""+JenisPemasaranFaker+"").click()

            driver.find_element(By.ID, "namaKegiatan").click()
            driver.find_element(By.ID, "namaKegiatan").send_keys(NamaKegiatanFaker)

            driver.find_element(By.ID, "tanggalPemasaran").send_keys(TanggalKegiatanFaker)
            driver.find_element(By.ID, "tanggalPemasaran").send_keys(Keys.ENTER)
            

            driver.find_element(By.ID, "mitra").click()
            WebDriverWait(driver, 0).until(EC.element_to_be_clickable((By.ID, ""+MitraFaker+"")))
            driver.find_element(By.ID, ""+MitraFaker+"").click()
            time.sleep(2)

          


            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "kota")))
            driver.find_element(By.ID, "kota").send_keys(KotaTujuan)
        
            driver.find_element(By.XPATH, "//li[contains(.,\'"+ KotaTujuan +"')]").click()
            driver.find_element(By.ID, "kota").send_keys(Keys.ENTER)

            driver.find_element(By.ID, "lokasi").click()

            driver.find_element(By.ID, "lokasi").send_keys(LokasiFaker)

            driver.find_element(By.ID, "uploadButton").click()
            time.sleep(1)
            uploadGambar(pathData)

            driver.execute_script("window.scrollTo(0,432)")
            driver.find_element(By.ID, "uraianKegiatan").click()
            driver.find_element(By.ID, "uraianKegiatan").send_keys(UraianFaker)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#addProduk path")))
            nav1 = driver.find_element(By.CSS_SELECTOR, "#addProduk path")
            ActionChains(driver).move_to_element(nav1).perform()
        

            if jumlahpemasaranFaker == 1:

                driver.find_element(By.ID, "bidang0").click()
                driver.find_element(By.XPATH, "//li[contains(.,\'"+ KegiatanKerjaFaker +"')]").click()

                driver.find_element(By.ID, "jenisBidang0").click()
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, ""+JenisKegiatanPemasaranFaker+"")))
                driver.find_element(By.ID, ""+JenisKegiatanPemasaranFaker+"").click()

                driver.find_element(By.ID, "jenisProduk0").click()
                time.sleep(1)
                try :
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ""+JenisProdukPemasaranFaker+"")))
                    driver.find_element(By.ID, ""+JenisProdukPemasaranFaker+"").click()

                except:
                    driver.find_element(By.ID, "jenisProduk0-opt1").click()

                try:
                    driver.find_element(By.ID, "produk0").click()
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ""+ProdukPemasaranFaker+"")))
                    driver.find_element(By.ID, ""+ProdukPemasaranFaker+"").click()
                except:
                    driver.find_element(By.ID, "produk0-opt0").click()

                driver.find_element(By.ID, "nilai0").send_keys(NilaiFaker)
                
            elif jumlahpemasaranFaker == 2:
                driver.find_element(By.CSS_SELECTOR, "#addProduk path").click()

                driver.find_element(By.ID, "bidang0").click()
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,\'"+ KegiatanKerjaFaker +"')]")))
                driver.find_element(By.XPATH, "//li[contains(.,\'"+ KegiatanKerjaFaker +"')]").click()

                driver.find_element(By.ID, "jenisBidang0").click()
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, ""+JenisKegiatanPemasaranFaker+"")))
                driver.find_element(By.ID, ""+JenisKegiatanPemasaranFaker+"").click()

                driver.find_element(By.ID, "jenisProduk0").click()
                time.sleep(1)
                try :
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ""+JenisProdukPemasaranFaker+"")))
                    driver.find_element(By.ID, ""+JenisProdukPemasaranFaker+"").click()

                except:
                    driver.find_element(By.ID, "jenisProduk0-opt1").click()

                try:
                    driver.find_element(By.ID, "produk0").click()
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ""+ProdukPemasaranFaker+"")))
                    driver.find_element(By.ID, ""+ProdukPemasaranFaker+"").click()
                except:
                    driver.find_element(By.ID, "produk0-opt0").click()

                driver.find_element(By.ID, "nilai0").send_keys(NilaiFaker)

                #----------------------------------------

                driver.find_element(By.ID, "bidang1").click()
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ""+KegiatanKerjaFaker1+"")))
                driver.find_element(By.ID, ""+KegiatanKerjaFaker1+"").click()

                driver.find_element(By.ID, "jenisBidang1").click()
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ""+JenisKegiatanPemasaranFaker1+"")))
                driver.find_element(By.CSS_SELECTOR, ""+JenisKegiatanPemasaranFaker1+"").click()

                driver.find_element(By.ID, "jenisProduk1").click()
                time.sleep(1)
                try :
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ""+JenisProdukPemasaranFaker1+"")))
                    driver.find_element(By.ID, ""+JenisProdukPemasaranFaker1+"").click()

                except:
                    driver.find_element(By.ID, "jenisProduk1-opt1").click()

                try:
                    driver.find_element(By.ID, "produk1").click()
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ""+ProdukPemasaranFaker1+"")))
                    driver.find_element(By.ID, ""+ProdukPemasaranFaker1+"").click()
                except:
                    driver.find_element(By.ID, "produk1-opt0").click()

                driver.find_element(By.ID, "nilai1").send_keys(NilaiFaker1)

                

           
            
            driver.find_element(By.CSS_SELECTOR, "#submitButton > span").click()

            Log.info('Operator mengisi form Pemasaran')
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "createButton")))
            Log.info('Operator berhasil mengisi form Pemasaran')
            attach(data=driver.get_screenshot_as_png())
            vars["x"] = driver.execute_script("return arguments[0]+1", vars["x"])
            condition = driver.execute_script("return (arguments[0]<2)", vars["x"])
        

@pytest.mark.webtest
def test_TC_GIATJA_010():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "createButton")))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.XPATH, "//li[@id='semua']").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    driver.find_element(By.CSS_SELECTOR, "#lihat0 > span").click()
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__close > svg").click()
    Log.info('Operator melihat bukti setor yang telah di upload')
    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtest
def test_TC_GIATJA_011():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "createButton")))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.XPATH, "//li[@id='semua']").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))

    driver.find_element(By.XPATH, "//tr[1]/td[8]/div/div/div/a/button").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".el-image__inner")))
    driver.find_element(By.CSS_SELECTOR, "#backButton > span").click()
    Log.info("Operator mengakses halaman Detail Pemasaran")
    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtest
def test_TC_GIATJA_012():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "createButton")))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.XPATH, "//li[@id='semua']").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#updateButton0 .h-5")))
    driver.find_element(By.CSS_SELECTOR, "#updateButton0 .h-5").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#backButton > span")))

    Log.info('Operator mengakses halaman Edit Pemasaran')
    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtest
def test_TC_GIATJA_013():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "uraianKegiatan")))
    driver.find_element(By.ID, "uraianKegiatan").send_keys(fake.text(max_nb_chars=255))
    driver.find_element(By.CSS_SELECTOR, "#submitButton > span").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "createButton")))


    Log.info('Operator mengubah data Pemasaran')
    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtest
def test_TC_GIATJA_014():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "createButton")))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.XPATH, "//li[@id='semua']").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    driver.find_element(By.CSS_SELECTOR, ".el-table__row:nth-child(1) .el-space__item > .el-button path").click()
    driver.find_element(By.CSS_SELECTOR, ".el-button--primary > span").click()

    Log.info('Operator menghapus data Pemasaran')
    attach(data=driver.get_screenshot_as_png())


    quit(driver)







    
    