# Generated by Django 4.2 on 2024-03-09 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bmart', '0002_orders_alter_product_desc'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
