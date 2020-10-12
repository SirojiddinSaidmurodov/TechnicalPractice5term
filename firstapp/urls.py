from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about', views.about_page, name='about_page'),
]
