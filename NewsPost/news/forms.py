from django import forms
from django.core.exceptions import ValidationError
from .models import Author, Post


class Create_news(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'post_title',
            'post_text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('post_title')
        text = cleaned_data.get('post_text')
        if text == title:
            raise ValidationError(
                {'text': 'Текст публикации не должен быть идентичен её названию'}
            )
        return cleaned_data
