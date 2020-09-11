from django import forms
from .models import Uploads, PostImages
from django.forms.widgets import ClearableFileInput


class UploadForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = ['title','content','preview_img','code',]

class ImageForm(forms.ModelForm):
    # post_files = forms.FileField(
    #      widget=ClearableFileInput(attrs={'multiple': True}),
    #  )

    class Meta:
        model = PostImages
        exclude = "__all__"
        fields = ('post_imgs',)
        widgets = {
            'post_imgs': ClearableFileInput(attrs={'multiple': True}),
        }
        #

