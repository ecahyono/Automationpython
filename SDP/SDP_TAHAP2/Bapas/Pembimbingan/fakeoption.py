from faker import Faker
from datetime import datetime
import openpyxl
from faker.providers import date_time
from datetime import datetime, timedelta
import random
from src import *

################-> input urutan Baris Di Exel yang akan di eksekusi
pembimbingan = 3


sheet = wb['PKpendampingan']
opsiJenisLayananBerikutnya    = [cell.value for cell in sheet['A'] if cell.value is not None]

fake = Faker('id_ID')

############################## PK->Pendampingan
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
Switchfield                   = fake.random_element(elements=('Tidak'))
jeniskel                      = fake.random_element(elements=('Laki-laki', 'Perempuan'))
metode                        = fake.random_element(elements=('wawancara', 'kunjungan','kuesioner'))
AlamatRumah                   = fake.address()
Radio                         = fake.random_element(elements=('Penolakan', 'Penyelesaian'))
Radio1                        = fake.random_element(elements=('Pengadilan Negeri','Pengadilan Tinggi','Mahkamah Agung'))
Pengadilan                    = tanggal_acak.strftime('%d/%m/%Y')
opsisesiterakhir              = fake.random_element(elements=('Telah Berakhir Masa Bimbingan','Pencabutan Pembimbingan','Meninggal Dunia'))
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

Pembimbng1 = 'Pembimbingan Diversi'
Pembimbng2 = 'Pembimbingan Penetapan Bagi Anak Berusia Kurang dari 12 Tahun'
Pembimbng3 = 'Pembimbingan Penetapan Tindakan Anak'
Pembimbng4 = 'Pembimbingan Pidana dengan Syarat Anak (pidana pembinaan di luar lembaga)'
Pembimbng5 = 'Pembimbingan Pidana dengan Syarat Anak (pelayanan masyarakat)'
Pembimbng6 = 'Pembimbingan Pidana dengan Syarat Anak (pidana pengawasan)'
Pembimbng7 = 'Pembimbingan Pidana Peringatan Anak'
Pembimbng8 = 'Pembimbingan Pidana Pelatihan Kerja Anak'
Pembimbng9 = 'Pembimbingan Asimilasi Anak'
Pembimbng10 = 'Pembimbingan CB Anak'
Pembimbng11 = 'Pembimbingan CMB Anak'
Pembimbng12 = 'Pembimbingan PB Anak'
Pembimbng13 = 'Pembimbingan Tambahan (After Care) Anak'
Pembimbng14 = 'Buku Ekspirasi Pembimbingan dan Pengawasan Anak'
Pembimbng15 = 'Pidana dengan Syarat'
Pembimbng16 = 'Pembimbingan Asimilasi'
Pembimbng17 = 'Pembimbingan CB'
Pembimbng18 = 'Pembimbingan CMB'
Pembimbng19 = 'Pembimbingan PB'
Pembimbng20 = 'Pembimbingan Tambahan After Care'
Pembimbng21 = 'Pembimbingan dan Pengawasan (buku pembantu register)'
