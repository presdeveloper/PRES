from django.shortcuts import render
from django.views import View

# Create your views here.

class FeedGeneral(View):
    template_name = 'postmain/post/feedgeneral.html'
    def get(self, request):
        return render(request, self.template_name)


    def post(self, request):
        pass
