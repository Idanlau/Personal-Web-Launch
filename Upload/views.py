from django.shortcuts import render, redirect
from Accounts.models import Profile
from django.views.generic.edit import FormView
from .models import Uploads,PostImages
from .forms import UploadForm, ImageForm


# Create your views here.
def AdminPostView(request):
    form = UploadForm(request.POST or None, request.FILES or None)
    img_form = ImageForm(request.POST or None, request.FILES or None)
    images = request.FILES.getlist('post_imgs')  # field name in model

    if form.is_valid() and img_form.is_valid():
        form.save()
        print('valid')
        for i in images:
            PostImages.objects.create(post = form.save(), post_imgs = i)

        return redirect('/prev/')

    return render(request,'UploadView.html',{'form':form, 'profile': Profile.objects.get(user=request.user), 'img_form':img_form})


