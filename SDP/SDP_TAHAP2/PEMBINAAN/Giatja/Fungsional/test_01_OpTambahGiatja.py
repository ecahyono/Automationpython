from source import *


Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_1_OpTambahGiatja.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


@pytest.mark.webtest
def test_TC_GIATJA_001():
    OpKemandirian(driver)
    Log.info('Login Op Giatja')
    attach(data=driver.get_screenshot_as_png())
    

@pytest.mark.webtest
def test_TC_GIATJA_002():
    sleep(driver)
    MenuGiatja(driver)
    Log.info('Operator mengakses halaman Kegiatan Kerja dan Produksi')
    attach(data=driver.get_screenshot_as_png())
    
@pytest.mark.webtest
def test_TC_GIATJA_003():
    sleep(driver)
    vars = {}
    vars["x"] = driver.execute_script("return 1")
    condition = True
    while condition:

        fake = Faker('id_ID')
        for i in range(1):
            namaKegiatanFakerX                 = fake.text(max_nb_chars=10)

        print('Click Create Button')
        #========= bulan sebelumnya
        # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "createButton")))
        # driver.find_element(By.ID, "filterBulanTahun").click()
        # driver.find_element(By.ID, "filterBulanTahun").send_keys("April 2023")
        # driver.find_element(By.ID, "buttonSearch").click()
        #========= bulan sebelumnya

        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "createButton")))
        driver.find_element(By.ID, "createButton").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "backButton")))
        attach(data=driver.get_screenshot_as_png())
        Log.info('Klik Button Tambah')

        sleep(driver)
        print('Input Bidang Kegiatan')
        driver.find_element(By.ID, "bidangKegiatan").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,\'"+ KegiatanKerjaFaker +"')]/span")))
        driver.find_element(By.XPATH, "//li[contains(.,\'"+ KegiatanKerjaFaker +"')]").click()
        Log.info('Input Bidang Kegiatan')
        attach(data=driver.get_screenshot_as_png())

        sleep(driver)
        print('Input Jenis Kegiatan')
        driver.find_element(By.ID, "jenisKegiatan").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, ""+JeniskegiatanFaker+"")))
        driver.find_element(By.ID, ""+JeniskegiatanFaker+"").click()
        attach(data=driver.get_screenshot_as_png())
        Log.info('Input Jenis Kegiatan')
    
        sleep(driver)
        driver.find_element(By.ID, "namaKegiatan").send_keys(namaKegiatanFakerX)
        Log.info('Input Nama Kegiatan')

        print('Input Skala Kegiatan')
        sleep(driver)
        driver.find_element(By.ID, "skalaKegiatan").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, ""+SkalakegiatanFaker+"")))
        driver.find_element(By.ID, ""+SkalakegiatanFaker+"").click()
        Log.info('Input Skala Kegiatan')

        print('Input Tanggal Awal Kegiatan')
        sleep(driver)
        driver.find_element(By.ID, "tanggalAwalKegiatan").send_keys(tanggalAwalKegiatanFaker)
        Log.info('Input Tanggal Awal Kegiatan')


        print('Input Tanggal Akhir Kegiatan')
        sleep(driver)
        driver.find_element(By.ID, "tanggalAkhirKegiatan").send_keys(tanggalAkhirKegiatanFaker)
        Log.info('Input Tanggal Akhir Kegiatan')

        print('Input Lokasi Kegiatan')
        sleep(driver)
        driver.find_element(By.ID, "lokasiKegiatan").send_keys(lokasiKegiatanFaker)
        Log.info('Input Lokasi Kegiatan')

        print('Input Alamat Kegiatan')
        sleep(driver)
        driver.find_element(By.ID, "areaKegiatan").click()
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, ""+ areaFaker+"")))
        driver.find_element(By.ID, ""+ areaFaker+"").click()
        Log.info('Input Area Kegiatan')

        print('Input Luas')
        sleep(driver)
        driver.find_element(By.ID, "luas").send_keys(luasLokasiKegiatanFaker)
        Log.info('Input Luas')

        print('Input jumlahRuang')
        sleep(driver)
        driver.find_element(By.ID, "jumlahRuang").send_keys(jumlahRuangKegiatanFaker)
        Log.info('Input Jumlah Ruang')
        
        print('Input  Sarana')
        sleep(driver)
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(7) .el-select__input").click()
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, ""+saranaFaker+"")))
        driver.find_element(By.ID, ""+saranaFaker+"").click()
        driver.find_element(By.CSS_SELECTOR, " .el-form-item:nth-child(7) > .el-form-item__label").click()
        Log.info('Input Sarana')

        print('Input Prasarana')
        sleep(driver)
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(8) .el-select__input").click()
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, ""+prasaranaFaker+"")))
        driver.find_element(By.ID, ""+prasaranaFaker+"").click()
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(8) .el-select__input").click()
        Log.info('Input Prasarana')
        
        print('Input Mitra')
        sleep(driver)
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(9) .el-select__input").click()
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, ""+mitraFaker+"")))
        driver.find_element(By.ID, ""+mitraFaker+"").click()
        Log.info('Input Mitra')
        
        print('Input Kegiatan')
        sleep(driver)
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(9) .el-select__input").click()
        driver.find_element(By.ID, "uploadButton").click()
        time.sleep(1)
        uploadGambar(driver)

        print('Input Kegiatan')
        sleep(driver)
        driver.find_element(By.ID, "keterangan").send_keys(ketereranganFaker)
        Log.info('Input Keterangan')
    
        print('Input Kegiatan')
        sleep(driver)
        driver.find_element(By.ID, "createPeserta").click()
        Log.info('Button Tambah Peserta')
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonFilter")))
        time.sleep(1)
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonFilter")))
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ""+ PesertaRandomFaker1 +"").click()
        Log.info('Tambah Peserta 1')
        driver.find_element(By.CSS_SELECTOR, ""+ PesertaRandomFaker2 +"").click()
        Log.info('Tambah Peserta 2')
        driver.find_element(By.CSS_SELECTOR, ""+ PesertaRandomFaker3 +"").click()
        Log.info('Tambah Peserta 3')
        driver.find_element(By.ID, "buttonDaftarkan").click()
        Log.info('Click Button Daftarkan')

        print('Click Button createProduk')
        sleep(driver)
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "createProduk")))
        driver.find_element(By.ID, "createProduk").click()
        Log.info('Click Button Create Produk')
        
        print('Input idJenisProduk')
        sleep(driver)
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "submitButtonProduk")))

        print('Input idJenisProduk')
        sleep(driver)
        driver.find_element(By.ID, "idJenisProduk").click()
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, ""+idjenisFaker+"")))
        driver.find_element(By.ID, ""+idjenisFaker+"").click()

        Log.info('Click Button Jenis Produk')

        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "submitButtonProduk")))
        print('Input Nama Produk')
      
        sleep(driver)
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "namaProduk")))
        driver.find_element(By.ID, "namaProduk").click()
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "produk0")))
        driver.find_element(By.ID, "produk0").click()
        

        Log.info('Input Nama Produk')
        sleep(driver)

        print('Input jumlah')
        sleep(driver)
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#jumlah .el-input__inner")))
        driver.find_element(By.CSS_SELECTOR, "#jumlah .el-input__inner").click()
        driver.find_element(By.CSS_SELECTOR, "#jumlah .el-input__inner").send_keys(jumlahprodukFaker)
        Log.info('Input Jumlah Produk')


        # driver.find_element(By.ID, "jenisSatuan").click()
        # time.sleep(1)
        # try :
        #     WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, ""+satuanFaker+"")))
        #     time.sleep(1)
        #     driver.find_element(By.ID, ""+satuanFaker+"").click()
        #     Log.info('Input Satuan Produk')
        # except:
        #     sleep(driver)

        # driver.find_element(By.ID, "harga").click()
        # driver.find_element(By.ID, "harga").send_keys(HargaFaker)
        # Log.info('Input Harga Produk')

        print('Input Gambar Produk')
        sleep(driver)
        driver.find_element(By.CSS_SELECTOR, "#uploadButtonProduk").click()
        uploadGambar(driver)
        Log.info('Input Gambar Produk')

        # sleep(driver)
        # driver.find_element(By.ID, "keteranganProduk").click()
        # driver.find_element(By.ID, "keteranganProduk").send_keys(ketereranganFaker)
        # Log.info('Input Keterangan Produk')
        
        # sleep(driver)
        # driver.find_element(By.ID, "lamaPengerjaan").click()
        # pyautogui.press('backspace')
        # driver.find_element(By.ID, "lamaPengerjaan").send_keys(lamaPengerjaanFaker)
        # Log.info('Input Lama Pengerjaan Produk')

        print('Click Button Submit Produk')
        sleep(driver)
        driver.find_element(By.CSS_SELECTOR, "#submitButtonProduk > span").click()
        Log.info('Click Button Submit Produk')

        print('Click Button Submit Kegiatan')
        sleep(driver)
        driver.execute_script("window.scrollTo(0,1160)")

        # driver.find_element(By.CSS_SELECTOR, ".el-form").click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#submitButton > span")))


        print('Input insentif')
        driver.find_element(By.ID, "insentif10").send_keys(NilaiFaker)

        driver.find_element(By.ID, "insentif11").send_keys(NilaiFaker)

        driver.find_element(By.ID, "insentif12").send_keys(NilaiFaker)


        Log.info('insentif')

        driver.find_element(By.ID, "submitButton").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "createButton")))
        vars["x"] = driver.execute_script("return arguments[0]+1", vars["x"])
        condition = driver.execute_script("return (arguments[0]<2)", vars["x"])


