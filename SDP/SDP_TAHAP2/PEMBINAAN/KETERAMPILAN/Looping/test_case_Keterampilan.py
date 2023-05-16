from source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('kETERAMPILAN.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

DataKeterampilan = wbd['KeterampilanData']

random1 = random.randint(1,9)
random2= random.randint(1,6)
random3 = random.randint(1,5)
peserta1 = random.randint(1,2)
peserta2 = random.randint(1,2)
peserta3 = random.randint(1,2)
peserta4 = random.randint(1,2)
peserta5 = random.randint(1,2)

Manufaktur                                  = DataKeterampilan['A'+str(random1)].value
jasa                                        = DataKeterampilan['B'+str(random2)].value
Agribisnis                                  = DataKeterampilan['C'+str(random3)].value
peserta0                                    = DataKeterampilan['D'+str(peserta1)].value
peserta1                                    = DataKeterampilan['E'+str(peserta2)].value
peserta2                                    = DataKeterampilan['F'+str(peserta3)].value
peserta3                                    = DataKeterampilan['G'+str(peserta4)].value
peserta4                                    = DataKeterampilan['H'+str(peserta5)].value
peserta5                                    = DataKeterampilan['I'+str(peserta5)].value
time.sleep(3)




@pytest.mark.webtest
def test_SetupKeterampilan():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')

@pytest.mark.webtest
def test_TC_KTR_001():      
    Op_Keterampilan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Login aplikasi menggunakan akun dengan role operator')

@pytest.mark.webtest
def test_TC_KTR_002():
    sleep(driver)
    MenuKegiatanPelatihan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Operator mengakses halaman Program Pelatihan Keterampilan')

@pytest.mark.webtest
def test_TC_KTR_003():
    driver.implicitly_wait(60)
    d = driver.find_element
    wait = WebDriverWait(driver, 50)
    sleep(driver)
    wait.until(EC.element_to_be_clickable((By.ID, "createButton")))
    d(By.ID, "createButton").click()
    Log.info('Operator mengklik tombol Tambah Program Pelatihan Keterampilan')

    wait.until(EC.element_to_be_clickable((By.ID, "backButton")))
    attach(data=driver.get_screenshot_as_png())

    wait.until(EC.element_to_be_clickable((By.ID, "jenisPelatihan")))
    d(By.ID, "jenisPelatihan").click()
    d(By.XPATH, "//li[contains(.,\'"+ PelatihanKeterampilanFaker +"')]").click()
    d(By.ID, "bidangPelatihan").click()
    if PelatihanKeterampilanExcel == 'Manufaktur':
        wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,\'"+ Manufaktur +"')]")))
        d(By.XPATH, "//li[contains(.,\'"+ Manufaktur +"')]").click()
        Log.info('Operator memilih jenis pelatihan keterampilan Manufaktur')
    elif PelatihanKeterampilanExcel == 'Jasa':
        sleep(driver)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,\'"+ jasa +"')]")))
        d(By.XPATH, "//li[contains(.,\'"+ jasa +"')]").click()
        Log.info('Operator memilih jenis pelatihan keterampilan Jasa')
    elif PelatihanKeterampilanExcel == 'Agribisnis':
        sleep(driver)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,\'"+ Agribisnis +"')]")))
        d(By.XPATH, "//li[contains(.,\'"+ Agribisnis +"')]").click()
        Log.info('Operator memilih jenis pelatihan keterampilan Agribisnis')

    d(By.ID, "tingkatPelatihan").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,\'"+ tingkatPelatihanFaker +"')]")))
    d(By.XPATH, "//li[contains(.,\'"+ tingkatPelatihanFaker +"')]").click()
    Log.info('Operator memilih tingkat pelatihan keterampilan ')

    d(By.ID, "namaProgram").send_keys(NamaProgramPelatihanFaker)
    Log.info('Operator mengisi nama program pelatihan keterampilan ')

    d(By.ID, "tempatPelaksanaan").send_keys(tempatPelatihanFaker)
    Log.info('Operator mengisi tempat pelatihan keterampilan ')

    d(By.ID, "waktuPelaksanaan").click()
    d(By.ID, "tanggalEmpty").send_keys(tanggalPelatihanFaker)
    Log.info('Operator mengisi waktu pelatihan keterampilan ')

    d(By.ID, "j").click()
    Log.info('Operator mengisi jam pelatihan keterampilan ')

    d(By.CSS_SELECTOR, ".flex:nth-child(5) > #submitButton > span").click()

    d(By.CSS_SELECTOR, ".el-form-item:nth-child(8) .el-select__input").click()
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@id=\'"+saranaFaker+"\']")))
    d(By.XPATH, "//li[@id=\'"+saranaFaker+"\']").click()
    Log.info('Operator memilih sarana pelatihan keterampilan ')

    d(By.CSS_SELECTOR, ".el-form-item:nth-child(9) .el-select__input").click()
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@id=\'"+prasaranaFaker+"\']")))
    d(By.XPATH, "//li[@id=\'"+prasaranaFaker+"\']").click()
    Log.info('Operator memilih prasarana pelatihan keterampilan ')

    d(By.CSS_SELECTOR, "#mitra").click()
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@id=\'"+mitraFaker+"\']")))
    d(By.XPATH, "//li[@id=\'"+mitraFaker+"\']").click()
    Log.info('Operator memilih mitra pelatihan keterampilan ')

    driver.execute_script("window.scrollTo(0,132)")

    d(By.ID, "instruktur-0").click()
    time.sleep(2)
    d(By.ID, "petugas-0").click()
    Log.info('Operator memilih instruktur pelatihan keterampilan ')

    d(By.ID, "instrukturSelect").click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@id=\'"+InstrukturOptionFaker+"\']")))
    d(By.XPATH, "//li[@id=\'"+InstrukturOptionFaker+"\']").click()
    Log.info('Operator memilih instruktur pelatihan keterampilan ')

    driver.execute_script("window.scrollTo(0,132)")

    d(By.ID, "penanggungJawan").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@id=\'"+penanggungJawabOptionFaker+"\']")))
    d(By.XPATH, "//li[@id=\'"+penanggungJawabOptionFaker+"\']").click()
    Log.info('Operator memilih penanggung jawab pelatihan keterampilan ')

    d(By.ID, "materi").send_keys(materiPelatihanFaker)
    Log.info('Operator mengisi materi pelatihan keterampilan ')

    d(By.ID, "keterangan").send_keys(keteranganFaker)
    Log.info('Operator mengisi keterangan pelatihan keterampilan ')
    
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#createButtonPeserta > span")))
    d(By.CSS_SELECTOR, "#createButtonPeserta > span").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Pilih')]")))
    if jumlahpesertaFaker == 1:
        d(By.CSS_SELECTOR, ""+peserta0+"").click()
        Log.info('Operator memilih 1 peserta pelatihan keterampilan ')
    elif jumlahpesertaFaker == 2:
        d(By.CSS_SELECTOR, ""+peserta0+"").click()
        d(By.CSS_SELECTOR, ""+peserta1+"").click()
        Log.info('Operator memilih 2 peserta pelatihan keterampilan ')
    elif jumlahpesertaFaker == 3:
        d(By.CSS_SELECTOR, ""+peserta0+"").click()
        d(By.CSS_SELECTOR, ""+peserta1+"").click()
        d(By.CSS_SELECTOR, ""+peserta2+"").click()
        Log.info('Operator memilih 3 peserta pelatihan keterampilan ')
    elif jumlahpesertaFaker == 4:
        d(By.CSS_SELECTOR, ""+peserta0+"").click()
        d(By.CSS_SELECTOR, ""+peserta1+"").click()
        d(By.CSS_SELECTOR, ""+peserta2+"").click()
        d(By.CSS_SELECTOR, ""+peserta3+"").click()
        Log.info('Operator memilih 4 peserta pelatihan keterampilan ')
    elif jumlahpesertaFaker == 5:
        d(By.CSS_SELECTOR, ""+peserta0+"").click()
        d(By.CSS_SELECTOR, ""+peserta1+"").click()
        d(By.CSS_SELECTOR, ""+peserta2+"").click()
        d(By.CSS_SELECTOR, ""+peserta3+"").click()
        d(By.CSS_SELECTOR, ""+peserta4+"").click()
        Log.info('Operator memilih 5 peserta pelatihan keterampilan ')
    d(By.XPATH, "//span[contains(.,'Pilih')]").click()
    
    d(By.ID, "submitButton").click()
    Log.info('Operator menekan tombol simpan pelatihan keterampilan ')

    wait.until(EC.element_to_be_clickable((By.ID, "createButton")))
    Log.info('Operator menambahkan Program Pelatihan Keterampilan')

