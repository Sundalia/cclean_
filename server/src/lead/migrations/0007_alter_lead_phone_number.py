# Generated by Django 5.0.3 on 2024-04-17 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0006_alter_lead_cleaning_type_alter_lead_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='phone_number',
            field=models.CharField(max_length=12, verbose_name='Номер телефона'),
        ),
    ]
