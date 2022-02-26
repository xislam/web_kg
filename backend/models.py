from ckeditor.fields import RichTextField
from django.db import models


class IndexText(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    text = RichTextField(verbose_name="Текст")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Тест главной страницы"
        verbose_name = "Тест главной страницы"


class IndexSlider1(models.Model):
    icon = models.ImageField(verbose_name="Логотип", upload_to="icon")
    img = models.ImageField(verbose_name="Фото", upload_to="img")
    title = models.CharField(max_length=70, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Что я должен делать"
        verbose_name_plural = "Что я должен делать"


class Direction(models.Model):
    img = models.ImageField(verbose_name="Фото", upload_to="img_direction")
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Направления"
        verbose_name = "Направления"
