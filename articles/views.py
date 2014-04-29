from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from articles.models import Articles
from articles.forms import ArticleForm


def list_articles(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Articles(
                title=form.cleaned_data['title'],
                markdown_text=form.cleaned_data['markdown_text']
            )
            article.save()
            messages.success(request, "Your article add.")
            return HttpResponseRedirect("/articles/all/")
    else:
        form = ArticleForm()
    articles = Articles.objects.all()
    return render(request, "articles/list_articles.html", {
        'form': form,
        "articles": articles,
    })


def show_article(request, article_id):
    article = Articles.objects.get(id=article_id)
    return render(request, "articles/show_article.html", {
        "article": article,
    })
