from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView
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

from benutzer.models import Benutzer

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
