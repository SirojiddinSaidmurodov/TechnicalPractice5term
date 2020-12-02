from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'created_date', 'publish_date')


class SearchForm(forms.Form):
    query = forms.CharField()
