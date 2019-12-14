# Generated by Django 3.0 on 2019-12-13 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import rekita_users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('level', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_loged', models.DateTimeField(auto_now=True)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=rekita_users.models.get_source_image)),
                ('file', models.FileField(upload_to=rekita_users.models.get_source_file)),
                ('description', models.TextField(max_length=5000)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('field', models.ManyToManyField(to='rekita_users.Field')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='lessons/images')),
                ('description', models.TextField(max_length=5000)),
                ('term', models.CharField(choices=[('9798', '97-98'), ('9899', '98-99')], max_length=50)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='sources', to='rekita_users.Source')),
            ],
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rekita_users.Field', to_field='name')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rekita_users.Person')),
                ('image', models.ImageField(upload_to=rekita_users.models.get_image)),
                ('stid', models.IntegerField(verbose_name=10)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rekita_users.Field')),
                ('uni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='students', to='rekita_users.University')),
            ],
            bases=('rekita_users.person',),
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rekita_users.Person')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rekita_users.Field')),
                ('uni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='masters', to='rekita_users.University')),
            ],
            bases=('rekita_users.person',),
        ),
    ]
