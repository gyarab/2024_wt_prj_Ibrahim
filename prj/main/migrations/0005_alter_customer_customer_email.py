# Generated by Django 5.1.7 on 2025-03-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_customer_lifetime_purchases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_email',
            field=models.CharField(max_length=300),
        ),
    ]
