from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def loginuser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are successfully logged in')
            
            return redirect('home')
        else:
            messages.error(request,'invalid details')
            return redirect('login')
    return render(request,'account/login.html')
def logoutuser(request):
    logout(request)
    return redirect('home')
def register(request):
    if request.method=='POST':
     firstname=request.POST['firstname']
     lastname=request.POST['lastname']
     username=request.POST['username']
     email=request.POST['email']
     password=request.POST['password']
     confirmpassword=request.POST['confirmpassword']
     if password==confirmpassword:
        if User.objects.filter(username=username).exists():
            messages.error(request,'username already exists')
            return redirect('register')
        else:
            if User.objects.filter(email=email).exists():
              messages.error(request,'email already exists')
              return redirect('register')
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                user.save()
                messages.success(request,"Account created successfully")
                return redirect('loginuser')
     else:
         messages.error(request,'password dont match')
         return redirect('register')
    return render(request,'account/register.html')
@login_required(login_url="loginuser")
def dashboard(request):
    return render(request,'account/dashboard.html')