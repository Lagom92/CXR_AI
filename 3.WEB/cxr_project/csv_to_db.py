# csv 파일을 db에 저장하기
import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cxr_project.settings")
django.setup()

from screening.models import Center

hand = open('./data_to_db/screening_center.csv', encoding='UTF8')
reader = csv.reader(hand)

bulk_list = []
for row in reader:
    bulk_list.append(Center(
        city = row[0],
        town = row[1],
        institutions = row[2], 
        address = row[3],
        phone = row[4],
        specimen = row[5],
    ))

Center.objects.bulk_create(bulk_list)

print("Complete !!")