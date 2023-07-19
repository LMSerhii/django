# Generated by Django 4.2 on 2023-04-04 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Текст')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Тему',
                'verbose_name_plural': 'Темы',
            },
        ),
    ]
