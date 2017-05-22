from django.conf.urls import include, url
from django.contrib import admin
from pyweb import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'pyweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.mainIndex, name='main'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^board/', include('board.urls', namespace = 'board')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^([0-9]{2,4})/', views.singleAlpha),
    url(r'^account/', include('django.contrib.auth.urls')),
    

]
'''
r : raw String -> 이스케이프 문자가 적용 되지 않는 문자열
^ : 패턴의 시작
$ : 패턴의 끝
[a-z] : 소문자 a부터 z까지 매치되는 문자 1개
[a-z]+ : 소문자 a부터 z까지 매치되는 문자 1개 이상
[A-Z] : 대문자 A부터 Z까지 매치되는 문자 1개
[A-Z]+ : 대문자 A부터 Z까지 매치되는 문자 1개 이상
[a-zA-Z]+ : 대소문자 구분 없이 매치 되는 문자 1개 이상
[0-9]+ : 숫자 0 ~ 9까지 매치되는 값 1자리 이상
[0-9]{4} : 숫자 0 ~ 9까지 4자리 매치되는 값
[0-9]{2,4} : 숫자 0 ~ 9까지 2~4자리 매치되는 값
(....) : 소괄호안의 매치되는 패턴을 함수의 인자로 전달
'''

'''
127.0.0.1:8000/board/
   게시판 페이지

127.0.0.1:8000/board/10/
   10번 게시물로 이동 완료

127.0.0.1:8000/blog/web/
    web 블로그 페이지

127.0.0.1:8000/blog/network/
    network 블로그 페이지
'''



