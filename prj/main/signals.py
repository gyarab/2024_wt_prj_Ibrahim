from django.dispatch import receiver
from allauth.account.signals import user_logged_in, user_signed_up
from .models import Customer

@receiver(user_signed_up)
def create_customer_on_signup(request, user, **kwargs):
    print(f"Signál user_signed_up pro {user.username}")
    if not Customer.objects.filter(username=user.username).exists():
        Customer.objects.create(
            username=user.username,
            customer_email=user.email
        )
        print("Customer vytvořen při signup")

@receiver(user_logged_in)
def ensure_customer_exists_on_login(request, user, **kwargs):
    print(f"Signál user_logged_in pro {user.username}")
    if not Customer.objects.filter(username=user.username).exists():
        Customer.objects.create(
            username=user.username,
            customer_email=user.email
        )
        print("Customer vytvořen při login")
