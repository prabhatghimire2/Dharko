# Generated by Django 2.1 on 2018-09-01 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='detail',
            field=models.TextField(max_length=14000),
        ),
    ]