@pytest.mark.webtest
def test_TC_KTR_004():
    driver.implicitly_wait(60)
    
    sleep(driver)
    d = driver.find_element

    wait = WebDriverWait(driver, 20) 
    wait.until(EC.element_to_be_clickable((By.ID, "createButton"))) 
    wait.until(EC.element_to_be_clickable((By.ID, "buttonSearch")))

    # d(By.ID, 'detail-0').click()
    # wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".circular")))
    # time.sleep(0.3)
    # d(By.ID, "backButton").click()

    attach(data=driver.get_screenshot_as_png())

    Log.info('Operator mengakses halaman Detail Program Pelatihan Keterampilan')

@pytest.mark.webtest
def test_TC_KTR_005():
    driver.implicitly_wait(60)
    sleep(driver)
    d = driver.find_element
    wait = WebDriverWait(driver, 20) 
    wait.until(EC.element_to_be_clickable((By.ID, "createButton"))) 
    wait.until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    time.sleep(1)
    d(By.ID, "update-0").click()
    Log.info('Operator mengakses halaman Ubah Program Pelatihan Keterampilan')


@pytest.mark.webtest
def test_TC_KTR_006():
    driver.implicitly_wait(60)
    sleep(driver)
    d = driver.find_element
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.ID, "submitButton")))
    wait.until(EC.element_to_be_clickable((By.ID, "keterangan")))
    driver.execute_script("window.scrollTo(0,972)")
    d(By.CSS_SELECTOR, '#keterangan').send_keys(keteranganFaker)
    d(By.ID, "submitButton").click()
    wait.until(EC.element_to_be_clickable((By.ID, "createButton"))) 
    Log.info('Operator mengubah data Program Pelatihan Keterampilan')

