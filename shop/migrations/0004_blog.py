# Generated by Django 2.2.5 on 2019-10-18 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_men'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='products/%y/%m/%d')),
                ('title', models.CharField(max_length=200, verbose_name='post title')),
                ('description', models.TextField()),
                ('posted_date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
