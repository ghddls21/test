from django.http import HttpResponse
from django.shortcuts import render

def mainIndex(request):
    return render(request, 'index.html')

def singleAlpha(request, number):
    return HttpResponse('{} 패턴 인자로 전달'.format(number))

def boardPage(request):
    return HttpResponse('게시판 페이지')

def boardDetail(reqeust, number):
    return HttpResponse('{}번 게시물로 이동 완료'.format(number))

def blogPage(request, title):
    return HttpResponse('{} 블로그 페이지'.format(title))