from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Penerimaan(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome(r'C:\Users\user\Documents\TRCH\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://192.168.2.11:32400/")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/div/div/span").click()
        driver.get("http://tiger.torche.id:8010/auth/realms/example/protocol/openid-connect/auth?client_id=frontend-sdp&redirect_uri=http%3A%2F%2F192.168.2.11%3A32400%2F&state=ed12019b-7490-43a6-8a68-f3be169fea82&response_mode=fragment&response_type=code&scope=openid&nonce=7f6b1bf2-18d3-41a1-bb38-ab8158efa4a1")
        driver.find_element(By.ID, "username").click()
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "username").send_keys("test-user")
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys("password")
        driver.find_element(By.ID, "kc-login").click()
        driver.get("http://192.168.2.11:32400/#state=ed12019b-7490-43a6-8a68-f3be169fea82&session_state=a1dfcc3a-8823-4a99-9bd9-4589e17e298c&code=d8cfcbe7-f88c-49c0-a99a-85e0351ca01a.a1dfcc3a-8823-4a99-9bd9-4589e17e298c.70cf2f8f-7a60-45ac-84c3-33c2f325021d")
        driver.find_element(By.XPATH, "//div[@id='app']/div/nav/ul/li[5]/div").click()
        driver.find_element(By.XPATH, "//div[@id='el-popper-container-6987']/div[7]/div/ul/li/a").click()
        driver.get("http://192.168.2.11:32400/rupbasan/penerimaan")
        driver.find_element(By.ID, "createButton").click()
        driver.find_element(By.ID, "input_jenis_registrasi_baran_basan").click()
        driver.find_element(By.XPATH, "//li[@id='RBR']/span").click()
        driver.find_element(By.XPATH, "//input[@name='']").click()
        driver.find_element(By.XPATH, "//div[@id='el-popper-container-6987']/div[13]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/div/span").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div/div[3]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div/div[3]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div/div[3]/div/div/input").send_keys("NOR123")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div/div[4]/div/div/div/div/input").click()
        driver.find_element(By.ID, "201507090003").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div/div[5]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div/div[5]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div/div[5]/div/div/input").send_keys("NORI1234")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div/div[6]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div/div[6]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div/div[6]/div/div/input").send_keys("NOSIP0980")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div/div[7]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='el-popper-container-6987']/div[15]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/div/span").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div[2]/div/div/div/div/div/input").click()
        driver.find_element(By.ID, "1").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div[2]/div[2]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div[2]/div[2]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div[2]/div[2]/div/div/input").send_keys("NoSP29384")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div[2]/div[3]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='el-popper-container-6987']/div[17]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/div/span").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div[2]/div[4]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div[2]/div[4]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div[2]/div[4]/div/div/input").send_keys("Pasal")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div[2]/div[5]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div[2]/div[5]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div[2]/div[5]/div/div/input").send_keys("NOBAST019342")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div[2]/div[6]/div/div/textarea").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div[2]/div[6]/div/div/textarea").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div/div[2]/div[6]/div/div/textarea").send_keys("Keterangan")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[2]/div/form/div/div/div/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[2]/div/form/div/div/div/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[2]/div/form/div/div/div/div/div/input").send_keys("Sara")
        driver.find_element(By.XPATH, "//li[@id='cariPetugasInternal']/div/div/table").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[3]/div/form/div/div/div/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[3]/div/form/div/div/div/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[3]/div/form/div/div/div/div/div/input").send_keys("rehan")
        driver.find_element(By.ID, "cariPetugasEksternal").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div/div/div/div/div/input").click()
        driver.find_element(By.ID, "Tersangka").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[2]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[2]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[2]/div/div/input").send_keys("NoRIND4354")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[3]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[3]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[3]/div/div/input").send_keys("Namasaya")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[4]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[4]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[4]/div/div/input").send_keys("2938479233984798")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[5]/div/div/div/div/input").click()
        driver.find_element(By.ID, "L").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[6]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='el-popper-container-6987']/div[22]/div/div/div/div/span").click()
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Perempuan'])[1]/following::*[name()='svg'][1]").click()
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Perempuan'])[1]/following::*[name()='svg'][1]").click()
        driver.find_element_by_link_text("2000").click()
        driver.find_element_by_link_text("Jan").click()
        driver.find_element(By.XPATH, "//div[@id='el-popper-container-6987']/div[22]/div/div/div/div[2]/table/tbody/tr[2]/td[6]/div/span").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[7]/div/div/textarea").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[7]/div/div/textarea").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[7]/div/div/textarea").send_keys("Alamat")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[8]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[8]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[8]/div/div/input").send_keys("0883274682348")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[9]/div/div/textarea").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[9]/div/div/textarea").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[5]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div[9]/div/div/textarea").send_keys("Keterangan")
        driver.find_element(By.ID, "tab-petugas_instansi").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[6]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div/div/label/span/span").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[6]/div/div[3]/div/div/div/table/tbody/tr/td/div/div[2]/form/div/div/div/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[6]/div/div[3]/div/div/div/table/tbody/tr/td/div/div[2]/form/div/div/div/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[6]/div/div[3]/div/div/div/table/tbody/tr/td/div/div[2]/form/div/div/div/div/div/input").send_keys("made")
        driver.find_element(By.XPATH, "//div[@id='el-popper-container-6987']/div[23]/div/div/div/ul/li").click()
        driver.find_element(By.ID, "tab-saksi_penerimaan").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[7]/div/div[3]/div/div/div/table/tbody/tr/td/div/div/div/div/label[2]/span/span").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[7]/div/div[3]/div/div/div/table/tbody/tr/td/div/div[2]/form/div/div/div/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[7]/div/div[3]/div/div/div/table/tbody/tr/td/div/div[2]/form/div/div/div/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div/div[2]/div/div/form/div[7]/div/div[3]/div/div/div/table/tbody/tr/td/div/div[2]/form/div/div/div/div/div/input").send_keys("rehan")
        driver.find_element(By.XPATH, "//div[@id='el-popper-container-6987']/div[24]/div/div/div/ul/li").click()
        driver.find_element(By.ID, "submitButton").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
