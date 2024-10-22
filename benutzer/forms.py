from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField
from django.forms import ModelForm, Textarea

from benutzer.models import Benutzer
from wanderstrecke.models import WanderStrecke

# Anmeldeform

class AnmeldeForm(AuthenticationForm):

    def clean_username(self):
        #import pdb; pdb.set_trace()
        data = self.cleaned_data['username']
        return data.lower()

class WanderStreckeUpdateForm(ModelForm):
    class Meta:
        model = WanderStrecke
        fields = [
            'bezeichnung',
            'beschreibung',
            'json',
            'url',
            'bild',
        ]
        widgets = {
            "beschreibung": Textarea(attrs={"cols": 80, "rows": 4}),
            "url": Textarea(attrs={"cols": 40, "rows": 8}),
        }
