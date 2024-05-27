from django.db import models
from django.utils.translation import gettext_lazy as _
# from django.core.validators import FileExtensionValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from src.user.models import User
from PIL import Image
from decimal import Decimal


PERCENTAGE_VALIDATOR = [MinValueValidator(Decimal(0)), MaxValueValidator(Decimal(100))]



class CleaningType(models.Model):
    name=models.CharField(max_length=150, verbose_name='Тип уборки')
    description=models.TextField(max_length=2500, verbose_name='Описание уборки')
    subdescription=models.CharField(max_length=2000, verbose_name='Субописание уборки', blank=True, null=True)
    price=models.DecimalField(max_digits=9,decimal_places=2, verbose_name='Цена за кв.м')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated=models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published=models.BooleanField(default=True, verbose_name='Опубликовано')
    
    class Meta:
        verbose_name='Тип уборки'
        verbose_name_plural='Типы уборки'
        permissions=[
            
        ]
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("cleaning_type_detail", kwargs={"pk": self.pk})
    
    
class PortfolioImage(models.Model):
    cleaning_type=models.ForeignKey(
         CleaningType,
         on_delete=models.CASCADE,
         verbose_name='Тип уборки',
         related_name='portfolio'
     )
    name=models.CharField(max_length=100, verbose_name='название изображения', default='Название', unique=True)
    picture=models.ImageField(
        upload_to='portfolio/%Y/%m/%d/',
        verbose_name='изображение' 
    )
    description=models.TextField(max_length=2000, verbose_name='описание')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated=models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published=models.BooleanField(default=True, verbose_name='Опубликовано')
    
    class Meta:
        verbose_name='Изображение портфолио'
        verbose_name_plural='Изображения портфолио'
        permissions=[
            
        ]
        
    def resize_save(self, *args, **kwargs):
        super(PortfolioImage, self).save(*args, **kwargs)
        img=Image.open(self.picture.path)
        if img.width > 800 or img.height > 600:
            output_size= (800, 400)
            img.thumbnail(output_size)
            img.save(self.picture.path)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("portfolio_image_detail", kwargs={"pk": self.pk})
        
    
    
class CleaningTypeIncludeList(models.Model): 
    name=models.CharField(max_length=1000, verbose_name='что входит в уборку(список)')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated=models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published=models.BooleanField(default=True, verbose_name='Опубликовано')
    
    class Meta:
        verbose_name='Что входит в уборку(список)'
        verbose_name_plural='Что входит в уборку(списки)'
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("cleaning_type_include_list_detail", kwargs={"pk": self.pk})
    
    

class CleaningTypeInclude(models.Model):
    include_list=models.ManyToManyField(
        CleaningTypeIncludeList,
        verbose_name="Список что входит",
        blank=True
    )
    name=models.CharField(max_length=500, verbose_name='Категория(что входит в уборку)')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated=models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published=models.BooleanField(default=True, verbose_name='Опубликовано')
    
    class Meta:
        verbose_name='Что входит в уборку(категория)'
        verbose_name_plural='Что входит в уборку(категории)'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("cleaning_type_include_detail", kwargs={"pk": self.pk})
    
    
    
class CleaningTypeCanAddList(models.Model): 
    name=models.CharField(max_length=1000, verbose_name='что можно добавить в уборку(список)')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated=models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published=models.BooleanField(default=True, verbose_name='Опубликовано')
    
    class Meta:
        verbose_name='Можно добавить(список)'
        verbose_name_plural='Можно добавить(списки)'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("cleaning_type_can_add_list_detail", kwargs={"pk": self.pk})
    
    

class CleaningTypeCanAdd(models.Model):
    can_add_list=models.ManyToManyField(
        CleaningTypeCanAddList,
        verbose_name="Список что можно добавить",
        blank=True 
    )
    name=models.CharField(max_length=500, verbose_name='Категория(что можно добавить в уборку)')
    price=models.DecimalField(max_digits=9,decimal_places=2, verbose_name='Цена')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated=models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published=models.BooleanField(default=True, verbose_name='Опубликовано')
    
    class Meta:
        verbose_name='Можно добавить(категория)'
        verbose_name_plural='Можно добавить(категории)'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("cleaning_type_can_add_detail", kwargs={"pk": self.pk})
    
     
     
     
