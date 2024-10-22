from django.shortcuts import render
from django.views.generic import ListView

from .models import WanderStrecke

# Create your views here.

class WanderStreckeListView(ListView):
    """Ansicht zur Anzeige aller Wanderstrecken."""
    model = WanderStrecke
