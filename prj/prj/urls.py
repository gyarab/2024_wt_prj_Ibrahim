from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', TemplateView.as_view(template_name='main/home.html'), name='home'),  # Notice trailing slash
    path('detail/', TemplateView.as_view(template_name='main/ball_detail.html'), name='detail'),
    path('', views.ball_list, name='ball_list'),
    path('ball/<int:pk>/', views.ball_detail, name='ball_detail'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('accounts/', include('allauth.urls')),
]
