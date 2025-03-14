from django.db import models

class PortfolioItem(models.Model):
    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to='portfolio_images/', blank=True, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title
