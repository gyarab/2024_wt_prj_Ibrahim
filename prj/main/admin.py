from django.contrib import admin
from .models import Ball
admin.site.register(Ball)

class BallAdmin(admin.ModelAdmin):
    list_display = {"id","name","price","hmotnost"}

    admin.site.register(id,name)
# Register your models here.
