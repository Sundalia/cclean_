# Generated by Django 5.0.4 on 2024-05-26 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_user_managers_alter_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_varified',
            field=models.BooleanField(default=False),
        ),
    ]
