from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms


def article_list_view(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html',
                  {'articles': articles})


def article_detail_view(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html',
                  {'article': article})


@login_required(login_url="/accounts/login/")
def article_create_view(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)

        if form.is_valid():
            # TODO: Save article to database
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()

    return render(request, 'articles/article_create.html', {'form': form})
