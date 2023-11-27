from seleniumbase import BaseCase
import time
import os
from faker import Faker

fake = Faker('id_ID')

class verifikasiregister(BaseCase):
  def testing_verifikasi(self):
    self.open("http://kumbang.torche.id:32400")
    self.maximize_window()
    self.wait_for_element("#login", timeout=2)
    self.click("#login")
    self.wait_for_element("#kc-form-login", timeout=2)
    self.input("#username", "kamilapk")
    self.input("#password", "password")
    self.click("#kc-login")
    time.sleep(3)
    self.open("http://kumbang.torche.id:32400/bapas/litmas/penerimaan")
    time.sleep(3)
    h1_selector = '.text-2xl.font-semibold.ml-2'
    switch = '.el-switch__core'
    sekarang = '.el-button.el-button--text.el-button--small.el-picker-panel__link-btn'
    metodenya = fake.random_element(elements=('wawancara', 'kunjungan','kuesioner'))

    for i in range(24) :
      self.wait_for_element_clickable("#CariFilter")
      self.click("#dropdownStatusBapas")
      self.click("#diproses")
      self.click("#CariFilter")
      self.wait_for_element_clickable("#CariFilter")
      time.sleep(3)
      self.click("#buttonJenisLitmas0")
      self.wait_for_element_present(h1_selector)
      self.type("#tempat","BAPAS BANDUNG")
      self.click("#metode")
      self.click(f"#{metodenya}")
      self.type("#informan","Informan")
      # self.click(switch)
      self.click("#waktu")
      self.type("#waktu","1 November 2023 09:10:11")
      self.click(sekarang)
      self.click("#buttonSimpanSesi")
      self.wait_for_element_clickable("#buttonSimpan")
      self.click("#buttonSimpan")
      