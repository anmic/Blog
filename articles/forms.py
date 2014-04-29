from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'special'}),
        max_length=50)
    markdown_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'special', 'rows': 4, 'cols': 20}),
        max_length=500)

    def __unicode__(self):
        return "Title: %r, Text: %r." % \
               (self.title, self.text)
