"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.urls import re_path as url
from myapp import views


urlpatterns = [
    path("", views.index),
    path("hello/", views.hello),
    # 若是要設定成首頁，則"hello/"改成""，也就是什麼都不要打，不是"/"喔，"/"是起始位置
    path("hello1/<number>", views.hello1),  # 位置對應法
    path("hello2/", views.hello2),
    # 名稱對應法(網址輸入法：.../hello2/?number=aaa&score=60；score、number反過來一樣可以執行.../hello2/?score=60&number=aaa)


    path("lotto/", views.getLotto),
    path("login/", views.login),
    url(r'^crups/', views.crudops, name='hello'),
    url(r'^articles/(\d{2})/(\d{4})/', views.viewArticles, name='articles'),
    # "^"是正則表示法的開頭
    url(r'^simpleemail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/',
        views.sendSimpleEmail, name='sendSimpleEmail'),

    url(r'^fireBaseDBtest/', views.fireBaseDBtest, name='fireBaseDBtest'),

    url(r'^signIn/', views.signIn, name='signIn'),
    url(r'^postsignIn/', views.postsignIn, name='postsignIn'),
    url(r'^signUp/', views.signUp, name='signUp'),
    url(r'^postsignUp/', views.postsignUp, name='postsignUp'),
    url(r'^logout/', views.logout, name='logout'),

]

#徐尉庭新增
from django.urls import path
from . import views

urlpatterns = [
    # ... 省略其他 URL 路径 ...
    path('get_horoscope_data/', views.get_horoscope_data, name='get_horoscope_data'),
]

