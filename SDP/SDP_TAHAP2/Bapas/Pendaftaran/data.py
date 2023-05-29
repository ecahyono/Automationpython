from faker import Faker
from datetime import datetime
import openpyxl
import random
from src import *

sheet = wb['KlienAPH']
opsiResidivis           = [cell.value for cell in sheet['C'] if cell.value is not None]
opsiwbpberesiko         = [cell.value for cell in sheet['J'] if cell.value is not None]
opsiwbpberpengaruh      = [cell.value for cell in sheet['K'] if cell.value is not None]
opsitempatasal          = [cell.value for cell in sheet['L'] if cell.value is not None]
opsitempattinggal       = [cell.value for cell in sheet['M'] if cell.value is not None]
opsikelamin             = [cell.value for cell in sheet['O'] if cell.value is not None]
opsikwarganegaraan      = [cell.value for cell in sheet['P'] if cell.value is not None]
opsinegara              = [cell.value for cell in sheet['Q'] if cell.value is not None]
opsiagama               = [cell.value for cell in sheet['R'] if cell.value is not None]
opsisuku                = [cell.value for cell in sheet['T'] if cell.value is not None]
opsistatuskawin         = [cell.value for cell in sheet['V'] if cell.value is not None]
opsiprovinsi            = [cell.value for cell in sheet['W'] if cell.value is not None]
opsiAsalinstansi        = [cell.value for cell in sheet['AC'] if cell.value is not None]
opsiJenisKejahatan      = [cell.value for cell in sheet['AD'] if cell.value is not None]
opsiDitahan             = [cell.value for cell in sheet['AH'] if cell.value is not None]
opsiJenisPekerjaan      = [cell.value for cell in sheet['AK'] if cell.value is not None]
opsiPendidikan          = [cell.value for cell in sheet['AO'] if cell.value is not None]
opsiKeahlian1           = [cell.value for cell in sheet['AQ'] if cell.value is not None]
opsiLevelKeahlian1      = [cell.value for cell in sheet['AS'] if cell.value is not None]
opsiKeahlian2           = [cell.value for cell in sheet['AT'] if cell.value is not None]
opsiLevelKeahlian2      = [cell.value for cell in sheet['AV'] if cell.value is not None]
opsiBentukRambut        = [cell.value for cell in sheet['BR'] if cell.value is not None]
opsiWarnaRambut         = [cell.value for cell in sheet['BS'] if cell.value is not None]
opsiBentukBibir         = [cell.value for cell in sheet['BT'] if cell.value is not None]
opsiBerkacamata         = [cell.value for cell in sheet['BU'] if cell.value is not None]
opsiBentukMata          = [cell.value for cell in sheet['BV'] if cell.value is not None]  
opsiWarnaMata           = [cell.value for cell in sheet['BW'] if cell.value is not None]  
opsiHidung              = [cell.value for cell in sheet['BX'] if cell.value is not None]
opsiRautMuka            = [cell.value for cell in sheet['BY'] if cell.value is not None]  
opsiTelinga             = [cell.value for cell in sheet['BZ'] if cell.value is not None]  
opsiMulut               = [cell.value for cell in sheet['CA'] if cell.value is not None]  
opsiLengan              = [cell.value for cell in sheet['CB'] if cell.value is not None]  
opsiTangan              = [cell.value for cell in sheet['CC'] if cell.value is not None]
opsiKaki                = [cell.value for cell in sheet['CD'] if cell.value is not None]  
opsiWarnaKulit          = [cell.value for cell in sheet['CE'] if cell.value is not None]

fake = Faker('id_ID')

