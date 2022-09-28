from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
from .models import Post, Author
from django import forms


class PostFilter(FilterSet):
    search_title = CharFilter(
        field_name='post_title',
        label='Заголовок',
        lookup_expr='icontains'
        )
    search_author = ModelChoiceFilter(
        field_name='author',
        label='Автор',
        queryset=Author.objects.all(),
        lookup_expr='icontains',
        )
    search_date = DateFilter(
        field_name='post_date',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата',
        lookup_expr='date__gte',
        )

    class Meta:
        model = Post
        fields = ['post_title', 'author', 'post_date']
