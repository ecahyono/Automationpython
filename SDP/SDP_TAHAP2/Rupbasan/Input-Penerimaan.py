from my_module import *
# init driver by os
@mark.fixture_penerimaan
def testconfigandlogin():
	global driver, pathData
	driver = initDriver()
	oprupbasanbdg(driver)

@mark.fixture_penerimaan
def test_menmabhapenerimaan():
	tambah = wb['TambahubahPenerimaan']
	for colume in tambah.iter_rows(min_row=2, values_only=True):
		JenisRegistrasi    				= colume[0] #Jenis Registrasi
		tglPenerimaan      				= colume[1] #Tanggal Penerimaan
		instansi           				= colume[2] #Instansi
		NomorSuratPengantar           	= colume[3] #Nomor Surat Pengantar
		NomorSuratPerintahPenyitaan		= colume[4] #Nomor Surat Perintah Penyitaan
		TanggalSuratPerintahPenyitaan   = colume[5] #Tanggal Surat Perintah Penyitaan
		PengadilanPenyita           	= colume[6] #Pengadilan Penyita
		NomorSuratPenetapanPengadilan	= colume[7] #Nomor Surat Penetapan Pengadilan
		tglSuratPenetapanPengadilan     = colume[8] #Tanggal Surat Penetapan Pengadilan
		InstitusiPenempatan    			= colume[9] #Institusi Penempatan
		Pasal         					= colume[10] #Pasal
		KategoriPidana        			= colume[11] #Kategori Pidana
		JenisKejahatan           		= colume[12] #JenisKejahatan
		NoBAPenyitaan    				= colume[13] #NoBAPenyitaan
		NoSuratPernyataan   			= colume[14] #No. Surat Pernyataan
		Keterangan					    = colume[15] #Keterangan
		Petugaspenerima             	= colume[16] #Petugas Penerima
		Namapetugasyangmenyerahkan	    = colume[17] #Nama Petugas yang Menyerahkan
		NIPNRPPetugasyangMenyerahkan  	= colume[18] #NIP/NRP Petugas yang Menyerahkan
		PangkatGolonganPetugas     		= colume[19] #Pangkat/Golongan Petugas yang Menyerahkan
		JabatanPetugas            		= colume[20] #Jabatan Petugas yang Menyerahkan
		IdentitasWBP         			= colume[21] #Identitas WBP
		Namasaksipenyerah            	= colume[22] #nama Petugas Instansi yang Menyerahkan
		NipNrpsaksiinstansipenyerh 		= colume[23] #nip Petugas Instansi yang Menyerahkan
		SaksiPenerimaan        			= colume[24] #Saksi Penerimaan
		Keterangandkumen      			= colume[25] #Keterangan Dokumen
		
		Penerimaan(driver)
		driver.find_element(By.ID, 'createButton').click()
		WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'dropdownJenisRegistrasi')))
		
		driver.find_element(By.ID, 'dropdownJenisRegistrasi').click()
		WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'jenisRegistrasi0')))
		driver.find_element(By.XPATH, "//li[contains(.,'"+ JenisRegistrasi+"')]").click()
		
		Tanggal_Penerimaan = driver.find_element(By.ID, 'inputTglPenerimaan')  
		Tanggal_Penerimaan.send_keys(tglPenerimaan)
		Tanggal_Penerimaan.send_keys(Keys.ENTER)
		
		driver.find_element(By.ID, 'dropdownInstansi').click()  
		WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'instansi0')))
		driver.find_element(By.XPATH, "//li[contains(.,'"+ instansi+"')]").click()
		
		driver.find_element(By.ID, 'inputNoRegInstansi').send_keys(NomorSuratPengantar)  
		driver.find_element(By.ID, 'inputNoSuratIzinPenyitaan').send_keys(NomorSuratPerintahPenyitaan) 
		
		Tanggal_Penerimaan = driver.find_element(By.ID, 'inputTglSuratIzinPenyitaan')  
		Tanggal_Penerimaan.send_keys(TanggalSuratPerintahPenyitaan)
		Tanggal_Penerimaan.send_keys(Keys.ENTER)
		
		driver.find_element(By.ID, 'dropdownPengadilanPenyita').click()
		WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'pengadilanNegeri0')))
		driver.find_element(By.XPATH, "//li[contains(.,'"+ PengadilanPenyita+"')]").click()
		
		driver.find_element(By.ID, 'inputNoSuratPenyitaan').send_keys(NomorSuratPenetapanPengadilan)   
		
		Tanggal_Surat_Izin_Penyitaan = driver.find_element(By.ID, 'inputTglSuratPenyitaan')  
		Tanggal_Surat_Izin_Penyitaan.send_keys(tglSuratPenetapanPengadilan)
		Tanggal_Surat_Izin_Penyitaan.send_keys(Keys.ENTER)
		
		driver.find_element(By.ID, 'dropdownInstitusiPenempatan').click()
		WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'institusiPenempatan0')))
		driver.find_element(By.XPATH, "//li[contains(.,'"+ InstitusiPenempatan+"')]").click()
		
		driver.find_element(By.ID, 'inputPasal').send_keys(Pasal)  
		
		driver.find_element(By.ID, 'dropdownKategoriPidana').click()
		WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'Pidana Umum')))
		driver.find_element(By.XPATH, "//li[contains(.,'"+ KategoriPidana+"')]").click()
		
		driver.find_element(By.ID, 'dropdownJenisKejahatan').click()
		WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'jenisKejahatan0')))
		driver.find_element(By.XPATH, "//li[contains(.,'"+ JenisKejahatan+"')]").click()
		
		driver.find_element(By.ID, 'inputNoBaPenyitaan').send_keys(NoBAPenyitaan)  
		driver.find_element(By.ID, 'inputNoSuratPernyataan').send_keys(NoSuratPernyataan)  
		driver.find_element(By.ID, 'inputKeterangan').send_keys(Keterangan)

		ppenerima = driver.find_element(By.ID, 'searchPetugasPenerima')
		ppenerima.click()
		ppenerima.send_keys(Petugaspenerima)
		WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'searchPetugasPenerima0')))
		driver.find_element(By.XPATH, "//li[contains(.,'"+ Petugaspenerima +"')]").click()
	
		driver.find_element(By.ID, 'nama_penyerah'	 ).send_keys(Namapetugasyangmenyerahkan) 
		driver.find_element(By.ID, 'nip_penyerah'	 ).send_keys(NIPNRPPetugasyangMenyerahkan) 
		driver.find_element(By.ID, 'pangkat_penyerah').send_keys(PangkatGolonganPetugas) 
		driver.find_element(By.ID, 'jabatan_penyerah').send_keys(JabatanPetugas) 
		
		tahanan = driver.find_element(By.ID, 'searchIdentitas-0')
		tahanan.click()
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'searchIdentitas-00')))
		driver.find_element(By.XPATH, "//li[contains(.,'"+ IdentitasWBP +"')]").click()

		driver.find_element(By.ID, "tab-petugas_instansi").click()
		driver.find_element(By.ID, 'nama_menyerahkan-0').send_keys(Namasaksipenyerah) 
		driver.find_element(By.ID, 'nip_menyerahkan-0' ).send_keys(NipNrpsaksiinstansipenyerh) 
				
		driver.find_element(By.ID, "tab-saksi_penerimaan").click()	

		ppenerima = driver.find_element(By.ID, 'searchSaksi-0')
		ppenerima.click()
		ppenerima.send_keys(SaksiPenerimaan)
		WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchSaksi-00')))
		driver.find_element(By.ID, 'searchSaksi-00').click()

		driver.find_element(By.ID, "tab-dokumen_files").click()		
		driver.find_element(By.ID, "verifikasi").click()
		WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'simpanVerifikasi')))
		inputpasswordverif = driver.find_element(By.ID, 'passwordVerifikasi')
		is_filled = inputpasswordverif.get_attribute("value") !=""
		if is_filled :
			pass
		else:
			inputpasswordverif.send_keys(environ.get("PASSSPV"))
		driver.find_element(By.ID, "simpanVerifikasi").click()
		WebDriverWait(driver, 50).until_not(EC.presence_of_element_located((By.ID, "simpanVerifikasi")))
		WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'pilihDokumenFile0')))
		driver.find_element(By.ID, "pilihDokumenFile0").click()
		time.sleep(3)
		pyautogui.write(environ.get("FILEPDF"))
		pyautogui.press('enter')
		driver.find_element(By.ID, 'keteranganDokumen-0').send_keys(Keterangandkumen) 
		
		driver.find_element(By.ID, "submitButton").click()
		WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
#############################################################################################################################
#############################################################################################################################
