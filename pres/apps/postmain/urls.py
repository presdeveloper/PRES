from django.urls import path, include

urlpatterns = [
    path('', include('pres.apps.postmain.post.urls')),
]
