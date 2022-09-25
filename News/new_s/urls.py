from .views import NewsList, PostDetail
from django.urls import path

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
]
