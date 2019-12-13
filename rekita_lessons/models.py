from django.db import models
# from django.db.models import F
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

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"""
        {self.lesson.name}-->{self.master.user.first_name}
        {self.master.user.last_name} and ({self.objects.student_set.count()}) student/s"""
    @classmethod
    def join_lesson(cls,user,key_code):
        """
        this methode is for students who want
        to join course panel via key code.
        if CoursePanel didnt find it returns False
        else it returns True and add student to CoursePanel
        """
        try:
            student = user.F('student')
            cp = cls.objects.get(key_code = key_code)
            cp.objects.student_set.add(student)
            return True
        except models.ObjectDoesNotExist:
            return False



def default_deadline(self):
    from django.utils import timezone
    delta = timezone.timedelta(days=7)
    return timezone.now() + delta

def directory(instance,file_name):
    main_dir = instance.creator.get_main_dir()
    return f'{main_dir}/{instance.cp.lesson.name}/task_{instance.id}/attach/{file_name}'

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


def directory_res(instance,f_name):
    main_dir = instance.student.get_main_dir()
    return f'{main_dir}/responses/response_{instance.date}/{f_name}'

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
    upload_to=directory_res
    )
    description = models.TextField(max_length=5000)
