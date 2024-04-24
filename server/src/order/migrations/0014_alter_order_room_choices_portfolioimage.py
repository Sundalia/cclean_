# Generated by Django 5.0.3 on 2024-04-09 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_alter_cleaningtypecanadd_can_add_list_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='room_choices',
            field=models.CharField(choices=[('workshop', 'Производство'), ('apartment', 'Квартира'), ('house', 'Загородный дом'), ('office', 'Офис'), ('yacht', 'Яхта')], default='apartment', max_length=100, verbose_name='Тип помещения'),
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='media/orders/portfolio/%Y/%m/%d/', verbose_name='изображение')),
                ('description', models.TextField(max_length=2000, verbose_name='описание')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('cleaning_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to='order.cleaningtype', verbose_name='Тип уборки')),
            ],
        ),
    ]
