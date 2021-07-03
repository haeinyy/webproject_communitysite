from restaurant.models import Rest
from django.shortcuts import get_object_or_404, render

# Create your views here.

def restaurant(request):
    # rest_list_offi = Rest.objects.filter(Rest_rmd='offi')
    # rest_list_kfq = Rest.objects.filter(Rest_rmd='kfq')
    # rest_list_score = Rest.objects.order_by('-Rest_score')
    # context = { 'rest_list_offi' : rest_list_offi, 'rest_list_kfq' : rest_list_kfq , 'rest_list_score' : rest_list_score }
    return render(request, 'restaurant/restaurant.html') #,context)
    

def restaurant_list(request):    #,rest_rmd): #rest_rmd : 어떤 추천(offi,kfq,starscore) 리스트인지
    #rest_list = Rest.objects.filter(Rest_rmd=rest_rmd)
    #context = { 'rest_list' : rest_list}
    return render(request, 'restaurant/restaurant_list.html',{})   #context)

def restaurant_detail(request): #, rest_name = None):
    #rest = get_object_or_404(Rest, rest_name=rest_name)
    ##rest = Rest.objects.filter(rest_name = rest_name)
    #context = { 'rest' : rest }
    return render(request, 'restaurant/restaurant_detail.html')#, context)

def restaurant_search(request):
    search = request.POST('search')
    if not Rest.objects.filter(rest_name = search).exists() :  #해당 가게명이 데이터 베이스에 없다.
        # 크롤링
        # 데이터베이스에 저장
        print('There isnt')

    else :              #해당 가게명이 데이터 베이스에 있다.
        search = rest_search[0].rest_name    
        
    restaurant_detail(request,search) #restaurant_search함수를 실행시킨다. -> 잘 찾아가는지 확인해야함

    