from django.shortcuts import render, get_object_or_404, redirect
from Upload.models import Uploads, PostImages
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from Accounts.models import Profile




# Create your views here.
def home_view(request):
    return render(request, "Home/home_view.html")


class preview(LoginRequiredMixin,ListView):
    #raise_exception = False
    login_url = '/not/prev/'
    redirect_field_name = 'redirect_to'
    model = Uploads
    template_name = 'Posts/preview.html'
    context_object_name = 'posts'
    ordering = ['-time']

    def get_context_data(self, **kwargs):
        data = super(preview, self).get_context_data(**kwargs)
        data['profile'] = Profile.objects.get(user=self.request.user)
        data['posts'] = Uploads.objects.order_by('-time')
        return data

    def get_queryset(self):
         profile = Profile.objects.get(user=self.request.user)
         posts = Uploads.objects.all()
         queryset = {
              'profile': Profile.objects.get(user=self.request.user),'posts': Uploads.objects.order_by('-time')
          }

         return queryset

class not_logged_preview(ListView):
    model = Uploads
    template_name = 'Posts/not_logged_prev.html'
    context_object_name = 'posts'
    ordering = ['-time']

    def get_context_data(self, **kwargs):
        data = super(not_logged_preview, self).get_context_data(**kwargs)
        data['posts'] = Uploads.objects.order_by('-time')
        return data

    def get_queryset(self):
         posts = Uploads.objects.all()
         queryset = {
            'posts': Uploads.objects.order_by('-time')
          }

         return queryset


def post_view(request,id):
    if request.user.is_authenticated:
            post = Uploads.objects.get(id=id)
            images = post.postimages_set.all()
            initial = images.first()

            images = images.exclude(id = initial.id)
            content = {'post':post , 'profile': request.user.Profile,'images': images, 'initial': initial }
            return render(request, "Posts/post_view.html",content)

    else:
        post = Uploads.objects.get(id=id)
        images = post.postimages_set.all()
        initial = images.first()
        content = {'post':post,'images': images, 'initial': initial }
        return render(request, "Posts/not_logged_post.html", content)
