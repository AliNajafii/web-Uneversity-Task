from django.test import TestCase
from . import models
from rekita_lessons import models as l_model
from django.db.models.sql.query import Query
from . import file_generator
import random

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
    for i in range(number):
        src = models.Source.objects.create(
        image = file_generator.random_image_dir(file_generator.files_dir),
        file = file_generator.random_file_dir(file_generator.files_dir),
        description =f'this is test dicription {i}',
        name = f'test_name {i}'
        )
        src.save()
        print(f'{i} instances made',end='\r')
    print('Source class done!')

def make_bulk_lesson(number):
    sources = models.Source.objects.all().count()
    for i in range(number):
        le = models.Lesson.objects.create(
        title = f'title_{i}',
        image = file_generator.random_image_dir(file_generator.files_dir),
        source = models.Source.objects.get(id = random.randint(1,sources)),
        description = f"this is test description {i}",
        term = '9798'
        )
        le.save()
        print(f'{i} instances made',end='\r')
    print('Lesson class done!')

def make_bulk_uiniversity(number):
    fields = models.Field.objects.all().count()
    for i in range(number):
        uni = models.University.objects.create(
        name = f'test_name_{i}'
        )
        uni.field.add(models.Field.objects.get(id = random.randint(1,fields)))
        uni.save()
        print(f'{i} instances made',end='\r')
    print('University class done!')

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
def get_num(cls):
    num = int(input("how many %s do you want to biuld?"%cls))
    return num
def main():
    n = get_num('Fields')
    make_bulk_fields(n)
    n = get_num('Attribute')
    make_bulk_attrri(n)
    n = get_num('Source')
    make_bulk_source(n)
    n = get_num("Lesson")
    make_bulk_lesson(n)
    n = get_num("University")
    make_bulk_uiniversity(n)
    print("All Done")
if __name__ == '__main__':
    main()
