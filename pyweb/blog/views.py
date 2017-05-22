from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import BlogTable
from datetime import datetime

# Create your views here.
def mainIndex(request):
    blog_table = BlogTable.objects.\
        values('id', '제목', '작성자', '조회수').all().order_by('-id')
    context = {
        'blog_table': blog_table
    }
    return render(request, 'blog/index.html', context)

def blogDetail(request, number):
    blog_table = BlogTable.objects.get(id=number)
    context = {
        'blog_table':blog_table
    }
    blog_table.조회수 += 1
    blog_table.save()
    
        
    return render(request, 'blog/detail.html', context)

def blogCreate(request):
    if request.method == "GET":
        return render(request, 'blog/create.html')
    elif request.method == "POST":
        blog_table = BlogTable()
        blog_table.제목 = request.POST.get('title')
        blog_table.내용 = request.POST.get('context')
        blog_table.작성자 = request.POST.get('author')
        blog_table.등록일 = datetime.now()
        blog_table.수정일 = datetime.now()
        blog_table.조회수 = 0
        blog_table.save()

        return redirect('blog:index')

def blogUpdate(request, number):
    if request.method == "GET":
        blog_table = BlogTable.objects.get(id=number)
        context = {
            'blog_table':blog_table
        }
        return render(request, 'blog/update.html', context)
    elif request.method == "POST":
        blog_table = BlogTable.objects.get(id=number)
        blog_table.제목 = request.POST.get('title')
        blog_table.내용 = request.POST.get('context')
        blog_table.작성자 = request.POST.get('author')
        blog_table.수정일 = datetime.now()
        blog_table.save()

        return redirect('blog:detail', number)

def blogDelete(request, number):
    blog_table = BlogTable.objects.get(id=number)
    
    context = {
        'blog_table':{'id':blog_table.id, '제목':blog_table.제목}
    }

    blog_table.delete()

    return render(request, 'blog/delete.html', context)