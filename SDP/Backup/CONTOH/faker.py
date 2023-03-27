import csv
from faker import Faker
import datetime
import random

def datagenerate(records, headers):
    a = records
    for i in range(0, int(a)+1):
       print
    fake = Faker('id_ID')
    fake1 = Faker('id_ID')   # To generate phone numbers
    

    with open("TEST.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            full_name = fake.name()
            FLname = full_name.split(" ")
            Fname = FLname[0]
            Lname = FLname[1]
            domain_name = "@testDomain.com"
            userId = Fname +"."+ Lname + domain_name
            my_word_list = ['Islam','Budha','Hindu','Katholik', 'Konghucu', 'Protestan' ]
            
            writer.writerow({
                    "NIP" : fake.year()+"1"f"{i+1:05}",
                    "Email Id" : userId,
                    "Prefix" : fake.prefix(),
                    "Name": fake.name(),
                    "Birth Date" : fake.date(pattern="%Y-%d-%m", end_datetime=datetime.date(2000, 1,1)),
                    "gender": "L",
                    "Phone Number" : fake1.phone_number(),
                    "Additional Email Id": fake.email(),
                    "Address" : fake.address(),
                    "City" : fake.city(),
                    "State" : fake.state(),
                    "Country" : fake.country(),
                    "Year":fake.year(),
                    "Time": fake.time(),
                    "Link": fake.url(),
                    "Text": fake.word(),
                    "Agama" : random.choice(my_word_list),
                    })
    
if __name__ == '__main__':
    records = 100
    headers = ["NIP", "Name", "Agama", "Birth Date", "gender", "City", "Email Id", "Prefix",   "Phone Number", "Additional Email Id",
               "Address", "State", "Country", "Year", "Time", "Link", "Text"]
    datagenerate(records, headers)
    print("CSV generation complete!")


