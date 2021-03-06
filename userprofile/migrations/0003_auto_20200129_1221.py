# Generated by Django 3.0.2 on 2020-01-29 06:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_userprofile_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='employee_Id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='experience',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(15), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
