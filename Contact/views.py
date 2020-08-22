from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from Accounts.models import Profile
from django.contrib.auth.models import User

def contactview(request):
    email=''
    subject=''
    message=''


    form= ContactForm(request.POST or None)

    if request.user.is_authenticated:

        if form.is_valid():
            email= form.cleaned_data.get("email")
            subject= form.cleaned_data.get("subject")
            message=form.cleaned_data.get("message")


            subject= str(request.user) + "'s Comment"


            message = email + " with the email, " + subject + ", sent the following message:\n\n" + message
            send_mail(subject, message, email, ['lauidan31@gmail.com'])

            return render(request, 'contact.html', {'form': form, 'profile': Profile.objects.get(user=request.user)})


        else:
            return render(request, 'contact.html', {'form': form, 'profile': Profile.objects.get(user=request.user)})

    else:
        if form.is_valid():
            email = form.cleaned_data.get("email")
            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("message")

            subject = "Guest" + "'s Comment"

            message = email + " with the email, " + subject + ", sent the following message:\n\n" + message
            send_mail(subject, message, email, ['lauidan31@gmail.com'])

        return render(request, 'not_logged_contact.html',{'form': form})