NamaKlien             = fake.first_name()
NIK                   = fake.numerify('################')
Residivis             = fake.random.choice(opsiResidivis)
NamaAlias1            = fake.first_name()
NamaAlias2            = fake.first_name()
NamaAlias3            = fake.first_name()
NamaKecil1            = fake.first_name()
NamaKecil2            = fake.first_name()
NamaKecil3            = fake.first_name()
WBPBeresikoTinggi     = fake.random.choice(opsiwbpberesiko)
MemilikiPengaruh      = fake.random.choice(opsiwbpberpengaruh)
TempatAsal            = fake.random.choice(opsitempatasal)
TempatLahir           = fake.random.choice(opsitempattinggal)
TanggalLahir          = fake.date_of_birth().strftime('%d/%m/%Y')
JenisKelamin          = fake.random.choice(opsikelamin)
Kewarganegaraan       = fake.random.choice(opsikwarganegaraan)
Negara                = fake.random.choice(opsinegara)
Agama                 = fake.random.choice(opsiagama)
Agamalain             = 'Ateis'
Suku                  = fake.random.choice(opsisuku)
SukuLain              = 'suku lain'
StatusPerkawinan      = fake.random.choice(opsistatuskawin)
Provinsi              = fake.random.choice(opsiprovinsi)
# profile = fake.profile()
# Provinsi = profile['address'].split('\n')[-1].strip()
# Kota = 
AlamatRumah           = fake.address()
AlamatLain            = fake.address()
Telepon               = "08" + str(fake.random_int(100000000, 999999999))
KodePOS               = fake.postcode()
AsalInstansi          = fake.random.choice(opsiAsalinstansi)
JenisKejahatan        = fake.random.choice(opsiJenisKejahatan)
UraianKejahatan       = fake.sentence(nb_words=6)
pasalutama            = fake.random_element(elements=('Pasal 1', 'Pasal 2', 'Pasal 3', 'Pasal 4'))
pasaltambahan         = fake.random_element(elements=('Pasal 5', 'Pasal 6', 'Pasal 7', 'Pasal 8'))
Ditahan               = fake.random.choice(opsiDitahan)
TanggalDitahan        = datetime.strptime(fake.date(), '%Y-%m-%d').strftime('%d/%m/%Y')
NoSuratPenahanan      = fake.random_number(digits=10)
JenisPekerjaan        = fake.random.choice(opsiJenisPekerjaan)
JenisPekerjaanLain    = fake.word()
TempatBekerja         = fake.company()
KeteranganKerja       = fake.sentence(nb_words=6)
Pendidikan            = fake.random.choice(opsiPendidikan)
TingkatPendidikanLain = fake.word()
Keahlian1             = fake.random.choice(opsiKeahlian1)
Keahlian1Lain         = fake.word()
LevelKeahlian1        = fake.random.choice(opsiLevelKeahlian1)
Keahlian2             = fake.random.choice(opsiKeahlian2)
Keahlian2Lain         = fake.word()
LevelKeahlian2        = fake.random.choice(opsiLevelKeahlian2)
Minat                 = fake.random_element(elements=('Musik', 'Olahraga', 'Seni', 'Teknologi', 'Kuliner', 'Perjalanan'))
NamaAyah              = fake.first_name_male()
AlamatAyah            = fake.address()
NamaIbu               = fake.first_name_female()
AlamatIbu             = fake.address()
AnakKe                = fake.random_int(min=1, max=5)
Dari                  = fake.random_int(min=1, max=5)
NamaSudara1           = fake.first_name()
NamaSudara2           = fake.first_name()
NamaSudara3           = fake.first_name()
NamaSudara4           = fake.first_name()
JumlahIstriSuami      = fake.random_int(min=1, max=3)
NamaIstriSuami1       = fake.name_female()
AlamatIstriSuami      = fake.address()
JumlahAnak            = fake.random_int(min=1, max=5)
NamaAnak1             = fake.first_name()
NamaAnak2             = fake.first_name()
NmAnak3               = fake.first_name()
TeleponKeluarga       = "08" + str(fake.random_int(100000000, 999999999))
Tinggi                = fake.random_int(min=1, max=200)
Berat                 = fake.random_int(min=1, max=200)
BentukRambut          = fake.random.choice(opsiBentukRambut)
WarnaRambut           = fake.random.choice(opsiWarnaRambut)
BentukBibir           = fake.random.choice(opsiBentukBibir)
Berkacamata           = fake.random.choice(opsiBerkacamata)
BentukMata            = fake.random.choice(opsiBentukMata)
WarnaMata             = fake.random.choice(opsiWarnaMata)
Hidung                = fake.random.choice(opsiHidung)
RautMuka              = fake.random.choice(opsiRautMuka)
Telinga               = fake.random.choice(opsiTelinga)
Mulut                 = fake.random.choice(opsiMulut)
Lengan                = fake.random.choice(opsiLengan)
Tangan                = fake.random.choice(opsiTangan)
Kaki                  = fake.random.choice(opsiKaki)
WarnaKulit            = fake.random.choice(opsiWarnaKulit)
CacatTubuh            = fake.word()
CiriKhusus1           = fake.word()
CiriKhusus2           = fake.word()
CiriKhusus3           = fake.word()
NoPaspor              = fake.random_number(digits=8)
RumusD                = fake.word()
NomorD                = fake.random_number(digits=8)
TempatPengambilanSJ   = fake.city_name()
TanggalAmbil          = datetime.strptime(fake.date(), '%Y-%m-%d').strftime('%d/%m/%Y')

