from django.urls import path

from django.contrib.auth import views as authviews
from . import views

app_name = 'benutzer'

urlpatterns = [

    # Eigene Views.
    path('anmeldung/',                                       views.WanderappLoginView.as_view(),                 name='login'),
    path("profil/",                                          views.redirect_to_user_profile,                     name="home"),
    path("profil/<int:pk>",                                  views.BenutzerProfilView.as_view(),                 name="profil"),
    path("wanderstrecken/",                                  views.redirect_to_user_wanderstrecken,              name="wanderhome"),
    path('wanderstrecken/<int:benutzer_id>/',                views.BenutzerWanderStreckeListView.as_view(),      name='wanderstrecken'),
    path('wanderstrecke/hinzu/',                             views.BenutzerWanderStreckeCreateView.as_view(),    name='wanderstrecke_hinzu'),
    path('wanderstrecke/<int:pk>/',                          views.BenutzerWanderStreckeDetailView.as_view(),    name='wanderstrecke'),
    path('wanderstrecke/bearbeiten/<int:pk>/',               views.BenutzerWanderStreckeUpdateView.as_view(),    name='wanderstrecke_bearbeiten'),

    # Views aus dem Paket django.contrib.auth
    path("abmeldung/",                       authviews.LogoutView.as_view(),                 name="logout"),
    path("passwortaenderung/",               authviews.PasswordChangeView.as_view(),         name="password_change"),
    path("passwordgeaendert/",               authviews.PasswordChangeDoneView.as_view(),     name="password_change_done"),
    path("passwordzuruecksetzen/",           authviews.PasswordResetView.as_view(),          name="password_reset"),
    path("passwordzurueckgesetzt/",          authviews.PasswordResetDoneView.as_view(),      name="password_reset_done"),
    path("zuruecksetzen/<uidb64>/<token>/",  authviews.PasswordResetConfirmView.as_view(),   name="password_reset_confirm"),
    path("zurueckgesetzt/",                  authviews.PasswordResetCompleteView.as_view(),  name="password_reset_complete"),

]
