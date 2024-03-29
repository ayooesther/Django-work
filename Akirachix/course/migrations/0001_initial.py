# Generated by Django 2.2.1 on 2019-05-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('duration_months', models.IntegerField(max_length=10)),
                ('start_date', models.DateField(max_length=10)),
                ('end_date', models.DateField(max_length=10)),
                ('description', models.TextField(max_length=100)),
            ],
        ),
    ]
