from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse
from .models import Post, Category
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q

# LISTAR POSTAGENS EM GERAL
def post_list(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    main_posts_01 = Post.objects.filter(published=True, main_01=True).order_by('-created_at')[:3]
    main_posts_02 = Post.objects.filter(published=True, main_02=True).order_by('-created_at')[:4]
    highlighted_posts = Post.objects.filter(published=True, highlighted=True).order_by('-created_at')[:5] # filtrar por destaques
    breaking_ticker = Post.objects.filter(published=True).order_by('-created_at')[:5]
    popular_posts = Post.objects.filter(published=True).order_by('-views')[:5] # Recuperar 5 postagens mais visualizadas
    paginator = Paginator(posts, 6)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'main_posts_01': main_posts_01,
        'main_posts_02': main_posts_02,
        'highlighted_posts': highlighted_posts,
        'breaking_ticker': breaking_ticker,
        'popular_posts': popular_posts,
        'page_obj': page_obj,
    }
    return render(request, "post_list.html", context)

# PESQUISA
def search_results(request):
    search_query = request.GET.get('q', '')
    results = Post.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
    popular_posts = Post.objects.filter(published=True).order_by('-views')[:5]
    paginator = Paginator(results, 6)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'search_query': search_query,
        'results': results,
        'popular_posts': popular_posts,
        'page_obj': page_obj
    }
    
    return render(request, 'search_results.html', context)


# LISTAR POSTAGENS POR CATEGORIA
def post_list_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category, published=True).order_by('-created_at')
    popular_posts = Post.objects.filter(published=True).order_by('-views')[:5]
    paginator = Paginator(posts, 6)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category': category,
        'posts': posts,
        'popular_posts': popular_posts,
        'page_obj': page_obj,
        'category_url': reverse('post_list_by_category', kwargs={'category_slug': category.slug})
        }
  
    return render(request, "post_list_by_category.html", context)


# Pagina de detalhes de um post
def post_detail(request, year, month, slug_url):
    post = get_object_or_404(Post, year=year, month=month, slug=slug_url, published=True)
    post.increase_views()
    popular_posts = Post.objects.filter(published=True).order_by('-views')[:5]
    context = {
        'post': post,
        'popular_posts': popular_posts,
    }
    return render(request, "post_detail.html", context)


def about(request):
    return render(request, 'about.html')

 