@pytest.mark.webtest
def test_TC_KTR_007():
    sleep(driver)
    # d = driver.find_element   
    # wait = WebDriverWait(driver, 20)
    # wait.until(EC.element_to_be_clickable((By.ID, "createButton"))) 
    # wait.until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h-5 w-5")))
    Log.info('Operator menghapus data Program Pelatihan Keterampilan')
    LogOut(driver)


@pytest.mark.webtest
def test_TC_KTR_008():      
    kasieKeterampilan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('"Berhasil login dan menu yang ditampilkan sesuai hak akses role kasie"')

@pytest.mark.webtest
def test_TC_KTR_009():
    sleep(driver)
    MenuPersetujuanPesertaKegiatan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Kasie mengakses halaman Persetujuan Peserta Kegiatan')

@pytest.mark.webtest
def test_TC_KTR_011():
    sleep(driver)
    driver.implicitly_wait(50)
    d = driver.find_element
    wait = WebDriverWait(driver, 30)
 
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#verifikasi-0 path:nth-child(2)")))

    d(By.CSS_SELECTOR, "#verifikasi-0 path:nth-child(2)").click()
    Log.info('Click Action Verifikasi')

    wait.until(EC.element_to_be_clickable((By.ID, "chooseVerifikasi")))
    d(By.ID, "chooseVerifikasi").click()
    wait.until(EC.element_to_be_clickable((By.ID, "verifikasi")))
    time.sleep(1)
    d(By.ID, "verifikasi").click()
    Log.info ('Click Verifikasi')

    d(By.ID, "keterangan").send_keys("Verifikasi Peserta Kegiatan")
    Log.info('Input Keterangan')
    wait.until(EC.element_to_be_clickable((By.ID, "submitButton")))
    d(By.ID, "submitButton").click()
    Log.info('Click Submit')
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Berhasil Memverifikasi Data')]")))
    Log.info('Kasie melakukan verifikasi peserta kegiatan pada kegiatan yang telah ditambahkan oleh operator')

@pytest.mark.webtest
def test_TC_KTR_010():
    sleep(driver)
    d=driver.find_element
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    d(By.CSS_SELECTOR, ".text-blue-500 .h-5").click()
    wait.until(EC.element_to_be_clickable((By.ID, "backButton")))
    
    Log.info('Kasie mengakses halaman Detail Program Pelatihan Keterampilan')
    LogOut(driver)


@pytest.mark.webtest
def test_TC_KTR_012():      
    KalapasKeterampilan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info("Login aplikasi menggunakan akundengan role kalapas")

@pytest.mark.webtest
def test_TC_KTR_013():
    sleep(driver)
    MenuPersetujuanPesertaKegiatan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Kalapas mengakses halaman Persetujuan Peserta Kegiatan')

@pytest.mark.webtest
def test_TC_KTR_015():
    sleep(driver)
    d = driver.find_element
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
   
    
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#verifikasi-0 path:nth-child(2)")))

    d(By.CSS_SELECTOR, "#verifikasi-0 path:nth-child(2)").click()
    Log.info('Click Action Verifikasi')

    wait.until(EC.element_to_be_clickable((By.ID, "chooseVerifikasi")))
    d(By.ID, "chooseVerifikasi").click()
    wait.until(EC.element_to_be_clickable((By.ID, "verifikasi")))
    d(By.ID, "verifikasi").click()
    Log.info ('Click Verifikasi')

    d(By.ID, "keterangan").send_keys("Verifikasi Peserta Kegiatan")
    Log.info('Input Keterangan')
    
    wait.until(EC.element_to_be_clickable((By.ID, "submitButton")))
    d(By.ID, "submitButton").click()
    Log.info('Click Submit')
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Berhasil Memverifikasi Data')]")))

    Log.info('Kasie melakukan verifikasi peserta kegiatan pada kegiatan yang telah ditambahkan oleh operator')

@pytest.mark.webtest
def test_TC_KTR_014():
    sleep(driver)
    d=driver.find_element
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    d(By.CSS_SELECTOR, ".text-blue-500 .h-5").click()
   

    Log.info('Kalapas mengakses halaman Detail Program Pelatihan Keterampilan')
    LogOut(driver)
@pytest.mark.webtest
def test_TC_KTR_016():      
    Op_Keterampilan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Login aplikasi menggunakan akun dengan role operator')

@pytest.mark.webtest
def test_TC_KTR_017():
    sleep(driver)
    MenuPresensiKegiatan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Operator mengakses halaman Program Pelatihan Keterampilan')

