from faker import Faker
from datetime import datetime
import openpyxl
from faker.providers import date_time
from datetime import datetime, timedelta
import random
from src import *

################-> input urutan Baris Di Exel yang akan di eksekusi
pendampingan = 4
litmas = 17
pembimbingan = 3
pengawsan = 12
curd = 2

sheet = wb['PKpendampingan']
opsiJenisLayananBerikutnya    = [cell.value for cell in sheet['A'] if cell.value is not None]

fake = Faker('id_ID')

############################## PK->Pendampingan
fake.add_provider(date_time)
TanggalPendampingan           = fake.date_time().strftime('%d/%m/%Y %H:%M')
NamaPenyidik                  = fake.first_name()
ResumeBeritaAcaraPendampingan = fake.random_element(elements=('Berita acara Pendampingan Pertama', 'Berita acara Pendampingan Kedua'))
TanggalPendampinganBerikutnya = datetime.strptime(fake.date(), '%Y-%m-%d').strftime('%d/%m/%Y')
JenisLayananBerikutnya        = fake.random.choice(opsiJenisLayananBerikutnya)
Switchfield                   = fake.random_element(elements=('Iya', 'Tidak'))
TipeLampiran                  = fake.random_element(elements=('Pendampingan Diversi', 'Pendampingan Pelaksanaan Kesepakatan Diversi'))
TingkatPengadilan             = fake.random_element(elements=('Negeri', 'Tinggi','Mahkamah'))

tanggal_sekarang = datetime.now()
tanggal_sebelumnya = tanggal_sekarang - timedelta(days=30)

A = wb['Register Pembimbingan']
UPTObimbingan                           = A['A'+str(pembimbingan)].value
NoregNamabimbingan                      = A['B'+str(pembimbingan)].value
jenisKlienPembimbingan                  = A['C'+str(pembimbingan)].value
JenisPembimbingan                       = A['D'+str(pembimbingan)].value
DasarPembimbingan                       = A['E'+str(pembimbingan)].value
TglAwalBimbingan                        = tanggal_sebelumnya.strftime('%d/%m/%Y')
TglAkhirBimbignan                       = datetime.now().strftime('%d/%m/%Y')
CariPetugasPembimbingan                 = A['H'+str(pembimbingan)].value
SuratDasarPembimbingan                  = A['I'+str(pembimbingan)].value
AsalsuratPembimbingan                   = A['J'+str(pembimbingan)].value
Nosurat1Pembimbingan                    = A['K'+str(pembimbingan)].value
tglsuratPembimbingan                    = A['L'+str(pembimbingan)].value   
Perihalsurat1Pembimbingan               = A['M'+str(pembimbingan)].value   
SuratPengantarPenyerahanPembimbingan    = A['N'+str(pembimbingan)].value   
BeritaAcaraSerahTerimaKlienPembimbingan = A['R'+str(pembimbingan)].value
SuratPerintahPembimbingan               = A['V'+str(pembimbingan)].value

B = wb['Register Litmas']
UPTOlitmas      = B['A'+str(litmas)].value
Namanoinduklitmas     = B['B'+str(litmas)].value
Jenislitmas     = B['C'+str(litmas)].value
Petpklitmas           = B['E'+str(litmas)].value
suratperintah   = B['F'+str(litmas)].value
asalsurat1      = B['G'+str(litmas)].value
nosurat1        = B['H'+str(litmas)].value
tglsurat1       = B['I'+str(litmas)].value
perihalsurat1   = B['J'+str(litmas)].value
permintaanpenp  = B['K'+str(litmas)].value
nosurat2        = B['L'+str(litmas)].value
tglsurat2       = B['M'+str(litmas)].value
perihalsurat2   = B['N'+str(litmas)].value

C = wb['Register Pendampingan']
opsiJenisPendampingan    = [cell.value for cell in C['C'] if cell.value is not None]
opsiasalsurat            = [cell.value for cell in C['G'] if cell.value is not None]

UPTOdamping     = C['A'+str(pendampingan)].value
Namanoinduk     = C['B'+str(pendampingan)].value
JenisPNP        = C['C'+str(pendampingan)].value
Kelusia         = C['D'+str(pendampingan)].value
Petpk           = C['E'+str(pendampingan)].value
suratperintah   = C['F'+str(pendampingan)].value
asalsurat1      = fake.random.choice(opsiasalsurat)
nosurat1        = C['H'+str(pendampingan)].value
tglsurat1       = datetime.strptime(fake.date(), '%Y-%m-%d').strftime('%d/%m/%Y')
perihalsurat1   = C['J'+str(pendampingan)].value
permintaanpenp  = C['K'+str(pendampingan)].value
nosurat2        = C['L'+str(pendampingan)].value
tglsurat2       = datetime.strptime(fake.date(), '%Y-%m-%d').strftime('%d/%m/%Y')
perihalsurat2   = C['N'+str(pendampingan)].value

D = wb['Register pengawasan']
UPTOawas                    = D['A'+str(pengawsan)].value
NoregNamapengawasan         = D['B'+str(pengawsan)].value
jenispengawasn              = D['C'+str(pengawsan)].value
CariPetugaspengawsan        = D['D'+str(pengawsan)].value
SuratDasarPembimbingan      = D['E'+str(pengawsan)].value
Asalsurat                   = D['F'+str(pengawsan)].value
nosurat1                    = D['G'+str(pengawsan)].value
tglsurat1                   = D['H'+str(pengawsan)].value
perihalsurat1               = D['I'+str(pengawsan)].value