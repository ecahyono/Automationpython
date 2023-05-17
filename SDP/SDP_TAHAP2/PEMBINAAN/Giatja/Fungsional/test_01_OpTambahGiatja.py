from source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log1OpTambahGiatja.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

@pytest.mark.webtest
def test_SetupOsOpen():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()      

@pytest.mark.webtest
def test_TC_GIATJA_001():
    Log.info('Setup Os')
    Op_Giatja(driver)
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
    try:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "createButton")))
        driver.find_element(By.ID, "createButton").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "backButton")))
        attach(data=driver.get_screenshot_as_png())
        Log.info('Klik Button Tambah')
    except Exception as e:
        Log.info('Button Tambah Tidak Ditemukan' )
        print('ERROR FOUND',
            type(e).__name__,          # TypeError
            __file__,                  # /tmp/example.py
            e.__traceback__.tb_lineno  # 2
        )
        quit(driver)
        assert False

    sleep(driver)
    try:
        driver.find_element(By.ID, "bidangKegiatan").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,\'"+ KegiatanKerjaFaker +"')]/span")))
        driver.find_element(By.XPATH, "//li[contains(.,\'"+ KegiatanKerjaFaker +"')]").click()
        Log.info('Input Bidang Kegiatan')
        attach(data=driver.get_screenshot_as_png())
    except Exception as e:
        Log.info('Input Bidang Kegiatan Tidak Ditemukan' )
        print('ERROR FOUND',
            type(e).__name__,          # TypeError
            __file__,                  # /tmp/example.py
            e.__traceback__.tb_lineno  # 2
        )
        quit(driver)
        assert False

    sleep(driver)
    driver.find_element(By.ID, "jenisKegiatan").click()
    driver.find_element(By.ID, ""+JeniskegiatanFaker+"").click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Input Jenis Kegiatan')
   
    sleep(driver)
    try:
        driver.find_element(By.ID, "namaKegiatan").send_keys(namaKegiatanFaker)
        Log.info('Input Nama Kegiatan')
    except Exception as e:
        Log.info('Input Nama Kegiatan Tidak Ditemukan' )
        print('ERROR FOUND',
            type(e).__name__,          # TypeError
            __file__,                  # /tmp/example.py
            e.__traceback__.tb_lineno  # 2
        )
        quit(driver)
        assert False

    sleep(driver)
    try:
        driver.find_element(By.ID, "skalaKegiatan").click()
        driver.find_element(By.ID, ""+SkalakegiatanFaker+"").click()
        Log.info('Input Skala Kegiatan')
    except Exception as e:
        Log.info('Input Skala Kegiatan Tidak Ditemukan' )
        print('ERROR FOUND',
            type(e).__name__,          # TypeError
            __file__,                  # /tmp/example.py
            e.__traceback__.tb_lineno  # 2
        )
        quit(driver)
        assert False

    sleep(driver)
    try:
        driver.find_element(By.ID, "tanggalAwalKegiatan").send_keys(tanggalAwalKegiatanFaker)
        Log.info('Input Tanggal Awal Kegiatan')
    except Exception as e:
        Log.info('Input Tanggal Awal Kegiatan Tidak Ditemukan' )
        print('ERROR FOUND',
            type(e).__name__,          # TypeError
            __file__,                  # /tmp/example.py
            e.__traceback__.tb_lineno  # 2
        )
        quit(driver)
        assert False

    sleep(driver)
    try:
        driver.find_element(By.ID, "tanggalAkhirKegiatan").send_keys(tanggalAkhirKegiatanFaker)
        Log.info('Input Tanggal Akhir Kegiatan')
    except Exception as e:
        Log.info('Input Tanggal Akhir Kegiatan Tidak Ditemukan' )
        print('ERROR FOUND',
            type(e).__name__,          # TypeError
            __file__,                  # /tmp/example.py
            e.__traceback__.tb_lineno  # 2
        )
        quit(driver)
        assert False

    sleep(driver)
    try:
        driver.find_element(By.ID, "lokasiKegiatan").send_keys(lokasiKegiatanFaker)
        Log.info('Input Lokasi Kegiatan')
    except Exception as e:
        Log.info('Input Lokasi Kegiatan Tidak Ditemukan' )
        print('ERROR FOUND',
            type(e).__name__,          
            __file__,                  
            e.__traceback__.tb_lineno  
        )
        quit(driver)
        assert False

    sleep(driver)
    driver.find_element(By.ID, "areaKegiatan").click()
    driver.find_element(By.ID, ""+ areaFaker+"").click()
    Log.info('Input Area Kegiatan')


    sleep(driver)
    try:
        driver.find_element(By.ID, "luas").send_keys(luasLokasiKegiatanFaker)
        Log.info('Input Luas')
    except Exception as e:
        Log.info('Input Luas Tidak Ditemukan' )
        print('ERROR FOUND',
            type(e).__name__,          
            __file__,                  
            e.__traceback__.tb_lineno  
        )
        time.sleep(5)
        quit(driver)
        assert False

    sleep(driver)
    try:
        driver.find_element(By.ID, "jumlahRuang").send_keys(jumlahRuangKegiatanFaker)
        Log.info('Input Jumlah Ruang')
    except Exception as e:
        Log.info('Input Jumlah Ruang Tidak Ditemukan' )
        print('ERROR FOUND',
            type(e).__name__,          
            __file__,                  
            e.__traceback__.tb_lineno  
        )
        quit(driver)
        assert False

    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(7) .el-select__input").click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, ""+saranaFaker+"")))
    driver.find_element(By.ID, ""+saranaFaker+"").click()
    driver.find_element(By.CSS_SELECTOR, " .el-form-item:nth-child(7) > .el-form-item__label").click()
    Log.info('Input Sarana')

    sleep(driver)
    try:
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(8) .el-select__input").click()
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, ""+prasaranaFaker+"")))
        driver.find_element(By.ID, ""+prasaranaFaker+"").click()
        Log.info('Input Prasarana')
    except Exception as e:
        Log.info('Input Prasarana Tidak Ditemukan' )
        print('ERROR FOUND',
            type(e).__name__,          
            __file__,                  
            e.__traceback__.tb_lineno  
        )
        time.sleep(5)
        quit(driver)
        assert False

    sleep(driver)
    try:
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(9) .el-select__input").click()
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, ""+mitraFaker+"")))
        driver.find_element(By.ID, ""+mitraFaker+"").click()
        Log.info('Input Mitra')
    except Exception as e:
        Log.info('Input Mitra Tidak Ditemukan' )
        print('ERROR FOUND',
            type(e).__name__,          
            __file__,                  
            e.__traceback__.tb_lineno  
        )
        time.sleep(5)
        quit(driver)
        assert False

    sleep(driver)
    try:
        driver.find_element(By.ID, "uploadButton").click()
        uploadGambar(driver)
        Log.info('Input gambar')
    except Exception as e:
        Log.info('Input gambar Tidak Ditemukan' )
        print('ERROR FOUND',
            type(e).__name__,          
            __file__,                  
            e.__traceback__.tb_lineno  
        )
        time.sleep(5)
        quit(driver)
        assert False

    sleep(driver)
    try:
        driver.find_element(By.ID, "keterangan").send_keys(ketereranganFaker)
        Log.info('Input Keterangan')
    except Exception as e:
        Log.info('Input Keterangan Tidak Ditemukan' )
        print('ERROR FOUND',
            type(e).__name__,          
            __file__,                  
            e.__traceback__.tb_lineno  
        )
        time.sleep(5)
        quit(driver)
        assert False

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

    sleep(driver)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "createProduk")))
    driver.find_element(By.ID, "createProduk").click()
    Log.info('Click Button Create Produk')

    sleep(driver)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "idJenisProduk")))
    driver.find_element(By.ID, "idJenisProduk").click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ""+idjenisFaker+"")))
    driver.find_element(By.CSS_SELECTOR, ""+idjenisFaker+"").click()
    Log.info('Click Button Jenis Produk')

    sleep(driver)
    driver.find_element(By.ID, "namaProduk").click()
    driver.find_element(By.ID, "namaProduk").send_keys(namaProdukFaker)
    driver.find_element(By.XPATH, "//li[contains(.,\'"+ namaProdukFaker +"')]").click()
    Log.info('Input Nama Produk')

    sleep(driver)
    driver.find_element(By.ID, "jumlah").click()
    driver.find_element(By.ID, "jumlah").send_keys(jumlahprodukFaker)
    Log.info('Input Jumlah Produk')

    sleep(driver)
    driver.find_element(By.ID, "jenisSatuan").click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, ""+satuanFaker+"")))
    driver.find_element(By.ID, ""+satuanFaker+"").click()
    Log.info('Input Satuan Produk')

    sleep(driver)
    driver.find_element(By.ID, "harga").click()
    driver.find_element(By.ID, "harga").send_keys(HargaFaker)
    Log.info('Input Harga Produk')

    sleep(driver)
    driver.find_element(By.ID, "lamaPengerjaan").click()
    pyautogui.press('backspace')
    driver.find_element(By.ID, "lamaPengerjaan").send_keys(lamaPengerjaanFaker)
    Log.info('Input Lama Pengerjaan Produk')

    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, "#uploadButtonProduk > span").click()
    uploadGambar(driver)
    Log.info('Input Gambar Produk')

    sleep(driver)
    driver.find_element(By.ID, "keteranganProduk").click()
    driver.find_element(By.ID, "keteranganProduk").send_keys(ketereranganFaker)
    Log.info('Input Keterangan Produk')

    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, "#submitButtonProduk > span").click()
    Log.info('Click Button Submit Produk')

    sleep(driver)
    driver.execute_script("window.scrollTo(0,1160)")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".el-form").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#submitButton > span")))
    time.sleep(2)
    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "createButton")))

