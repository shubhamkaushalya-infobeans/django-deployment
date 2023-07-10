import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

from first_app.models import Student,StudentBooks,Books
from faker import Faker
import random

fakegen = Faker()
students = ['Henry','John', 'Boby']

def add_students(fake_id,fake_lname,fake_email):
    stu = Student.objects.get_or_create(id=fake_id, first_name = random.choice(students),last_name = fake_lname, email = fake_email )[0]
    stu.save()
    return fake_id

def populate(N=10):
    for entry in range(N):
        fake_id = random.randint(1, 100000)
        fake_lname = fakegen.name()
        fake_email = 'test'+str(fake_id)+'gmail.com'
        # print(fake_id)
        stu = add_students(fake_id,fake_lname,fake_email)
        # print(stu)

        



if __name__ == '__main__':
    print('Start to call')
    populate(1)
# print('End of call')