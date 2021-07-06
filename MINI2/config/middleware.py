import re

from django.conf import settings
from django.shortcuts import redirect, render

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]

if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

# 웹사이트를 로그인으로 redirection시키는 것이다.
# 다른 url로 이동할 수 있기 때문에 사용자가 로그인안하면 로그인페이지로
class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')
        
        # print('weweew')
        # print(path)
        try:
            print(request.session['user_phone'])

        except Exception as e:
            print(e)
            if not any(url.match(path) for url in EXEMPT_URLS):
                return redirect(settings.LOGIN_URL)