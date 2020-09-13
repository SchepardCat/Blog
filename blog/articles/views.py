from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def article_list(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page', 1)
    page =paginator.get_page(page_number)

    return render(request, 'articles/article_list.html', { 'page_object': page })
    
def article_detail(request, slug):
    
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', { 'article': article })


