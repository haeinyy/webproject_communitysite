from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
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
        user_name = request.POST['user_name']
        user_pw = request.POST['user_pw']
        user_pwchk = request.POST['user_pwchk']
        user_phone = request.POST['user_phone']

        message_dict = {} # html에 던져줄 dictionary
        
        m = Member(
            user_name = user_name, user_pw=user_pw,
            user_phone = user_phone)
        m.c_date = timezone.now()
        m.save()
        messages.warning(request, '회원가입 성공')
        return redirect('member:register') # urls.py/view-name을 적어야함

def login(request):
    if request.method == 'GET':
        return render(request, 'member/register.html', {})
     # POST
    else:
        # 받은 정보 확인
        u_id = request.POST['user_phone']
        u_pw = request.POST['user_pw']
        
        try:
            m = Member.objects.get(user_phone=u_id)
        
        except:
            return HttpResponse('등록된 회원이 없습니다.')
        else:
            if m.user_pw != u_pw:
                error_messages = '로그인 실패'   
                return render(request, 'member/register.html', 
                        {'error_messages':error_messages})
            else:
                error_messages = ''
                request.session['user_phone'] = u_id
                request.session['user_name'] = m.user_name
                return redirect('mainpage:mainhome')

def logout(request):
    if request.session['user_phone']:
        del request.session['user_phone']
        del request.session['user_name']
        return redirect('mainpage:mainhome')
