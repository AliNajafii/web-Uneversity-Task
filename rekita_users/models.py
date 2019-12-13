from django.db import models
from django.shortcuts import reverse
from rekita_lessons import models as lesson_model
__doc__ = """
created by Ali Najafi on 12/12/2019 at 11:57 pm
"""

class Person(models.Model):
    from django.contrib.auth import get_user_model

    user = models.OneToOneField(get_user_model(),
    on_delete=models.CASCADE)

    last_loged = models.DateTimeField(auto_now=True)

    join_date = models.DateTimeField(auto_now_add=True)


def get_image(instance,f_name):
    return f'{instance.get_main_dir()}/picture/{f_name}'

class Student(Person):
    image = models.ImageField(
    upload_to = get_image
    )
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

    def send_response(self,task_id,*args,**kwargs):
            """
                this method is for sending the response
                to an exercise(Task). if the task DoesNotExists it returns False

            """
            if type(cp_id) == int:
                try:
                    task = lesson_model.Task.objects.get(id = task_id)
                    res = lesson_model.Response.objects.create(
                    task=task,*args,**kwargs
                    )
                    res.save()
                    return True
                except models.ObjectDoesNotExist:
                    return False
            else:
                 return False


    def get_courspanels(self):
        return self.objects.coursepanel_set.order_by('-date_created')
    def get_std_lessons_dict(self):
        return self.get_courspanels().values('lesson')
    def get_responses(self):
        return self.objects.response_set
    def get_masters_dict(self):
        return self.get_courspanels().values('master')



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


    def create_task(self,cp_id,*args,**kwargs):
        """
            master can make tasks with this method.
            if cp_id is not integer itwould rturns False
            and if CoursePanel DoesNotExists via cp_id
            it returns False.
        """
        if type(cp_id) == int:
            try:
                cp = lesson_model.CoursePanel.get(id=cp_id)
                task = lesson_model.Task.objects.create(
                cp=cp,*args,**kwargs
                )
                task.save()
                return True
            except models.ObjectDoesNotExist:
                return False
        else:
            return False
    def get_courspanels(self):
        return self.objects.coursepanel_set
    def get_students_dict(self):
        return self.get_courspanels().values('students')
    def get_tasks(self):
        return self.objects.task_set


class University(models.Model):
    name = models.CharField(max_length = 1000)
    field = models.ManyToManyField(
    "Field"
    )

class Field(models.Model):

    name = models.CharField(max_length = 256,unique=True)
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
    term_choice = [('9798','97-98'),('9899','98-99')]
    term = models.CharField(choices=term_choice,max_length=50)

    def get_courspanel(self):
        return self.objects.coursepanel
    def get_master(self):
        return self.get_courspanel().master
    def get_students(self):
        return self.get_courspanel().F(get)



def get_source_image(instance,f_name):
    main_dir = 'lessons/source_%d/'%instance.id
    return main_dir + f'image/{f_name}'

def  get_source_file(instance,f_name):
    main_dir = 'lessons/source_%d/'%instance.id
    return main_dir + f'file/{f_name}'


class Source(models.Model):
    image = models.ImageField(
    upload_to = get_source_image
    )
    file = models.FileField(
    upload_to= get_source_file
    )
    description = models.TextField(max_length=5000)
    name = models.CharField(max_length=200)
