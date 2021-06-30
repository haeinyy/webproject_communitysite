from django.shortcuts import render

# Create your views here.

def list_1(request):
    return render(request, 'restaurant/restaurant1.html',{})