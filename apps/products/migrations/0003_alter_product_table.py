# Generated by Django 4.2.3 on 2023-08-14 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_product_sku"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="product",
            table="products",
        ),
    ]
