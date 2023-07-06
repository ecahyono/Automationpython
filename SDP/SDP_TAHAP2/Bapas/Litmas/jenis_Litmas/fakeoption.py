from faker import Faker
from datetime import datetime
import openpyxl
from faker.providers import date_time
from datetime import datetime, timedelta
import random
from jenis_Litmas.src import *

################-> input urutan Baris Di Exel yang akan di eksekusi
litmas = 17

sheet = wb['PKpendampingan']
opsiJenisLayananBerikutnya    = [cell.value for cell in sheet['A'] if cell.value is not None]

fake = Faker('id_ID')

############################## PK->Litmas
# Tanggal sebulan
tanggal_sekarang = datetime.now()
tanggal_awal = tanggal_sekarang - timedelta(days=30)
tanggal_akhir = tanggal_sekarang
# Menghasilkan tanggal acak dalam rentang waktu sebulan
tanggal_acak = fake.date_between_dates(date_start=tanggal_awal, date_end=tanggal_akhir)
fake.add_provider(date_time)

Tanggalbaisa                  = fake.date_time().strftime('%d/%m/%Y %H:%M')
Namapalsu                     = fake.first_name()
dateandtime                   = datetime.strptime(fake.date(), '%Y-%m-%d').strftime('%d/%m/%Y')
JenisLayananBerikutnya        = fake.random.choice(opsiJenisLayananBerikutnya)
Switchfield                   = fake.random_element(elements=('Iya','Tidak'))
jeniskel                      = fake.random_element(elements=('Laki-laki', 'Perempuan'))
metode                        = fake.random_element(elements=('wawancara', 'kunjungan','kuesioner'))
AlamatRumah                   = fake.address()
Radio                         = fake.random_element(elements=('Penolakan', 'Penyelesaian'))
tanggal_hasil                 = tanggal_acak.strftime('%d/%m/%Y')

B = wb['Register Litmas']
UPTOlitmas      = B['A'+str(litmas)].value
Namanoinduk     = B['B'+str(litmas)].value
JenisPNP        = B['C'+str(litmas)].value
Petpk           = B['E'+str(litmas)].value
suratperintah   = B['F'+str(litmas)].value
asalsurat1      = B['G'+str(litmas)].value
nosurat1        = B['H'+str(litmas)].value
tglsurat1       = B['I'+str(litmas)].value
perihalsurat1   = B['J'+str(litmas)].value
permintaanpenp  = B['K'+str(litmas)].value
nosurat2        = B['L'+str(litmas)].value
tglsurat2       = B['M'+str(litmas)].value
perihalsurat2   = B['N'+str(litmas)].value

Lit1 = 'Litmas Diversi'
Lit2 = 'Litmas Proses Peradilan Anak'
Lit3 = 'Litmas Program Pelayanan Anak(LPAS)'
Lit4 = 'Litmas Program Pembinaan Awal Anak'
Lit5 = 'Litmas Program Asimilasi Anak'
Lit6 = 'Litmas Program Re-Integrasi (CB) Anak'
Lit7 = 'Litmas Program Re-Integrasi (CMB) Anak'
Lit8 = 'Litmas Program Re-Integrasi (PB) Anak'
Lit9 = 'Litmas Pembimbingan'
Lit10 = 'Litmas Proses Peradilan Dewasa'
Lit11 = 'Litmas untuk Program Pelayanan di RUTAN'
Lit12 = 'Litmas Pembinaan Awal'
Lit13 = 'Litmas Program Asimilasi'
Lit14 = 'Litmas Program Re-Integrasi (CB)'
Lit15 = 'Litmas Program Re-Integrasi (CMB)'
Lit16 = 'Litmas Program Re-Integrasi (PB)'