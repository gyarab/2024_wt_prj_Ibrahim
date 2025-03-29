from django.db import models

class Ball(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField(default=0, verbose_name= "Price (CZK)")
    weight = models.IntegerField(default=0)
    diameter = models.IntegerField(default=0)
    purpose = models.CharField(max_length=70)
    brand = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.name}"

class Customer(models.Model):
    customer_email = models.CharField(max_length=300)
    username = models.CharField(max_length=300)
    balls_purchased = models.ManyToManyField(Ball, through='Purchase')

    def __str__(self):
        return f"{self.username}"

class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ball = models.ForeignKey(Ball, on_delete=models.CASCADE)
    purchase_date = models.DateField()  # Corrected to a DateField
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, verbose_name="Total price (CZK)")
 
    def count_total_price(self):
        self.total_price = self.quantity * self.ball.price

    def save(self, *args, **kwargs):
        self.count_total_price()  # Ensure total price is calculated before saving
        super().save(*args, **kwargs)


