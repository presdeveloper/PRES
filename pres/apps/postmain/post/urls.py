from django.urls import path, include
from .views_list import FeedGeneral, CreatePost

urlpatterns = [
    path('feed-geral/', FeedGeneral.as_view()),
    path('postar/', CreatePost.as_view(), name='create_post')

]
