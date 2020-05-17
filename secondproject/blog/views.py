from django.shortcuts import render , get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
def home(request):
    blogs = Blog.objects #쿼리셋 #메소드
    return render(request, 'home.html',{'blogs':blogs})

#쿼리셋과 메소드의 형식
#모델.쿼리셋(objects).메소드

def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html',{'blog':blog})

def new(request):
    return render(request,'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.pub_date = timezone.datetime.now()
    new_blog.body= request.POST['body']
    new_blog.save()
    return redirect('/blog/'+str(new_blog.id))

def edit(request,blog_id):
    edit_blog = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'edit.html',{'blog':edit_blog})

def update(request,blog_id):
    update_blog = get_object_or_404(Blog,pk = blog_id)
    update_blog.title = request.POST['title']
    update_blog.pub_date = timezone.datetime.now()
    update_blog.body= request.POST['body']
    update_blog.save()
    return redirect('detail',update_blog.id)

def delete(request,blog_id):
    delete_blog = get_object_or_404(Blog, pk = blog_id)
    delete_blog.delete()
    return redirect('home')