from django.db.models.query import RawQuerySet
from django.http import HttpResponse, request
from member.models import Member, Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from . models import Attendences, Blog
from calcapp.forms import BlogUpdate
from django.core.paginator import Paginator


# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ## ajax테스트 start
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
def contact(request):
    return render(request, 'calcapp/contact.html', {} )

def donation(request):
    return render(request,'calcapp/donation.html', {} )

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ## FAQ START
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
def faq(request):
    blogs = Blog.objects.all()
    # 페이징( notice 수정 )
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list,3) # 3개씩
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'calcapp/faq.html', {'blogs':blogs,'posts':posts} )
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ## 건의사항 START
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
def suggest(request):
    blogs = Blog.objects.all()
    # 페이징( notice 수정 )
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list,3) # 3개씩
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'calcapp/suggest.html', {'blogs':blogs,'posts':posts} )
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ## QnA START
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
def qna(request):
    blogs = Blog.objects.all()
    # 페이징( notice 수정 )
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list,3) # 3개씩
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'calcapp/qna.html', {'blogs':blogs,'posts':posts} )
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ## 공지사항 START
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
def notice(request):
    blogs = Blog.objects.all()
    # 페이징( home 수정 )
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list,3) # 3개씩
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'calcapp/notice.html', {'blogs':blogs,'posts':posts} )

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id) # blog_id는 글이 생기면 장고에서 저절로 부여하는 고유 번호
    return render(request, 'calcapp/detail.html', {
        'blog': blog_detail,
    })

def create(request):
    return render(request, 'calcapp/create.html')

def postcreate(request):
    blog = Blog()
    session_value = request.session['user_name']
    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.body = request.POST.get('body')
        blog.images = request.FILES.get('images')
        blog.pub_date = timezone.datetime.now()
        blog.user = session_value
        blog.save()
    return redirect('/calcapp/detail/' + str(blog.id))

def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method =='POST':
        form = BlogUpdate(request.POST)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.images = form.cleaned_data['images']
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('/calcapp/detail/' + str(blog.id))
    else:
        form = BlogUpdate(instance = blog)

        return render(request,'calcapp/update.html', {'form':form})

def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/calcapp/notice/')

# 검색기능
def search(request):
    blogs = Blog.objects.all().order_by('-id')

    q = request.POST.get('q', "")

    if q:
        blogs = blogs.filter(title__icontains=q)
        return render(request, 'calcapp/search.html', {'blogs' : blogs, 'q' : q})

    else:
        return render(request, 'calcapp/search.html')


# 계산기
def calcpage(request):
    pay = int(15000)
    day1 = int(request.POST['num1'])
    result = day1 * pay
    return render(request, 'calcapp/calcpage.html', {'result':result})

# 상세현황 및 수료현황
def calcpage_result(request):
    attendancesList = Attendences.objects.all()
    u_phone = request.session['user_phone']

    try: # 나는 학생이니까 정보가 있찌.
        user_info_list = Attendences.objects.get(user_phone_id=u_phone)
        user_profile = Profile.objects.get(user_name_id=u_phone)
        context = {
            'u_phone': u_phone,
            'name': user_info_list.name,
            'attend': user_info_list.attend,
            'absent': user_info_list.absent,
            'time': user_info_list.time,
            'time_rate': user_info_list.time_rate,
            'day_rate': user_info_list.day_rate,
            'time_cum_rate': user_info_list.time_cum_rate,
            'day_cum_rate': user_info_list.day_cum_rate,

            'nickname': user_profile.nickname,
            'description': user_profile.description,
            'image': user_profile.image,
            }
        return render(request, 'calcapp/calcpage_result.html', context)

    except: # 나는 관리자니까 정보가 없지.
        context = {
            'u_phone': u_phone,
            'attendances': attendancesList
        }
        return render(request, 'calcapp/calcpage_result.html', context)
        # return HttpResponse('등록된 정보가 없습니다.')

# 프로필
def ProfileView(request):
    profiles = Profile.objects.all()
    u_phone = request.session['user_phone']
    try:
        user_profile = Profile.objects.get(user_name_id=u_phone)
        # user_profile.images = request.FILES.get('images')
        context = {
            'u_phone': u_phone,
            'username': user_profile.user_name,
            'nickname': user_profile.nickname,
            'description': user_profile.description,
            'images': user_profile.images,
        }
        return render(request, 'calcapp/calcpage_result.html', context)

    except:
        context = {
            'u_phone': u_phone,
            'username': profiles.user_name,
            'nickname': profiles.nickname,
            'description': profiles.description,
            'images': profiles.images,
        }
        return render(request, 'calcapp/calcpage_result.html', context)
