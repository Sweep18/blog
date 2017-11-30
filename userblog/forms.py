from django import forms

from .models import News, CommentNews


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentNews
        fields = ['comment', ]

