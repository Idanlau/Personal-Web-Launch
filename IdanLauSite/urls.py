"""IdanLauSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLcid = models.AutoField(primary_key=True, **options)nf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from Accounts.views import account_view, account_create_view, logout_view, edit_profile_view, CustomLoginView
from Pages.views import home_view, preview, post_view, not_logged_preview
from Upload.views import AdminPostView
from Contact.views import contactview
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('create/', account_create_view),
    path('account/profile/', account_view),
    path('logout/', logout_view),
    path('prev/', preview.as_view()),
    path('post/<id>/', post_view),
    path('edit/bio/', edit_profile_view),
    path('login/', CustomLoginView.as_view()),
    path('upload/',AdminPostView),
    path('not/prev/', not_logged_preview.as_view()),
    path('contact/', contactview),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
