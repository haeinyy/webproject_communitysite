from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Member
from django.utils import timezone

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'member/join.html')
    else:
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_name = request.POST['user_name']

        m = member(
            user_id = user_id, user_pw=user_pw,
            user_name = user_name)
        m.c_date = timezone.now()
        m.save()

        return HttpResponse('가입 완료' + user_id + user_pw + user_name)

def login(request):
    if request.method == 'GET':
        return render(request, 'member/login.html', {})
    else:
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']

        try:
            member = \
                Member.objects.get(user_id=user_id, user_pw=user_pw)
        except:            
            return HttpResponse('로그인 실패')
        else:
            # 세션에 로그인 관련 정보 저장
            request.session['user_id'] = user_id
            
            a = request.session['user_id']
            # del request.session['user_id'] 로그아웃

            return HttpResponse('로그인 성공')