@pytest.mark.webtest
def test_TC_GIATJA_004():
    sleep(driver)
    time.sleep(8)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "filterColumn")))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.ID, "semua").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detail0 .h-5")))
    driver.find_element(By.CSS_SELECTOR, "#detail0 .h-5").click()
    time.sleep(10)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[4]/span")))
    driver.find_element(By.XPATH, "//span[4]/span").click()
    Log.info('Click Button Detail')
    
@pytest.mark.webtest
def test_TC_GIATJA_005():
    sleep(driver)
    time.sleep(5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#edit0 .h-5")))
    driver.find_element(By.CSS_SELECTOR, "#edit0 .h-5").click()
    Log.info('Click Button Edit')
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))

@pytest.mark.webtest
def test_TC_GIATJA_006():
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(7) .el-select__input").click()
    # kegiatan = driver.find_element(By.ID, "namaKegiatan")
    # kegiatan.clear()
    # kegiatan.send_keys(namaKegiatanFaker) 
    
    driver.find_element(By.ID, "keterangan").send_keys(keteranganFaker)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, ""+saranaFaker+"")))
    driver.find_element(By.ID, ""+saranaFaker+"").click()
    driver.find_element(By.CSS_SELECTOR, " .el-form-item:nth-child(7) > .el-form-item__label").click()

    driver.execute_script("window.scrollTo(0,1160)")
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submitButton")))
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#submitButton svg").click()
    WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.ID, "createButton")))
    Log.info("2.Klik button Ubah")


@pytest.mark.webtest
def test_TC_GIATJA_007():
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".el-table__row:nth-child(1) .el-space__item > .el-button")))
    driver.find_element(By.CSS_SELECTOR, ".el-table__row:nth-child(1) .el-space__item > .el-button").click()

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Batalkan')]")))
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[3]/button[2]")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(.,'Berhasil Menghapus')]")))
    Log.info('Delete Data')

    quit(driver)







    
    