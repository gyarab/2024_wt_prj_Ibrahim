# Generated by Django 5.1.7 on 2025-03-29 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='lifetime_purchases',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
