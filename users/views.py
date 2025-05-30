from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Profile
from .forms import ProfileForm
from forum.models import Topic, Post

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен!')
            return redirect('users:profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/profile_edit.html', {'form': form})

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/user_profile.html', {'profile_user': user})

def user_topics(request, username):
    user = get_object_or_404(User, username=username)
    topics = user.topics.all()
    paginator = Paginator(topics, 10)
    page = request.GET.get('page')
    topics = paginator.get_page(page)
    return render(request, 'users/user_topics.html', {
        'profile_user': user,
        'topics': topics,
    })

def user_posts(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.posts.all()
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'users/user_posts.html', {
        'profile_user': user,
        'posts': posts,
    })
