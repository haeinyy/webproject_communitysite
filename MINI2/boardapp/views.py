# from django.core.checks import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import BoardAllContentList, Board_comment, Image, Member
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
import json
from django.views.generic import View, ListView, DetailView, FormView, CreateView


# 자유게시판 메인 목록
def freeboard(request):
    content_list = BoardAllContentList.objects.order_by('-id')
    
    # 페이지 번호
    p = Paginator(content_list,10)
    page = request.GET.get('page')

    if not page:
        page = 1

    info = p.get_page(page)

    # 시작페이지
    start_page = (int(page)-1) // 10 * 10 +1
    end_page = start_page + 9

    # 현재페이지
    now_page = info.number
    # print(now_page)


    # now_page = boards.number # 현재페이지
    # end_page = boards.paginator.num_pages # 마지막페이지

    if end_page > p.num_pages:
        end_page = p.num_pages

    context = {
        'content_list':info,
        'pagination' : range(start_page,end_page+1),
        'end_page' : end_page,
        'now_page' : now_page,
    }
    
    return render(request, 'boardapp/board_free.html', context)


# 글쓰기 양식
def writetext(request):
    content = BoardAllContentList()

    # 세션에 로그인 관련 정보 저장
    # 해인
    # request.session['user_phone'] = user_phone
    session_value = request.session['user_name']
    # m = Member.objects.get(user_phone=session_value)
    # request.session['user_name'] = m.user_name

    if request.method == 'POST': # 내용 입력후, 전달 할때
        content.title = request.POST['title']
        content.text = request.POST['text']
        content.date = timezone.datetime.now()
        content.user = session_value
        content.board_kind = request.POST['board_kind']
        content.save()
        
        for img in request.FILES.getlist('images'):
            # image 객체 생성
            image = Image()
            # 현재 게시물의 기본키 참조
            image.content = content.id
            # images로부터 가져온 이미지파일 하나씩 저장
            image.image = img
            # db에 저장
            image.save()
        return redirect('/boardapp/' + str(content.pk))
    # 내용 입력 없을 떄
    return render(request, 'boardapp/board_write.html',{})


# 게시글 페이지
def content_view(request, pk):
    content = BoardAllContentList.objects.get(pk=pk)
    content.seenum += 1 # 조회수
    content.save()
    user = Member.objects.all()
    return render(request, 'boardapp/content_view.html', {'content':content})


# 게시글 삭제
def content_delete(request, pk):
    # login_session = request.session.get('login_session','')
    session_user = request.session['user_name']
    print(session_user)
    content = get_object_or_404(BoardAllContentList, pk=pk)
    if content.user == session_user:
        content.delete()
        return redirect('/boardapp/freeboard')
    else:
        return redirect('/boardapp/' + str(content.pk))

# class NoticeListView(ListView):
# # 게시물 리스트 검색
    model = BoardAllContentList
    paginate_by = 10
    template_name = 'boardapp/board_free.html'
    context_object_name = 'search_content'

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        search_content = BoardAllContentList.objects.order_by('-id') 

        if search_keyword :
            if len(search_keyword) > 1 :
                if search_type == 'all':
                    search_notice_list = search_content.filter(Q (title__icontains=search_keyword) | Q (text__icontains=search_keyword) | Q (user__icontains=search_keyword))
                elif search_type == 'title_content':
                    search_notice_list = search_content.filter(Q (title__icontains=search_keyword) | Q (text__icontains=search_keyword))
                elif search_type == 'title':
                    search_notice_list = search_content.filter(title__icontains=search_keyword)    
                elif search_type == 'content':
                    search_notice_list = search_content.filter(text__icontains=search_keyword)    
                elif search_type == 'writer':
                    search_notice_list = search_content.filter(user__icontains=search_keyword)

                return search_notice_list
            else:
                messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
        return search_content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        
        if len(search_keyword) > 1 :
            context['q'] = search_keyword
            context['type'] = search_type

        return context


# 게시글 댓글
def comment_write(request, pk):
    # if request.method == 'POST':
    content = get_object_or_404(BoardAllContentList, pk = pk)
    
    # session_phone = request.session['user_phone']
    # user = Member.objects.get(user_phone = session_phone)
    session_value = request.session['user_name']
    
    content.content.create(comment_content = request.POST.get('comment'), comment_date = timezone.now(), comment_writer=session_value)
    return redirect('/boardapp/'+str(content.pk))


# 게시글 좋아요
def likes(request):
    # now_login = request.session['user_name'] # 현재 로그인한 유저
    # print(now_login)
    user = Member.objects.get(user_phone=request.session['user_phone']) # 현재 로그인한 유저

    if request.is_ajax():
        content_id = request.GET['content_id'] # 좋아요 누른 게시물 id
        content = BoardAllContentList.objects.get(id=content_id)
        # print(id)
        like_user_list = content.like.all() # 좋아요 누른 유저 리스트
        print('리스트',like_user_list)

        # 현재 게시물에 좋아요한 사람 중 로그인한사람이 있으면 (이미 좋아요 누른경우이면)
        if user in like_user_list:
            content.like.remove(user) # 현재 로그인한 사람지워
            message ='좋아요취소'
        else:
            content.like.add(user)
            message ='좋아요'
        
        like_count = content.like.count() # 게시물이 받은 좋아요수
        context={'like_count':like_count, 'message':message}
    
    return HttpResponse(json.dumps(context), content_type='application/json')