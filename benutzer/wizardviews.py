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
from django.contrib.auth.mixins import LoginRequiredMixin

from benutzer.models import Benutzer
from benutzer.wizardforms import WanderStreckeUpdateForm1
from benutzer.wizardforms import WanderStreckeUpdateForm2
from benutzer.wizardforms import WanderStreckeUpdateForm3
from benutzer.wizardforms import WanderAbschnittCreateForm1
from benutzer.wizardforms import WanderAbschnittCreateForm2

from wanderstrecke.models import WanderStrecke, WanderAbschnitt

class WizardCreateView(LoginRequiredMixin, CreateView):
    """Ansicht zum Hinzufügen einer Wanderstrecke eines Benutzers - Schritt 1."""
    model = WanderStrecke
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
        return super(WizardCreateView, self).form_valid(form)


class WizardUpdateView1(LoginRequiredMixin, UpdateView):
    """Ansicht zum Hinzufügen einer Wanderstrecke eines Benutzers - Schritt 1 (Edit-Modus)."""
    model = WanderStrecke
    form_class = WanderStreckeUpdateForm1
    template_name = 'benutzer/wanderstrecke_wizard_1.html'

    def get_success_url(self):
        return reverse("benutzer:wizard2", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Wanderstrecke bearbeiten - Schritt 1.'
        return context

    def form_valid(self, form):
        return super().form_valid(form)


class WizardUpdateView2(LoginRequiredMixin, UpdateView):
    """Ansicht zum Hinzufügen einer Wanderstrecke eines Benutzers - Schritt 2."""
    model = WanderStrecke
    form_class = WanderStreckeUpdateForm2
    template_name = 'benutzer/wanderstrecke_wizard_2.html'

    def get_success_url(self):
        if 'weiter_mit_neuem_abschnitt' in self.request.POST:
            return reverse("benutzer:wizard3cneu", kwargs={"pk": self.object.id})
        if 'weiter_mit_vorhandenem_abschnitt' in self.request.POST:
            return reverse("benutzer:wizard3vorhanden", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Wanderstrecke bearbeiten - Schritt 2.'
        return context

    def form_valid(self, form):
        return super().form_valid(form)

########################################################################################################################
#
# Arbeiten mit einem neuen Wanderabschnitt.
#
#########################################################################################################################

class WizardCreateView3Neu(LoginRequiredMixin, CreateView):
    """Ansicht zum Hinzufügen eines Wanderabschnittes zu einer Wanderstrecke eines Benutzers -  Schritt 3."""
    model = WanderAbschnitt
    form_class = WanderAbschnittCreateForm1
    template_name = 'benutzer/wanderstrecke_wizard_3neu.html'

    def get_success_url(self):
        return reverse("benutzer:wizard4neu", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Wanderstrecke hinzufügen - Schritt 3.'
        context['subtitle'] = 'Wanderabschnitt erzeugen - Startpunkt festlegen.'
        context['wanderstrecke_id'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        form.instance.wanderstrecke = get_object_or_404(WanderStrecke, pk=self.kwargs['pk'])
        return super().form_valid(form)


class WizardUpdateView3Neu(LoginRequiredMixin, UpdateView):
    """Ansicht zum Hinzufügen eines Wanderabschnittes zu einer Wanderstrecke eines Benutzers -  Schritt 3."""
    model = WanderAbschnitt
    form_class = WanderAbschnittCreateForm1
    template_name = 'benutzer/wanderstrecke_wizard_3neu.html'

    def get_success_url(self):
        return reverse("benutzer:wizard4neu", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Wanderstrecke hinzufügen - Schritt 3.'
        context['subtitle'] = 'Wanderabschnitt bearbeiten - Startpunkt festlegen.'
        context['wanderstrecke_id'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        form.instance.wanderstrecke = self.kwargs['pk']
        return super().form_valid(form)

class WizardUpdateView4Neu(LoginRequiredMixin, UpdateView):
    """Ansicht zum Bearbeiten eines Wanderabschnittes zu einer Wanderstrecke eines Benutzers -  Schritt 4."""
    model = WanderAbschnitt
    form_class = WanderAbschnittCreateForm2
    template_name = 'benutzer/wanderstrecke_wizard_4neu.html'

    def get_success_url(self):
        return reverse("benutzer:wanderstrecke", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Wanderstrecke hinzufügen - Schritt 4.'
        context['subtitle'] = 'Wanderabschnitt bearbeiten - Strecke festlegen.'
        context['wanderabschnitt_id'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        form.instance.wanderstrecke = self.kwargs['pk']
        return super().form_valid(form)

########################################################################################################################
#
# Arbeiten mit einem vorhandenen Wanderabschnitt.
#
#########################################################################################################################

class WizardUpdateView3Vorhanden(LoginRequiredMixin, CreateView):
    """Ansicht zum Hinzufügen eines Wanderabschnittes zu einer Wanderstrecke eines Benutzers -  Schritt 3."""
    model = WanderAbschnitt
    form_class = WanderStreckeUpdateForm3
    template_name = 'benutzer/wanderstrecke_wizard_3_vorhanden.html'

    def get_success_url(self):
        return reverse("benutzer:wanderstrecke", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Wanderstrecke hinzufügen - Schritt 3.'
        context['wanderstrecke_id'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        form.instance.wanderstrecke = self.kwargs['pk']
        return super().form_valid(form)

#messages.success(self.request, f'Wanderstrecke "{self.object.__str__()}" erzeugt.')

class HilfeJSONView(TemplateView):
    """View zur Anzeige der Hilfe zum Thema JSON Datei erzeugen auf Strecken_messen.de."""
    template_name = "benutzer/hilfe_json.html"

class HilfeURLView(TemplateView):
    """View zur Anzeige der Hilfe zum Thema URL - Schnellverweis auf Strecken_messen.de."""
    template_name = "benutzer/hilfe_url.html"
