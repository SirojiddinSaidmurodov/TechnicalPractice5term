from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about', views.about_page, name='about_page'),
    path('list/', views.index, name='index_list'),
    path('form/', views.post, name='post'),
    path('list/filter/', views.filter_list, name='filter_list')
]
