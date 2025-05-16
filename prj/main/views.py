from django.shortcuts import render, get_object_or_404
from .models import Ball
from django.db.models import Q  # Pro pokročilé filtrování
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


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

from django.contrib.auth.models import User
from django.http import JsonResponse
import json

def signup_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        username = data.get('username')  # Ensure username is provided
        password = data.get('password')

        # Validate that username is not empty
        if not username:
            return JsonResponse({'success': False, 'message': 'Username is required.'}, status=400)

        # Check if the email or username already exists
        if User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'Email already exists.'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'message': 'Username already exists.'}, status=400)

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)

        return JsonResponse({'success': True, 'message': 'Registration successful.'})
    return JsonResponse({'error': 'Invalid request method.'}, status=405)


def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return JsonResponse({'success': True, 'message': 'Login successful.'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials.'}, status=400)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)