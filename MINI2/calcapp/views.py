from django.shortcuts import render, redirect
from django.http import HttpResponse

userinfoList = [
    {
        'id': '1',
        'title': 'A',
        'description': 'a',
        'topRated': True
    },
    {
        'id': '2',
        'title': 'B',
        'description': 'b',
        'topRated': False
    },
    {
        'id': '3',
        'title': 'C',
        'description': 'c',
        'topRated': True
    }
]

def calcpage(request):
    pay = int(15000)
    day1 = int(request.POST['num1'])
    result = day1 * pay
    return render(request, 'calcapp/calcpage.html', {'result':result})

def calcpage_result(request):
    return render(request, 'calcapp/calcpage_result.html', {'name':'name'})

# def calcpage1(request, pk):
#     userinfoObject = None

#     for i in userinfoList:
#         if i['id'] == str(pk):
#             userinfoObject = i

# return HttpResponse('Calc page:' + str(pk))
#     return render(request, 'calcapp/calcpage1.html', {'userinfo':userinfoObject})
    
def calcpage_info(request):
    context = {'userinfos': userinfoList}
    
    return render(request, 'calcapp/calcpage_info.html', context)

def calcpage_user(request):
    user = 'Kim Sohee'
    age = 25
    context = {'user': user, 'age':age}
    return render(request, 'calcapp/calcpage_user.html', context)