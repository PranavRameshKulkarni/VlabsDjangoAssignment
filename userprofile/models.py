import datetime

from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    mobile = models.BigIntegerField( validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)])
    birthdate = models.DateField(_("Date"), default=datetime.date.today)
    employee_Id = models.IntegerField()
    company = models.CharField(max_length=100, default='')
    experience = models.IntegerField(
        validators=[MaxValueValidator(15), MinValueValidator(1)]
    )
    salary = models.IntegerField()
    isVerified = models.BooleanField(default=False)
    uid = models.CharField(max_length=32, default='')
    def __str__(self):
        return self.user.username

class Dropdown(models.Model):
    key = models.CharField(max_length=10,primary_key=True)
    company = models.CharField(max_length=100)
    def __str__(self):
        return self.company
