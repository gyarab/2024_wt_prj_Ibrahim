from django.contrib import admin
from .models import Ball, customer

class BallAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'weight', 'purpose', 'brand')  # Fields to display in the admin list view

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_email', 'username')  # Fields to display in the admin list view

# Register the Ball model with the custom BallAdmin class
admin.site.register(Ball, BallAdmin)

# Register the Customer model with the custom CustomerAdmin class
admin.site.register(customer, CustomerAdmin)
