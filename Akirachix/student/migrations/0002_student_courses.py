# Generated by Django 2.2.1 on 2019-05-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_teacher'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(null=True, to='course.Course'),
        ),
    ]
