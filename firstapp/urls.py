from django.urls import path, re_path

from . import views
from .views import PostDetailView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about', views.about_page, name='about_page'),
    path('postlist/', views.index, name='index_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/create', views.PostCreate.as_view(), name='post_create'),
    re_path(r'^posts/(?P<pk>\d+)/update/$', views.PostUpdate.as_view(), name='post_update'),
    re_path(r'^posts/(?P<pk>\d+)/delete/$', views.PostDelete.as_view(), name='post_delete')
]
