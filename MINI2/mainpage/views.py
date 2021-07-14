from django.http.response import HttpResponse
from django.shortcuts import render
from calcapp.models import Blog
from restaurant.models import Rest
from boardapp.models import BoardAllContentList

# Create your views here.
def mainhome(request):
    get_user_phone = request.session.get('user_phone')
    # get_user_phone = request.session['user_phone']
    blogs = Blog.objects.all()
    rest = Rest.objects.all()

    boards = BoardAllContentList.objects.all()

    context = {
        'get_user_phone':get_user_phone,
        'blogs': blogs,
        'rest':rest,
        'boards':boards,
    }

    return render(request, 'mainpage/mainhome.html', context)