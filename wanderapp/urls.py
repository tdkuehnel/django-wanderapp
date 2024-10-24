"""wanderapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.urls import re_path
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.urls import path, include

from .views import index

urlpatterns = [

    # Hauptansicht
    path('',                               index,                                                                name='index'),
    re_path(r'^abmelden/$',                LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL},    name='abmelden'),

    # Admin Interface
    path('admin/', admin.site.urls),

    # Benutzer
    path('benutzer/', include('benutzer.urls')),

    # Wanderstrecken
    path('wanderstrecken/', include('wanderstrecke.urls')),

    # TinyMCE
    path('tinymce/', include('tinymce.urls')),

    # django-simple-captcha
    path('captcha/', include('captcha.urls')),

    # allauth
    path('benutzer/', include('wanderapp.authurls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
