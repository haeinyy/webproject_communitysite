from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def mainhome(request):

    return render(request, 'mainpage/mainhome.html')