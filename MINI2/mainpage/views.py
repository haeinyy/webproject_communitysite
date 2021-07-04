from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def mainhome(request):
    get_user_phone = request.session.get('user_phone')
    # get_user_phone = request.session['user_phone']

    return render(request, 'mainpage/mainhome.html',
                {'get_user_phone':get_user_phone})