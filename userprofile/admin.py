from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy

from userprofile.models import Userprofile, Dropdown

# Register your models here.
admin.site.register(Userprofile)
admin.site.register(Dropdown)

class UserAdmin(AdminSite):

    login_form = AuthenticationForm
    site_title = ugettext_lazy('MY Admin')
    site_header = ugettext_lazy("My Header")
    index_title = ugettext_lazy("MyIndex")

    def has_permission(self,request):

        return request.user.is_active

user_admin_site = UserAdmin(name = 'user admin')

user_admin_site.register(User)
user_admin_site.register(Userprofile)