from django.shortcuts import render
from .models import BoardAllContentList
from django.http import HttpResponse


# Create your views here.
def freeboard(request):
    return render(request, 'boardapp/board_free.html', {})

def writetext(request):
    return render(request, 'boardapp/board_write.html',{})
