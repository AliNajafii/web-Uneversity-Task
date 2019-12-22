from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from . import models
from rekita_lessons import models as l_model
from django.db.models.sql.query import Query
import random
Query.sql
def make_bulk_fields(number):

    level = ['bs','ms','dr']
    for i in range(number):
        f = models.Field.objects.create(
        name= f'field_{i}',
        level = random.choices(level)
        )
        f.save()


def make_bulk_attrri(number):
    f_num = models.Field.objects.all().count()
    for i in range(number):
        attri = models.Attribute.objects.create(
        name = f'attribut_{i}',
        field = models.Field.objects.get(id= random.randint(1,f_num))
        )
        attri.save()
        print(f'{i} instances made',end='\r')
    print('attribut done!')


def make_bulk_source(number):
    pass

def make_bulk_lesson(number):
    pass

def make_bulk_uiniversity(number):
    pass

def  make_bulk_user(number):
    pass

def make_bulk_student(number):
    pass

def make_bulk_master(number):
    pass


def make_cp():
    pass

def make_task():
    pass

def make_respone():
    pass
