from ckeditor.fields import RichTextField
from django.db import models


class IndexText(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    text = RichTextField(verbose_name="Текст")

    def __str__(self):
        return self.title

