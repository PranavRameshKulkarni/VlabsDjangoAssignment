from django.contrib import admin
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,\
    PasswordResetCompleteView
from django.urls import path, include

from userprofile import views
from userprofile.admin import user_admin_site

urlpatterns = [
    path('', views.homepage, name='home'),
    path('signuppage', views.signup, name='signuppage'),
    path('postlogin', views.postlogin, name='postlogin'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('update', views.update, name='update'),
    path('verification/<username>/<uid>', views.verification_view, name='verification'),
    path('logoutpage', views.logoutpage, name='logoutpage'),
    path('completelogout', views.completelogout, name='completelogout'),
    path('resetpassword',PasswordResetView.as_view(), name='password_reset'),
    path('resetpassword/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('resetpassword/confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('resetpassword/complete',PasswordResetCompleteView.as_view(template_name = 'registration/password_reset_complete.html'), name='password_reset_complete'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('user-admin',user_admin_site.urls,)
]
