from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import LoginForm,RegisterForm\
    # , UserUpdateProfile, ProfileUpdateForm
from django.contrib.auth import authenticate,login,logout
User = get_user_model()
from .models import Profile
# Create your views here.


def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                print('user', user)
                login(request, user)
                return redirect('/users/main/')
            else:
                print('Not authenticated')
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/users/main/')
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print('form is valid')
            user = User(
                        first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name'],
                        username=form.cleaned_data['username'],
                        email=form.cleaned_data['email'])
            user.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            print('user', user)
            return redirect('/users/login/')
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/users/main/')
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


# def MainView(request):
#     if request.method == 'POST':
#         u_form = UserUpdateProfile(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             return redirect('users:profile')
#
#     else:
#         u_form = UserUpdateProfile(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#
#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#
#     return render(request,'users/profile.html',{'u_form': u_form,
#         'p_form': p_form})

def MainView(request):
    p=Profile.objects.all()
    return render(request,'users/profile.html',{'p':p})

def LogoutView(request):
    logout(request)
    return redirect('/users/login/')

