# Generated by Django 5.0.3 on 2024-03-15 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_phone_user_mobile_alter_user_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_cleaner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=False),
        ),
    ]
