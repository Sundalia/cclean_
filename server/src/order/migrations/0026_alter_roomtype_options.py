# Generated by Django 5.0.3 on 2024-04-23 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0025_delete_thingscluttered'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roomtype',
            options={'verbose_name': 'Тип помещения', 'verbose_name_plural': 'Типы помещений'},
        ),
    ]