@pytest.mark.webtest
def test_TC_GIATJA_004():
    sleep(driver)
  
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
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#edit0 .h-5")))
    driver.find_element(By.CSS_SELECTOR, "#edit0 .h-5").click()
    Log.info('Click Button Edit')
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "keterangan")))
    driver.find_element(By.ID, "keterangan").send_keys(ketereranganFaker)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))

@pytest.mark.webtest
def test_TC_GIATJA_006():
    sleep(driver)
    try:

        sleep(driver)
        driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(7) .el-select__input").click()
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, ""+saranaFaker+"")))
        driver.find_element(By.ID, ""+saranaFaker+"").click()
        driver.find_element(By.CSS_SELECTOR, " .el-form-item:nth-child(7) > .el-form-item__label").click()

        driver.execute_script("window.scrollTo(0,1160)")
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#submitButton svg").click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "createButton")))
        Log.info("2.Klik button Ubah")
    except Exception as e:
        driver.execute_script("window.scrollTo(0,0)")
        driver.find_element(By.CSS_SELECTOR, "#backButton").click()
        Log.info('Input Keterangan Tidak Ditemukan' )
        print('ERROR FOUND',
            type(e).__name__,          
            __file__,                  
            e.__traceback__.tb_lineno  
        )
        time.sleep(5)
        assert False


@pytest.mark.webtest
def test_TC_GIATJA_007():
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".el-table__row:nth-child(1) .el-space__item > .el-button")))
    driver.find_element(By.CSS_SELECTOR, ".el-table__row:nth-child(1) .el-space__item > .el-button").click()
    Log.info('Click Button delete')
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Batalkan')]")))
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")))

@pytest.mark.webtest
def test_EXIT():
    quit(driver)
    Log.info('Exit')







    
    