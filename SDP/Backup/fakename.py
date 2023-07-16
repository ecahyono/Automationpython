from faker import Faker

# Membuat objek Faker
fake = Faker('id_ID')

# Menghasilkan 100 nama depan orang Indonesia
nama_depan = [fake.first_name_male() for _ in range(10)] + [fake.first_name_female() for _ in range(10)]

# Menampilkan nama depan
for nama in nama_depan:
    print(nama)