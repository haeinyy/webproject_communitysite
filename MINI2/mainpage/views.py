from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def mainhome(request):
    aa = "값 전달하는거 연습"
    return render(request, 'mainpage/mainhome.html', {'aa':aa})
def abc(request):
    aa = "값 전달하는거 연습"
    return render(request, 'boardapp/border-study.html', {'aa':aa})
