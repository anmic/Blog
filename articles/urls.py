from django.conf.urls.defaults import url, patterns


urlpatterns = patterns(
    '',
    (r'^all/$', "articles.views.list_articles"),
    url(r'^articles/(?P<article_id>\d{1,4})/$',
        'articles.views.show_article',
        name='articles-list'),
)