@pytest.mark.webtest
def test_TC_KTR_018():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "buttonSearch")))


    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    time.sleep(1)

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#absensi-0 > span")))
    time.sleep(2)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    driver.find_element(By.CSS_SELECTOR, "#absensi-0 > span").click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "backButton")))

    driver.find_element(By.CSS_SELECTOR, ".el-select__input").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "pesertaOption-0")))

    if JumlahPeserta == 1:  
        driver.find_element(By.ID, "pesertaOption-0").click()
    elif JumlahPeserta == 2:
        driver.find_element(By.ID, "pesertaOption-0").click()
        driver.find_element(By.ID, "pesertaOption-1").click()
    elif JumlahPeserta == 3:
        driver.find_element(By.ID, "pesertaOption-0").click()
        driver.find_element(By.ID, "pesertaOption-1").click()
        driver.find_element(By.ID, "pesertaOption-2").click()
    elif JumlahPeserta == 4:
        driver.find_element(By.ID, "pesertaOption-0").click()
        driver.find_element(By.ID, "pesertaOption-1").click()
        driver.find_element(By.ID, "pesertaOption-2").click()
        driver.find_element(By.ID, "pesertaOption-3").click()
    elif JumlahPeserta == 5:
        driver.find_element(By.ID, "pesertaOption-0").click()
        driver.find_element(By.ID, "pesertaOption-1").click()
        driver.find_element(By.ID, "pesertaOption-2").click()
        driver.find_element(By.ID, "pesertaOption-3").click()
        driver.find_element(By.ID, "pesertaOption-4").click()

    driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(2) > #submitButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Berhasil Ditambahkan')]")))
    driver.find_element(By.CSS_SELECTOR, ".mt-6 > #submitButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))


    attach(data=driver.get_screenshot_as_png())
    Log.info('Operator mencatat absensi peserta kegiatan')


@pytest.mark.webtest
def test_TC_KTR_019():
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "buttonSearch")))


   
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    time.sleep(1)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#absensi-0 > span")))
    time.sleep(2)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#detail-0 .h-5")))
    driver.find_element(By.CSS_SELECTOR, "#detail-0 .h-5").click()

    driver.find_element(By.CSS_SELECTOR, ".el-breadcrumb__item:nth-child(4) > .el-breadcrumb__inner").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))

    Log.info('Operator mengakses halaman Detail Absensi Kegiatan')
    LogOut(driver)

@pytest.mark.webtest
def test_TC_KTR_020():
    attach(data=driver.get_screenshot_as_png())      
    kasieKeterampilan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('"Login aplikasi menggunakan akun dengan role kasie"')

@pytest.mark.webtest
def test_TC_KTR_021():
    sleep(driver)
    MenuPersetujuanPresensiPesertaKegiatan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Kasie mengakses halaman Persetujuan Presensi Peserta Kegiatan')


@pytest.mark.webtest
def test_TC_KTR_022():
    attach(data=driver.get_screenshot_as_png())
    driver.implicitly_wait(60)
    sleep(driver)


    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))

    time.sleep(0.3)
    driver.find_element(By.CSS_SELECTOR, "#verifikasi-0 .h-5").click()

    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) > .el-form-item__content > .el-select .el-input__inner").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#submitButton > span")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "chooseVerifikasi")))
    driver.find_element(By.ID, "verifikasi").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "keterangan")))
    driver.find_element(By.ID, "keterangan").send_keys("Verifikasi")
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Berhasil Memverifikasi Data')]")))

    Log.info("Kasie melakukan v erifikasi pada presensi peserta kegiatan")

@pytest.mark.webtest
def test_TC_KTR_023():
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    driver.find_element(By.CSS_SELECTOR, "#detail-0 .h-5").click()
    
    Log.info('Kasie mengakses halaman Detail Absensi Kegiatan')
    LogOut(driver)

@pytest.mark.webtest
def test_TC_KTR_024():      
    Op_Keterampilan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Login aplikasi menggunakan akun dengan role operator')

@pytest.mark.webtest
def test_TC_KTR_025():
    sleep(driver)
    MenuPresensiKegiatan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Operator mengakses halaman Program Pelatihan Keterampilan')

