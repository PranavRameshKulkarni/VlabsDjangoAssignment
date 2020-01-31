

from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.forms import model_to_dict
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.utils.crypto import get_random_string

from userprofile.forms import CreateUserForm, Profileform, EditProfileForm
from userprofile.models import Dropdown, Userprofile


# @login_required(login_url='loginpage')
def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        profile_form = Profileform(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            uid = get_random_string(length=32)
            profile.uid = uid
            profile.save()
            message = "http://djangointerns.herokuapp.com/verification/" + str(form.cleaned_data['username']) + "/" + uid
            send_mail("Verification", message, EMAIL_HOST_USER, [form.cleaned_data['email']], fail_silently=False)
            messages.info(request,"Verification link sent")
            return redirect('loginpage')
        else:
            return render(request, 'registration/signup.html', {'form': form, 'profileform': profile_form})
        # except:
        #     print(form.errors, profile_form.errors)
        #     return render(request, 'registration/signup.html', {'form': form, 'profileform': profile_form})
    else:
        form = CreateUserForm()
        profile = Profileform()
        print(Dropdown.objects.all())
        return render(request, 'registration/signup.html', {'form': form, 'profileform': profile})


def loginpage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # print(username , password)
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     user = model_to_dict(user.user_profile)
        if form.is_valid() and form.get_user().user_profile.isVerified:
            user = form.get_user()
            login(request, user)
            user = model_to_dict(user.user_profile)
            return redirect('postlogin')
        else:
            if form.is_valid():
                if form.get_user().user_profile.isVerified==False:
                    messages.error(request,'Email is not verified')
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})


def homepage(request):
    return render(request, 'registration/index.html')


def postlogin(request):
    user = request.user
    print(user.email)
    userprofile = model_to_dict(user.user_profile)
    user = model_to_dict(user)
    return render(request, 'registration/sidebar.html', {'user': user, 'userprofile': userprofile})


def verification_view(request, username, uid):
    user = User.objects.get(username=username)
    print(user.username)
    if (user):
        print(user.email)
        if (user.user_profile.uid == uid):
            print(user.user_profile.isVerified)
            user.user_profile.isVerified = True
            user.user_profile.save()
            print(user.user_profile.isVerified)
            return redirect('loginpage')
    raise Http404("Not Verified")


def update(request):
    user = get_object_or_404(User,id= request.user.id)
    userprofile = get_object_or_404(Userprofile, user_id= request.user.id)
    print(userprofile.birthdate)
    form = Profileform(request.POST or None, instance=userprofile)
    form1 = EditProfileForm(request.POST or None, instance=user)
    # print('FORM!!!!!!!!!!!!!!!!!!',form)
    if request.method=='POST':
        print('i am here')
    if form.is_valid() and form1.is_valid():
        print('goodbye')
        user = form1.save()
        profile = form.save(commit=False)
        profile.user=user
        profile.save()
        return redirect('postlogin')
    else:
        print(form.errors,form1.errors)
    return render(request, 'registration/update.html',{
        'form':form,
        'form1':form1
    })
def completelogout(request):
    logout(request)
    return redirect('loginpage')

def logoutpage(request):
    return render(request, 'registration/logoutpage.html')

def changepassword(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('postlogin')
        else:
            print("please correct the error")
            return render(request, 'registration/changepassword.html', {'form': form})
    else:
        form = PasswordChangeForm(request.user)
        print(form)
        return render(request,'registration/changepassword.html', {'form':form})

