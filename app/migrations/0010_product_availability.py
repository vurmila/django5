# Generated by Django 5.0.4 on 2024-04-26 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_brand_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Availability',
            field=models.CharField(choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')], max_length=100, null=True),
        ),
    ]
