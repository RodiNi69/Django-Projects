from .views import NewsList, PostDetail, NewsFilter, Create_n, Create_edit, Delete_news
from django.urls import path

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('search/', NewsFilter.as_view(), name='search'),
    path('create/', Create_n.as_view(), name='create_news'),
    path('<int:pk>/edit/', Create_edit.as_view(), name='edit'),
    path('<int:pk>/delete/', Delete_news.as_view(), name='delete'),
 ]