@pytest.mark.webtest
def test_TC_KTR_026():
    sleep(driver)
    driver.implicitly_wait(30)
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))



    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5")))
    time.sleep(9)
    driver.find_element(By.CSS_SELECTOR, ".h-5").click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[contains(.,'Catat Kelulusan')]")))

    if JumlahPeserta == 1:  
        driver.find_element(By.ID, "catatKelulusan-0").click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "no_sertifikat")))
        driver.find_element(By.ID, "no_sertifikat").clear()
        driver.find_element(By.ID, "no_sertifikat").send_keys(no_sertifikatFaker0)
        driver.find_element(By.ID, 'pilihFile').click()
        uploadGambar(driver)
        driver.find_element(By.ID, 'nilai').send_keys(NilaiFaker0)
        driver.find_element(By.ID, 'predikat').send_keys(PredikatFaker0)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        driver.find_element(By.ID, 'submitButton').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detailKelulusan-0 > span")))
        
    elif JumlahPeserta == 2:
        driver.find_element(By.ID, "catatKelulusan-0").click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "no_sertifikat")))
        driver.find_element(By.ID, "no_sertifikat").clear()
        driver.find_element(By.ID, "no_sertifikat").send_keys(no_sertifikatFaker0)
        driver.find_element(By.ID, 'pilihFile').click()
        uploadGambar(driver)
        driver.find_element(By.ID, 'nilai').send_keys(NilaiFaker0)
        driver.find_element(By.ID, 'predikat').send_keys(PredikatFaker0)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        driver.find_element(By.ID, 'submitButton').click()
        time.sleep(10)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Catat Kelulusan')]")))
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detailKelulusan-0 > span")))
        
        driver.find_element(By.ID, "catatKelulusan-1").click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "no_sertifikat")))
        driver.find_element(By.ID, "no_sertifikat").clear()
        driver.find_element(By.ID, "no_sertifikat").send_keys(no_sertifikatFaker1)
        driver.find_element(By.ID, 'pilihFile').click()
        uploadGambar(driver)
        driver.find_element(By.ID, 'nilai').send_keys(NilaiFaker1)
        driver.find_element(By.ID, 'predikat').send_keys(PredikatFaker1)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        driver.find_element(By.ID, 'submitButton').click()
        time.sleep(10)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detailKelulusan-1 > span")))
        
    elif JumlahPeserta == 3:
        driver.find_element(By.ID, "catatKelulusan-0").click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "no_sertifikat")))
        driver.find_element(By.ID, "no_sertifikat").clear()
        driver.find_element(By.ID, "no_sertifikat").send_keys(no_sertifikatFaker0)
        driver.find_element(By.ID, 'pilihFile').click()
        uploadGambar(driver)
        driver.find_element(By.ID, 'nilai').send_keys(NilaiFaker0)
        driver.find_element(By.ID, 'predikat').send_keys(PredikatFaker0)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        driver.find_element(By.ID, 'submitButton').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))

    
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Catat Kelulusan')]")))
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detailKelulusan-0 > span")))
        

        driver.find_element(By.ID, "catatKelulusan-1").click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "no_sertifikat")))
        driver.find_element(By.ID, "no_sertifikat").clear()
        driver.find_element(By.ID, "no_sertifikat").send_keys(no_sertifikatFaker1)
        driver.find_element(By.ID, 'pilihFile').click()
        uploadGambar(driver)
        driver.find_element(By.ID, 'nilai').send_keys(NilaiFaker1)
        driver.find_element(By.ID, 'predikat').send_keys(PredikatFaker1)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        driver.find_element(By.ID, 'submitButton').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        time.sleep(2)
    
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Catat Kelulusan')]")))
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detailKelulusan-1 > span")))
        
        driver.find_element(By.ID, "catatKelulusan-2").click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "no_sertifikat")))
        driver.find_element(By.ID, "no_sertifikat").clear()
        driver.find_element(By.ID, "no_sertifikat").send_keys(no_sertifikatFaker2)
        driver.find_element(By.ID, 'pilihFile').click()
        uploadGambar(driver)
        driver.find_element(By.ID, 'nilai').send_keys(NilaiFaker2)
        driver.find_element(By.ID, 'predikat').send_keys(PredikatFaker2)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        driver.find_element(By.ID, 'submitButton').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detailKelulusan-2 > span")))
        
    elif JumlahPeserta == 4:
        driver.find_element(By.ID, "catatKelulusan-0").click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "no_sertifikat")))
        driver.find_element(By.ID, "no_sertifikat").clear()
        driver.find_element(By.ID, "no_sertifikat").send_keys(no_sertifikatFaker0)
        driver.find_element(By.ID, 'pilihFile').click()
        uploadGambar(driver)
        driver.find_element(By.ID, 'nilai').send_keys(NilaiFaker0)
        driver.find_element(By.ID, 'predikat').send_keys(PredikatFaker0)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        driver.find_element(By.ID, 'submitButton').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        time.sleep(2)
    
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Catat Kelulusan')]")))
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detailKelulusan-0 > span")))
        
        
        driver.find_element(By.ID, "catatKelulusan-1").click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "no_sertifikat")))
        driver.find_element(By.ID, "no_sertifikat").clear()
        driver.find_element(By.ID, "no_sertifikat").send_keys(no_sertifikatFaker1)
        driver.find_element(By.ID, 'pilihFile').click()
        uploadGambar(driver)
        driver.find_element(By.ID, 'nilai').send_keys(NilaiFaker1)
        driver.find_element(By.ID, 'predikat').send_keys(PredikatFaker1)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        driver.find_element(By.ID, 'submitButton').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        time.sleep(2)
    
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Catat Kelulusan')]")))
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detailKelulusan-1 > span")))
        
        
        driver.find_element(By.ID, "catatKelulusan-2").click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "no_sertifikat")))
        driver.find_element(By.ID, "no_sertifikat").clear()
        driver.find_element(By.ID, "no_sertifikat").send_keys(no_sertifikatFaker2)
        driver.find_element(By.ID, 'pilihFile').click()
        uploadGambar(driver)
        driver.find_element(By.ID, 'nilai').send_keys(NilaiFaker2)
        driver.find_element(By.ID, 'predikat').send_keys(PredikatFaker2)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        driver.find_element(By.ID, 'submitButton').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        time.sleep(2)
    
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Catat Kelulusan')]")))
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detailKelulusan-2 > span")))
        
        
        driver.find_element(By.ID, "catatKelulusan-3").click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "no_sertifikat")))
        driver.find_element(By.ID, "no_sertifikat").clear()
        driver.find_element(By.ID, "no_sertifikat").send_keys(no_sertifikatFaker3)
        driver.find_element(By.ID, 'pilihFile').click()
        uploadGambar(driver)
        driver.find_element(By.ID, 'nilai').send_keys(NilaiFaker3)
        driver.find_element(By.ID, 'predikat').send_keys(PredikatFaker3)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        driver.find_element(By.ID, 'submitButton').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detailKelulusan-0 > span")))
        

    elif JumlahPeserta == 5:
        driver.find_element(By.ID, "catatKelulusan-0").click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "no_sertifikat")))
        driver.find_element(By.ID, "no_sertifikat").clear()
        driver.find_element(By.ID, "no_sertifikat").send_keys(no_sertifikatFaker0)
        driver.find_element(By.ID, 'pilihFile').click()
        uploadGambar(driver)
        driver.find_element(By.ID, 'nilai').send_keys(NilaiFaker0)
        driver.find_element(By.ID, 'predikat').send_keys(PredikatFaker0)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        driver.find_element(By.ID, 'submitButton').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        time.sleep(2)
    
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Catat Kelulusan')]")))
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detailKelulusan-0 > span")))
        
        
        driver.find_element(By.ID, "catatKelulusan-1").click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "no_sertifikat")))
        driver.find_element(By.ID, "no_sertifikat").clear()
        driver.find_element(By.ID, "no_sertifikat").send_keys(no_sertifikatFaker1)
        driver.find_element(By.ID, 'pilihFile').click()
        uploadGambar(driver)
        driver.find_element(By.ID, 'nilai').send_keys(NilaiFaker1)
        driver.find_element(By.ID, 'predikat').send_keys(PredikatFaker1)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        driver.find_element(By.ID, 'submitButton').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        time.sleep(2)
    
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Catat Kelulusan')]")))
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detailKelulusan-1 > span")))
        
        
        driver.find_element(By.ID, "catatKelulusan-2").click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "no_sertifikat")))
        driver.find_element(By.ID, "no_sertifikat").clear()
        driver.find_element(By.ID, "no_sertifikat").send_keys(no_sertifikatFaker2)
        driver.find_element(By.ID, 'pilihFile').click()
        uploadGambar(driver)
        driver.find_element(By.ID, 'nilai').send_keys(NilaiFaker2)
        driver.find_element(By.ID, 'predikat').send_keys(PredikatFaker2)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        driver.find_element(By.ID, 'submitButton').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        time.sleep(2)
    
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Catat Kelulusan')]")))
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detailKelulusan-2 > span")))
        
        
        driver.find_element(By.ID, "catatKelulusan-3").click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "no_sertifikat")))
        driver.find_element(By.ID, "no_sertifikat").clear()
        driver.find_element(By.ID, "no_sertifikat").send_keys(no_sertifikatFaker3)
        driver.find_element(By.ID, 'pilihFile').click()
        uploadGambar(driver)
        driver.find_element(By.ID, 'nilai').send_keys(NilaiFaker3)
        driver.find_element(By.ID, 'predikat').send_keys(PredikatFaker3)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        driver.find_element(By.ID, 'submitButton').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        time.sleep(2)
    
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Catat Kelulusan')]")))
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detailKelulusan-3 > span")))
        
        
        driver.find_element(By.ID, "catatKelulusan-4").click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "no_sertifikat")))
        driver.find_element(By.ID, "no_sertifikat").clear()
        driver.find_element(By.ID, "no_sertifikat").send_keys(no_sertifikatFaker4)
        driver.find_element(By.ID, 'pilihFile').click()
        uploadGambar(driver)
        driver.find_element(By.ID, 'nilai').send_keys(NilaiFaker4)
        driver.find_element(By.ID, 'predikat').send_keys(PredikatFaker4)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        driver.find_element(By.ID, 'submitButton').click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detailKelulusan-4 > span")))
        
        
    
    Log.info('Operator mengklik tab Kegiatan Pelatihan')
    LogOut(driver)

