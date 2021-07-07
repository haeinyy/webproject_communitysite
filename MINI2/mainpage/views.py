from django.http.response import HttpResponse
from django.shortcuts import render
from calcapp.models import Blog
from restaurant.models import Rest


# Create your views here.
def mainhome(request):
    get_user_phone = request.session.get('user_phone')
    # get_user_phone = request.session['user_phone']
    blogs = Blog.objects.all()
    rest = Rest.objects.all()

    return render(request, 'mainpage/mainhome.html',
                {'get_user_phone':get_user_phone,
                'blogs': blogs,
                'rest':rest})