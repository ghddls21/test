from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mainIndex(reqeust):
    context = {
        'boardTable':[
            {
                'id':1, 'title':'文대통령, 출퇴근 종료', 'author':'이데일리'
            },
            {
                'id':2, 'title':'식사 \'스킨십 소통\'', 'author':'SBS 뉴스'
            },
            {
                'id':3, 'title':'참모들과 대통령', 'author':'한국경제'
            },
            {
                'id':4, 'title':'文 대통령 드라이브', 'author':'한국일보'
            }
        ]
    }
    return render(reqeust, 'board/index.html', context)

def boardDetail(reqeust, number):
    context = {
        'board':{'id':number, 'title':'제목',
            'author':'admin', 'context':'게시물 내용'
        }
    }
    
    return render(reqeust, 'board/detail.html', context)

def boardCreate(reqeust):
    return render(reqeust, 'board/create.html')

def boardUpdate(reqeust, number):
    return render(reqeust, 'board/update.html')

def boardDelete(reqeust, number):
    return render(reqeust, 'board/delete.html')