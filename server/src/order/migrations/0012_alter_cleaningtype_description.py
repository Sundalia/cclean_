# Generated by Django 5.0.3 on 2024-03-24 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_alter_cleaningtypelocation_can_add_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleaningtype',
            name='description',
            field=models.TextField(max_length=2500, verbose_name='Описание уборки'),
        ),
    ]