# print(NamaKlien)
# print(NIK)
# print(Residivis)
# print(NamaAlias1)
# print(NamaAlias2)
# print(NamaAlias3)
# print(NamaKecil1)
# print(NamaKecil2)
# print(NamaKecil3)
# print(WBPBeresikoTinggi)
# print(MemilikiPengaruh)
# print(TempatAsal)
# print(TempatLahir)
# print(TanggalLahir)
# print(JenisKelamin)
# print(Kewarganegaraan)
# print(Negara)
# print(Agama)
# print(Agamalain)
# print(Suku)
# print(SukuLain)
# print(StatusPerkawinan)
# print(Provinsi)
# # print(Kota)
# print(AlamatRumah)
# print(AlamatLain)
# print(Telepon)
# print(KodePOS)
# print(AsalInstansi)
# print(JenisKejahatan)
# print(UraianKejahatan)
# print(pasalutama)
# print(pasaltambahan)
# print(Ditahan)
# print(TanggalDitahan)
# print(NoSuratPenahanan)
# print(JenisPekerjaan)
# print(JenisPekerjaanLain)
# print(TempatBekerja)
# print(KeteranganKerja)
# print(Pendidikan)
# print(TingkatPendidikanLain)
# print(Keahlian1)
# print(Keahlian1Lain)
# print(LevelKeahlian1)
# print(Keahlian2)
# print(Keahlian2Lain)
# print(LevelKeahlian2)
# print(Minat)
# print(NamaAyah)
# print(AlamatAyah)
# print(NamaIbu)
# print(AlamatIbu)
# print(AnakKe)
# print(Dari)
# print(NamaSudara1)
# print(NamaSudara2)
# print(NamaSudara3)
# print(NamaSudara4)
# print(JumlahIstriSuami)
# print(NamaIstriSuami1)
# print(AlamatIstriSuami)
# print(JumlahAnak)
# print(NamaAnak1)
# print(NamaAnak2)
# print(NmAnak3)
# print(TeleponKeluarga)
# print(Tinggi)
# print(Berat)
# print(BentukRambut)
# print(WarnaRambut)
# print(BentukBibir)
# print(Berkacamata)
# print(BentukMata)
# print(WarnaMata)
# print(Hidung)
# print(RautMuka)
# print(Telinga)
# print(Mulut)
# print(Lengan)
# print(Tangan)
# print(Kaki)
# print(WarnaKulit)
# print(CacatTubuh)
# print(CiriKhusus1)
# print(CiriKhusus2)
# print(CiriKhusus3)
# print(NoPaspor)
# print(RumusD)
# print(NomorD)
# print(TempatPengambilanSJ)
# print(TanggalAmbil)
