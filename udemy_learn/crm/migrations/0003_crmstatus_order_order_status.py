# Generated by Django 4.1.7 on 2023-04-01 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_alter_order_options_alter_order_order_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrmStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crm_status', models.CharField(max_length=100, verbose_name='Название статуса')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='crm.crmstatus', verbose_name='Статус'),
        ),
    ]