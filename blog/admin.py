from django.contrib import admin

from blog.articles.models import Articles
from blog.articles.models import User


admin.site.register(Articles)
admin.site.register(User)
