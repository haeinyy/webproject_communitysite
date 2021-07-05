from django.core.checks import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import BoardAllContentList, Board_comment, Image, Member, Profile
from django.utils import timezone
from django.core.paginator import Paginator
import json

# 자유게시판 메인 목록
def freeboard(request):
    content_list = BoardAllContentList.objects.all()
    content_list = list(reversed(content_list)) # 최근순부터 출력하기 위해

    return render(request, 'boardapp/board_free.html', {'content_list':content_list})

# 글쓰기 양식
def writetext(request):
    content = BoardAllContentList()
    # user =  Member.objects.all()
    # content_list = BoardAllContentList.objects.all()

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
    user = Member.objects.all()
    return render(request, 'boardapp/content_view.html', {'content':content})

# 게시글 댓글
def comment_write(request, pk):
    # if request.method == 'POST':
    content = get_object_or_404(BoardAllContentList, pk = pk)

    # session_phone = request.session['user_phone']
    # user = Member.objects.get(user_phone = session_phone)
    session_value = request.session['user_name']
    
    content.content.create(comment_content = request.POST.get('comment'), comment_date = timezone.now(), comment_writer=session_value)
    return redirect('/boardapp/'+str(content.pk))

def post_like_toggle(request, pk):
    content = get_object_or_404(BoardAllContentList, id=pk)
    user = request.session['user_name']
    profile = Profile.objects.get(user=user_name)

    check_like_post = profile.like_posts.filter(id=pk)

    if check_like_post.exists():
        profile.like_posts.remove(content)
        content.like_count -= 1
        content.save()
    else:
        profile.like_posts.add(content)
        content.like_count += 1
        content.save()

    return redirect('/boardapp/'+str(content.pk), pk)

# 게시글 좋아요
def like_post(request):
    pk = request.POST.get('pk', None)
    content = get_object_or_404(BoardAllContentList, pk=pk)
    user = request.user

    if content.like.filter(id=user.id).exits():
        content.like.remove(user)
        message = "좋아요 취소"
    else:
        content.like.add(user)
        message = "좋아요"

    context = {'likes_count':content.count_likes_user(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")


# 페이지네이션
def index(request):
    
    content_list = BoardAllContentList.objects.all()
    content_list = list(reversed(content_list)) # 최근순부터 출력하기 위해
    print(content_list)

    # 조회
    # content_list = BoardAllContentList.objects.order_by('-date')

    # 페이징처리
    paginator = Paginator(content_list, 10)  # 페이지당 10개씩 보여주기
    
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    page_obj = paginator.get_page(page)

    return render(request, 'boardapp/board_free.html', {'page_obj': page_obj})
