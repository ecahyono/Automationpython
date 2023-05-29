from faker import Faker
from datetime import datetime
import openpyxl
import random
from src import *

sheet = wb['PKpendampingan']
opsiJenisLayananBerikutnya    = [cell.value for cell in sheet['A'] if cell.value is not None]

fake = Faker('id_ID')

NamaKlien                     = fake.first_name()
NIK                           = fake.numerify('################')
TanggalPendampingan           = datetime(2023, 5, 13, 0, 0).strftime("%d/%m/%Y %H:%M")
NamaPenyidik                  = fake.first_name()
ResumeBeritaAcaraPendampingan = fake.random_element(elements=('Berita acara Pendampingan Pertama', 'Berita acara Pendampingan Kedua'))
TanggalPendampinganBerikutnya = datetime.strptime(fake.date(), '%Y-%m-%d').strftime('%d/%m/%Y')
JenisLayananBerikutnya        = fake.random.choice(opsiJenisLayananBerikutnya)
PKLayananBerikutnya           = fake.random_element(elements=('Iya', 'Tidak'))
# print(NamaKlien)
# print(NIK)
# print(Residivis)