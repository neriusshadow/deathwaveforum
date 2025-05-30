from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Category, Topic, Post
from .forms import TopicForm, PostForm

def home(request):
    categories = Category.objects.all()
    latest_topics = Topic.objects.all().order_by('-created_at')[:5]
    context = {
        'categories': categories,
        'latest_topics': latest_topics,
    }
    return render(request, 'forum/index.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    topics = category.topics.all()
    paginator = Paginator(topics, 10)
    page = request.GET.get('page')
    topics = paginator.get_page(page)
    context = {
        'category': category,
        'topics': topics,
    }
    return render(request, 'forum/category_detail.html', context)

def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    topic.views += 1
    topic.save()
    posts = topic.posts.all()
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'topic': topic,
        'posts': posts,
    }
    return render(request, 'forum/topic_detail.html', context)

@login_required
def topic_create(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            messages.success(request, 'Тема успешно создана!')
            return redirect('forum:topic_detail', slug=topic.slug)
    else:
        form = TopicForm()
    return render(request, 'forum/topic_form.html', {'form': form})

@login_required
def topic_edit(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    if request.user != topic.author:
        messages.error(request, 'У вас нет прав для редактирования этой темы!')
        return redirect('forum:topic_detail', slug=topic.slug)
    
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            messages.success(request, 'Тема успешно обновлена!')
            return redirect('forum:topic_detail', slug=topic.slug)
    else:
        form = TopicForm(instance=topic)
    return render(request, 'forum/topic_form.html', {'form': form})

@login_required
def topic_delete(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    if request.user != topic.author:
        messages.error(request, 'У вас нет прав для удаления этой темы!')
        return redirect('forum:topic_detail', slug=topic.slug)
    
    if request.method == 'POST':
        topic.delete()
        messages.success(request, 'Тема успешно удалена!')
        return redirect('forum:home')
    return render(request, 'forum/topic_confirm_delete.html', {'topic': topic})

@login_required
def post_create(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.author = request.user
            post.save()
            messages.success(request, 'Ответ успешно добавлен!')
            return redirect('forum:topic_detail', slug=topic.slug)
    else:
        form = PostForm()
    return render(request, 'forum/post_form.html', {'form': form, 'topic': topic})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        messages.error(request, 'У вас нет прав для редактирования этого сообщения!')
        return redirect('forum:topic_detail', slug=post.topic.slug)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сообщение успешно обновлено!')
            return redirect('forum:topic_detail', slug=post.topic.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'forum/post_form.html', {'form': form, 'topic': post.topic})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        messages.error(request, 'У вас нет прав для удаления этого сообщения!')
        return redirect('forum:topic_detail', slug=post.topic.slug)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Сообщение успешно удалено!')
        return redirect('forum:topic_detail', slug=post.topic.slug)
    return render(request, 'forum/post_confirm_delete.html', {'post': post})

def search(request):
    query = request.GET.get('q')
    if query:
        topics = Topic.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        posts = Post.objects.filter(content__icontains=query)
    else:
        topics = Topic.objects.none()
        posts = Post.objects.none()
    
    context = {
        'query': query,
        'topics': topics,
        'posts': posts,
    }
    return render(request, 'forum/search.html', context)
