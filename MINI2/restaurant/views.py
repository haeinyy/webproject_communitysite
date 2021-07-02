from restaurant.models import Rest
from django.shortcuts import get_object_or_404, render

# Create your views here.

def restaurant(request):
    rest_list_offi = Rest.objects.filter(Rest_rmd='offi')
    rest_list_kfq = Rest.objects.filter(Rest_rmd='kfq')
    rest_list_score = Rest.objects.order_by('-Rest_score')
    context = { 'rest_list_offi' : rest_list_offi, 'rest_list_kfq' : rest_list_kfq , 'rest_list_score' : rest_list_score }
    return render(request, 'restaurant/restaurant.html',context)
    

def restaurant_list(request):    #,rest_rmd): #rest_rmd : 어떤 추천(offi,kfq,starscore) 리스트인지
    #rest_list = Rest.objects.filter(Rest_rmd=rest_rmd)
    #context = { 'rest_list' : rest_list}
    return render(request, 'restaurant/restaurant_list.html',{})   #context)

def restaurant_detail(request, rest_url):
    # # 데이터 베이스에서 자료 가져와서 출력 보내줘야함
    rest = get_object_or_404(Rest, Rest_url=rest_url)
    context = { 'rest' : rest }
    return render(request, 'restaurant/restaurant_detail.html', context)
