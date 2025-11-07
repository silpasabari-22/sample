from django.shortcuts import render,redirect
from .models import profile
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
import random
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def reg(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')

        age=request.POST.get('age')
        phno=request.POST.get('phno')
        data=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,password=password,email=email)
        data.save()
        data1=profile.objects.create(user_id=data,age=age,phno=phno)
        data1.save()
        return redirect('login')
    else:
        return render(request,'register.html')
    

def Login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None and user.is_superuser==False:
            login(request,user)
            return redirect('userhome')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def userhome(request):
    return render(request,'userhome.html')

def Profile(request):
    data=profile.objects.get(user_id=request.user)
    return render(request,'profile.html',{'data':data})


def send_otp(email):
    otp=random.randint(10000,999999)
    send_mail(
        'Your Otp Code',''
        f'Your OTP Code is:{otp}',
        'silpasabari2203@gmail.com',
        [email],
        fail_silently=False,
    )
    return otp

def password_reset_request(request):
    if request.method=='POST':
        email=request.POST['email']
        try:
            user=User.objects.get(email=email)
            otp=send_otp(email)

            context={
                "email":email,
                "otp":otp,
            }
            return render(request,'verify_otp.html',context)
        
        except User.DoesNotExist:
            messages.error(request,'Email address not found.')
    else:
        return render(request,'password_reset.html')
    return render(request,'password_reset.html')


def verify_otp(request):
    if request.method=='POST':
        email=request.POST.get('email')
        otpold=request.POST.get('otpold')
        otp=request.POST.get('otp')

        if otpold==otp:
            context={
                'otp':otp,
                'email':email
            }
            return render(request,'set_new_password.html',context)
        else:
            messages.error(request,"Invalid OTP")
    return render(request,'verify_otp.html')


def set_new_password(request):
    if request.method=='POST':
        email=request.POST.get('email')
        new_password=request.POST.get('new_password')
        confirm_password=request.POST.get('confirm_password')
        if new_password==confirm_password:
            try:

                user=User.objects.get(email=email)
                user.set_password(new_password)
                user.save()
                messages.success(request,'password has been reset successfully')
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request,'password doesnot match')
        return render(request,'set_new_password.html',{'email':email})
    return render(request,'set_new_password.html',{'email':email})
