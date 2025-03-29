from django.contrib import admin
from .models import Ball, Customer, Purchase

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('customer', 'ball', 'quantity', 'total_price', 'purchase_date')  # Columns to display
    list_filter = ('purchase_date', 'customer')  # Filter options
    search_fields = ('customer__username', 'ball__name')  # Search by customer name or ball name
    ordering = ('purchase_date',)  # Order by purchase date

class BallAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'weight', 'diameter', 'purpose', 'brand')
    search_fields = ('name', 'brand')  # Search by ball name or brand

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'customer_email')
    search_fields = ('username', 'customer_email')  # Search by username or email

admin.site.register(Ball, BallAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Purchase, PurchaseAdmin)
