from django.http.response import HttpResponse
from restaurant.models import Rest
from django.shortcuts import render
from django.utils import timezone


from selenium import  webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Create your views here.

def restaurant(request):
    rest_list_offi = Rest.objects.filter(rest_rmd='offi')
    rest_list_kfq = Rest.objects.filter(rest_rmd='kfq')
    rest_list_score = Rest.objects.order_by('-rest_score')
    context = { 'rest_list_offi' : rest_list_offi, 'rest_list_kfq' : rest_list_kfq , 'rest_list_score' : rest_list_score }
    return render(request, 'restaurant/restaurant.html',context)
    

def restaurant_list(request):    #,rest_rmd): #rest_rmd : 어떤 추천(offi,kfq,starscore) 리스트인지
    #rest_list = Rest.objects.filter(Rest_rmd=rest_rmd)
    #context = { 'rest_list' : rest_list }

    ############## 테스트 ################
    rest_list = Rest.objects.all()
    context = {'rest_list' : rest_list }
    ######################################
    return render(request, 'restaurant/restaurant_list.html',{})   #context)

def restaurant_detail(request): # = None):
    #rest = get_object_or_404(Rest, rest_name=rest_name)
    search = request.POST.get('search')

    if not Rest.objects.filter(rest_name__contains=search).exists() :  #해당 가게명이 데이터 베이스에 없다.
        
        
        ##########################      크롤링     #######################################
        url = 'https://www.mangoplate.com/'

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        driver =  webdriver.Chrome(executable_path='C:/pr2/webproject_communitysite/MINI2/static/chromedriver.exe', chrome_options=options)
        driver.get(url)
        time.sleep(0.5)
        elem = driver.find_element_by_class_name('Header__LogoIcon')
        action_chains = ActionChains(driver)
        action_chains.move_to_element_with_offset(elem, 0, 0).perform()
        action_chains.click().perform()

        element=driver.find_element_by_name('main-search') #검색란 찾기
        element.send_keys(search) #검색어 입력

        ser_btn=driver.find_element_by_class_name("btn-search")# 검색찾기
        ser_btn.click()
        #################################################################
        # html = driver.page_source
        # soup = BeautifulSoup(html, 'html.parser')
        # if soup.select('body > main > article > div.column-wrapper > div > div > section > div.search_result_empty_message > div > p') == '검색한 식당이 망고플레이트에 보이지 않을 땐??':
        #     return HttpResponse('검색어가 존재하지 않습니다.')
        #################################################################
        try :
            elem2 = driver.find_element_by_class_name('thumb')
        except :
            return HttpResponse('검색어가 존재하지 않습니다.')
        action_chains = ActionChains(driver)
        action_chains.move_to_element_with_offset(elem2, 0, 0).perform()
        action_chains.click().perform()
        html = driver.page_source
        rest_url = driver.current_url.split('/')[-1]

        #만약 같은 url 주소를 가진 것이 없다면 데이터를 수집한다.
        if not Rest.objects.filter(rest_url = rest_url).exists() : 

            soup = BeautifulSoup(html, 'html.parser')

            img_list = soup.select('.restaurant-photos-item img')
            img_list #이미지 주소
            img_url_list = [] #이미지 주소 리스트
            for img in img_list: 
                rest_photo_url = img.attrs['src']
                img_url_list.append(rest_photo_url)

            if len(img_url_list) > 0 :
                rest_img1 = img_url_list[0]
            if len(img_url_list) > 1 :
                rest_img2 = str()
                for i in img_url_list[1:] :
                    rest_img2 += i + '@@'
                rest_img2 = rest_img2[:-2]


            # for i in range(1,len(img_url_list)+1):
            #     globals()['rest_img{}'.format(i)] = [x for x in img_url_list]

            name = soup.select('.restaurant_name')
            rest_name = name[0].text #가게명
            try :
                score = soup.select('.rate-point')
                rest_score = score[0].text #점수
            except :
                rest_score = 0

            starscore = 0
            starscore = int(float(rest_score))
            starscore = '*' * starscore

            td = soup.select('section.restaurant-detail > ul > li:nth-child(1) > div.Restaurant__InfoItemLabel > div.Restaurant__InfoItemLabel--RoadAddressText')
            rest_address = td[0].text #가게 주소 도로명

            tel = soup.select('section.restaurant-detail > table > tbody > tr:nth-child(2) > td')
            rest_tel = tel[0].text #가게 전화번호

            td = soup.select('body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody > tr:nth-child(3) > td')
            rest_kind = td[0].text #가게음식종류

            td = soup.select('body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody > tr:nth-child(4) > td')
            rest_price = td[0].text #가격대

            rest = Rest(
                rest_update = timezone.now(),
                rest_tel = rest_tel,
                rest_price = rest_price,
                rest_name = rest_name,
                rest_address = rest_address,
                rest_kind = rest_kind,
                rest_score = rest_score,
                rest_url = rest_url,
                rest_starscore = starscore
                #입력 안된 것 : seenum, rmd
            )
            if 'rest_img1' in locals() :
                rest.rest_img1 = rest_img1
            if 'rest_img2' in locals() :
                rest.rest_img2 = rest_img2
            rest.save()
        else :
            rest = Rest.objects.get(rest_url = rest_url)
    else :
        rest = Rest.objects.get(rest_name__contains=search)

    
    context = { 'rest' : rest } 
    return render(request, 'restaurant/restaurant_detail.html', context)