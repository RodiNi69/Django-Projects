from news.views import NewsList, PostDetail, Create_n, Create_edit, Delete_news
from django.urls import path


urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('create/', Create_n.as_view(), name='article_create'),
    path('<int:pk>/edit/', Create_edit.as_view(), name='article_edit'),
    path('<int:pk>/delete/', Delete_news.as_view(), name='article_delete'),
]
