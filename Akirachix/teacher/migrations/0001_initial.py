# Generated by Django 2.2.1 on 2019-05-23 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('registration_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=70)),
                ('phone_number', models.CharField(max_length=60)),
                ('date_employed', models.DateField(max_length=70)),
            ],
        ),
    ]