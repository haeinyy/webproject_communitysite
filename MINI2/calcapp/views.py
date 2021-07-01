from django.shortcuts import render, redirect

def calc(request):
    pay = int(15000)
    val1 = int(request.POST['num1'])

    res = val1 * pay

    return render(request, 'mainpage/middlebox.html', {'result':res})
    # return render(request, 'calcapp/calcpage.html', {'result':res})