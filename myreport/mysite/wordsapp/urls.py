from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('search_company/', views.search_company, name='search_company'),
    path('search_horoscope/', views.search_horoscope, name='search_horoscope'),
]
