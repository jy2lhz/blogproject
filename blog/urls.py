from django.urls import path,re_path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/(?P<pk>[0-9]+)/', views.PostDetailView.as_view(), name='detail'),
    path('archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/', views.ArchivesView.as_view(), name='archives'),
    path('category/(?P<pk>[0-9]+)/', views.CategoryView.as_view(), name='category'),
    path('tag/(?P<pk>[0-9]+)/', views.TagView.as_view(), name='tag'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about')
]
