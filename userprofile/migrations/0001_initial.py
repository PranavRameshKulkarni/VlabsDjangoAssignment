# Generated by Django 3.0.2 on 2020-01-29 06:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.IntegerField(default=0)),
                ('birthdate', models.DateField()),
                ('employee_Id', models.IntegerField(default=0)),
                ('experience', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(15), django.core.validators.MinValueValidator(1)])),
                ('salary', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]