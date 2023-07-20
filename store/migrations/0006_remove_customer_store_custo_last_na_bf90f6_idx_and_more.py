# Generated by Django 4.2.3 on 2023-07-20 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_customer_store_custo_last_na_e6a359_idx_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='customer',
            name='store_custo_last_na_bf90f6_idx',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='given_name',
            new_name='first_name',
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['last_name', 'first_name'], name='store_custo_last_na_e6a359_idx'),
        ),
    ]
