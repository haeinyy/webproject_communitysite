from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import BoardAllContentList, Board_comment, Image
from django.utils import timezone

# 자유게시판 메인 목록
def freeboard(request):
    content_list = BoardAllContentList.objects.all()
    content_list = list(reversed(content_list)) # 최근순부터 출력하기 위해
    return render(request, 'boardapp/board_free.html', {'content_list':content_list})

# 글쓰기 양식
def writetext(request):
    content = BoardAllContentList()
    # content_list = BoardAllContentList.objects.all()

    if request.method == 'POST': # 내용 입력후, 전달 할때
        content.title = request.POST['title']
        content.text = request.POST['text']
        content.date = timezone.datetime.now()
        # content.user = request.user
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
    return render(request, 'boardapp/content_view.html', {'content':content})

# 게시글 댓글
def comment_write(request, pk):
    # if request.method == 'POST':
    content = get_object_or_404(BoardAllContentList, pk = pk)

    content.content.create(comment_content = request.POST.get('comment'), comment_date = timezone.now())
    return redirect('/boardapp/'+str(content.pk))

# 게시글 좋아요
def like_post(request, pk):
    content = get_object_or_404(BoardAllContentList, pk = pk)
    if request.user in content.like_users.all():
        content.like.remove(request.user)
    else:
        content.like.add(request.user)