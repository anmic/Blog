from markdown import markdown
from django.db import models
from datetime import datetime
from django.contrib import admin
from django.core.urlresolvers import reverse


class Articles(models.Model):
    title = models.CharField(max_length=50)
    markdown_text = models.TextField(max_length=500)
    html_text = models.TextField(editable=False)
    creation_time = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ["-creation_time"]

    def __unicode__(self):
        return "Title: %r, Text: %r." % \
               (self.title, self.markdown_text)

    @models.permalink
    def get_absolute_url(self):
        return ('articles-list', (), dict(article_id=self.id))

    def url_to_edit_object(obj):
        url = reverse(
            'admin:%s_%s_change' % (obj._meta.app_label, obj._meta.module_name),
            args=[obj.id],
        )
        return url

    def save(self):
        self.html_text = markdown(self.markdown_text)  # may be error
        super(Articles, self).save()


class ArticlesAdmin(admin.ModelAdmin):
    date_hierarchy = 'creation_time'
    list_display = ('title', 'markdown_text')
    search_fields = ('title', )
    list_display_links = ('title',)

    def short_text(self, obj):
        if len(obj.text) > 50:
            return ("%s ..." % (obj.text[:50]))
        else:
            return ("%s" % (obj.text))

    short_text.short_description = 'Text(50)'
