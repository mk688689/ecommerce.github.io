# Generated by Django 2.2.5 on 2019-10-14 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=123456789, max_length=30),
            preserve_default=False,
        ),
    ]
