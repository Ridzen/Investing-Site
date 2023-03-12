from django.db import models

# Create your models here.

from ckeditor.fields import RichTextField
from django.db import models

from apps.users.models import BusinessOwner


# Create your models here.

class Category(models.Model):
    """
    Моделька категорий, для того чтобы понимали в какой сфере бизнес, с полями
    id, title
    """
    title = models.CharField(
        max_length=255, null=False, blank=False,
        verbose_name='Название Категории',  help_text='Название Категории',
        default='Введите ваш текст'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.title}'


class Business(models.Model):
    """
    Моделька для публикации объявлений о бизнесе с полями
    id, title, image, owner, budget, currency, term, description, is_active, is_premium
    category, location, created_at
    """

    title = models.CharField(
        max_length=100, null=True, blank=False, verbose_name='Название'
    )
    image = models.ImageField(
        null=False, blank=False, verbose_name='Логотип', help_text='Логотип'
    )
    owner = models.ForeignKey(
        BusinessOwner, on_delete=models.CASCADE,  verbose_name='Владелец'
    )
    budget = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Сумма инвестиций'
    )
    currency = models.CharField(
        max_length=20, verbose_name='Валюта', null=False, blank=False,
        help_text='Валюта, отправляется в любом формате'
    )
    term = models.CharField(
        verbose_name='Срок окупаемости', help_text='Срок за сколько окупится проект', max_length=255
    )
    description = models.TextField(
        verbose_name='Описание', help_text='Подробное описание объявления'
    )
    is_active = models.BooleanField(
        default=True, verbose_name="Активный ли пользователь"
    )
    is_premium = models.BooleanField(
        default=False, verbose_name='Премиум объявление'
    )
    category = models.ForeignKey(
        Category, on_delete=models.RESTRICT,
        max_length=100, null=True, blank=True, verbose_name='Сфера деятельности', help_text='Категории'
    )
    location = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Локация(Город)'
    )
    created_at = models.DateField(
        auto_now_add=True, verbose_name='Дата создания поста', help_text='Дата создания поста'
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Бизнес'
        verbose_name_plural = 'Бизнесы'
        ordering = ['-id']


class BusinessDetail(models.Model):
    """
    Моделька подробного ознакомления с объявлением, с полями
    business, file, contact
    """
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, verbose_name='Бизнес от которого он наследуется',
        null=False, blank=False
    )
    file = models.FileField(
        verbose_name='Моделька для Бизнес Плана и так далее'
    )
    contact = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Контакт для связи', help_text='Контакт для связи'
    )

    def __str__(self):
        return f'{self.business}'

    class Meta:
        verbose_name = 'Бизнес Деталь'
        verbose_name_plural = 'Бизнес Детали'
