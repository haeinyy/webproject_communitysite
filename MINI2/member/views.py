from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, resolve_url
from django.utils import timezone


from django.contrib import messages

from .models import Member
# redierct - url을 이동. name으로 접근. render처럼 context값을 넘기지는 못함.
# render - 화면에 html파일을 띄우기때문에 url이안변함. context값 넘길 수 있음.
# reverse - 

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'member/register.html')
     #"POST"
    else: 
        # HTML로부터 받은 정보 확인
        user_phone = request.POST['user_phone']
        user_name = request.POST['user_name']
        user_pw = request.POST['user_pw']
        
        # --------같은 이름이 없는지 확인하고 회원가입-------
        # code
        # ---------------

        m = Member(
            user_name = user_name, user_pw=user_pw,
            user_phone = user_phone)
        m.c_date = timezone.now()
        m.save()
        messages.warning(request, '회원가입 성공')
        return redirect('member:login') # urls.py/view-name을 적어야함
        # return render(request, 'member/login.html')
        # return HttpResponse('가입 완료' + user_name + user_pw + user_phone)

def login(request):
    if request.method == 'GET':
        return render(request, 'member/login.html', {})
    else:
        # 받은 정보 확인
        user_phone = request.POST['user_phone']
        user_pw = request.POST['user_pw']
        
        try:
            m = Member.objects.get(user_phone=user_phone, 
                                        user_pw=user_pw)
        except:            
            return HttpResponse('로그인 실패')
            # return render(request, 'member/login.html', {})
        else:
            # 1. DB와 확인해서 로그인 -> db에 아이디가 있다면 로그인 성공

            
            # 세션에 로그인 관련 정보 저장
            request.session['user_phone'] = user_phone
            
            a = request.session['user_phone']
            # -------del request.session['user_id'] 로그아웃-------
            # code
            # -----------------------------------
            return redirect('mainpage:mainhome')
            # return render(request, 'mainpage/mainhome.html', {})
            # return HttpResponse('로그인 성공')