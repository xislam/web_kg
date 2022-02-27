# Generated by Django 4.0.2 on 2022-02-27 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_indexslider1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img_direction', verbose_name='Фото')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Направления',
                'verbose_name_plural': 'Направления',
            },
        ),
        migrations.AlterModelOptions(
            name='indexslider1',
            options={'verbose_name': 'Что я должен делать', 'verbose_name_plural': 'Что я должен делать'},
        ),
    ]