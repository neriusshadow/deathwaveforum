from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('profile/<str:username>/topics/', views.user_topics, name='user_topics'),
    path('profile/<str:username>/posts/', views.user_posts, name='user_posts'),
] 