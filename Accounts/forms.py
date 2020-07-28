from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from crispy_forms.helper import FormHelper
from .models import Profile



class CustomCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(CustomCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'first_name','last_name','email','password1', 'password2']:
           self.fields[fieldname].help_text = None


class RegistrationForm(CustomCreateForm):
    #helper = FormHelper()
    #helper.form_show_labels = True
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',

        )


    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class edit_profile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description','image']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
