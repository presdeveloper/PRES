from django.urls import path, include
from .views_list import FeedGeneral

urlpatterns = [
    path('feed-geral/', FeedGeneral.as_view())
]
