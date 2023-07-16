from Source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_7_WaliPenilaian.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


@pytest.mark.webtest
def test_TC_SPPN_024_LoginWali():
    print('Login aplikasi menggunakan akun dengan role wali')
    wali_SURIYAH(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role Kasie")

@pytest.mark.webtest
def test_TC_SPPN_025_AksesMenuPenilaian():
    print('wali mengakses submenu Penilaian ')
    sleep(driver)
    MenuPenilaian(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')

@pytest.mark.webtest
def test_TC_SPPN_020():
    sleep(driver)
    print('wali melakukan penilaian')
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    driver.find_element(By.ID, "penilaian0").click()