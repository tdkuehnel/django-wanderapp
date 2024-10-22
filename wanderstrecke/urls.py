from django.urls import path

from django.contrib.auth import views as authviews
from . import views

app_name = 'wanderstrecke'

urlpatterns = [
    path('',                                 views.WanderStreckeListView.as_view(),                          name='index'),
]
