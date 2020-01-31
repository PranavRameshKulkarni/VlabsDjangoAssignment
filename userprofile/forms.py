from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

from userprofile.models import Userprofile, Dropdown
companyList = []

class CreateUserForm(UserCreationForm):
    email = forms.CharField(required=True , widget=forms.EmailInput(attrs={'class': 'validate',}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',]


class Profileform(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Dropdown.objects.all(), empty_label='select company')
    birthdate = forms.SelectDateWidget(years = range(1900,2100))
    class Meta:
        model = Userprofile
        fields =['mobile' , 'birthdate', 'employee_Id','experience', 'salary', 'company' ]


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username']