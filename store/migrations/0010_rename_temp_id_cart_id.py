# Generated by Django 4.2.3 on 2023-07-27 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_remove_cart_id_alter_cart_temp_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='temp_id',
            new_name='id',
        ),
    ]
