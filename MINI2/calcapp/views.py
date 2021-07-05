from django.http import HttpResponse, request
from . models import Member
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from . models import AttendHistroy, Blog
from calcapp.forms import BlogUpdate
from django.core.paginator import Paginator

# 공지사항
def home(request):
    blogs = Blog.objects.order_by('-id')
    # 페이징( home 수정 )
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list,3) # 3개씩
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'calcapp/home.html', {'blogs':blogs,'posts':posts} )

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id) # blog_id는 글이 생기면 장고에서 저절로 부여하는 고유 번호
    return render(request, 'calcapp/detail.html', {'blog': blog_detail})

def create(request):
    return render(request, 'calcapp/create.html')

def postcreate(request):
    
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.images = request.FILES['images']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/calcapp/detail/' + str(blog.id))

def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method =='POST':
        form = BlogUpdate(request.POST)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('/calcapp/detail/' + str(blog.id))
    else:
        form = BlogUpdate(instance = blog)
 
        return render(request,'calcapp/update.html', {'form':form})

def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/calcapp/home/')

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
def index(request, pk):
    # attendances = AttendHistroy.objects.all()
    # str =''
    # for attendance in attendances:
    #     str += "<p> name: {} attend: {}".format(attendance.name, attendance.attend)
    # return HttpResponse(str)
    
    attendancesList = AttendHistroy.objects.all()
    # a = '0219'
    # memberList = Member.objects.all()
    # attenda = []
    # for i in attendancesList:
    #     if i.user_phone == a:
    #         attenda.append(i)

    context = {
        'attnedances': attendancesList
    }
    return render(request, 'calcapp/calcpage_info.html', context)
    # return render(request, 'calcapp/index.html', context)

    ## 메모
    # a = request.session['user_phone']

def calcpage(request):
    pay = int(15000)
    day1 = int(request.POST['num1'])
    result = day1 * pay
    return render(request, 'calcapp/calcpage.html', {'result':result})

def calcpage_result(request):
    return render(request, 'calcapp/calcpage_result.html', {'name':'name'})
 
def calcpage_info(request):
    return render(request, 'calcapp/calcpage_info.html')

def calcpage_user(request):
    attendancesList = AttendHistroy.objects.all()    
    context = {'attnedances': attendancesList}
    return render(request, 'calcapp/calcpage_user.html', context) 