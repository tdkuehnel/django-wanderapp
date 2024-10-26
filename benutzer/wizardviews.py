from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from benutzer.models import Benutzer
from benutzer.wizardforms import WanderStreckeUpdateForm1
from benutzer.wizardforms import WanderStreckeUpdateForm2
from benutzer.wizardforms import WanderStreckeUpdateForm3

from wanderstrecke.models import WanderStrecke

class WizardCreateView(CreateView):
    """Ansicht zum Hinzufügen einer Wanderstrecke eines Benutzers Schritt 1."""
    model = WanderStrecke
    #fields = ['bezeichnung', 'json', 'url', 'bild',]
    form_class = WanderStreckeUpdateForm1
    template_name = 'benutzer/wanderstrecke_wizard_1.html'

    def get_success_url(self):
        return reverse("benutzer:wizard2", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Wanderstrecke hinzufügen - Schritt 1.'
        return context

    def form_valid(self, form):
        form.instance.benutzer = self.request.user
        #messages.success(self.request, f'Wanderstrecke "{self.object.__str__()}" erzeugt.')
        return super(WizardCreateView, self).form_valid(form)

class WizardUpdateView1(UpdateView):
    """Ansicht zum Hinzufügen einer Wanderstrecke eines Benutzers Schritt 1 (Edit-Modus)."""
    model = WanderStrecke
    #fields = ['bezeichnung', 'json', 'url', 'bild',]
    form_class = WanderStreckeUpdateForm1
    template_name = 'benutzer/wanderstrecke_wizard_1.html'

    def get_success_url(self):
        return reverse("benutzer:wizard2", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Wanderstrecke bearbeiten - Schritt 1.'
        return context

    def form_valid(self, form):
        #messages.success(self.request, f'Wanderstrecke "{self.object.__str__()}" erzeugt.')
        return super().form_valid(form)


class WizardUpdateView2(UpdateView):
    """Ansicht zum Hinzufügen einer Wanderstrecke eines Benutzers Schritt 2."""
    model = WanderStrecke
    #fields = ['bezeichnung', 'json', 'url', 'bild',]
    form_class = WanderStreckeUpdateForm2
    template_name = 'benutzer/wanderstrecke_wizard_2.html'

    def get_success_url(self):
        return reverse("benutzer:wizard3", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Wanderstrecke bearbeiten - Schritt 2.'
        return context

    def form_valid(self, form):
        #messages.success(self.request, f'Wanderstrecke "{self.object.__str__()}" erzeugt.')
        return super().form_valid(form)


class WizardUpdateView3(UpdateView):
    """Ansicht zum Hinzufügen einer Wanderstrecke eines Benutzers Schritt 3."""
    model = WanderStrecke
    #fields = ['bezeichnung', 'json', 'url', 'bild',]
    form_class = WanderStreckeUpdateForm3
    template_name = 'benutzer/wanderstrecke_wizard_3.html'

    def get_success_url(self):
        return reverse("benutzer:wanderstrecke", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Wanderstrecke hinzufügen - Schritt 3.'
        return context

    def form_valid(self, form):
        #messages.success(self.request, f'Wanderstrecke "{self.object.__str__()}" erzeugt.')
        return super().form_valid(form)

class HilfeJSONView(TemplateView):
    """View zur Anzeige der Hilfe zum Thema JSON Datei erzeugen auf Strecken_messen.de."""
    template_name = "benutzer/hilfe_json.html"

class HilfeURLView(TemplateView):
    """View zur Anzeige der Hilfe zum Thema URL - Schnellverweis auf Strecken_messen.de."""
    template_name = "benutzer/hilfe_url.html"
