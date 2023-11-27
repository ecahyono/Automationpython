# VERIFIKASI CEPAT Register Litmas
from seleniumbase import BaseCase
import time
import os

class verifikasiregister(BaseCase):
  def testing_verifikasi(self):
    self.open("http://kumbang.torche.id:32400")
    self.maximize_window()
    self.wait_for_element("#login", timeout=2)
    self.click("#login")
    self.wait_for_element("#kc-form-login", timeout=2)
    self.input("#username", "kiandra")
    self.input("#password", "password")
    self.click("#kc-login")
    time.sleep(3)
    self.open("http://kumbang.torche.id:32400/bapas/pendaftaran/register-litmas")
    time.sleep(3)
    
    # while True:
    #   try:
    for i in range(24) :
      self.wait_for_element_clickable("#buttonCari")  
      self.click("#kode_status")
      self.click("#permohonan")
      self.click("#buttonCari")
      time.sleep(2)
      self.wait_for_element_clickable("#buttonCari")  
      self.click("#detailButton0")
      self.wait_for_element_clickable("#dropdownJenisRegistrasi")  
      self.click("#dropdownJenisRegistrasi")
      self.click("#DisetujuiDrop")
      self.click("#submitButton")
      self.wait_for_element_clickable("#buttonCari")  
      # except :
      #   self.open("http://kumbang.torche.id:32400")
        