@pytest.mark.webtest
def test_TC_KTR_027():      
    kasieKeterampilan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Login aplikasi menggunakan akun dengan role operator')

@pytest.mark.webtest
def test_TC_KTR_028():
    sleep(driver)
    VerifikasiKelulusanPesertaKegiatan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Operator mengakses halaman Program Pelatihan Keterampilan')


@pytest.mark.webtest
def test_TC_KTR_029():
    attach(data=driver.get_screenshot_as_png())
    driver.implicitly_wait(60)
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))


    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))

    time.sleep(0.3)
    driver.find_element(By.CSS_SELECTOR, "#verifikasi-0 .h-5").click()

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
    driver.find_element(By.ID, "chooseVerifikasi").click()
    driver.find_element(By.ID, "verifikasi").click()

    driver.find_element(By.ID, "keterangan").send_keys(PredikatFaker0)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(.,'Berhasil Memverifikasi Data')]")))


    

    Log.info("Kasie melakukan v erifikasi pada presensi peserta kegiatan")

@pytest.mark.webtest
def test_TC_KTR_030():
    attach(data=driver.get_screenshot_as_png())
    driver.implicitly_wait(60)
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    time.sleep(8)
    driver.find_element(By.ID, "detail-0").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "backButton")))
    LogOut(driver)



