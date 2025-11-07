from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Students

# Create your views here.

def fun3(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        age=request.POST['age']
        email=request.POST['email']
        Phno=request.POST['PH NO:']
        if Students.objects.filter(ph_number=Phno).exists():
            return HttpResponse("PH no is already registered")
        data=Students.objects.create(first_name=firstname,last_name=lastname,age=age,email=email,ph_number=Phno)
        data.save()
        return HttpResponse("data submitted successfully")
    else:
        return render(request,'form.html') 

def dataview(request):
    a=Students.objects.all()
    return render(request,'views.html',{'data':a})

def data(request):
    return render(request,'index.html')

def delete_student(request, id): 
    student_obj = Students.objects.get(id=id)
    student_obj.delete()
    return redirect('card')

def edit_student(request,id):
    std_obj=Students.objects.get(id=id)
    if request.method=='POST':
        std_obj.first_name=request.POST['firstname']
        std_obj.last_name=request.POST['lastname']
        std_obj.age=request.POST['age']
        std_obj.email=request.POST['email']
        std_obj.ph_number=request.POST['Phone:']
        std_obj.save()
        return redirect('card')
    else:
        return render(request,'edit.html',{'std_obj':std_obj})