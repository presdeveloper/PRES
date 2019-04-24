from django.shortcuts import render
from django.views import View

from pres.apps.postmain.post.models import Post


class FeedGeneral(View):
    template_name = 'postmain/post/feedgeneral.html'
    def get(self, request):
        context = {}

        user_logged = request.user
        post_list = Post.objects.all()

        context['post_list'] = post_list

        return render(request, self.template_name, context)


class CreatePost(View):
    template_name = 'postmain/post/createpost.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass
