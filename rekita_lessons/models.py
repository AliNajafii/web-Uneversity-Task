from django.db import models
__doc__ ="""
created by Ali Najafi on 12/13/2019 at 12:39 Am
"""

class CoursePanel(models.Model):

    key_code = models.AutoField(
    db_index = True,
    primary_key = True
    )

    lesson = models.OneToOneField(
    "rekita_users.Lesson",
    on_delete=models.CASCADE
    )

    master = models.ForeignKey(
    "rekita_users.Master",
    on_delete=models.CASCADE
    )

    students = models.ManyToManyField(
    "rekita_users.Student",

    )

class Task(models.Model):
    description = models.CharField(max_length = 5000)
    dead_line = models.DateTimeField(
    default = default_deadline
    )
    creator = models.ForeignKey(
    "rekita_users.Master",
    on_delete=models.CASCADE,
    related_query_name='exercises'
    )
    attach = models.FileField(
    upload_to= directory
    )

    cp = models.ForeignKey(
    "CoursePanel",
    on_delete=models.CASCADE
    )

    def directory(self):
        main_dir = slef.creator.get_main_dir()
        return f'{main_dir}/{self.cp.lesson.name}/task_{self.id}/attach'

class Response(models.Model):
    task = models.ForeignKey(
    "Task",
    on_delete=models.CASCADE
    )

    student = models.ForeignKey(
    "rekita_users.Student",
    on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add = True)
    file = models.FileField(
    upload_to=directory
    )
    description = models.TextField(max_length=5000)

    def directory(self):
        main_dir = self.student.get_main_dir()
        return f'{main_dir}/responses/response_{self.date}'
        
