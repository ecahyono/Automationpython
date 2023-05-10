from src import *
# init driver by os
@mark.fixture_penerimaan
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Memasukan User name dan Password di halaman Login')
	bapasbdg(driver)

A = wb['Register Pembimbingan']
g = 2  # barisexel
UPTO                        = A['A'+str(g)].value
NoregNama                   = A['B'+str(g)].value
jenisKlien                  = A['C'+str(g)].value
JenisPembimbingan           = A['D'+str(g)].value
DasarPembimbingan           = A['E'+str(g)].value
TglAwalBimbingan            = A['F'+str(g)].value
TglAkhirBimbignan           = A['G'+str(g)].value
CariPetugas                 = A['H'+str(g)].value
SuratDasarPembimbingan      = A['I'+str(g)].value
Asalsurat                   = A['J'+str(g)].value
Nosurat1                    = A['K'+str(g)].value
Nosurat1                    = A['L'+str(g)].value   
Perihalsurat1               = A['M'+str(g)].value   
SuratPengantarPenyerahan    = A['N'+str(g)].value   
BeritaAcaraSerahTerimaKlien = A['R'+str(g)].value
SuratPerintah               = A['V'+str(g)].value

@mark.fixture_pendampingan
def testpendampingan():
  Log.info('Menambah Data Register Pendampingan')
  driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/penolakan/create')

