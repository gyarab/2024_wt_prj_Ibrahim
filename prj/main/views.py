from django.shortcuts import render, get_object_or_404
from .models import Ball
from django.db.models import Q  # Pro pokročilé filtrování

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
