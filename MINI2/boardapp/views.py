from django.shortcuts import render

# Create your views here.
def freeboard(request):
    return render(request, 'boardapp/board_free.html', {})

def writetext(request):
    return render(request, 'boardapp/board_write.html',{})

def ddd(request):
    return render(request, 'boardapp/ddd.html',{})