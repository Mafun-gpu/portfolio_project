from django.db import models
from django.utils.text import slugify
from enum import Enum
from .enums import CategoryType

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)

class PortfolioItem(models.Model):
    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to='portfolio_images/', blank=True, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField(max_length=255,  blank=True, null=True)
    is_published = models.BooleanField("Опубликовано", default=True)

    # Поле для категории, используя Enum:
    category = models.CharField(
        "Категория",
        max_length=50,
        choices=[(tag.name, tag.value) for tag in CategoryType],  # превращаем Enum в список кортежей
        default=CategoryType.OTHER.name
    )

    objects = models.Manager()  # стандартный менеджер unique=True,
    published = PublishedManager()  # пользовательский менеджер

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
