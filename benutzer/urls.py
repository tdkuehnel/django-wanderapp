from django.urls import path

from django.contrib.auth import views as authviews
from . import views
from . import wizardviews

app_name = 'benutzer'

urlpatterns = [

    # Eigene Views.
    path('anmeldung/',                                       views.WanderappLoginView.as_view(),                 name='login'),
    path("profil/",                                          views.redirect_to_user_profile,                     name="home"),
    path("profil/<int:pk>/",                                 views.BenutzerProfilView.as_view(),                 name="profil"),
    path("wanderstrecken/",                                  views.redirect_to_user_wanderstrecken,              name="wanderhome"),
    path('wanderstrecken/<int:benutzer_id>/',                views.BenutzerWanderStreckeListView.as_view(),      name='wanderstrecken'),
    path('wanderstrecke/hinzu/',                             views.BenutzerWanderStreckeCreateView.as_view(),    name='wanderstrecke_hinzu'),
    path('wanderstrecke/<int:pk>/',                          views.BenutzerWanderStreckeDetailView.as_view(),    name='wanderstrecke'),
    path('wanderstrecke/bearbeiten/<int:pk>/',               views.BenutzerWanderStreckeUpdateView.as_view(),    name='wanderstrecke_bearbeiten'),
    path('wanderstrecke/loeschen/<int:pk>/',                 views.BenutzerWanderStreckeDeleteView.as_view(),    name='wanderstrecke_loeschen'),

    path('wanderstreckewizardc1/',                           wizardviews.WizardCreateView.as_view(),             name='wizardc1'),
    path('wanderstreckewizard1/<int:pk>/',                   wizardviews.WizardUpdateView1.as_view(),            name='wizard1'),
    path('wanderstreckewizard2/<int:pk>/',                   wizardviews.WizardUpdateView2.as_view(),            name='wizard2'),
    #path('wanderstreckewizard3/<int:pk>/',                   wizardviews.WizardUpdateView3.as_view(),            name='wizard3'),
    path('wanderstreckewizard3cneu/<int:pk>/',               wizardviews.WizardCreateView3Neu.as_view(),         name='wizard3cneu'),
    path('wanderstreckewizard3neu/<int:pk>/',                wizardviews.WizardUpdateView3Neu.as_view(),         name='wizard3neu'),
    path('wanderstreckewizard4neu/<int:pk>/',                wizardviews.WizardUpdateView4Neu.as_view(),         name='wizard4neu'),
    path('wanderstreckewizard3vorhanden/<int:pk>/',          wizardviews.WizardUpdateView3Vorhanden.as_view(),   name='wizard3vorhanden'),

    path('hilfejson/',                                       wizardviews.HilfeJSONView.as_view(),                name='hilfe_json'),
    path('hilfeurl/',                                        wizardviews.HilfeURLView.as_view(),                 name='hilfe_url'),

    # Views aus dem Paket django.contrib.auth
    path("abmeldung/",                       authviews.LogoutView.as_view(),                 name="logout"),
    path("passwortaenderung/",               authviews.PasswordChangeView.as_view(),         name="password_change"),
    path("passwordgeaendert/",               authviews.PasswordChangeDoneView.as_view(),     name="password_change_done"),
    path("passwordzuruecksetzen/",           authviews.PasswordResetView.as_view(),          name="password_reset"),
    path("passwordzurueckgesetzt/",          authviews.PasswordResetDoneView.as_view(),      name="password_reset_done"),
    path("zuruecksetzen/<uidb64>/<token>/",  authviews.PasswordResetConfirmView.as_view(),   name="password_reset_confirm"),
    path("zurueckgesetzt/",                  authviews.PasswordResetCompleteView.as_view(),  name="password_reset_complete"),

]
