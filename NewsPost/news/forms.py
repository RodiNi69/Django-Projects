from django import forms
from .models import Author, Post


class Create_news(forms.ModelForm):
    author = forms.ModelChoiceField(
        label='Автор',
        queryset=Author.objects.order_by('-full_name').all(),
        empty_label='Выберите автора',
    )
    post_title = forms.CharField(
        label='Заголовок'
    )
    post_text = forms.CharField(
        label='Текст',
        widget=forms.Textarea
    )

    class Meta:
        model = Post
        fields = [
            'post_title',
            'post_text',
            'author',
        ]
