from django.shortcuts import render
from .models import Ball
from django.shortcuts import render, get_object_or_404
from .models import Ball



def ball_list(request):
    balls = Ball.objects.all().order_by('name')  # Order balls by name alphabetically
    return render(request, 'main/ball_list.html', {'balls': balls})




def ball_detail(request, pk):
    ball = get_object_or_404(Ball, pk=pk)
    return render(request, 'main/ball_detail.html', {'ball': ball})

