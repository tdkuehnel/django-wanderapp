from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from django import forms

from .models import WanderStrecke

# Register your models here.

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
