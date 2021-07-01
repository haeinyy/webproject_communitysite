from django.shortcuts import render

# Create your views here.

def restaurant(request):
    return render(request, 'restaurant/restaurant.html',{})

def restaurant_list(request):
    return render(request, 'restaurant/restaurant_list.html',{})