class CleaningTypeLocation(models.Model):
     cleaning_type=models.ForeignKey(
         CleaningType,
         on_delete=models.PROTECT,
         verbose_name='Тип уборки',
         related_name='location'
     )
     include=models.ManyToManyField(
         CleaningTypeInclude,
         verbose_name='Что входит',
         blank=True
     )
     can_add=models.ManyToManyField(
         CleaningTypeCanAdd,
         verbose_name='Можно добавить',
         blank=True
     )
     name=models.CharField(max_length=150, verbose_name='Локация')
     subname=models.CharField(max_length=150, verbose_name='К какому типу уборки')
     created=models.DateTimeField(auto_now_add=True, verbose_name='Создано')
     updated=models.DateTimeField(auto_now=True, verbose_name='Обновлено')
     is_published=models.BooleanField(default=True, verbose_name='Опубликовано')
     
     class Meta:
         verbose_name='Локация типа уборки'
         verbose_name_plural='Локации типов уборки'
     
     def __str__(self):
         return f"{self.name}{self.subname}"
     
     def get_absolute_url(self):
         return reverse("cleaning_type_location_detail", kwargs={"pk": self.pk})  
     
     

class FurnitureCluttered(models.Model):
    name=models.CharField(max_length=100, verbose_name='Степень заставленности мебелью')
    description=models.CharField(max_length=2000, verbose_name='Справка')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated=models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published=models.BooleanField(default=True, verbose_name='Опубликовано')
    markup=models.DecimalField(max_digits=3, decimal_places=0, default=0, validators=PERCENTAGE_VALIDATOR, verbose_name="Наценка в процентах")
    
    class Meta:
        verbose_name='Степень заставленности мебелью'
        verbose_name_plural='Степень заставленности мебелью'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("furniture_cluttered_detail", kwargs={"pk": self.pk})
    
    


class PollutionDegree(models.Model):
    name=models.CharField(max_length=100, verbose_name='Степень загрязнения')
    description=models.CharField(max_length=2000, verbose_name='Справка')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated=models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published=models.BooleanField(default=True, verbose_name='Опубликовано')
    markup=models.DecimalField(max_digits=3, decimal_places=0, default=0, validators=PERCENTAGE_VALIDATOR, verbose_name="Наценка в процентах")
    
    class Meta:
        verbose_name='Степень загрязнения'
        verbose_name_plural='Степень загрязнения'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("pollution_degree_detail", kwargs={"pk": self.pk})
    


class Promo(models.Model):
    name=models.CharField(max_length=150, verbose_name='Название акции')
    description=models.CharField(max_length=2000, verbose_name='Описание акции')
    markup=models.DecimalField(max_digits=3, decimal_places=0, default=0, validators=PERCENTAGE_VALIDATOR, verbose_name="Скидка в процентах")
    promocode=models.TextField(verbose_name='Промокод', blank=True, null=True)
    cleaning_type=models.OneToOneField(
        CleaningType, 
        on_delete=models.PROTECT, 
        blank=True, 
        null=True,
        verbose_name='Для какого типа уборки'
    )
    created=models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated=models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published=models.BooleanField(default=True, verbose_name='Опубликовано')
    
    class Meta:
        verbose_name='Акция'
        verbose_name_plural='Акции'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("promo_detail", kwargs={"pk": self.pk})    
    
    
    
class RoomType(models.Model):
    name=models.CharField(max_length=150, verbose_name='Название помещения')
    markup=models.DecimalField(max_digits=3, decimal_places=0, default=0, validators=PERCENTAGE_VALIDATOR, verbose_name="Наценка в процентах")
    created=models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated=models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published=models.BooleanField(default=True, verbose_name='Опубликовано')
    
    class Meta:
        verbose_name='Тип помещения'
        verbose_name_plural='Типы помещений'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("room_type_detail", kwargs={"pk": self.pk})    



