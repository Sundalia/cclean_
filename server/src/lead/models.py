from django.db import models
from django.urls import reverse

class Lead(models.Model):
  cleaning_type=models.CharField(verbose_name='Тип уборки', max_length=100)
  counter_room=models.IntegerField(verbose_name='Количество комнат')
  counter_toilet=models.IntegerField(verbose_name='Количество санузлов')
  phone_number=models.CharField(max_length=12, verbose_name='Номер телефона', unique=False)
  created=models.DateTimeField(auto_now_add=True, verbose_name='Создано')
  updated=models.DateTimeField(auto_now=True, verbose_name='Обновлено')
  is_treatmened=models.BooleanField(verbose_name="Обрабртано", default=False)
  comment=models.CharField(verbose_name="комментарий", blank=True, null=True, max_length=1000)
  price=models.CharField(verbose_name="Предварительная цена", blank=True, null=True)
  
  class Meta:
    verbose_name='Лид'
    verbose_name_plural='Лиды'
    
  def __str__(self):
    return self.phone_number
  
  def get_absolute_url(self):
      return reverse("lead_detail", kwargs={"pk": self.pk})
  
    
    