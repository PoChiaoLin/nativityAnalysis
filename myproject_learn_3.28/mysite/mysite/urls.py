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
from django.contrib import admin
from django.urls import path, include
# from django.urls import re_path as url
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("hello/", views.hello),
    # 若是要設定成首頁，則"hello/"改成""，也就是什麼都不要打，不是"/"喔，"/"是起始位置
    # path("hello1/<number>", views.hello1),  # 位置對應法
    # path("hello2/", views.hello2),
    # 名稱對應法(網址輸入法：.../hello2/?number=aaa&score=60；score、number反過來一樣可以執行.../hello2/?score=60&number=aaa)
    path("myapp/", include('myapp.urls')),
    path("wordsapp/", include('wordsapp.urls')),

    # path("lotto/", views.getLotto),


]
