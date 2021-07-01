from django.shortcuts import render

# Create your views here.
def freeboard(request):
    return  render(request, 'boardapp/board_free.html', {})