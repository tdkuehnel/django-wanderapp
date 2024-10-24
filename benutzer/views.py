from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetConfirmView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.forms.models import modelform_factory

from benutzer.models import Benutzer
from benutzer.forms import WanderStreckeUpdateForm
from wanderstrecke.models import WanderStrecke

from .forms import AnmeldeForm

class WanderappLoginView(LoginView):
    form_class = AnmeldeForm
    redirect_authenticated_user = True

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=401)


class BenutzerProfilView(UpdateView):
    model = Benutzer
    fields = ['username', 'email', 'avatar',]
    template_name_suffix = "_update_form"

    #form_class = AnmeldeForm
    #redirect_authenticated_user = True

    def get_success_url(self):
        return reverse("benutzer:profil", kwargs={"pk": self.kwargs["pk"]})

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=401)

    def form_valid(self, form):
        if form.changed_data:
            messages.success(self.request, f'Die Änderungen an Ihrem Profil wurden gespeichert.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = 'Bitte bearbeiten Sie ihr Profil.'
        return context

@login_required
def redirect_to_user_profile(request):
    return HttpResponseRedirect(
        reverse('benutzer:profil',
                args=[request.user.id]))

@login_required
def redirect_to_user_wanderstrecken(request):
    return HttpResponseRedirect(
        reverse('benutzer:wanderstrecken',
                args=[request.user.id]))

# Mixin from https://stackoverflow.com/questions/16937076/how-does-one-use-a-custom-widget-with-a-generic-updateview-without-having-to-red
# Zur Zeit nicht benutzt.

class ModelFormWidgetMixin(object):
    def get_form_class(self):
        return modelform_factory(self.model, fields=self.fields, widgets=self.widgets)

class BenutzerWanderStreckeListView(ListView):
    """Ansicht zur Anzeige der Wanderstrecken eines Benutzers."""
    model = WanderStrecke
    template_name = 'benutzer/wanderstrecken_list.html'

    def get_queryset(self):
        self.benutzer = get_object_or_404(Benutzer, id=self.kwargs["benutzer_id"])
        return WanderStrecke.objects.filter(benutzer=self.benutzer)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ihre Wanderstrecken.'
        return context

class BenutzerWanderStreckeCreateView(CreateView):
    """Ansicht zum Hinzufügen einer Wanderstrecke eines Benutzers."""
    model = WanderStrecke
    #fields = ['bezeichnung', 'json', 'url', 'bild',]
    form_class = WanderStreckeUpdateForm
    template_name = 'benutzer/wanderstrecke_create_form.html'

    def get_success_url(self):
        return reverse("benutzer:wanderstrecke", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Wanderstrecke hinzufügen.'
        return context

    def form_valid(self, form):
        messages.success(self.request, f'Wanderstrecke "{self.object.__str__()}" erzeugt.')
        return super().form_valid(form)

class BenutzerWanderStreckeDetailView(DetailView):
    """Ansicht zum Anzeigen einer Wanderstrecke eines Benutzers."""
    model = WanderStrecke
    fields = ['bezeichnung', 'json']
    template_name = 'benutzer/wanderstrecke_detail_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Wanderstrecke anzeigen.'
        return context

class BenutzerWanderStreckeUpdateView(UpdateView):
    """Ansicht zum Bearbeiten einer Wanderstrecke eines Benutzers."""
    model = WanderStrecke
    #fields = ['bezeichnung', 'json', 'url', 'bild',]
    form_class = WanderStreckeUpdateForm
    template_name = 'benutzer/wanderstrecke_update_form.html'

    def get_success_url(self):
        return reverse("benutzer:wanderstrecke", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Wanderstrecke bearbeiten.'
        return context

    def form_valid(self, form):
        if form.changed_data:
            messages.success(self.request, f'Änderungen an der Wanderstrecke "{self.object.__str__()}" wurden gespeichert.')
        return super().form_valid(form)

class BenutzerWanderStreckeDeleteView(DeleteView):
    """Ansicht zum Löschen einer Wanderstrecke eines Benutzers."""
    model = WanderStrecke
    #fields = ['bezeichnung', 'json', 'url', 'bild',]
    #form_class = WanderStreckeUpdateForm
    template_name = 'benutzer/wanderstrecke_loeschen_form.html'

    def get_success_url(self):
        return reverse("benutzer:wanderhome")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Wanderstrecke löschen.'
        return context
