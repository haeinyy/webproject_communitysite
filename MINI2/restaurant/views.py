from restaurant.models import Rest
from django.shortcuts import get_object_or_404, render

# Create your views here.

def restaurant(request):
    return render(request, 'restaurant/restaurant.html',{})

def restaurant_list(request):
    return render(request, 'restaurant/restaurant_list.html',{})

def restaurant_detail(request, rest_url):
    # 데이터 베이스에서 자료 가져와서 출력 보내줘야함
    rest_url = get_object_or_404(Rest, Rest_url=rest_url)
    #question = Question.object.get(pk=question_id)
    url = rest_rul
    



    # context = {'rest': rest}
    return render(request, 'restaurant/restaurant_detail.html',context)
