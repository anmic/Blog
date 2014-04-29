from django.contrib import admin

from models import Articles, ArticlesAdmin

admin.site.register(Articles, ArticlesAdmin)
