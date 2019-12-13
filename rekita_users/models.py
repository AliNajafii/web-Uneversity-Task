from django.db import models
from django.shortcuts import reverse
__doc__ = """
created by Ali Najafi on 12/12/2019 at 11:57 pm
"""

class Person(models.Model):
    from django.contrib.auth import get_user_model

    user = models.OneToOneField(get_user_model(),
    on_delete=models.CASCADE)

    last_loged = models.DateTimeField(auto_now=True)

    join_date = models.DateTimeField(auto_now_add=True)

    class Meta(models.Model):
        abstract = True

class Student(Person):
    stid = models.IntegerField(10)
    uni = models.ForeignKey(
    "University",
    on_delete=models.CASCADE,
    related_query_name='students'
    )
    field = models.ForeignKey(
    "Field",
    on_delete=models.CASCADE
    )

    def get_main_dir(self):
        return f'students/student_{self.id}'

class Master(Person):
    uni = models.ForeignKey(
    "University",
    on_delete=models.CASCADE,
    related_query_name='masters'
    )
    field = field = models.ForeignKey(
    "Field",
    on_delete=models.CASCADE
    )

    def get_main_dir(self):
        return f'masters/master_{self.id}'

class University(models.Model):
    name = models.CharField(max_length = 1000)
    field = models.ManyToManyField(
    "Field"
    )

class Field(models.Model):

    name = models.CharField(max_length = 256)
    level = models.CharField(max_length = 256)

class Attribute(models.Model):
    """
        this class is for trend or attribute of a field.
        exp : computer engineering (field),
         software enginerring(attribute)
    """

    name = models.CharField(max_length = 256)
    field = models.ForeignKey(
    "Field",
    on_delete=models.CASCADE,
    to_field='name'
    )

class Lesson(models.Model):
    title = models.CharField(max_length = 256)
    image = models.ImageField(
    upload_to = 'lessons/images'
    )
    source = models.ForeignKey(
    "Source",
    on_delete=models.CASCADE,
    related_query_name='sources'
    )

    description = models.TextField(max_length=5000)
    term_choice = [('9798'),('97-98'),('9899'),('98-99')]
    term = models.CharField(choices=term_choice,max_length=50)

class Source(models.Model):
    image = models.ImageField(
    upload_to = get_source_image
    )
    file = models.FileField(
    upload_to= get_source_file
    )
    description = models.TextField(max_length=5000)
    name = models.CharField(max_length=200)

    def get_source_image(self):
        main_dir = 'lessons/source_%d/'%self.id
        return main_dir + 'image'

    def def get_source_file(self):
        main_dir = 'lessons/source_%d/'%self.id
        return main_dir + 'file'
