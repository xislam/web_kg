# Generated by Django 4.0.2 on 2022-03-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_rename_contacts_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(default=2, max_length=50, verbose_name='Адрес'),
            preserve_default=False,
        ),
    ]
