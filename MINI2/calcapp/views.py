from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from . models import AttendHistroy
from . models import Member

def index(request, pk):
    # attendances = AttendHistroy.objects.all()
    # str =''
    # for attendance in attendances:
    #     str += "<p> name: {} attend: {}".format(attendance.name, attendance.attend)
    # return HttpResponse(str)
    
    attendancesList = AttendHistroy.objects.all()
    # a = '0219'
    # memberList = Member.objects.all()
    # attenda = []
    # for i in attendancesList:
    #     if i.user_phone == a:
    #         attenda.append(i)

    context = {
        'attnedances': attendancesList
    }
    return render(request, 'calcapp/calcpage_info.html', context)
    # return render(request, 'calcapp/index.html', context)

    ## 메모
    # a = request.session['user_phone']

def calcpage(request):
    pay = int(15000)
    day1 = int(request.POST['num1'])
    result = day1 * pay
    return render(request, 'calcapp/calcpage.html', {'result':result})

def calcpage_result(request):
    return render(request, 'calcapp/calcpage_result.html', {'name':'name'})
 
def calcpage_info(request):
    return render(request, 'calcapp/calcpage_info.html')

def calcpage_user(request):
    attendancesList = AttendHistroy.objects.all()    
    context = {'attnedances': attendancesList}
    return render(request, 'calcapp/calcpage_user.html', context) 