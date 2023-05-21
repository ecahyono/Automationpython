from source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/log_4_Laporan.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)



   

@pytest.mark.webtest
def test_TC_GIATJA_022():
    Op_Giatja(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Setup Os Akses aplikasi SDP')
    sleep(driver)
    MenuLaporan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Operator mengakses halaman Laporan Kegiatan Kerja dan Produksi')

@pytest.mark.webtest
def test_TC_GIATJA_023():
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.ID, "Aprilsarana3")))
    if TanggalSetorFaker == "01":
        driver.find_element(By.ID, "Januarikegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Januari Kegiatan Kerja')
    elif TanggalSetorFaker == "02":
        driver.find_element(By.ID, "Febuarikegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Febuari Kegiatan Kerja')
    elif TanggalSetorFaker == "03":
        driver.find_element(By.ID, "Maretkegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Maret Kegiatan Kerja')
    elif TanggalSetorFaker == "04":
        driver.find_element(By.ID, "Aprilkegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('April Kegiatan Kerja')
    elif TanggalSetorFaker == "05":
        driver.find_element(By.ID, "Meikegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Mei Kegiatan Kerja')
     
    elif TanggalSetorFaker == "06":
        driver.find_element(By.ID, "Junikegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juni Kegiatan Kerja')
     
    elif TanggalSetorFaker == "07":
        driver.find_element(By.ID, "Julikegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juli Kegiatan Kerja')
     
    elif TanggalSetorFaker == "08":
        driver.find_element(By.ID, "Agustuskegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Agustus Kegiatan Kerja')
     
    elif TanggalSetorFaker == "09":
        driver.find_element(By.ID, "Septemberkegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('September Kegiatan Kerja')
     
    elif TanggalSetorFaker == "10":
        driver.find_element(By.ID, "Oktoberkegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Oktober Kegiatan Kerja')
     
    elif TanggalSetorFaker == "11":
        driver.find_element(By.ID, "Novemberkegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('November Kegiatan Kerja')
     
    elif TanggalSetorFaker == "12":
        driver.find_element(By.ID, "Desemberkegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Desember Kegiatan Kerja')

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'OK')]")))
    driver.find_element(By.XPATH, "//button[contains(.,'OK')]").click()

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(.,'Membuat Laporan Berhasil !')]")))
     
    Log.info('membuat Laporan Kegiatan Kerja dan Produksi')

    sleep(driver)
    quit(driver)






    
    