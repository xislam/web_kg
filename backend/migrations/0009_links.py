# Generated by Django 4.0.2 on 2022-03-07 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_contact_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='ссылки')),
                ('youtube', models.URLField(verbose_name='youtube')),
                ('what_sap', models.URLField(verbose_name='whatsapp')),
                ('facebook', models.URLField(verbose_name='facebook')),
            ],
            options={
                'verbose_name': 'Ссылки',
                'verbose_name_plural': 'Ссылки',
            },
        ),
    ]
