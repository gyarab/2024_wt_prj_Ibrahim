from django.shortcuts import render, get_object_or_404
from .models import Ball
from django.db.models import Q  # Pro pokročilé filtrování
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.shortcuts import redirect, get_object_or_404
from .models import Ball

def purchase_ball(request, pk):
    ball = get_object_or_404(Ball, pk=pk)
    # Zde přidej logiku pro nákup (např. přidání do objednávky)
    # Prozatím jen přesměrování zpět na detail míče
    return redirect('ball_detail', pk=pk)
# Zobrazení seznamu míčů s vyhledáváním
def ball_list(request):
    query = request.GET.get('q')  # Získáme dotaz z parametru URL
    if query:
        balls = Ball.objects.filter(
            Q(name__icontains=query) | Q(brand__icontains=query)
        ).order_by('name')
    else:
        balls = Ball.objects.all().order_by('name')
    
    return render(request, 'main/ball_list.html', {'balls': balls})

# Detail míče podle primárního klíče
def ball_detail(request, pk):
    ball = get_object_or_404(Ball, pk=pk)
    return render(request, 'main/ball_detail.html', {'ball': ball})

