from django.contrib import admin
from django.contrib.gis import forms as gisforms
from simple_history.admin import SimpleHistoryAdmin
from django import forms

from .models import WanderStrecke
from .models import WanderPunkt
from .models import WanderAbschnitt

# Register your models here.

##################################################################################################
#
# WanderStrecke.
#
##################################################################################################

class WanderStreckeAdminForm(forms.ModelForm):

    class Meta:
        model = WanderStrecke
        fields = [
            'bezeichnung',
            'beschreibung',
            'json',
            'url',
            'bild',
            'benutzer',
        ]
        widgets = {
            'beschreibung'         : forms.Textarea(attrs={'cols': 120, 'rows': 4}),
        }

class WanderStreckeInline(admin.TabularInline):
    model = WanderStrecke
    extra = 0
    show_change_link = True

@admin.register(WanderStrecke)
class WanderStreckeAdmin(SimpleHistoryAdmin):
    form = WanderStreckeAdminForm
    list_filter = ['benutzer',]
    filter_horizontal = [
        #'quellen',
    ]

##################################################################################################
#
# WanderPunkt.
#
##################################################################################################

class WanderPunktAdminForm(forms.ModelForm):

    class Meta:
        model = WanderPunkt
        fields = [
            'bezeichnung',
            'beschreibung',
            'ort',
        ]
        widgets = {
            'beschreibung'         : forms.Textarea(attrs={'cols': 120, 'rows': 4}),
            'ort'                  : gisforms.OSMWidget(attrs={"display_raw": True, 'default_lat': 51.75679, 'default_lon': 10.62035}),
        }

class WanderPunktInline(admin.TabularInline):
    model = WanderPunkt
    extra = 0
    show_change_link = True

@admin.register(WanderPunkt)
class WanderPunktAdmin(SimpleHistoryAdmin):
    form = WanderPunktAdminForm
    #list_filter = ['benutzer',]
    filter_horizontal = [
        #'quellen',
    ]

##################################################################################################
#
# WanderAbschnitt.
#
##################################################################################################

class WanderAbschnittAdminForm(forms.ModelForm):

    class Meta:
        model = WanderAbschnitt
        fields = [
            'bezeichnung',
            'beschreibung',
            'ort1',
            'ort2',
            'strecke',
        ]
        widgets = {
            'beschreibung'         : forms.Textarea(attrs={'cols': 120, 'rows': 4}),
            'strecke'              : gisforms.OSMWidget(attrs={"display_raw": True, 'default_lat': 51.75679, 'default_lon': 10.62035}),
        }

class WanderAbschnittInline(admin.TabularInline):
    model = WanderAbschnitt
    extra = 0
    show_change_link = True

@admin.register(WanderAbschnitt)
class WanderAbschnittAdmin(SimpleHistoryAdmin):
    form = WanderAbschnittAdminForm
    #list_filter = ['benutzer',]
    filter_horizontal = [
        #'quellen',
    ]
