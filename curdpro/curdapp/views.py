from django.shortcuts import render , redirect
from .models import employee_data
from django.http import HttpResponse

def display_data(request):
    employees = employee_data.objects.all()
    return render(request,'display_data.html', {'employees': employees})

def add_data(request):
    return render(request,'add_data.html')

def save_data(request):
    ename1 = request.POST.get('ename')
    lname1 = request.POST.get('lname')
    email1 = request.POST.get('email')
    number1 = request.POST.get('number')
    loc1 = request.POST.get('loc')
    sal1 = request.POST.get('sal')

    cdata = employee_data(
        first_name=ename1,
        last_name=lname1,
        email_id=email1,
        mobile_number=number1,
        location=loc1,
        salary=sal1
    )
    cdata.save()
    return redirect('/')

def update_data(request,pk):
    employee = employee_data.objects.get(id=pk)
    return render(request,'update.html',{'employee':employee})

def data_update(request,pk):
    employee = employee_data.objects.get(id=pk)

    employee.first_name = request.POST.get('ename')
    employee.last_name =request.POST.get('lname')
    employee.email_id = request.POST.get('email')
    employee.mobile_number = request.POST.get('number')
    employee.location = request.POST.get('loc')
    employee.salary = request.POST.get('sal')

    employee.save()

    return redirect('/')

def delect_data(request,pk):
    employee = employee_data.objects.get(id=pk)
    employee.delete()

    return redirect('/')