@pytest.mark.webtest
def test_TC_KTR_031():      
    KalapasKeterampilan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Login aplikasi menggunakan akun dengan role Kalapas')

@pytest.mark.webtest
def test_TC_KTR_032():
    sleep(driver)
    VerifikasiKelulusanPesertaKegiatan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Kalapas mengakses halaman Verifikasi Kelulusan Peserta Kegiatan')

@pytest.mark.webtest
def test_TC_KTR_033():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))


    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))

    time.sleep(0.3)
    driver.find_element(By.CSS_SELECTOR, "#verifikasi-0 .h-5").click()

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
    driver.find_element(By.ID, "chooseVerifikasi").click()
    driver.find_element(By.ID, "verifikasi").click()

    driver.find_element(By.ID, "keterangan").send_keys(PredikatFaker0)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(.,'Berhasil Memverifikasi Data')]")))

    Log.info('Kalapas melakukan otorisasi kelulusan untuk peserta kegiatan')

@pytest.mark.webtest
def test_TC_KTR_034():
    attach(data=driver.get_screenshot_as_png())
    driver.implicitly_wait(60)
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    time.sleep(8)
    driver.find_element(By.ID, "detail-0").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "backButton")))

    Log.info('Kalapas melihat detail peserta yang telah diverifikasi kelulusannya')
    LogOut(driver)


@pytest.mark.webtest
def test_TC_KTR_035():      
    Op_Keterampilan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Login aplikasi menggunakan akun dengan role Operator')

@pytest.mark.webtest
def test_TC_KTR_036():
    sleep(driver)
    LaporanPelatihanKeterampilan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Operator mengakses halaman Laporan Pelatihan Keterampilan')

# @pytest.mark.webtest
# def test_TC_KTR_037():
#     sleep(driver)
#     attach(data=driver.get_screenshot_as_png())
#     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonBulan-0-1")))
    
#     if BulanFaker == "01":
#         driver.find_element(By.ID, "buttonBulan-0-0").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Januari Laporan')
#     elif BulanFaker == "02":
#         driver.find_element(By.ID, "buttonBulan-0-1").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Febuari Laporan')
#     elif BulanFaker == "03":
#         driver.find_element(By.ID, "buttonBulan-0-2").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Maret Laporan')
#     elif BulanFaker == "04":
#         driver.find_element(By.ID, "buttonBulan-0-3").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('April Laporan')
#     elif BulanFaker == "05":
#         driver.find_element(By.ID, "buttonBulan-0-4").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Mei Laporan')
     
#     elif BulanFaker == "06":
#         driver.find_element(By.ID, "buttonBulan-0-5").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Juni Laporan')
     
#     elif BulanFaker == "07":
#         driver.find_element(By.ID, "buttonBulan-0-6").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Juli Laporan')
     
#     elif BulanFaker == "08":
#         driver.find_element(By.ID, "buttonBulan-0-7").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Agustus Laporan')
     
#     elif BulanFaker == "09":
#         driver.find_element(By.ID, "buttonBulan-0-8").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('September Laporan')
     
#     elif BulanFaker == "10":
#         driver.find_element(By.ID, "buttonBulan-0-09").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Oktober Laporan')
     
#     elif BulanFaker == "11":
#         driver.find_element(By.ID, "buttonBulan-0-10").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('November Laporan')
     
#     elif BulanFaker == "12":
#         driver.find_element(By.ID, "buttonBulan-0-11").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Desember Laporan')

#     driver.find_element(By.XPATH, "//button[contains(.,'OK')]").click()
#     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(.,'Membuat Laporan Berhasil !')]")))

#     Log.info('"Operator membuat Laporan Pelatihan Keterampilan"')
#     LogOut(driver)

# @pytest.mark.webtest
# def test_TC_KTR_038():      
#     kasieKeterampilan(driver)
#     attach(data=driver.get_screenshot_as_png())
#     Log.info('Login aplikasi menggunakan akun dengan role Kalapas')

# @pytest.mark.webtest
# def test_TC_KTR_039():
#     sleep(driver)
#     LaporanPelatihanKeterampilan(driver)
#     attach(data=driver.get_screenshot_as_png())
#     Log.info('Kasie mengakses halaman Laporan Pelatihan Keterampilan')


# @pytest.mark.webtest
# def test_TC_KTR_040():
#     sleep(driver)
#     attach(data=driver.get_screenshot_as_png())
#     WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "buttonBulan-0-1")))
    
#     if BulanFaker == "01":
#         driver.find_element(By.ID, "buttonBulan-0-0").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Januari Laporan')
#     elif BulanFaker == "02":
#         driver.find_element(By.ID, "buttonBulan-0-1").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Febuari Laporan')
#     elif BulanFaker == "03":
#         driver.find_element(By.ID, "buttonBulan-0-2").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Maret Laporan')
#     elif BulanFaker == "04":
#         driver.find_element(By.ID, "buttonBulan-0-3").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('April Laporan')
#     elif BulanFaker == "05":
#         driver.find_element(By.ID, "buttonBulan-0-4").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Mei Laporan')
     
