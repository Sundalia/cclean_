# Generated by Django 5.0.3 on 2024-04-18 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0022_alter_order_pollution_degree_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название помещения')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена за кв.м')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='room_choices',
        ),
        migrations.AlterField(
            model_name='order',
            name='cleaners_photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/orders/cleaner/%Y/%m/%D/', verbose_name='Фото квартиры после уборки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/orders/%Y/%m/%D/', verbose_name='Фото квартиры'),
        ),
        migrations.AddField(
            model_name='order',
            name='room_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='order.roomtype', verbose_name='Тип помещения'),
        ),
    ]
