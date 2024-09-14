# Generated by Django 5.1 on 2024-09-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_card_category_alter_card_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение для задания'),
        ),
        migrations.AddField(
            model_name='tasks',
            name='left_gradient',
            field=models.CharField(default='#', max_length=250, verbose_name='Левый цвет'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasks',
            name='right_gradient',
            field=models.CharField(default='#', max_length=250, verbose_name='Правый цвет'),
            preserve_default=False,
        ),
    ]
