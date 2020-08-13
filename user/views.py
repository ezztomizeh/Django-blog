from django.shortcuts import render , redirect , HttpResponseRedirect
from blog2 import settings
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import mask_hash , make_password , check_password
from django.contrib import messages

# Create your views here.
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password = password)
        if user is not None:
            login(request,user=user)
            messages.success(request,"Login successfully")    
            return redirect('/')
        else:
            messages.error(request,'Something went wrong')
            return redirect('blog-Login')

    else:
        return render(request,'Login.html')

def SignUp(request):
    if request.method == 'POST':
        FullName = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        password = make_password(password=pass1)
        if User.objects.filter(username=username):
            messages.info(request,'Username is taken')
            return redirect('blog-SignUp')
        elif User.objects.filter(email=email):
            messages.info(request,'Email is token')
            return redirect('blog-SignUp')
        else:
            if pass1 == pass2 and len(pass1) >= 8:
                user = User.objects.create(username=username,email=email,password=password,first_name=FullName)
                user.save()
                messages.success(request,f'{username},Welcome to our blog')
                return redirect('blog-Login')
            else:
                messages.info(request,'Password not match or less than 8 char')
                return redirect('blog-SignUp')
    else:
        return render(request,'SignUp.html')

@login_required
def Logout(request):
    logout(request)
    messages.success(request,'Logout seccessfully')
    return redirect('blog-home')

@login_required
def Profile(request):
    user = User.objects.filter(username=request.user).first()
    context = {
        'user' : user
    }
    return render(request,'Profile.html',context)

@login_required
def ChangeUsername(requset):
    if requset.method == 'POST':
        user = User.objects.get(username=requset.user)
        NewUsername = requset.POST['username']
        if User.objects.filter(username=NewUsername).first():
            messages.error(requset,'This Username is used , Choose anthor one')
            return redirect('ChangeUsername')
        else:
            user.username = NewUsername
            user.save()
            messages.success(requset,'Username changed seccessfully')
            return redirect('Profile')
    else:
        user = User.objects.filter(username=requset.user).first()
        return render(requset,'ChangeUsername.html',context={'user':user})

@login_required
def ChangeName(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        name = request.POST['name']
        user.first_name = name
        user.save()
        messages.success(request,'Your name Change Seccessfully')
        return redirect('Profile')
    else:
        user = User.objects.filter(username=request.user).first()
        return render(request,'ChangeName.html',context={'user':user})

@login_required
def ChangeEmail(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        email = request.POST['email']
        if User.objects.filter(email=email).first():
            messages.error(request,'This email is used')
            return redirect('ChangeEmail')
        else:
            user.email = email
            user.save()
            messages.success(request,'Your email changed seccessfully')
            return redirect('Profile')
    else:
        return render(request,'ChangeEmail.html')

def ChangePassword(request):
    if request.method == 'POST':
        OldPassword = request.POST['OldPassword']
        NewPassword1 = request.POST['Password1']
        NewPassword2 = request.POST['Password2']
        user = User.objects.get(username=request.user)
        if check_password(OldPassword,user.password):
            if NewPassword1 == NewPassword2 and len(NewPassword1) >= 8:
                NewPassword = make_password(NewPassword1)
                user.password = NewPassword
                user.save()
                messages.success(request,'Password Changed seccessfully')
                return redirect('user-logout') 
    else:
        return render(request,'ChangePassword.html')