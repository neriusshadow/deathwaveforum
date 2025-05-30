from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('topic/new/', views.topic_create, name='topic_create'),
    path('topic/<slug:slug>/', views.topic_detail, name='topic_detail'),
    path('topic/<slug:slug>/edit/', views.topic_edit, name='topic_edit'),
    path('topic/<slug:slug>/delete/', views.topic_delete, name='topic_delete'),
    path('topic/<slug:slug>/reply/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('search/', views.search, name='search'),
] 