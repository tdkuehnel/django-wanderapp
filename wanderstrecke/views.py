from django.shortcuts import render
from django.views.generic import ListView

from .models import WanderStrecke

# Create your views here.

class BenutzerWanderStreckeListView(ListView):
    """Ansicht zur Anzeige der Wanderstrecken eines Benutzers."""
    model = WanderStrecke
