# Generated by Django 2.2.2 on 2019-06-19 03:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('descriptions', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('is_mvp', models.BooleanField(default=False)),
                ('hire_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
