from django.conf import settings
from django.urls import path, re_path

from allauth import app_settings as allauth_app_settings
from allauth.account import app_settings

from allauth.account import views

# Hier werden die benötigten URL-Einträge aus dem Django allauth-Paket mit deutschen URL-Bezeichnungen neu definiert.
# So erscheinen schöne, deutsche Begriffe in der Adresszeile des Anzeigeprogrammes für Inhalte des weltweiten digitalen Netzwerkes.

urlpatterns = [
    path("anmelden/",              views.login,                     name="account_login"),
    path("abmelden/",              views.logout,                    name="account_logout"),
    path("inaktiv/",               views.account_inactive,          name="account_inactive"),
]

# Dazu werden die benötigten Abschnitte einfach auf den Dateien in
# <pythoninterpreter>/site-packages/allauth/urls.py und
# -/accounts/urls.py hierher kopiert und angepaßt.

urlpatterns.extend(
    [
        path("registrieren/",                                                  views.signup,                         name="account_signup"),
        path("registrierungsauffrischung/",                                    views.reauthenticate,                 name="account_reauthenticate"),
        # Email
        path("epost/",                                                         views.email,                          name="account_email"),
        path("epost-bestaetigen/",                                             views.email_verification_sent,        name="account_email_verification_sent",),
        re_path(r"^epost-bestaetigen/(?P<key>[-:\w]+)/$",                      views.confirm_email,                  name="account_confirm_email",),
        path("kennwort/aendern/",                                              views.password_change,                name="account_change_password",),
        path("kennwort/setzen/",                                               views.password_set,                   name="account_set_password"),
        # password reset
        path("kennwort/zuruecksetzen/",                                        views.password_reset,                 name="account_reset_password"),
        path("kennwort/zuruecksetzen/erledigt/",                               views.password_reset_done,            name="account_reset_password_done",),
        re_path(
            r"^kennwort/zuruecksetzen/kennzeichen/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
                                                                               views.password_reset_from_key,        name="account_reset_password_from_key",),
        path("kennwort/zuruecksetzen/kennzeichen/erledigt/",                   views.password_reset_from_key_done,   name="account_reset_password_from_key_done",),
        path("anmelden/kennzeichen/bestaetigen/",                              views.confirm_login_code,             name="account_confirm_login_code",),
    ]
)
if getattr(settings, "MFA_PASSKEY_SIGNUP_ENABLED", False):
    urlpatterns.append(
        path("registrieren/schluesselkennzeichen/",                            views.signup_by_passkey,              name="account_signup_by_passkey",)
    )

if app_settings.LOGIN_BY_CODE_ENABLED:
    urlpatterns.extend(
        [
            path("anmelden/kennzeichen/",                                       views.request_login_code,             name="account_request_login_code",),
        ]
    )
