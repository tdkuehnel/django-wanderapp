from django.shortcuts import render
from django.views.generic import ListView

from .models import WanderStrecke

# Create your views here.

class WanderStreckeListView(ListView):
    """Ansicht zur Anzeige aller Wanderstrecken."""
    model = WanderStrecke

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sehenswerte Wanderstrecken.'
        return context