class Order(models.Model):
    customer=models.ForeignKey(
        User, 
        on_delete=models.PROTECT, 
        verbose_name='Клиент'
    )
    cleaning_type=models.ForeignKey(
        CleaningType, 
        on_delete=models.PROTECT, 
        verbose_name='Тип уборки',
        blank=True,
        null=True
    )
    square=models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Площадь помещения')
    furniture_cluttered=models.ForeignKey(
        FurnitureCluttered,
        on_delete=models.PROTECT,
        verbose_name='Заставленность мебелью',
        blank=True,
        null=True
    )
        
    pollution_degree=models.ForeignKey(
        PollutionDegree, 
        on_delete=models.PROTECT,
        verbose_name='Степень загрязнения',
        blank=True,
        null=True
    )
    room_type = models.ForeignKey(
        RoomType,
        on_delete=models.PROTECT,
        verbose_name='Тип помещения',
        blank=True,
        null=True
    )
    cleaning_date=models.DateField(editable=True, blank=False, verbose_name='Дата уборки')
    cleaning_time=models.TimeField(editable=True, blank=False, verbose_name='Время')
    photo=models.ImageField(
        upload_to='media/orders/%Y/%m/%D/', 
        blank=True,
        null=True,
        verbose_name='Фото квартиры'
    )
    is_windows = models.BooleanField(default=False, verbose_name='Мойка окон')
    is_microwave = models.BooleanField(default=False, verbose_name='Мойка микроволновки')
    is_oven = models.BooleanField(default=False, verbose_name='Мойка духового шкафа')
    is_garbage = models.BooleanField(default=False, verbose_name='Вынос мусора')
    is_fridge = models.BooleanField(default=False, verbose_name='Мойка холодильника')
    is_linen = models.BooleanField(default=False, verbose_name='Погладить бельё')
    is_deep_floor = models.BooleanField(default=False, verbose_name='Глубокая чистка пола')
    is_tile_joint = models.BooleanField(default=False, verbose_name='Чистка межплиточных швов')
    address=models.CharField(max_length=255, verbose_name='Адрес')
    comment=models.TextField(max_length=1000, verbose_name='Пожелания/комментарии', blank=True, null=True)
    promo=models.ForeignKey(
        Promo, 
        on_delete=models.PROTECT, 
        verbose_name='ПРОМОКОД',
        blank=True,
        null=True
    )
    price=models.CharField(max_length=100, verbose_name='Цена')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated=models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published=models.BooleanField(default=True, verbose_name='Опубликовано')
    cleaners_photo=models.ImageField(
        upload_to='media/orders/cleaner/%Y/%m/%D/', 
        blank=True,
        null=True,
        verbose_name='Фото квартиры после уборки'
    )
    
    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='Заказы'
    
    def __str__(self):
        return self.address
    
    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})



class OrderStatus(models.Model):
    order=models.OneToOneField('Order', on_delete=models.PROTECT, primary_key=True)
    is_confirmed=models.BooleanField(default=False, verbose_name='Заказ взят в работу')
    is_started=models.BooleanField(default=False, verbose_name='Начата уборка')
    is_finished=models.BooleanField(default=False, verbose_name='Уборка закончена')
    is_paid=models.BooleanField(default=False, verbose_name='Оплачен')
    
    class Meta:
        verbose_name='статус заказа'
        verbose_name_plural='статусы заказа'
    
    def __str__(self):
        return self.order
    
    def get_absolute_url(self):
        return reverse("order_status_detail", kwargs={"pk": self.pk})
    
    

class FeedBack(models.Model):
    name=models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Клиент'
    )
    order=models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        verbose_name='Заказ'
    )
    
    cleaning_type=models.ForeignKey(
        CleaningType,
        on_delete=models.PROTECT,
        verbose_name='Тип уборки'
    )
    
    feedback_body=models.TextField(max_length=1000, verbose_name='Отзыв')
    
    RATING_CHOICES = [
        (1, "Очень плохо"),
        (2, "Плохо"),
        (3, "Удовлетворительно"),
        (4, "Хорошо"),
        (5, "Восхитительно")
    ]
        
    feedback_rating=models.IntegerField(choices=RATING_CHOICES, default='amazing', verbose_name='Рейтинг')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated=models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published=models.BooleanField(default=True, verbose_name='Опубликовано')


    
    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='Отзывы'
    
    def __str__(self):
        return self.feedback_body
    
    def get_absolute_url(self):
        return reverse("feedback_detail", kwargs={"pk": self.pk})
    




    



