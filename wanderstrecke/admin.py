from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from django import forms

from .models import WanderStrecke
from .models import WanderPunkt

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
        ]
        widgets = {
            'beschreibung'         : forms.Textarea(attrs={'cols': 120, 'rows': 4}),
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
