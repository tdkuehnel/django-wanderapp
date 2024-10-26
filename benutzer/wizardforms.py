from django import forms
from django.forms import ModelForm, Textarea

from benutzer.models import Benutzer
from wanderstrecke.models import WanderStrecke

# Die Formulare für den WizardView um eine Wanderstrecke zu erzeugen.
# Das Formular WanderStreckeUpdateForm1 wird auch für das erste
# Erzeugen eines Wanderstreckenobjektes mittel eines CreateViews
# genutzt.

class WanderStreckeUpdateForm1(ModelForm):
    class Meta:
        model = WanderStrecke
        fields = [
            'bezeichnung',
            'beschreibung',
        ]
        widgets = {
            "beschreibung": Textarea(attrs={"cols": 80, "rows": 4}),
        }

class WanderStreckeUpdateForm2(ModelForm):
    class Meta:
        model = WanderStrecke
        fields = [
            'json',
            'url',
        ]
        widgets = {
            "url": Textarea(attrs={"cols": 40, "rows": 8}),
        }

class WanderStreckeUpdateForm3(ModelForm):
    class Meta:
        model = WanderStrecke
        fields = [
            'bild',
        ]
        widgets = {
        }