#     elif BulanFaker == "06":
#         driver.find_element(By.ID, "buttonBulan-0-5").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Juni Laporan')
     
#     elif BulanFaker == "07":
#         driver.find_element(By.ID, "buttonBulan-0-6").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Juli Laporan')
     
#     elif BulanFaker == "08":
#         driver.find_element(By.ID, "buttonBulan-0-7").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Agustus Laporan')
     
#     elif BulanFaker == "09":
#         driver.find_element(By.ID, "buttonBulan-0-8").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('September Laporan')
     
#     elif BulanFaker == "10":
#         driver.find_element(By.ID, "buttonBulan-0-09").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Oktober Laporan')
     
#     elif BulanFaker == "11":
#         driver.find_element(By.ID, "buttonBulan-0-10").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('November Laporan')
     
#     elif BulanFaker == "12":
#         driver.find_element(By.ID, "buttonBulan-0-11").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Desember Laporan')
#     WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Belum Verifikasi')]")))
#     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".el-button:nth-child(2) > span")))
#     driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(2) > span").click()
#     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".w-full .el-input__inner")))
#     driver.find_element(By.CSS_SELECTOR, ".w-full .el-input__inner").click()
#     driver.find_element(By.XPATH, "//div[5]/div/div/div/ul/li").click()
#     driver.find_element(By.CSS_SELECTOR, ".el-textarea__inner").send_keys(KeteranganFaker)
#     driver.find_element(By.ID, "submitButton").click()
    
#     Log.info('Kasie melakukan verifikasi pada Laporan Pelatihan Keterampilan yang telah di generate oleh operator')
#     LogOut(driver)




# @pytest.mark.webtest
# def test_TC_KTR_041():      
#     KalapasKeterampilan(driver)
#     attach(data=driver.get_screenshot_as_png())
#     Log.info('Login aplikasi menggunakan akun dengan role Kalapas')

# @pytest.mark.webtest
# def test_TC_KTR_042():
#     sleep(driver)
#     LaporanPelatihanKeterampilan(driver)
#     attach(data=driver.get_screenshot_as_png())
#     Log.info('Kalapas mengakses halaman Laporan Pelatihan Keterampilan')


# @pytest.mark.webtest
# def test_TC_KTR_043():
#     sleep(driver)
#     attach(data=driver.get_screenshot_as_png())
#     WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "buttonBulan-0-1")))
    
#     if BulanFaker == "01":
#         driver.find_element(By.ID, "buttonBulan-0-0").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Januari Laporan')
#     elif BulanFaker == "02":
#         driver.find_element(By.ID, "buttonBulan-0-1").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Febuari Laporan')
#     elif BulanFaker == "03":
#         driver.find_element(By.ID, "buttonBulan-0-2").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Maret Laporan')
#     elif BulanFaker == "04":
#         driver.find_element(By.ID, "buttonBulan-0-3").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('April Laporan')
#     elif BulanFaker == "05":
#         driver.find_element(By.ID, "buttonBulan-0-4").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Mei Laporan')
     
#     elif BulanFaker == "06":
#         driver.find_element(By.ID, "buttonBulan-0-5").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Juni Laporan')
     
#     elif BulanFaker == "07":
#         driver.find_element(By.ID, "buttonBulan-0-6").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Juli Laporan')
     
#     elif BulanFaker == "08":
#         driver.find_element(By.ID, "buttonBulan-0-7").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Agustus Laporan')
     
#     elif BulanFaker == "09":
#         driver.find_element(By.ID, "buttonBulan-0-8").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('September Laporan')
     
#     elif BulanFaker == "10":
#         driver.find_element(By.ID, "buttonBulan-0-09").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Oktober Laporan')
     
#     elif BulanFaker == "11":
#         driver.find_element(By.ID, "buttonBulan-0-10").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('November Laporan')
     
#     elif BulanFaker == "12":
#         driver.find_element(By.ID, "buttonBulan-0-11").click()
#         sleep(driver)
#         attach(data=driver.get_screenshot_as_png())
#         Log.info('Desember Laporan')

#     WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Belum Verifikasi')]")))
#     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".el-button:nth-child(2) > span")))
#     driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(2) > span").click()
#     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".w-full .el-input__inner")))
#     driver.find_element(By.CSS_SELECTOR, ".w-full .el-input__inner").click()
#     driver.find_element(By.XPATH, "//div[5]/div/div/div/ul/li").click()
#     driver.find_element(By.CSS_SELECTOR, ".el-textarea__inner").send_keys(KeteranganFaker)
#     driver.find_element(By.ID, "submitButton").click()
    
#     Log.info('Kalapas melakukan verifikasi pada Laporan Pelatihan Keterampilan yang telah di Verifikasi oleh Kasie')
    
#     LogOut(driver)

@pytest.mark.webtest
def test_ExitKeterampilan():
    LogOut(driver)
    quit(driver)
    Log.info('Exit')

