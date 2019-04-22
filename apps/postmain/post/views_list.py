from django.shortcuts import render
from django.views import View

# Create your views here.

class FeedGeneral(View):
    def get(self, request):
        return render(request, 'postmain/post/feedgeneral.html')


    def post(self, request):
        pass
