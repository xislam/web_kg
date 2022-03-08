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


class CategoryDirection(models.Model):
    name = models.CharField(max_length=70, verbose_name="Наименование категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категории напровлении"
        verbose_name_plural = "Категории напровлении"


class Direction(models.Model):
    category = models.ForeignKey(CategoryDirection, verbose_name="Категория", on_delete=models.CASCADE)
    img = models.ImageField(verbose_name="Фото", upload_to="img_direction")
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Направления"
        verbose_name = "Направления"


class AboutUs(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = RichTextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "О нас"
        verbose_name = "О нас"


class AboutKg(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = RichTextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "О Кыргызстане"
        verbose_name_plural = "О Кыргызстане"


class Gallery(models.Model):
    img = models.ImageField(verbose_name="Фото", upload_to="gallery_img")
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    text = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Галерея"
        verbose_name = "Галерея"


class Blog(models.Model):
    img = models.ImageField(verbose_name="Фото", upload_to="blog_img")
    title = models.CharField(verbose_name="Заголовок", max_length=70)
    text = RichTextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блог"


class Contact(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    text = RichTextField(verbose_name="Описание")
    phone_1 = models.CharField(verbose_name="Номер вотцап", max_length=12)
    phone_2 = models.CharField(verbose_name="Номер телефона", max_length=12)
    email = models.EmailField(verbose_name="Почта")
    address = models.CharField(max_length=50, verbose_name="Адрес")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Контакты"
        verbose_name = "Контакты"


class Links(models.Model):
    title = models.CharField(verbose_name="ссылки", max_length=60)
    youtube = models.URLField(verbose_name="youtube")
    what_sap = models.URLField(verbose_name='whatsapp')
    facebook = models.URLField(verbose_name='facebook')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Ссылки"
        verbose_name = "Ссылки"
