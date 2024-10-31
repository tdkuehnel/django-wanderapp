from django import forms
from django.contrib.gis import forms as gisforms
from django.forms import ModelForm, Textarea

from benutzer.models import Benutzer
from wanderstrecke.models import WanderStrecke, WanderAbschnitt

class WanderappOsmWidget(gisforms.OSMWidget):
    class Media:
        extend = False
        css = {
            'all': [
                'wanderstrecke/os3.css',
                'https://cdn.jsdelivr.net/npm/ol@v7.2.2/ol.css'
            ]
        }
        js = [
            'https://cdn.jsdelivr.net/npm/ol@v7.2.2/dist/ol.js',
            'wanderstrecke/OLMapWidget.js'
        ]

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
            'bild',
        ]
        widgets = {
        }

class WanderStreckeUpdateForm3(ModelForm):
    """Dieses Formular bearbeitet einen WanderAbschnitt."""
    class Meta:
        model = WanderAbschnitt
        fields = [
            'json',
            'url',
        ]
        widgets = {
            "url": Textarea(attrs={"cols": 40, "rows": 8}),
        }

class WanderAbschnittCreateForm1(ModelForm):
    """Dieses Formular bearbeitet einen WanderAbschnitt."""
    class Meta:
        model = WanderAbschnitt
        fields = [
            'startpunkt',
            'ort1',
        ]
        widgets = {
            'startpunkt': WanderappOsmWidget(attrs={"display_raw": False, 'default_lat': 51.75679, 'default_lon': 10.62035}),
        }
    class Media:
        css = { 'all': ['wanderstrecke/os3.css'] }

class WanderAbschnittCreateForm2(ModelForm):
    """Dieses Formular bearbeitet einen WanderAbschnitt."""
    class Meta:
        model = WanderAbschnitt
        fields = [
            'strecke',
        ]
        widgets = {
            'strecke': WanderappOsmWidget(attrs={"display_raw": True, 'default_lat': 51.75679, 'default_lon': 10.62035}),
        }
    class Media:
        css = { 'all': ['wanderstrecke/os3.css'] }
