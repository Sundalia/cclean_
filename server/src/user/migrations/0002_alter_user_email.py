# Generated by Django 5.0.1 on 2024-03-14 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Почта'),
        ),
    ]
