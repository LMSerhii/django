# Generated by Django 4.2.2 on 2023-06-24 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmsSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_img', models.ImageField(upload_to='sliderimg/', verbose_name='Зображення слайдера')),
                ('sl_title', models.CharField(max_length=100, verbose_name='Заголовок слайдера')),
                ('sl_text', models.CharField(max_length=250, verbose_name='Текст слайдера')),
                ('sl_css', models.CharField(default='-', max_length=50, null=True, verbose_name='CSS класс')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайди',
            },
        ),
    ]
